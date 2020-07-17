from __future__ import unicode_literals

from typing import Text, Optional, Any
import json
import six

from stone.backend import CodeBackend
from stone.ir.api import Api, ApiNamespace, ApiRoute
from stone.ir.data_types import (
    DataType,
    Nullable,
    Void,
    Alias,
    List as ListDataType,
    is_user_defined_type,
    is_primitive_type,
    is_void_type,
    Struct,
    Union,
    UserDefined,
    Example,
)

ENDPOINT_FORMATS = {
    "rpc": "RPC",
    "download": "Content-download",
    "upload": "Content-upload",
}

AUTH_TYPES = {
    "noauth": "No Authentication",
    "user": "User Authentication",
    "team": "Team Authentication",
    "app": "App Authentication",
}


class ListRoutesBackend(CodeBackend):
    methods = set()

    def generate(self, api):
        # type: (Api) -> None

        with self.output_to_relative_path('index.html.md'):
            with open('teamplate.html.md') as f:
                self.emit_raw(f.read())

            for namespace in api.namespaces.values():
                self.generate_namespace(namespace)

        with self.output_to_relative_path('_datatypes.md'):
            self.emit("# Data Types")
            for namespace in api.namespaces.values():
                for data_type in namespace.data_types:
                    if isinstance(data_type, Struct):
                        self.emit("## {}".format(data_type.name))
                        self.generate_examples(data_type)
                        self.generate_struct_type(data_type, namespace)
                    elif isinstance(data_type, Union):
                        self.emit("## {}".format(data_type.name))
                        self.generate_examples(data_type)
                        self.generate_union_type(data_type, namespace)


    def generate_namespace(self, namespace):
        # type: (ApiNamespace) -> None
        if len(namespace.routes) > 0:
            self.emit("# {}".format(namespace.name.capitalize()))

        for route in namespace.routes:
            self.generate_route(namespace, route)

    def generate_route(self, namespace, route):
        # type: (ApiNamespace, ApiRoute) -> None

        if route.version == 1:
            self.emit("## {}".format(route.name))
        else:
            self.emit("## {}_v{}".format(route.name, route.version))

        self.generate_route_curl_example(namespace, route)
        self.generate_route_return_example(route.result_data_type)
        self.generate_route_doc(namespace, route)
        self.generate_route_auth_type(route)

        self.emit("### ENDPOINT FORMAT")
        self.emit(ENDPOINT_FORMATS[route.attrs.get("style", "rpc")])

        # generate scope
        if route.attrs.get("scope") is not None:
            self.emit("### Required Scope")
            self.emit(route.attrs.get("scope"))

        self.generate_route_data_types(route, namespace)

    def generate_route_curl_example(self, namespace, route):
        # type: (ApiNamespace, ApiRoute) -> None

        example_str = dropbox_curl_example(namespace, route)

        if example_str is not None:
            self.emit("```shell")
            self.emit_raw(example_str + "\n")
            self.emit("```")
            self.emit("")

    def generate_route_return_example(self, data_type):
        # type: (DataType) -> None

        if isinstance(data_type, UserDefined):
            examples = data_type.get_examples()

            if not examples:
                return

            default_example = examples.get("default") or examples.values()[0]
            example_dict = default_example.value

            if not example_dict:
                # example is just {}
                return

            self.emit("> The above command returns JSON structured like this:")
            self.emit("")
            self.emit("```json")
            self.emit_raw(json.dumps(example_dict, indent=4) + "\n")
            self.emit("```")
            self.emit("")

    def generate_examples(self, data_type):
        # type: (DataType) -> None
        if not isinstance(data_type, UserDefined):
            return

        examples = data_type.get_examples()

        if not examples:
            return

        for tag, example in examples.items():
            example_dict = example.value

            if not example_dict:
                continue

            self.emit("")
            self.emit("> Example: {}".format(tag))
            self.emit("")
            self.emit("```json")
            self.emit_raw(json.dumps(example_dict, indent=4) + "\n")
            self.emit("```")
            self.emit("")


    def generate_route_auth_type(self, route):
        # type: (ApiRoute) -> None
        self.emit("### Authentication")
        auth_types = route.attrs.get("auth", "user")
        auth_type_strs = [AUTH_TYPES[auth] for auth in auth_types.split(", ")]
        self.emit(", ".join(auth_type_strs))

    def generate_route_doc(self, namespace, route):
        # type: (ApiNamespace, ApiRoute) -> None
        if route.doc is not None:
            self.emit("### Description")
            self.emit_raw(self.handle_doc(route.doc, None, namespace))
        else:
            print("{}{} is missing doc".format(namespace.name, route.name))


    def generate_route_data_types(self, route, namespace):
        # type: (ApiRoute, ApiNamespace) -> None

        self.emit("### Query Parameters")

        self.generate_top_level_data_type(route.arg_data_type, namespace)

        self.emit("### Return Values")

        self.generate_top_level_data_type(route.result_data_type, namespace)

        self.emit("### Error Values")

        self.generate_top_level_data_type(route.error_data_type, namespace)

    def generate_top_level_data_type(self, datatype, namespace):
        # type: (DataType, ApiNamespace) -> None
        if is_user_defined_type(datatype):
            if isinstance(datatype, Struct):
                self.generate_struct_type(datatype, namespace)
            elif isinstance(datatype, Union):
                self.generate_union_type(datatype, namespace)
            else:
                print("Found new user defined type: {}".format(datatype.name))
                self.emit(self.handle_data_type(datatype))
        else:
            self.emit(self.handle_data_type(datatype))

    def generate_struct_type(self, struct, namespace):
        # type: (Struct, ApiNamespace) -> None
        self.emit(self.get_data_type_link(struct.name))
        self.emit("")

        if struct.doc is not None:
            self.emit_raw(self.handle_doc(struct.doc, struct, namespace))
            self.emit("")

        self.emit("Field Name | Data Type | Description")
        self.emit("--------- | ------- | -----------")
        for field in struct.all_fields:
            doc_cell = ""
            if field.doc is not None:
                doc_cell = self.handle_doc(field.doc, struct, namespace).replace("\n", "<br>")
            self.emit("{} | {} | {}".format(
                field.name,
                self.handle_data_type(field.data_type),
                doc_cell)
            )

    def generate_union_type(self, union, namespace):
        # type: (Union, ApiNamespace) -> None
        self.emit(self.get_data_type_link(union.name))
        self.emit("")

        if union.doc is not None:
            self.emit_raw(self.handle_doc(union.doc, union, namespace))
            self.emit("")

        self.emit("The value will be one of the following datatypes.")
        self.emit("")
        self.emit("Tag Name | Data Type | Description")
        self.emit("--------- | ------- | -----------")
        for field in union.all_fields:
            doc_cell = ""
            if field.doc is not None:
                doc_cell = self.handle_doc(field.doc, union, namespace).replace("\n", "<br>")
            self.emit("{} | {} | {}".format(
                field.name,
                self.handle_data_type(field.data_type),
                doc_cell)
            )

    def handle_data_type(self, datatype):
        # type: (DataType) -> Text
        if isinstance(datatype, Nullable):
            return "Optional[{}]".format(self.handle_data_type(datatype.data_type))
        if isinstance(datatype, ListDataType):
            return "List[{}]".format(self.handle_data_type(datatype.data_type))
        if isinstance(datatype, Alias):
            return "{}, alias of {}".format(datatype.name, self.handle_data_type(
                datatype.data_type))

        if is_user_defined_type(datatype):
            return self.get_data_type_link(datatype.name)

        return six.text_type(datatype.name)

    @staticmethod
    def get_data_type_link(datatype_name):
        # type: (Text) -> Text
        return "[{}](#data-types-{})".format(datatype_name, datatype_name.lower())

    @staticmethod
    def get_route_link(route_name, namespace_name):
        # type: (Text, Text) -> Text
        processed_route_name = route_name.replace(":", "_v").replace("/", "-")
        return "[{}/{}](#{}-{})".format(
            namespace_name,
            route_name,
            namespace_name.lower(),
            processed_route_name.lower(),
        )

    @staticmethod
    def get_field_link(current_data_type, val):
        # type: (Optional[DataType], Text) -> Text
        if "." not in val:
            if current_data_type is not None:
                return "[{}](#data-types-{})".format(val, current_data_type.name.lower())
            else:
                return val

        data_type_name, _ = val.split(".")
        return "[{}](#data-types-{})".format(val, data_type_name.lower())

    @staticmethod
    def get_direct_link(val):
        elements = val.split(" ")
        url = elements[-1]
        display_item = " ".join(elements[:-1])
        return "[{}]({})".format(display_item, url)


    def handle_doc(self, doc, data_type, namespace):
        # type: (Text, DataType, ApiNamespace) -> Text
        assert doc is not None

        def doc_processer(tag, val):
            # type: (Text, Text) -> Text
            if tag == "type":
                return self.get_data_type_link(val)
            if tag == "route":
                if data_type and namespace:
                    return self.get_route_link(val, namespace.name)
                else:
                    return val
            if tag == "field":
                return self.get_field_link(data_type, val)
            if tag == "link":
                return self.get_direct_link(val)

            return val

        return self.process_doc(doc, doc_processer) + "\n"




        return self.process_doc(doc, doc_processer) + "\n"





## code copied from DBX code base.

def dropbox_curl_example(namespace, route):
    # type: (ApiNamespace, ApiRoute) -> Optional[Text]
    """
    Returns pyxl with curl examples code or None if no example could be
    generated.

    full_route_name - string with "<namespace>/<route_name>".
    attrs - a dictionary of string keys to values that are either int,
        float, bool, str, or None. These are the route attributes assigned
        in the spec.
    """
    datatype, full_route_name, attrs = route.arg_data_type, format_route(
        namespace.name, route.name, version=route.version), route.attrs
    if is_void_type(datatype):
        arg_dict = None
    else:
        # Always demo compact serialization for requests.
        examples = datatype.get_examples(compact=True)
        if not examples:
            print("{} is missing example".format(datatype.name))
            return None

        arg_dict = examples.get("default")
        if not arg_dict:
            # If there is no example with label "default", let's just take
            # the first example from the spec.
            arg_dict = examples.values()[0]

    subdomain = attrs.get("host", "api")
    style = attrs.get("style", "rpc")
    auth = attrs.get("auth", "user")

    command = "curl -X POST https://{subdomain}.dropboxapi.com/2/{full_route_name}".format(
        subdomain=subdomain, full_route_name=full_route_name
    )

    curl_data = None
    if arg_dict is not None:
        curl_data = escape_shell_argument(
            json.dumps(arg_dict.value, separators=(",", ": "))
        )

    if auth == "app":
        command += ' \\\n    --header "Authorization: Basic [app_key_and_secret]"'
    elif auth != "noauth":
        command += ' \\\n    --header "Authorization: Bearer [access_token]"'

    if style in ("upload", "download"):
        if curl_data is not None:
            command += ' \\\n    --header "Dropbox-API-Arg: {curl_data}"'.format(
                curl_data=curl_data
            )
    if style == "upload":
        command += ' \\\n    --header "Content-Type: application/octet-stream"'
        command += " \\\n    --data-binary @local_file.txt"
    elif style == "rpc" and (curl_data is not None):
        command += (
            ' \\\n    --header "Content-Type: application/json" \\\n'
            + '    --data "{curl_data}"'
        ).format(curl_data=curl_data)

    return command


def escape_shell_argument(s):
    # type: (Text) -> Text
    # Feel free to improve, but remember that it should work for Unix and Windows.
    return s.replace('"', '\\"')


def format_route(namespace, name, version=None, as_link_url=False):
    # type: (Text, Any, Optional[Any], bool) -> Text
    str = "{}/".format(namespace)
    if version is not None and (version > 1 or as_link_url):
        str += "{}_v{}".format(name, version)
    else:
        str += name
    if as_link_url:
        str = _format_link_url(str)
    return str


def _format_link_url(name):
    # type: (Text) -> Text
    """Format String for identifier representation given route or type names."""
    return "-".join(name.split("/"))



