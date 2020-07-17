---
title: API Reference

language_tabs: # must be one of https://git.io/vQNgJ
  - shell

toc_footers:
  - <a href='#'>Sign Up for Dropbox Developer</a>
  - <a href='https://www.dropbox.com/developers'>Documentation Powered by Slate</a>

includes:
  - datatypes

search: true

code_clipboard: true
---
# Introduction

This is a hack week project to generate API documentation page was created with [Slate](https://github.com/slatedocs/slate)


# Account
## set_profile_photo
```shell
curl -X POST https://api.dropboxapi.com/2/account/set_profile_photo \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"photo\": {\".tag\": \"base64_data\",\"base64_data\": \"SW1hZ2UgZGF0YSBpbiBiYXNlNjQtZW5jb2RlZCBieXRlcy4gTm90IGEgdmFsaWQgZXhhbXBsZS4=\"}}"
```

> The above command returns JSON structured like this:

```json
{
    "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
}
```

### Description
Sets a user's profile photo.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
account_info.write
### Query Parameters
[SetProfilePhotoArg](#data-types-setprofilephotoarg)

Field Name | Data Type | Description
--------- | ------- | -----------
photo | [PhotoSourceArg](#data-types-photosourcearg) | Image to set as the user's new profile photo.<br>
### Return Values
[SetProfilePhotoResult](#data-types-setprofilephotoresult)

Field Name | Data Type | Description
--------- | ------- | -----------
profile_photo_url | String | URL for the photo representing the user, if one is set.<br>
### Error Values
[SetProfilePhotoError](#data-types-setprofilephotoerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
file_type_error | Void | File cannot be set as profile photo.<br>
file_size_error | Void | File cannot exceed 10 MB.<br>
dimension_error | Void | Image must be larger than 128 x 128.<br>
thumbnail_error | Void | Image could not be thumbnailed.<br>
transient_error | Void | Temporary infrastructure failure, please retry.<br>
other | Void | 
# Auth
## token/from_oauth1
```shell
curl -X POST https://api.dropboxapi.com/2/auth/token/from_oauth1 \
    --header "Authorization: Basic [app_key_and_secret]" \
    --header "Content-Type: application/json" \
    --data "{\"oauth1_token\": \"qievr8hamyg6ndck\",\"oauth1_token_secret\": \"qomoftv0472git7\"}"
```

> The above command returns JSON structured like this:

```json
{
    "oauth2_token": "9mCrkS7BIdAAAAAAAAAAHHS0TsSnpYvKQVtKdBnN5IuzhYOGblSgTcHgBFKFMmFn"
}
```

### Description
Creates an OAuth 2.0 access token from the supplied OAuth 1.0 access token.
### Authentication
App Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[TokenFromOAuth1Arg](#data-types-tokenfromoauth1arg)

Field Name | Data Type | Description
--------- | ------- | -----------
oauth1_token | String | The supplied OAuth 1.0 access token.<br>
oauth1_token_secret | String | The token secret associated with the supplied access token.<br>
### Return Values
[TokenFromOAuth1Result](#data-types-tokenfromoauth1result)

Field Name | Data Type | Description
--------- | ------- | -----------
oauth2_token | String | The OAuth 2.0 token generated from the supplied OAuth 1.0 token.<br>
### Error Values
[TokenFromOAuth1Error](#data-types-tokenfromoauth1error)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_oauth1_token_info | Void | Part or all of the OAuth 1.0 access token info is invalid.<br>
app_id_mismatch | Void | The authorized app does not match the app associated with the supplied access token.<br>
other | Void | 
## token/revoke
```shell
curl -X POST https://api.dropboxapi.com/2/auth/token/revoke \
    --header "Authorization: Bearer [access_token]"
```

### Description
Disables the access token used to authenticate the call.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
Void
### Return Values
Void
### Error Values
Void
# Check
## app
```shell
curl -X POST https://api.dropboxapi.com/2/check/app \
    --header "Authorization: Basic [app_key_and_secret]" \
    --header "Content-Type: application/json" \
    --data "{\"query\": \"foo\"}"
```

> The above command returns JSON structured like this:

```json
{
    "result": "foo"
}
```

### Description
This endpoint performs App Authentication, validating the supplied app key and secret, and returns the supplied string, to allow you to test your code and connection to the Dropbox API. It has no other effect. If you receive an HTTP 200 response with the supplied query, it indicates at least part of the Dropbox API infrastructure is working and that the app key and secret valid.
### Authentication
App Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[EchoArg](#data-types-echoarg)

EchoArg contains the arguments to be sent to the Dropbox servers.

Field Name | Data Type | Description
--------- | ------- | -----------
query | String | The string that you'd like to be echoed back to you.<br>
### Return Values
[EchoResult](#data-types-echoresult)

EchoResult contains the result returned from the Dropbox servers.

Field Name | Data Type | Description
--------- | ------- | -----------
result | String | If everything worked correctly, this would be the same as query.<br>
### Error Values
Void
## user
```shell
curl -X POST https://api.dropboxapi.com/2/check/user \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"query\": \"foo\"}"
```

> The above command returns JSON structured like this:

```json
{
    "result": "foo"
}
```

### Description
This endpoint performs User Authentication, validating the supplied access token, and returns the supplied string, to allow you to test your code and connection to the Dropbox API. It has no other effect. If you receive an HTTP 200 response with the supplied query, it indicates at least part of the Dropbox API infrastructure is working and that the access token is valid.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[EchoArg](#data-types-echoarg)

EchoArg contains the arguments to be sent to the Dropbox servers.

Field Name | Data Type | Description
--------- | ------- | -----------
query | String | The string that you'd like to be echoed back to you.<br>
### Return Values
[EchoResult](#data-types-echoresult)

EchoResult contains the result returned from the Dropbox servers.

Field Name | Data Type | Description
--------- | ------- | -----------
result | String | If everything worked correctly, this would be the same as query.<br>
### Error Values
Void
# Cloud_docs
## get_content
```shell
curl -X POST https://content.dropboxapi.com/2/cloud_docs/get_content \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"file_id\": \"id:pXGlEfaZvvAAAAAAAAAAGw\"}"
```

### Description
Fetch the binary content of the requested document. This route requires Cloud Docs auth. Please make a request to cloud_docs/authorize and supply that token in the Authorization header.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Query Parameters
[GetContentArg](#data-types-getcontentarg)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | 
### Return Values
Void
### Error Values
[CloudDocsAccessError](#data-types-clouddocsaccesserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_doc_id | Void | The Cloud Doc ID is invalid.<br>
not_found | Void | A Cloud Doc could not be found for the given ID.<br>
permission_denied | Void | Permission denied for the Cloud Doc with the given ID.<br>
other | Void | 
## get_metadata
### Description
Fetches metadata associated with a Cloud Doc and user. This route requires Cloud Docs auth. Please make a request to cloud_docs/authorize and supply that token in the Authorization header.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[GetMetadataArg](#data-types-getmetadataarg)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | API ID ("id:...") associated with the Cloud Doc.<br>
### Return Values
[GetMetadataResult](#data-types-getmetadataresult)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | 
title | String | Title of the Cloud Doc without extension.<br>
mime_type | String | MIME type of the Cloud Doc.<br>
version | String | Opaque string representing the version of the document stored in Dropbox (only set for Dropbox-stored Documents).<br>
provider_version | String | Application specific string representing the revision of a document (only set for App-stored Documents).<br>
user | Optional[[UserInfo](#data-types-userinfo)] | User identified by the auth token.<br>
is_deleted | Boolean | true if the document is deleted or purged.<br>
user_permissions | Optional[[UserPermissions](#data-types-userpermissions)] | Actions that the user identified by the auth token can performn. This message will not be populated for deleted documents.<br>
### Error Values
[GetMetadataError](#data-types-getmetadataerror)

Field Name | Data Type | Description
--------- | ------- | -----------
get_metadata_error_tag | Optional[[get_metadata_error_tag_union](#data-types-get_metadata_error_tag_union)] | 
## lock
### Description
Lock a Cloud Doc. This route requires Cloud Docs auth. Please make a request to cloud_docs/authorize and supply that token in the Authorization header.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[LockArg](#data-types-lockarg)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | The API ID ("id:...") associated with the Cloud Doc<br>
### Return Values
[LockResult](#data-types-lockresult)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | 
expires_at | Int64 | The timestamp after which the lock will expire, measured in seconds since 1970-01-01 00:00:00 UTC<br>
### Error Values
[LockingError](#data-types-lockingerror)

Field Name | Data Type | Description
--------- | ------- | -----------
locking_error_tag | Optional[[locking_error_tag_union](#data-types-locking_error_tag_union)] | 
## rename
### Description
Update the title of a Cloud Doc. This route requires Cloud Docs auth. Please make a request to cloud_docs/authorize and supply that token in the Authorization header.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[RenameArg](#data-types-renamearg)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | The API ID ("id:...") associated with the Cloud Doc<br>
title | String | The new title of the doc, excluding extension<br>
### Return Values
[RenameResult](#data-types-renameresult)

Field Name | Data Type | Description
--------- | ------- | -----------
title | String | The updated title of the doc without extension, which could be different from the supplied title in the request because Dropbox may remove/replace charaters that are not supported in Dropbox Filesystem.<br>
### Error Values
[RenameError](#data-types-renameerror)

Field Name | Data Type | Description
--------- | ------- | -----------
rename_error_tag | Optional[[rename_error_tag_union](#data-types-rename_error_tag_union)] | 
## unlock
### Description
Unlock a Cloud Doc. This route requires Cloud Docs auth. Please make a request to cloud_docs/authorize and supply that token in the Authorization header.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[UnlockArg](#data-types-unlockarg)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | The API ID ("id:...") associated with the Cloud Doc<br>
### Return Values
[UnlockResult](#data-types-unlockresult)

Empty message for unlock

Field Name | Data Type | Description
--------- | ------- | -----------
### Error Values
[LockingError](#data-types-lockingerror)

Field Name | Data Type | Description
--------- | ------- | -----------
locking_error_tag | Optional[[locking_error_tag_union](#data-types-locking_error_tag_union)] | 
## update_content
```shell
curl -X POST https://content.dropboxapi.com/2/cloud_docs/update_content \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"file_id\": \"id:pXGlEfaZvvAAAAAAAAAAGw\",\"actor_tokens\": [\"AAAJagNapzVCQzKrX-LTY7DjVc1itPHiCI6COvcE3BpyN7-sTY1gxcjXY2nST3dONovrmYDdKxVe_TSMA0p8DTYbk2kfkA_1hHIplGxc4glyJwh2nK5NcxxScT8AYLx2cgepxAX2PALm2hwDdcE9P060_iedPWIqqseyFjxo9bMmDWQZFSGAyTlBlvPudGprVhQ=\"],\"additional_contents\": []}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "version": "1mPVXsONgX_d6QlFqs6gGz3MzGU="
}
```

### Description
Update the contents of a Cloud Doc. This should be called for files with a max size of 150MB. This route requires Cloud Docs auth. Please make a request to cloud_docs/authorize and supply that token in the Authorization header.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Query Parameters
[UpdateContentArg](#data-types-updatecontentarg)

Field Name | Data Type | Description
--------- | ------- | -----------
file_id | String | 
actor_tokens | List[String] | A list of auth_tokens, one for each editor who made changes to the document since the last call to update_content.<br>
additional_contents | Optional[List[[Content](#data-types-content)]] | Currently, this will always be empty until we implement upload_additional_content.<br>
### Return Values
[UpdateContentResult](#data-types-updatecontentresult)

Field Name | Data Type | Description
--------- | ------- | -----------
version | String | Version of the document stored in Dropbox.<br>
### Error Values
[UpdateContentError](#data-types-updatecontenterror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_doc_id | Void | The Cloud Doc ID is invalid.<br>
not_found | Void | A Cloud Doc could not be found for the given ID.<br>
permission_denied | Void | Permission denied for the Cloud Doc with the given ID.<br>
other | Void | 
upload_size_too_large | Void | Upload payload exceeds maximum allowed size of 150MB.<br>
conflict | Void | A lock on the document identified by path_or_id is held by another editor.<br>
unlocked | Void | A lock is not held on the document identified by path_or_id. Acquire lock before uploading content for the document.<br>
# Contacts
## delete_manual_contacts
```shell
curl -X POST https://api.dropboxapi.com/2/contacts/delete_manual_contacts \
    --header "Authorization: Bearer [access_token]"
```

### Description
Removes all manually added contacts. You'll still keep contacts who are on your team or who you imported. New contacts will be added when you share.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
contacts.write
### Query Parameters
Void
### Return Values
Void
### Error Values
Void
## delete_manual_contacts_batch
```shell
curl -X POST https://api.dropboxapi.com/2/contacts/delete_manual_contacts_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"email_addresses\": [\"contactemailaddress1@domain.com\",\"contactemailaddress2@domain.com\"]}"
```

### Description
Removes manually added contacts from the given list.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
contacts.write
### Query Parameters
[DeleteManualContactsArg](#data-types-deletemanualcontactsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
email_addresses | List[String] | List of manually added contacts to be deleted.<br>
### Return Values
Void
### Error Values
[DeleteManualContactsError](#data-types-deletemanualcontactserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
contacts_not_found | List[String] | Can't delete contacts from this list. Make sure the list only has manually added contacts. The deletion was cancelled.<br>
other | Void | 
# File_properties
## properties/add
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/properties/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"property_groups\": [{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"fields\": [{\"name\": \"Security Policy\",\"value\": \"Confidential\"}]}]}"
```

### Description
Add property groups to a Dropbox file. See templates/add_for_user or templates/add_for_team to create new templates.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[AddPropertiesArg](#data-types-addpropertiesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
property_groups | List[[PropertyGroup](#data-types-propertygroup)] | The property groups which are to be added to a Dropbox file. No two groups in the input should  refer to the same template.<br>
### Return Values
Void
### Error Values
[AddPropertiesError](#data-types-addpropertieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_field_too_large | Void | One or more of the supplied property field values is too large.<br>
does_not_fit_template | Void | One or more of the supplied property fields does not conform to the template specifications.<br>
duplicate_property_groups | Void | There are 2 or more property groups referring to the same templates in the input.<br>
property_group_already_exists | Void | A property group associated with this template and file already exists.<br>
## properties/overwrite
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/properties/overwrite \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"property_groups\": [{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"fields\": [{\"name\": \"Security Policy\",\"value\": \"Confidential\"}]}]}"
```

### Description
Overwrite property groups associated with a file. This endpoint should be used instead of properties/update when property groups are being updated via a "snapshot" instead of via a "delta". In other words, this endpoint will delete all omitted fields from a property group, whereas properties/update will only delete fields that are explicitly marked for deletion.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[OverwritePropertyGroupArg](#data-types-overwritepropertygrouparg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
property_groups | List[[PropertyGroup](#data-types-propertygroup)] | The property groups "snapshot" updates to force apply. No two groups in the input should  refer to the same template.<br>
### Return Values
Void
### Error Values
[InvalidPropertyGroupError](#data-types-invalidpropertygrouperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_field_too_large | Void | One or more of the supplied property field values is too large.<br>
does_not_fit_template | Void | One or more of the supplied property fields does not conform to the template specifications.<br>
duplicate_property_groups | Void | There are 2 or more property groups referring to the same templates in the input.<br>
## properties/remove
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/properties/remove \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"property_template_ids\": [\"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"]}"
```

### Description
Permanently removes the specified property group from the file. To remove specific property field key value pairs, see properties/update. To update a template, see templates/update_for_user or templates/update_for_team. To remove a template, see templates/remove_for_user or templates/remove_for_team.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[RemovePropertiesArg](#data-types-removepropertiesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
property_template_ids | List[String] | A list of identifiers for a template created by [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Return Values
Void
### Error Values
[RemovePropertiesError](#data-types-removepropertieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_group_lookup | [LookUpPropertiesError](#data-types-lookuppropertieserror) | 
## properties/search
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/properties/search \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"queries\": [{\"query\": \"Confidential\",\"mode\": {\".tag\": \"field_name\",\"field_name\": \"Security\"},\"logical_operator\": \"or_operator\"}],\"template_filter\": \"filter_none\"}"
```

> The above command returns JSON structured like this:

```json
{
    "matches": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
            "path": "/my_awesome/word.docx", 
            "is_deleted": false, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ]
        }
    ]
}
```

### Description
Search across property templates for particular property field values.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[PropertiesSearchArg](#data-types-propertiessearcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
queries | List[[PropertiesSearchQuery](#data-types-propertiessearchquery)] | Queries to search.<br>
template_filter | [TemplateFilter](#data-types-templatefilter) | Filter results to contain only properties associated with these template IDs.<br>
### Return Values
[PropertiesSearchResult](#data-types-propertiessearchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
matches | List[[PropertiesSearchMatch](#data-types-propertiessearchmatch)] | A list (possibly empty) of matches for the query.<br>
cursor | Optional[String] | Pass the cursor into [file_properties/properties/search/continue](#file_properties-properties-search-continue) to continue to receive search results. Cursor will be null when there are no more results.<br>
### Error Values
[PropertiesSearchError](#data-types-propertiessearcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
property_group_lookup | [LookUpPropertiesError](#data-types-lookuppropertieserror) | 
other | Void | 
## properties/search/continue
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/properties/search/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "matches": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
            "path": "/my_awesome/word.docx", 
            "is_deleted": false, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ]
        }
    ]
}
```

### Description
Once a cursor has been retrieved from properties/search, use this to paginate through all search results.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[PropertiesSearchContinueArg](#data-types-propertiessearchcontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by your last call to [file_properties/properties/search](#file_properties-properties-search) or [file_properties/properties/search/continue](#file_properties-properties-search-continue).<br>
### Return Values
[PropertiesSearchResult](#data-types-propertiessearchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
matches | List[[PropertiesSearchMatch](#data-types-propertiessearchmatch)] | A list (possibly empty) of matches for the query.<br>
cursor | Optional[String] | Pass the cursor into [file_properties/properties/search/continue](#file_properties-properties-search-continue) to continue to receive search results. Cursor will be null when there are no more results.<br>
### Error Values
[PropertiesSearchContinueError](#data-types-propertiessearchcontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
reset | Void | Indicates that the cursor has been invalidated. Call [file_properties/properties/search](#file_properties-properties-search) to obtain a new cursor.<br>
other | Void | 
## properties/update
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/properties/update \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"update_property_groups\": [{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"add_or_update_fields\": [{\"name\": \"Security Policy\",\"value\": \"Confidential\"}],\"remove_fields\": []}]}"
```

### Description
Add, update or remove properties associated with the supplied file and templates. This endpoint should be used instead of properties/overwrite when property groups are being updated via a "delta" instead of via a "snapshot" . In other words, this endpoint will not delete any omitted fields from a property group, whereas properties/overwrite will delete any fields that are omitted from a property group.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[UpdatePropertiesArg](#data-types-updatepropertiesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
update_property_groups | List[[PropertyGroupUpdate](#data-types-propertygroupupdate)] | The property groups "delta" updates to apply.<br>
### Return Values
Void
### Error Values
[UpdatePropertiesError](#data-types-updatepropertieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_field_too_large | Void | One or more of the supplied property field values is too large.<br>
does_not_fit_template | Void | One or more of the supplied property fields does not conform to the template specifications.<br>
duplicate_property_groups | Void | There are 2 or more property groups referring to the same templates in the input.<br>
property_group_lookup | [LookUpPropertiesError](#data-types-lookuppropertieserror) | 
## templates/add_for_team
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/add_for_team \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"name\": \"Security\",\"description\": \"These properties describe how confidential this file or folder is.\",\"fields\": [{\"name\": \"Security Policy\",\"description\": \"This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.\",\"type\": \"string\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
}
```

### Description
Add a template associated with a team. See properties/add to add properties to a file or folder.
Note: this endpoint will create team-owned templates.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.team_metadata.write
### Query Parameters
[AddTemplateArg](#data-types-addtemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Return Values
[AddTemplateResult](#data-types-addtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Error Values
[ModifyTemplateError](#data-types-modifytemplateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
conflicting_property_names | Void | A property field key with that name already exists in the template.<br>
too_many_properties | Void | There are too many properties in the changed template. The maximum number of properties per template is 32.<br>
too_many_templates | Void | There are too many templates for the team.<br>
template_attribute_too_large | Void | The template name, description or one or more of the property field keys is too large.<br>
## templates/add_for_user
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/add_for_user \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"name\": \"Security\",\"description\": \"These properties describe how confidential this file or folder is.\",\"fields\": [{\"name\": \"Security Policy\",\"description\": \"This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.\",\"type\": \"string\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
}
```

### Description
Add a template associated with a user. See properties/add to add properties to a file. This endpoint can't be called on a team member or admin's behalf.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[AddTemplateArg](#data-types-addtemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Return Values
[AddTemplateResult](#data-types-addtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Error Values
[ModifyTemplateError](#data-types-modifytemplateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
conflicting_property_names | Void | A property field key with that name already exists in the template.<br>
too_many_properties | Void | There are too many properties in the changed template. The maximum number of properties per template is 32.<br>
too_many_templates | Void | There are too many templates for the team.<br>
template_attribute_too_large | Void | The template name, description or one or more of the property field keys is too large.<br>
## templates/get_for_team
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/get_for_team \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Security", 
    "description": "These properties describe how confidential this file or folder is.", 
    "fields": [
        {
            "name": "Security Policy", 
            "description": "This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.", 
            "type": {
                ".tag": "string"
            }
        }
    ]
}
```

### Description
Get the schema for a specified template.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.team_metadata.write
### Query Parameters
[GetTemplateArg](#data-types-gettemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Return Values
[GetTemplateResult](#data-types-gettemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## templates/get_for_user
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/get_for_user \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Security", 
    "description": "These properties describe how confidential this file or folder is.", 
    "fields": [
        {
            "name": "Security Policy", 
            "description": "This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.", 
            "type": {
                ".tag": "string"
            }
        }
    ]
}
```

### Description
Get the schema for a specified template. This endpoint can't be called on a team member or admin's behalf.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[GetTemplateArg](#data-types-gettemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Return Values
[GetTemplateResult](#data-types-gettemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## templates/list_for_team
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/list_for_team \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "template_ids": [
        "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
    ]
}
```

### Description
Get the template identifiers for a team. To get the schema of each template use templates/get_for_team.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.team_metadata.write
### Query Parameters
Void
### Return Values
[ListTemplateResult](#data-types-listtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_ids | List[String] | List of identifiers for templates added by  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## templates/list_for_user
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/list_for_user \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "template_ids": [
        "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
    ]
}
```

### Description
Get the template identifiers for a team. To get the schema of each template use templates/get_for_user. This endpoint can't be called on a team member or admin's behalf.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
Void
### Return Values
[ListTemplateResult](#data-types-listtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_ids | List[String] | List of identifiers for templates added by  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## templates/remove_for_team
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/remove_for_team \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"}"
```

### Description
Permanently removes the specified template created from templates/add_for_user. All properties associated with the template will also be removed. This action cannot be undone.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.team_metadata.write
### Query Parameters
[RemoveTemplateArg](#data-types-removetemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for a template created by [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Return Values
Void
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## templates/remove_for_user
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/remove_for_user \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"}"
```

### Description
Permanently removes the specified template created from templates/add_for_user. All properties associated with the template will also be removed. This action cannot be undone.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[RemoveTemplateArg](#data-types-removetemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for a template created by [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Return Values
Void
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## templates/update_for_team
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/update_for_team \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"name\": \"New Security Template Name\",\"description\": \"These properties will describe how confidential this file or folder is.\",\"add_fields\": [{\"name\": \"Security Policy\",\"description\": \"This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.\",\"type\": \"string\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
}
```

### Description
Update a template associated with a team. This route can update the template name, the template description and add optional properties to templates.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.team_metadata.write
### Query Parameters
[UpdateTemplateArg](#data-types-updatetemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
name | Optional[String] | A display name for the template. template names can be up to 256 bytes.<br>
description | Optional[String] | Description for the new template. Template descriptions can be up to 1024 bytes.<br>
add_fields | Optional[List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)]] | Property field templates to be added to the group template. There can be up to 32 properties in a single template.<br>
### Return Values
[UpdateTemplateResult](#data-types-updatetemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Error Values
[ModifyTemplateError](#data-types-modifytemplateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
conflicting_property_names | Void | A property field key with that name already exists in the template.<br>
too_many_properties | Void | There are too many properties in the changed template. The maximum number of properties per template is 32.<br>
too_many_templates | Void | There are too many templates for the team.<br>
template_attribute_too_large | Void | The template name, description or one or more of the property field keys is too large.<br>
## templates/update_for_user
```shell
curl -X POST https://api.dropboxapi.com/2/file_properties/templates/update_for_user \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"name\": \"New Security Template Name\",\"description\": \"These properties will describe how confidential this file or folder is.\",\"add_fields\": [{\"name\": \"Security Policy\",\"description\": \"This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.\",\"type\": \"string\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
}
```

### Description
Update a template associated with a user. This route can update the template name, the template description and add optional properties to templates. This endpoint can't be called on a team member or admin's behalf.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.write
### Query Parameters
[UpdateTemplateArg](#data-types-updatetemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
name | Optional[String] | A display name for the template. template names can be up to 256 bytes.<br>
description | Optional[String] | Description for the new template. Template descriptions can be up to 1024 bytes.<br>
add_fields | Optional[List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)]] | Property field templates to be added to the group template. There can be up to 32 properties in a single template.<br>
### Return Values
[UpdateTemplateResult](#data-types-updatetemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [file_properties/templates/add_for_user](#file_properties-templates-add_for_user) or [file_properties/templates/add_for_team](#file_properties-templates-add_for_team).<br>
### Error Values
[ModifyTemplateError](#data-types-modifytemplateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
conflicting_property_names | Void | A property field key with that name already exists in the template.<br>
too_many_properties | Void | There are too many properties in the changed template. The maximum number of properties per template is 32.<br>
too_many_templates | Void | There are too many templates for the team.<br>
template_attribute_too_large | Void | The template name, description or one or more of the property field keys is too large.<br>
# File_requests
## count
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/count \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "file_request_count": 15
}
```

### Description
Returns the total number of file requests owned by this user. Includes both open and closed file requests.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.read
### Query Parameters
Void
### Return Values
[CountFileRequestsResult](#data-types-countfilerequestsresult)

Result for [file_requests/count](#file_requests-count).

Field Name | Data Type | Description
--------- | ------- | -----------
file_request_count | UInt64 | The number file requests owner by this user.<br>
### Error Values
[CountFileRequestsError](#data-types-countfilerequestserror)

There was an error counting the file requests.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
## create
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/create \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"title\": \"Homework submission\",\"destination\": \"/File Requests/Homework\",\"deadline\": {\"deadline\": \"2020-10-12T17:00:00Z\",\"allow_late_uploads\": \"seven_days\"},\"open\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "oaCAVmEyrqYnkZX9955Y", 
    "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
    "title": "Homework submission", 
    "created": "2015-10-05T17:00:00Z", 
    "is_open": true, 
    "file_count": 3, 
    "destination": "/File Requests/Homework", 
    "deadline": {
        "deadline": "2020-10-12T17:00:00Z", 
        "allow_late_uploads": {
            ".tag": "seven_days"
        }
    }
}
```

### Description
Creates a file request for this user.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.write
### Query Parameters
[CreateFileRequestArgs](#data-types-createfilerequestargs)

Arguments for [file_requests/create](#file_requests-create).

Field Name | Data Type | Description
--------- | ------- | -----------
title | String | The title of the file request. Must not be empty.<br>
destination | String | The path of the folder in the Dropbox where uploaded files will be sent. For apps with the app folder permission, this will be relative to the app folder.<br>
deadline | Optional[[FileRequestDeadline](#data-types-filerequestdeadline)] | The deadline for the file request. Deadlines can only be set by Professional and Business accounts.<br>
open | Boolean | Whether or not the file request should be open. If the file request is closed, it will not accept any file submissions, but it can be opened later.<br>
### Return Values
[FileRequest](#data-types-filerequest)

A [file request](https://www.dropbox.com/help/9090) for receiving files into the user's Dropbox account.

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The ID of the file request.<br>
url | String | The URL of the file request.<br>
title | String | The title of the file request.<br>
created | Timestamp | When this file request was created.<br>
is_open | Boolean | Whether or not the file request is open. If the file request is closed, it will not accept any more file submissions.<br>
file_count | Int64 | The number of files this file request has received.<br>
destination | Optional[String] | The path of the folder in the Dropbox where uploaded files will be sent. This can be null if the destination was removed. For apps with the app folder permission, this will be relative to the app folder.<br>
deadline | Optional[[FileRequestDeadline](#data-types-filerequestdeadline)] | The deadline for this file request. Only set if the request has a deadline.<br>
### Error Values
[CreateFileRequestError](#data-types-createfilerequesterror)

There was an error creating the file request.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
not_found | Void | This file request ID was not found.<br>
not_a_folder | Void | The specified path is not a folder.<br>
app_lacks_access | Void | This file request is not accessible to this app. Apps with the app folder permission can only access file requests in their app folder.<br>
no_permission | Void | This user doesn't have permission to access or modify this file request.<br>
email_unverified | Void | This user's email address is not verified. File requests are only available on accounts with a verified email address. Users can verify their email address [here](https://www.dropbox.com/help/317).<br>
validation_error | Void | There was an error validating the request. For example, the title was invalid, or there were disallowed characters in the destination path.<br>
invalid_location | Void | File requests are not available on the specified folder.<br>
rate_limit | Void | The user has reached the rate limit for creating file requests. The limit is currently 4000 file requests total.<br>
## delete
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"ids\": [\"oaCAVmEyrqYnkZX9955Y\",\"BaZmehYoXMPtaRmfTbSG\"]}"
```

> The above command returns JSON structured like this:

```json
{
    "file_requests": [
        {
            "id": "oaCAVmEyrqYnkZX9955Y", 
            "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
            "title": "Homework submission", 
            "created": "2015-10-05T17:00:00Z", 
            "is_open": true, 
            "file_count": 3, 
            "destination": "/File Requests/Homework", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z", 
                "allow_late_uploads": {
                    ".tag": "seven_days"
                }
            }
        }, 
        {
            "id": "BAJ7IrRGicQKGToykQdB", 
            "url": "https://www.dropbox.com/request/BAJ7IrRGjcQKGToykQdB", 
            "title": "Photo contest submission", 
            "created": "2015-11-02T04:00:00Z", 
            "is_open": true, 
            "file_count": 105, 
            "destination": "/Photo contest entries", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z"
            }
        }, 
        {
            "id": "rxwMPvK3ATTa0VxOJu5T", 
            "url": "https://www.dropbox.com/request/rxwMPvK3ATTa0VxOJu5T", 
            "title": "Wedding photo submission", 
            "created": "2015-12-15T13:02:00Z", 
            "is_open": true, 
            "file_count": 37, 
            "destination": "/Wedding photos"
        }
    ]
}
```

### Description
Delete a batch of closed file requests.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.write
### Query Parameters
[DeleteFileRequestArgs](#data-types-deletefilerequestargs)

Arguments for [file_requests/delete](#file_requests-delete).

Field Name | Data Type | Description
--------- | ------- | -----------
ids | List[String] | List IDs of the file requests to delete.<br>
### Return Values
[DeleteFileRequestsResult](#data-types-deletefilerequestsresult)

Result for [file_requests/delete](#file_requests-delete).

Field Name | Data Type | Description
--------- | ------- | -----------
file_requests | List[[FileRequest](#data-types-filerequest)] | The file requests deleted by the request.<br>
### Error Values
[DeleteFileRequestError](#data-types-deletefilerequesterror)

There was an error deleting these file requests.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
not_found | Void | This file request ID was not found.<br>
not_a_folder | Void | The specified path is not a folder.<br>
app_lacks_access | Void | This file request is not accessible to this app. Apps with the app folder permission can only access file requests in their app folder.<br>
no_permission | Void | This user doesn't have permission to access or modify this file request.<br>
email_unverified | Void | This user's email address is not verified. File requests are only available on accounts with a verified email address. Users can verify their email address [here](https://www.dropbox.com/help/317).<br>
validation_error | Void | There was an error validating the request. For example, the title was invalid, or there were disallowed characters in the destination path.<br>
file_request_open | Void | One or more file requests currently open.<br>
## delete_all_closed
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/delete_all_closed \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "file_requests": [
        {
            "id": "oaCAVmEyrqYnkZX9955Y", 
            "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
            "title": "Homework submission", 
            "created": "2015-10-05T17:00:00Z", 
            "is_open": true, 
            "file_count": 3, 
            "destination": "/File Requests/Homework", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z", 
                "allow_late_uploads": {
                    ".tag": "seven_days"
                }
            }
        }, 
        {
            "id": "BAJ7IrRGicQKGToykQdB", 
            "url": "https://www.dropbox.com/request/BAJ7IrRGjcQKGToykQdB", 
            "title": "Photo contest submission", 
            "created": "2015-11-02T04:00:00Z", 
            "is_open": true, 
            "file_count": 105, 
            "destination": "/Photo contest entries", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z"
            }
        }, 
        {
            "id": "rxwMPvK3ATTa0VxOJu5T", 
            "url": "https://www.dropbox.com/request/rxwMPvK3ATTa0VxOJu5T", 
            "title": "Wedding photo submission", 
            "created": "2015-12-15T13:02:00Z", 
            "is_open": true, 
            "file_count": 37, 
            "destination": "/Wedding photos"
        }
    ]
}
```

### Description
Delete all closed file requests owned by this user.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.write
### Query Parameters
Void
### Return Values
[DeleteAllClosedFileRequestsResult](#data-types-deleteallclosedfilerequestsresult)

Result for [file_requests/delete_all_closed](#file_requests-delete_all_closed).

Field Name | Data Type | Description
--------- | ------- | -----------
file_requests | List[[FileRequest](#data-types-filerequest)] | The file requests deleted for this user.<br>
### Error Values
[DeleteAllClosedFileRequestsError](#data-types-deleteallclosedfilerequestserror)

There was an error deleting all closed file requests.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
not_found | Void | This file request ID was not found.<br>
not_a_folder | Void | The specified path is not a folder.<br>
app_lacks_access | Void | This file request is not accessible to this app. Apps with the app folder permission can only access file requests in their app folder.<br>
no_permission | Void | This user doesn't have permission to access or modify this file request.<br>
email_unverified | Void | This user's email address is not verified. File requests are only available on accounts with a verified email address. Users can verify their email address [here](https://www.dropbox.com/help/317).<br>
validation_error | Void | There was an error validating the request. For example, the title was invalid, or there were disallowed characters in the destination path.<br>
## get
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"oaCAVmEyrqYnkZX9955Y\"}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "oaCAVmEyrqYnkZX9955Y", 
    "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
    "title": "Homework submission", 
    "created": "2015-10-05T17:00:00Z", 
    "is_open": true, 
    "file_count": 3, 
    "destination": "/File Requests/Homework", 
    "deadline": {
        "deadline": "2020-10-12T17:00:00Z", 
        "allow_late_uploads": {
            ".tag": "seven_days"
        }
    }
}
```

### Description
Returns the specified file request.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.read
### Query Parameters
[GetFileRequestArgs](#data-types-getfilerequestargs)

Arguments for [file_requests/get](#file_requests-get).

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The ID of the file request to retrieve.<br>
### Return Values
[FileRequest](#data-types-filerequest)

A [file request](https://www.dropbox.com/help/9090) for receiving files into the user's Dropbox account.

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The ID of the file request.<br>
url | String | The URL of the file request.<br>
title | String | The title of the file request.<br>
created | Timestamp | When this file request was created.<br>
is_open | Boolean | Whether or not the file request is open. If the file request is closed, it will not accept any more file submissions.<br>
file_count | Int64 | The number of files this file request has received.<br>
destination | Optional[String] | The path of the folder in the Dropbox where uploaded files will be sent. This can be null if the destination was removed. For apps with the app folder permission, this will be relative to the app folder.<br>
deadline | Optional[[FileRequestDeadline](#data-types-filerequestdeadline)] | The deadline for this file request. Only set if the request has a deadline.<br>
### Error Values
[GetFileRequestError](#data-types-getfilerequesterror)

There was an error retrieving the specified file request.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
not_found | Void | This file request ID was not found.<br>
not_a_folder | Void | The specified path is not a folder.<br>
app_lacks_access | Void | This file request is not accessible to this app. Apps with the app folder permission can only access file requests in their app folder.<br>
no_permission | Void | This user doesn't have permission to access or modify this file request.<br>
email_unverified | Void | This user's email address is not verified. File requests are only available on accounts with a verified email address. Users can verify their email address [here](https://www.dropbox.com/help/317).<br>
validation_error | Void | There was an error validating the request. For example, the title was invalid, or there were disallowed characters in the destination path.<br>
## list_v2
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/list_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 1000}"
```

> The above command returns JSON structured like this:

```json
{
    "file_requests": [
        {
            "id": "oaCAVmEyrqYnkZX9955Y", 
            "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
            "title": "Homework submission", 
            "created": "2015-10-05T17:00:00Z", 
            "is_open": true, 
            "file_count": 3, 
            "destination": "/File Requests/Homework", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z", 
                "allow_late_uploads": {
                    ".tag": "seven_days"
                }
            }
        }, 
        {
            "id": "BAJ7IrRGicQKGToykQdB", 
            "url": "https://www.dropbox.com/request/BAJ7IrRGjcQKGToykQdB", 
            "title": "Photo contest submission", 
            "created": "2015-11-02T04:00:00Z", 
            "is_open": true, 
            "file_count": 105, 
            "destination": "/Photo contest entries", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z"
            }
        }, 
        {
            "id": "rxwMPvK3ATTa0VxOJu5T", 
            "url": "https://www.dropbox.com/request/rxwMPvK3ATTa0VxOJu5T", 
            "title": "Wedding photo submission", 
            "created": "2015-12-15T13:02:00Z", 
            "is_open": true, 
            "file_count": 37, 
            "destination": "/Wedding photos"
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": true
}
```

### Description
Returns a list of file requests owned by this user. For apps with the app folder permission, this will only return file requests with destinations in the app folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.read
### Query Parameters
[ListFileRequestsArg](#data-types-listfilerequestsarg)

Arguments for [file_requests/list:2](#file_requests-list_v2).

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt64 | The maximum number of file requests that should be returned per request.<br>
### Return Values
[ListFileRequestsV2Result](#data-types-listfilerequestsv2result)

Result for [file_requests/list:2](#file_requests-list_v2) and [file_requests/list/continue](#file_requests-list-continue).

Field Name | Data Type | Description
--------- | ------- | -----------
file_requests | List[[FileRequest](#data-types-filerequest)] | The file requests owned by this user. Apps with the app folder permission will only see file requests in their app folder.<br>
cursor | String | Pass the cursor into [file_requests/list/continue](#file_requests-list-continue) to obtain additional file requests.<br>
has_more | Boolean | Is true if there are additional file requests that have not been returned yet. An additional call to :route:list/continue` can retrieve them.<br>
### Error Values
[ListFileRequestsError](#data-types-listfilerequestserror)

There was an error retrieving the file requests.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
## list
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/list \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "file_requests": [
        {
            "id": "oaCAVmEyrqYnkZX9955Y", 
            "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
            "title": "Homework submission", 
            "created": "2015-10-05T17:00:00Z", 
            "is_open": true, 
            "file_count": 3, 
            "destination": "/File Requests/Homework", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z", 
                "allow_late_uploads": {
                    ".tag": "seven_days"
                }
            }
        }, 
        {
            "id": "BAJ7IrRGicQKGToykQdB", 
            "url": "https://www.dropbox.com/request/BAJ7IrRGjcQKGToykQdB", 
            "title": "Photo contest submission", 
            "created": "2015-11-02T04:00:00Z", 
            "is_open": true, 
            "file_count": 105, 
            "destination": "/Photo contest entries", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z"
            }
        }, 
        {
            "id": "rxwMPvK3ATTa0VxOJu5T", 
            "url": "https://www.dropbox.com/request/rxwMPvK3ATTa0VxOJu5T", 
            "title": "Wedding photo submission", 
            "created": "2015-12-15T13:02:00Z", 
            "is_open": true, 
            "file_count": 37, 
            "destination": "/Wedding photos"
        }
    ]
}
```

### Description
Returns a list of file requests owned by this user. For apps with the app folder permission, this will only return file requests with destinations in the app folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.read
### Query Parameters
Void
### Return Values
[ListFileRequestsResult](#data-types-listfilerequestsresult)

Result for [file_requests/list](#file_requests-list).

Field Name | Data Type | Description
--------- | ------- | -----------
file_requests | List[[FileRequest](#data-types-filerequest)] | The file requests owned by this user. Apps with the app folder permission will only see file requests in their app folder.<br>
### Error Values
[ListFileRequestsError](#data-types-listfilerequestserror)

There was an error retrieving the file requests.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
## list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "file_requests": [
        {
            "id": "oaCAVmEyrqYnkZX9955Y", 
            "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
            "title": "Homework submission", 
            "created": "2015-10-05T17:00:00Z", 
            "is_open": true, 
            "file_count": 3, 
            "destination": "/File Requests/Homework", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z", 
                "allow_late_uploads": {
                    ".tag": "seven_days"
                }
            }
        }, 
        {
            "id": "BAJ7IrRGicQKGToykQdB", 
            "url": "https://www.dropbox.com/request/BAJ7IrRGjcQKGToykQdB", 
            "title": "Photo contest submission", 
            "created": "2015-11-02T04:00:00Z", 
            "is_open": true, 
            "file_count": 105, 
            "destination": "/Photo contest entries", 
            "deadline": {
                "deadline": "2020-10-12T17:00:00Z"
            }
        }, 
        {
            "id": "rxwMPvK3ATTa0VxOJu5T", 
            "url": "https://www.dropbox.com/request/rxwMPvK3ATTa0VxOJu5T", 
            "title": "Wedding photo submission", 
            "created": "2015-12-15T13:02:00Z", 
            "is_open": true, 
            "file_count": 37, 
            "destination": "/Wedding photos"
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": true
}
```

### Description
Once a cursor has been retrieved from list:2, use this to paginate through all file requests. The cursor must come from a previous call to list:2 or list/continue.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.read
### Query Parameters
[ListFileRequestsContinueArg](#data-types-listfilerequestscontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by the previous API call specified in the endpoint description.<br>
### Return Values
[ListFileRequestsV2Result](#data-types-listfilerequestsv2result)

Result for [file_requests/list:2](#file_requests-list_v2) and [file_requests/list/continue](#file_requests-list-continue).

Field Name | Data Type | Description
--------- | ------- | -----------
file_requests | List[[FileRequest](#data-types-filerequest)] | The file requests owned by this user. Apps with the app folder permission will only see file requests in their app folder.<br>
cursor | String | Pass the cursor into [file_requests/list/continue](#file_requests-list-continue) to obtain additional file requests.<br>
has_more | Boolean | Is true if there are additional file requests that have not been returned yet. An additional call to :route:list/continue` can retrieve them.<br>
### Error Values
[ListFileRequestsContinueError](#data-types-listfilerequestscontinueerror)

There was an error retrieving the file requests.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
invalid_cursor | Void | The cursor is invalid.<br>
## update
```shell
curl -X POST https://api.dropboxapi.com/2/file_requests/update \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"oaCAVmEyrqYnkZX9955Y\",\"title\": \"Homework submission\",\"destination\": \"/File Requests/Homework\",\"deadline\": {\".tag\": \"update\",\"deadline\": \"2020-10-12T17:00:00Z\",\"allow_late_uploads\": \"seven_days\"},\"open\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "oaCAVmEyrqYnkZX9955Y", 
    "url": "https://www.dropbox.com/request/oaCAVmEyrqYnkZX9955Y", 
    "title": "Homework submission", 
    "created": "2015-10-05T17:00:00Z", 
    "is_open": true, 
    "file_count": 3, 
    "destination": "/File Requests/Homework", 
    "deadline": {
        "deadline": "2020-10-12T17:00:00Z", 
        "allow_late_uploads": {
            ".tag": "seven_days"
        }
    }
}
```

### Description
Update a file request.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
file_requests.write
### Query Parameters
[UpdateFileRequestArgs](#data-types-updatefilerequestargs)

Arguments for [file_requests/update](#file_requests-update).

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The ID of the file request to update.<br>
title | Optional[String] | The new title of the file request. Must not be empty.<br>
destination | Optional[String] | The new path of the folder in the Dropbox where uploaded files will be sent. For apps with the app folder permission, this will be relative to the app folder.<br>
deadline | [UpdateFileRequestDeadline](#data-types-updatefilerequestdeadline) | The new deadline for the file request. Deadlines can only be set by Professional and Business accounts.<br>
open | Optional[Boolean] | Whether to set this file request as open or closed.<br>
### Return Values
[FileRequest](#data-types-filerequest)

A [file request](https://www.dropbox.com/help/9090) for receiving files into the user's Dropbox account.

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The ID of the file request.<br>
url | String | The URL of the file request.<br>
title | String | The title of the file request.<br>
created | Timestamp | When this file request was created.<br>
is_open | Boolean | Whether or not the file request is open. If the file request is closed, it will not accept any more file submissions.<br>
file_count | Int64 | The number of files this file request has received.<br>
destination | Optional[String] | The path of the folder in the Dropbox where uploaded files will be sent. This can be null if the destination was removed. For apps with the app folder permission, this will be relative to the app folder.<br>
deadline | Optional[[FileRequestDeadline](#data-types-filerequestdeadline)] | The deadline for this file request. Only set if the request has a deadline.<br>
### Error Values
[UpdateFileRequestError](#data-types-updatefilerequesterror)

There is an error updating the file request.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
disabled_for_team | Void | This user's Dropbox Business team doesn't allow file requests.<br>
other | Void | 
not_found | Void | This file request ID was not found.<br>
not_a_folder | Void | The specified path is not a folder.<br>
app_lacks_access | Void | This file request is not accessible to this app. Apps with the app folder permission can only access file requests in their app folder.<br>
no_permission | Void | This user doesn't have permission to access or modify this file request.<br>
email_unverified | Void | This user's email address is not verified. File requests are only available on accounts with a verified email address. Users can verify their email address [here](https://www.dropbox.com/help/317).<br>
validation_error | Void | There was an error validating the request. For example, the title was invalid, or there were disallowed characters in the destination path.<br>
# Files
## alpha/get_metadata
```shell
curl -X POST https://api.dropboxapi.com/2/files/alpha/get_metadata \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math\",\"include_media_info\": false,\"include_deleted\": false,\"include_has_explicit_shared_members\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Returns the metadata for a file or folder. This is an alpha endpoint compatible with the properties API.
Note: Metadata for the root folder is unsupported.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[AlphaGetMetadataArg](#data-types-alphagetmetadataarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path of a file or folder on Dropbox.<br>
include_media_info | Boolean | If true, [FileMetadata.media_info](#data-types-filemetadata) is set for photo and video.<br>
include_deleted | Boolean | If true, [DeletedMetadata](#data-types-deletedmetadata) will be returned for deleted file or folder, otherwise [LookupError.not_found](#data-types-lookuperror) will be returned.<br>
include_has_explicit_shared_members | Boolean | If true, the results will include a flag for each file indicating whether or not  that file has any explicit members.<br>
include_property_groups | Optional[[TemplateFilterBase](#data-types-templatefilterbase)] | If set to a valid list of template IDs, [FileMetadata.property_groups](#data-types-filemetadata) is set if there exists property data associated with the file and each of the listed templates.<br>
include_property_templates | Optional[List[String]] | Field is deprecated. If set to a valid list of template IDs, [FileMetadata.property_groups](#data-types-filemetadata) is set for files with custom properties.<br>
### Return Values
[Metadata](#data-types-metadata)

Metadata for a file or folder.

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
### Error Values
[AlphaGetMetadataError](#data-types-alphagetmetadataerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
properties_error | [LookUpPropertiesError](#data-types-lookuppropertieserror) | 
## alpha/upload
```shell
curl -X POST https://content.dropboxapi.com/2/files/alpha/upload \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/Homework/math/Matrices.txt\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Create a new file with the contents provided in the request. Note that this endpoint is part of the properties API alpha and is slightly different from upload.
Do not use this to upload a file larger than 150 MB. Instead, create an upload session with upload_session/start.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Query Parameters
[CommitInfoWithProperties](#data-types-commitinfowithproperties)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to save the file.<br>
mode | [WriteMode](#data-types-writemode) | Selects what to do if the file already exists.<br>
autorename | Boolean | If there's a conflict, as determined by [mode](#data-types-commitinfowithproperties), have the Dropbox server try to autorename the file to avoid conflict.<br>
client_modified | Optional[Timestamp] | The value to store as the [client_modified](#data-types-commitinfowithproperties) timestamp. Dropbox automatically records the time at which the file was written to the Dropbox servers. It can also record an additional timestamp, provided by Dropbox desktop clients, mobile clients, and API apps of when the file was actually created or modified.<br>
mute | Boolean | Normally, users are made aware of any file modifications in their Dropbox account via notifications in the client software. If true, this tells the clients that this modification shouldn't result in a user notification.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | List of custom properties to add to file.<br>
strict_conflict | Boolean | Be more strict about how each [WriteMode](#data-types-writemode) detects conflict. For example, always return a conflict error when [mode](#data-types-commitinfowithproperties) = [WriteMode.update](#data-types-writemode) and the given "rev" doesn't match the existing file's "rev", even if the existing file has been deleted.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[UploadErrorWithProperties](#data-types-uploaderrorwithproperties)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [UploadWriteFailed](#data-types-uploadwritefailed) | Unable to save the uploaded contents to a file.<br>
properties_error | [InvalidPropertyGroupError](#data-types-invalidpropertygrouperror) | The supplied property group is invalid. The file has uploaded without property groups.<br>
other | Void | 
## copy_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\",\"allow_shared_folder\": false,\"autorename\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        ".tag": "file", 
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }
}
```

### Description
Copy a file or folder to a different location in the user's Dropbox.
If the source path is a folder all its contents will be copied.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationArg](#data-types-relocationarg)

Field Name | Data Type | Description
--------- | ------- | -----------
from_path | String | Path in the user's Dropbox to be copied or moved.<br>
to_path | String | Path in the user's Dropbox that is the destination.<br>
allow_shared_folder | Boolean | If true, [files/copy](#files-copy) will copy contents in shared folder, otherwise [RelocationError.cant_copy_shared_folder](#data-types-relocationerror) will be returned if [from_path](#data-types-relocationarg) contains shared folder. This field is always true for [files/move](#files-move).<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the file to avoid the conflict.<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[RelocationResult](#data-types-relocationresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [Metadata](#data-types-metadata) | Metadata of the relocated object.<br>
### Error Values
[RelocationError](#data-types-relocationerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
from_lookup | [LookupError](#data-types-lookuperror) | 
from_write | [WriteError](#data-types-writeerror) | 
to | [WriteError](#data-types-writeerror) | 
cant_copy_shared_folder | Void | Shared folders can't be copied.<br>
cant_nest_shared_folder | Void | Your move operation would result in nested shared folders.  This is not allowed.<br>
cant_move_folder_into_itself | Void | You cannot move a folder into itself.<br>
too_many_files | Void | The operation would involve more than 10,000 files and folders.<br>
duplicated_or_nested_paths | Void | There are duplicated/nested paths among [RelocationArg.from_path](#data-types-relocationarg) and [RelocationArg.to_path](#data-types-relocationarg).<br>
cant_transfer_ownership | Void | Your move operation would result in an ownership transfer. You may reissue the request with the field [RelocationArg.allow_ownership_transfer](#data-types-relocationarg) to true.<br>
insufficient_quota | Void | The current user does not have enough space to move or copy the files.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
cant_move_shared_folder | Void | Can't move the shared folder to the given destination.<br>
other | Void | 
## copy
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\",\"allow_shared_folder\": false,\"autorename\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Copy a file or folder to a different location in the user's Dropbox.
If the source path is a folder all its contents will be copied.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationArg](#data-types-relocationarg)

Field Name | Data Type | Description
--------- | ------- | -----------
from_path | String | Path in the user's Dropbox to be copied or moved.<br>
to_path | String | Path in the user's Dropbox that is the destination.<br>
allow_shared_folder | Boolean | If true, [files/copy](#files-copy) will copy contents in shared folder, otherwise [RelocationError.cant_copy_shared_folder](#data-types-relocationerror) will be returned if [from_path](#data-types-relocationarg) contains shared folder. This field is always true for [files/move](#files-move).<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the file to avoid the conflict.<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[Metadata](#data-types-metadata)

Metadata for a file or folder.

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
### Error Values
[RelocationError](#data-types-relocationerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
from_lookup | [LookupError](#data-types-lookuperror) | 
from_write | [WriteError](#data-types-writeerror) | 
to | [WriteError](#data-types-writeerror) | 
cant_copy_shared_folder | Void | Shared folders can't be copied.<br>
cant_nest_shared_folder | Void | Your move operation would result in nested shared folders.  This is not allowed.<br>
cant_move_folder_into_itself | Void | You cannot move a folder into itself.<br>
too_many_files | Void | The operation would involve more than 10,000 files and folders.<br>
duplicated_or_nested_paths | Void | There are duplicated/nested paths among [RelocationArg.from_path](#data-types-relocationarg) and [RelocationArg.to_path](#data-types-relocationarg).<br>
cant_transfer_ownership | Void | Your move operation would result in an ownership transfer. You may reissue the request with the field [RelocationArg.allow_ownership_transfer](#data-types-relocationarg) to true.<br>
insufficient_quota | Void | The current user does not have enough space to move or copy the files.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
cant_move_shared_folder | Void | Can't move the shared folder to the given destination.<br>
other | Void | 
## copy_batch_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_batch_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\"}],\"autorename\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "success": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Copy multiple files or folders to different locations at once in the user's Dropbox.
This route will replace copy_batch:1. The main difference is this route will return status for each entry, while copy_batch:1 raises failure if any entry fails.
This route will either finish synchronously, or return a job ID and do the async copy job in background. Please use copy_batch/check:2 to check the job status.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationBatchArgBase](#data-types-relocationbatchargbase)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[RelocationPath](#data-types-relocationpath)] | List of entries to be moved or copied. Each entry is [RelocationPath](#data-types-relocationpath).<br>
autorename | Boolean | If there's a conflict with any file, have the Dropbox server try to autorename that file to avoid the conflict.<br>
### Return Values
[RelocationBatchV2Launch](#data-types-relocationbatchv2launch)

Result returned by [files/copy_batch:2](#files-copy_batch_v2) or [files/move_batch:2](#files-move_batch_v2) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [RelocationBatchV2Result](#data-types-relocationbatchv2result) | 
### Error Values
Void
## copy_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\"}],\"autorename\": false,\"allow_shared_folder\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Copy multiple files or folders to different locations at once in the user's Dropbox.
If [RelocationBatchArg.allow_shared_folder](#data-types-relocationbatcharg) is false, this route is atomic. If one entry fails, the whole transaction will abort. If [RelocationBatchArg.allow_shared_folder](#data-types-relocationbatcharg) is true, atomicity is not guaranteed, but it allows you to copy the contents of shared folders to new locations.
This route will return job ID immediately and do the async copy job in background. Please use copy_batch/check:1 to check the job status.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationBatchArg](#data-types-relocationbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[RelocationPath](#data-types-relocationpath)] | List of entries to be moved or copied. Each entry is [RelocationPath](#data-types-relocationpath).<br>
autorename | Boolean | If there's a conflict with any file, have the Dropbox server try to autorename that file to avoid the conflict.<br>
allow_shared_folder | Boolean | If true, [files/copy_batch](#files-copy_batch) will copy contents in shared folder, otherwise [RelocationError.cant_copy_shared_folder](#data-types-relocationerror) will be returned if [RelocationPath.from_path](#data-types-relocationpath) contains shared folder. This field is always true for [files/move_batch](#files-move_batch).<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[RelocationBatchLaunch](#data-types-relocationbatchlaunch)

Result returned by [files/copy_batch](#files-copy_batch) or [files/move_batch](#files-move_batch) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [RelocationBatchResult](#data-types-relocationbatchresult) | 
other | Void | 
### Error Values
Void
## copy_batch/check_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_batch/check_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "success": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for copy_batch:2. It returns list of results for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[RelocationBatchV2JobStatus](#data-types-relocationbatchv2jobstatus)

Result returned by [files/copy_batch/check:2](#files-copy_batch-check_v2) or [files/move_batch/check:2](#files-move_batch-check_v2) that may either be in progress or completed with result for each entry.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [RelocationBatchV2Result](#data-types-relocationbatchv2result) | The copy or move batch job has finished.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## copy_batch/check
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_batch/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for copy_batch:1. If success, it returns list of results for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[RelocationBatchJobStatus](#data-types-relocationbatchjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [RelocationBatchResult](#data-types-relocationbatchresult) | The copy or move batch job has finished.<br>
failed | [RelocationBatchError](#data-types-relocationbatcherror) | The copy or move batch job has failed with exception.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## copy_reference/get
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_reference/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/video.mp4\"}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        ".tag": "file", 
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }, 
    "copy_reference": "z1X6ATl6aWtzOGq0c3g5Ng", 
    "expires": "2045-05-12T15:50:38Z"
}
```

### Description
Get a copy reference to a file or folder. This reference string can be used to save that file or folder to another user's Dropbox by passing it to copy_reference/save.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[GetCopyReferenceArg](#data-types-getcopyreferencearg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to the file or folder you want to get a copy reference to.<br>
### Return Values
[GetCopyReferenceResult](#data-types-getcopyreferenceresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [Metadata](#data-types-metadata) | Metadata of the file or folder.<br>
copy_reference | String | A copy reference to the file or folder.<br>
expires | Timestamp | The expiration date of the copy reference. This value is currently set to be far enough in the future so that expiration is effectively not an issue.<br>
### Error Values
[GetCopyReferenceError](#data-types-getcopyreferenceerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
other | Void | 
## copy_reference/save
```shell
curl -X POST https://api.dropboxapi.com/2/files/copy_reference/save \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"copy_reference\": \"z1X6ATl6aWtzOGq0c3g5Ng\",\"path\": \"/video.mp4\"}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        ".tag": "file", 
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }
}
```

### Description
Save a copy reference returned by copy_reference/get to the user's Dropbox.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[SaveCopyReferenceArg](#data-types-savecopyreferencearg)

Field Name | Data Type | Description
--------- | ------- | -----------
copy_reference | String | A copy reference returned by [files/copy_reference/get](#files-copy_reference-get).<br>
path | String | Path in the user's Dropbox that is the destination.<br>
### Return Values
[SaveCopyReferenceResult](#data-types-savecopyreferenceresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [Metadata](#data-types-metadata) | The metadata of the saved file or folder in the user's Dropbox.<br>
### Error Values
[SaveCopyReferenceError](#data-types-savecopyreferenceerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [WriteError](#data-types-writeerror) | 
invalid_copy_reference | Void | The copy reference is invalid.<br>
no_permission | Void | You don't have permission to save the given copy reference. Please make sure this app is same app which created the copy reference and the source user is still linked to the app.<br>
not_found | Void | The file referenced by the copy reference cannot be found.<br>
too_many_files | Void | The operation would involve more than 10,000 files and folders.<br>
other | Void | 
## create_folder_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/create_folder_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math\",\"autorename\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        "name": "math", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
        "path_lower": "/homework/math", 
        "path_display": "/Homework/math", 
        "sharing_info": {
            "read_only": false, 
            "parent_shared_folder_id": "84528192421", 
            "traverse_only": false, 
            "no_access": false
        }, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ]
    }
}
```

### Description
Create a folder at a given path.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[CreateFolderArg](#data-types-createfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to create.<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the folder to avoid the conflict.<br>
### Return Values
[CreateFolderResult](#data-types-createfolderresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [FolderMetadata](#data-types-foldermetadata) | Metadata of the created folder.<br>
### Error Values
[CreateFolderError](#data-types-createfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [WriteError](#data-types-writeerror) | 
## create_folder
```shell
curl -X POST https://api.dropboxapi.com/2/files/create_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math\",\"autorename\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "math", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
    "path_lower": "/homework/math", 
    "path_display": "/Homework/math", 
    "sharing_info": {
        "read_only": false, 
        "parent_shared_folder_id": "84528192421", 
        "traverse_only": false, 
        "no_access": false
    }, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ]
}
```

### Description
Create a folder at a given path.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[CreateFolderArg](#data-types-createfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to create.<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the folder to avoid the conflict.<br>
### Return Values
[FolderMetadata](#data-types-foldermetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the folder.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
shared_folder_id | Optional[String] | Field is deprecated. Please use [sharing_info](#data-types-foldermetadata) instead.<br>
sharing_info | Optional[[FolderSharingInfo](#data-types-foldersharinginfo)] | Set if the folder is contained in a shared folder or is a shared folder mount point.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified. Note that only properties associated with user-owned templates, not team-owned templates, can be attached to folders.<br>
### Error Values
[CreateFolderError](#data-types-createfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [WriteError](#data-types-writeerror) | 
## create_folder_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/create_folder_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"paths\": [\"/Homework/math\"],\"autorename\": false,\"force_async\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                "name": "math", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
                "path_lower": "/homework/math", 
                "path_display": "/Homework/math", 
                "sharing_info": {
                    "read_only": false, 
                    "parent_shared_folder_id": "84528192421", 
                    "traverse_only": false, 
                    "no_access": false
                }, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

### Description
Create multiple folders at once.
This route is asynchronous for large batches, which returns a job ID immediately and runs the create folder batch asynchronously. Otherwise, creates the folders and returns the result synchronously for smaller inputs. You can force asynchronous behaviour by using the [CreateFolderBatchArg.force_async](#data-types-createfolderbatcharg) flag.  Use create_folder_batch/check to check the job status.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[CreateFolderBatchArg](#data-types-createfolderbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
paths | List[String] | List of paths to be created in the user's Dropbox. Duplicate path arguments in the batch are considered only once.<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the folder to avoid the conflict.<br>
force_async | Boolean | Whether to force the create to happen asynchronously.<br>
### Return Values
[CreateFolderBatchLaunch](#data-types-createfolderbatchlaunch)

Result returned by [files/create_folder_batch](#files-create_folder_batch) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [CreateFolderBatchResult](#data-types-createfolderbatchresult) | 
other | Void | 
### Error Values
Void
## create_folder_batch/check
```shell
curl -X POST https://api.dropboxapi.com/2/files/create_folder_batch/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                "name": "math", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
                "path_lower": "/homework/math", 
                "path_display": "/Homework/math", 
                "sharing_info": {
                    "read_only": false, 
                    "parent_shared_folder_id": "84528192421", 
                    "traverse_only": false, 
                    "no_access": false
                }, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for create_folder_batch. If success, it returns list of result for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[CreateFolderBatchJobStatus](#data-types-createfolderbatchjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [CreateFolderBatchResult](#data-types-createfolderbatchresult) | The batch create folder has finished.<br>
failed | [CreateFolderBatchError](#data-types-createfolderbatcherror) | The batch create folder has failed.<br>
other | Void | 
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## delete_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/delete_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math/Prime_Numbers.txt\"}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        ".tag": "file", 
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }
}
```

### Description
Delete the file or folder at a given path.
If the path is a folder, all its contents will be deleted too.
A successful response indicates that the file or folder was deleted. The returned metadata will be the corresponding [FileMetadata](#data-types-filemetadata) or [FolderMetadata](#data-types-foldermetadata) for the item at time of deletion, and not a [DeletedMetadata](#data-types-deletedmetadata) object.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[DeleteArg](#data-types-deletearg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to delete.<br>
parent_rev | Optional[String] | Perform delete if given "rev" matches the existing file's latest "rev". This field does not support deleting a folder.<br>
### Return Values
[DeleteResult](#data-types-deleteresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [Metadata](#data-types-metadata) | Metadata of the deleted object.<br>
### Error Values
[DeleteError](#data-types-deleteerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | 
path_write | [WriteError](#data-types-writeerror) | 
too_many_write_operations | Void | There are too many write operations in user's Dropbox. Please retry this request.<br>
too_many_files | Void | There are too many files in one request. Please retry with fewer files.<br>
other | Void | 
## delete
```shell
curl -X POST https://api.dropboxapi.com/2/files/delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math/Prime_Numbers.txt\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Delete the file or folder at a given path.
If the path is a folder, all its contents will be deleted too.
A successful response indicates that the file or folder was deleted. The returned metadata will be the corresponding [FileMetadata](#data-types-filemetadata) or [FolderMetadata](#data-types-foldermetadata) for the item at time of deletion, and not a [DeletedMetadata](#data-types-deletedmetadata) object.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[DeleteArg](#data-types-deletearg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to delete.<br>
parent_rev | Optional[String] | Perform delete if given "rev" matches the existing file's latest "rev". This field does not support deleting a folder.<br>
### Return Values
[Metadata](#data-types-metadata)

Metadata for a file or folder.

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
### Error Values
[DeleteError](#data-types-deleteerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | 
path_write | [WriteError](#data-types-writeerror) | 
too_many_write_operations | Void | There are too many write operations in user's Dropbox. Please retry this request.<br>
too_many_files | Void | There are too many files in one request. Please retry with fewer files.<br>
other | Void | 
## delete_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/delete_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"path\": \"/Homework/math/Prime_Numbers.txt\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Delete multiple files/folders at once.
This route is asynchronous, which returns a job ID immediately and runs the delete batch asynchronously. Use delete_batch/check to check the job status.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[DeleteBatchArg](#data-types-deletebatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[DeleteArg](#data-types-deletearg)] | 
### Return Values
[DeleteBatchLaunch](#data-types-deletebatchlaunch)

Result returned by [files/delete_batch](#files-delete_batch) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [DeleteBatchResult](#data-types-deletebatchresult) | 
other | Void | 
### Error Values
Void
## delete_batch/check
```shell
curl -X POST https://api.dropboxapi.com/2/files/delete_batch/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for delete_batch. If success, it returns list of result for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[DeleteBatchJobStatus](#data-types-deletebatchjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [DeleteBatchResult](#data-types-deletebatchresult) | The batch delete has finished.<br>
failed | [DeleteBatchError](#data-types-deletebatcherror) | The batch delete has failed.<br>
other | Void | 
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## download
```shell
curl -X POST https://content.dropboxapi.com/2/files/download \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/Homework/math/Prime_Numbers.txt\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Download a file from a user's Dropbox.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[DownloadArg](#data-types-downloadarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path of the file to download.<br>
rev | Optional[String] | Field is deprecated. Please specify revision in [path](#data-types-downloadarg) instead.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[DownloadError](#data-types-downloaderror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
unsupported_file | Void | This file type cannot be downloaded directly; use [files/export](#files-export) instead.<br>
other | Void | 
## download_zip
```shell
curl -X POST https://content.dropboxapi.com/2/files/download_zip \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/Homework/math\"}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        "name": "math", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
        "path_lower": "/homework/math", 
        "path_display": "/Homework/math", 
        "sharing_info": {
            "read_only": false, 
            "parent_shared_folder_id": "84528192421", 
            "traverse_only": false, 
            "no_access": false
        }, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ]
    }
}
```

### Description
Download a folder from the user's Dropbox, as a zip file. The folder must be less than 20 GB in size and have fewer than 10,000 total files. The input cannot be a single file. Any single file must be less than 4GB in size.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[DownloadZipArg](#data-types-downloadziparg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path of the folder to download.<br>
### Return Values
[DownloadZipResult](#data-types-downloadzipresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [FolderMetadata](#data-types-foldermetadata) | 
### Error Values
[DownloadZipError](#data-types-downloadziperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
too_large | Void | The folder or a file is too large to download.<br>
too_many_files | Void | The folder has too many files to download.<br>
other | Void | 
## export
```shell
curl -X POST https://content.dropboxapi.com/2/files/export \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/Homework/math/Prime_Numbers.gsheet\"}"
```

> The above command returns JSON structured like this:

```json
{
    "export_metadata": {
        "name": "Prime_Numbers.xlsx", 
        "size": 7189, 
        "export_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }, 
    "file_metadata": {
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }
}
```

### Description
Export a file from a user's Dropbox. This route only supports exporting files that cannot be downloaded directly  and whose [ExportResult.file_metadata](#data-types-exportresult) has [ExportInfo.export_as](#data-types-exportinfo) populated.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[ExportArg](#data-types-exportarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path of the file to be exported.<br>
### Return Values
[ExportResult](#data-types-exportresult)

Field Name | Data Type | Description
--------- | ------- | -----------
export_metadata | [ExportMetadata](#data-types-exportmetadata) | Metadata for the exported version of the file.<br>
file_metadata | [FileMetadata](#data-types-filemetadata) | Metadata for the original file.<br>
### Error Values
[ExportError](#data-types-exporterror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
non_exportable | Void | This file type cannot be exported. Use [files/download](#files-download) instead.<br>
retry_error | Void | The exportable content is not yet available. Please retry later.<br>
other | Void | 
## get_file_lock_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/get_file_lock_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"path\": \"/John Doe/sample/test.pdf\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }, 
            "lock": {
                "content": {
                    ".tag": "single_user", 
                    "created": "2015-05-12T15:50:38Z", 
                    "lock_holder_account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                    "lock_holder_team_id": "dbtid:1234abcd"
                }
            }
        }
    ]
}
```

### Description
Return the lock metadata for the given list of paths.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.read
### Query Parameters
[LockFileBatchArg](#data-types-lockfilebatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LockFileArg](#data-types-lockfilearg)] | List of 'entries'. Each 'entry' contains a path of the file which will be locked or queried. Duplicate path arguments in the batch are considered only once.<br>
### Return Values
[LockFileBatchResult](#data-types-lockfilebatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LockFileResultEntry](#data-types-lockfileresultentry)] | Each Entry in the 'entries' will have '.tag' with the operation status (e.g. success), the metadata for the file and the lock state after the operation.<br>
### Error Values
[LockFileError](#data-types-lockfileerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | Could not find the specified resource.<br>
too_many_write_operations | Void | There are too many write operations in user's Dropbox. Please retry this request.<br>
too_many_files | Void | There are too many files in one request. Please retry with fewer files.<br>
no_write_permission | Void | The user does not have permissions to change the lock state or access the file.<br>
cannot_be_locked | Void | Item is a type that cannot be locked.<br>
file_not_shared | Void | Requested file is not currently shared.<br>
lock_conflict | [LockConflictError](#data-types-lockconflicterror) | The user action conflicts with an existing lock on the file.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## get_metadata
```shell
curl -X POST https://api.dropboxapi.com/2/files/get_metadata \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math\",\"include_media_info\": false,\"include_deleted\": false,\"include_has_explicit_shared_members\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Returns the metadata for a file or folder.
Note: Metadata for the root folder is unsupported.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[GetMetadataArg](#data-types-getmetadataarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path of a file or folder on Dropbox.<br>
include_media_info | Boolean | If true, [FileMetadata.media_info](#data-types-filemetadata) is set for photo and video.<br>
include_deleted | Boolean | If true, [DeletedMetadata](#data-types-deletedmetadata) will be returned for deleted file or folder, otherwise [LookupError.not_found](#data-types-lookuperror) will be returned.<br>
include_has_explicit_shared_members | Boolean | If true, the results will include a flag for each file indicating whether or not  that file has any explicit members.<br>
include_property_groups | Optional[[TemplateFilterBase](#data-types-templatefilterbase)] | If set to a valid list of template IDs, [FileMetadata.property_groups](#data-types-filemetadata) is set if there exists property data associated with the file and each of the listed templates.<br>
### Return Values
[Metadata](#data-types-metadata)

Metadata for a file or folder.

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
### Error Values
[GetMetadataError](#data-types-getmetadataerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
## get_preview
```shell
curl -X POST https://content.dropboxapi.com/2/files/get_preview \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/word.docx\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Get a preview for a file.
Currently, PDF previews are generated for files with the following extensions: .ai, .doc, .docm, .docx, .eps, .gdoc, .gslides, .odp, .odt, .pps, .ppsm, .ppsx, .ppt, .pptm, .pptx, .rtf.
HTML previews are generated for files with the following extensions: .csv, .ods, .xls, .xlsm, .gsheet, .xlsx.
Other formats will return an unsupported extension error.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[PreviewArg](#data-types-previewarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path of the file to preview.<br>
rev | Optional[String] | Field is deprecated. Please specify revision in [path](#data-types-previewarg) instead.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[PreviewError](#data-types-previewerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | An error occurs when downloading metadata for the file.<br>
in_progress | Void | This preview generation is still in progress and the file is not ready  for preview yet.<br>
unsupported_extension | Void | The file extension is not supported preview generation.<br>
unsupported_content | Void | The file content is not supported for preview generation.<br>
## get_temporary_link
```shell
curl -X POST https://api.dropboxapi.com/2/files/get_temporary_link \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/video.mp4\"}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }, 
    "link": "https://dl.dropboxusercontent.com/apitl/1/YXNkZmFzZGcyMzQyMzI0NjU2NDU2NDU2"
}
```

### Description
Get a temporary link to stream content of a file. This link will expire in four hours and afterwards you will get 410 Gone. This URL should not be used to display content directly in the browser. The Content-Type of the link is determined automatically by the file's mime type.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.read
### Query Parameters
[GetTemporaryLinkArg](#data-types-gettemporarylinkarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to the file you want a temporary link to.<br>
### Return Values
[GetTemporaryLinkResult](#data-types-gettemporarylinkresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [FileMetadata](#data-types-filemetadata) | Metadata of the file.<br>
link | String | The temporary link which can be used to stream content the file.<br>
### Error Values
[GetTemporaryLinkError](#data-types-gettemporarylinkerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
email_not_verified | Void | The user's email address needs to be verified to use this functionality.<br>
unsupported_file | Void | Cannot get temporary link to this file type; use [files/export](#files-export) instead.<br>
other | Void | 
## get_temporary_upload_link
```shell
curl -X POST https://api.dropboxapi.com/2/files/get_temporary_upload_link \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"commit_info\": {\"path\": \"/Homework/math/Matrices.txt\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false},\"duration\": 3600}"
```

> The above command returns JSON structured like this:

```json
{
    "link": "https://content.dropboxapi.com/apitul/1/bNi2uIYF51cVBND"
}
```

### Description
Get a one-time use temporary upload link to upload a file to a Dropbox location.

This endpoint acts as a delayed upload. The returned temporary upload link may be used to make a POST request with the data to be uploaded. The upload will then be perfomed with the [CommitInfo](#data-types-commitinfo) previously provided to get_temporary_upload_link but evaluated only upon consumption. Hence, errors stemming from invalid [CommitInfo](#data-types-commitinfo) with respect to the state of the user's Dropbox will only be communicated at consumption time. Additionally, these errors are surfaced as generic HTTP 409 Conflict responses, potentially hiding issue details. The maximum temporary upload link duration is 4 hours. Upon consumption or expiration, a new link will have to be generated. Multiple links may exist for a specific upload path at any given time.

The POST request on the temporary upload link must have its Content-Type set to "application/octet-stream".

Example temporary upload link consumption request:

curl -X POST https://content.dropboxapi.com/apitul/1/bNi2uIYF51cVBND
--header "Content-Type: application/octet-stream"
--data-binary @local_file.txt

A successful temporary upload link consumption request returns the content hash of the uploaded data in JSON format.

Example succesful temporary upload link consumption response:
{"content-hash": "599d71033d700ac892a0e48fa61b125d2f5994"}

An unsuccessful temporary upload link consumption request returns any of the following status codes:

HTTP 400 Bad Request: Content-Type is not one of application/octet-stream and text/plain or request is invalid.
HTTP 409 Conflict: The temporary upload link does not exist or is currently unavailable, the upload failed, or another error happened.
HTTP 410 Gone: The temporary upload link is expired or consumed.

Example unsuccessful temporary upload link consumption response:
Temporary upload link has been recently consumed.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[GetTemporaryUploadLinkArg](#data-types-gettemporaryuploadlinkarg)

Field Name | Data Type | Description
--------- | ------- | -----------
commit_info | [CommitInfo](#data-types-commitinfo) | Contains the path and other optional modifiers for the future upload commit. Equivalent to the parameters provided to [files/upload](#files-upload).<br>
duration | Float64 | How long before this link expires, in seconds.  Attempting to start an upload with this link longer than this period  of time after link creation will result in an error.<br>
### Return Values
[GetTemporaryUploadLinkResult](#data-types-gettemporaryuploadlinkresult)

Field Name | Data Type | Description
--------- | ------- | -----------
link | String | The temporary link which can be used to stream a file to a Dropbox location.<br>
### Error Values
Void
## get_thumbnail
```shell
curl -X POST https://content.dropboxapi.com/2/files/get_thumbnail \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/image.jpg\",\"format\": \"jpeg\",\"size\": \"w64h64\",\"mode\": \"strict\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Get a thumbnail for an image.
This method currently supports files with the following file extensions: jpg, jpeg, png, tiff, tif, gif and bmp. Photos that are larger than 20MB in size won't be converted to a thumbnail.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[ThumbnailArg](#data-types-thumbnailarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to the image file you want to thumbnail.<br>
format | [ThumbnailFormat](#data-types-thumbnailformat) | The format for the thumbnail image, jpeg (default) or png. For  images that are photos, jpeg should be preferred, while png is  better for screenshots and digital arts.<br>
size | [ThumbnailSize](#data-types-thumbnailsize) | The size for the thumbnail image.<br>
mode | [ThumbnailMode](#data-types-thumbnailmode) | How to resize and crop the image to achieve the desired size.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[ThumbnailError](#data-types-thumbnailerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | An error occurs when downloading metadata for the image.<br>
unsupported_extension | Void | The file extension doesn't allow conversion to a thumbnail.<br>
unsupported_image | Void | The image cannot be converted to a thumbnail.<br>
conversion_error | Void | An error occurs during thumbnail conversion.<br>
## get_thumbnail_v2
```shell
curl -X POST https://content.dropboxapi.com/2/files/get_thumbnail_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"resource\": {\".tag\": \"path\",\"path\": \"/a.docx\"},\"format\": \"jpeg\",\"size\": \"w64h64\",\"mode\": \"strict\"}"
```

> The above command returns JSON structured like this:

```json
{
    "file_metadata": {
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }
}
```

### Description
Get a thumbnail for a file.
### Authentication
App Authentication, User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[ThumbnailV2Arg](#data-types-thumbnailv2arg)

Field Name | Data Type | Description
--------- | ------- | -----------
resource | [PathOrLink](#data-types-pathorlink) | Information specifying which file to preview. This could be a path to a file, a shared link pointing to a file, or a shared link pointing to a folder, with a relative path.<br>
format | [ThumbnailFormat](#data-types-thumbnailformat) | The format for the thumbnail image, jpeg (default) or png. For  images that are photos, jpeg should be preferred, while png is  better for screenshots and digital arts.<br>
size | [ThumbnailSize](#data-types-thumbnailsize) | The size for the thumbnail image.<br>
mode | [ThumbnailMode](#data-types-thumbnailmode) | How to resize and crop the image to achieve the desired size.<br>
### Return Values
[PreviewResult](#data-types-previewresult)

Field Name | Data Type | Description
--------- | ------- | -----------
file_metadata | Optional[[FileMetadata](#data-types-filemetadata)] | Metadata corresponding to the file received as an argument. Will be populated if the endpoint is called with a path (ReadPath).<br>
link_metadata | Optional[[MinimalFileLinkMetadata](#data-types-minimalfilelinkmetadata)] | Minimal metadata corresponding to the file received as an argument. Will be populated if the endpoint is called using a shared link (SharedLinkFileInfo).<br>
### Error Values
[ThumbnailV2Error](#data-types-thumbnailv2error)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | An error occurred when downloading metadata for the image.<br>
unsupported_extension | Void | The file extension doesn't allow conversion to a thumbnail.<br>
unsupported_image | Void | The image cannot be converted to a thumbnail.<br>
conversion_error | Void | An error occurred during thumbnail conversion.<br>
access_denied | Void | Access to this shared link is forbidden.<br>
not_found | Void | The shared link does not exist.<br>
other | Void | 
## get_thumbnail_batch
```shell
curl -X POST https://content.dropboxapi.com/2/files/get_thumbnail_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"path\": \"/image.jpg\",\"format\": \"jpeg\",\"size\": \"w64h64\",\"mode\": \"strict\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }, 
            "thumbnail": "iVBORw0KGgoAAAANSUhEUgAAAdcAAABrCAMAAAI="
        }
    ]
}
```

### Description
Get thumbnails for a list of images. We allow up to 25 thumbnails in a single batch.
This method currently supports files with the following file extensions: jpg, jpeg, png, tiff, tif, gif and bmp. Photos that are larger than 20MB in size won't be converted to a thumbnail.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.read
### Query Parameters
[GetThumbnailBatchArg](#data-types-getthumbnailbatcharg)

Arguments for [files/get_thumbnail_batch](#files-get_thumbnail_batch).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[ThumbnailArg](#data-types-thumbnailarg)] | List of files to get thumbnails.<br>
### Return Values
[GetThumbnailBatchResult](#data-types-getthumbnailbatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[GetThumbnailBatchResultEntry](#data-types-getthumbnailbatchresultentry)] | List of files and their thumbnails.<br>
### Error Values
[GetThumbnailBatchError](#data-types-getthumbnailbatcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
too_many_files | Void | The operation involves more than 25 files.<br>
other | Void | 
## list_folder
```shell
curl -X POST https://api.dropboxapi.com/2/files/list_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math\",\"recursive\": false,\"include_media_info\": false,\"include_deleted\": false,\"include_has_explicit_shared_members\": false,\"include_mounted_folders\": true,\"include_non_downloadable_files\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            ".tag": "file", 
            "name": "Prime_Numbers.txt", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "client_modified": "2015-05-12T15:50:38Z", 
            "server_modified": "2015-05-12T15:50:38Z", 
            "rev": "a1c10ce0dd78", 
            "size": 7212, 
            "path_lower": "/homework/math/prime_numbers.txt", 
            "path_display": "/Homework/math/Prime_Numbers.txt", 
            "sharing_info": {
                "read_only": true, 
                "parent_shared_folder_id": "84528192421", 
                "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
            }, 
            "is_downloadable": true, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ], 
            "has_explicit_shared_members": false, 
            "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
            "file_lock_info": {
                "is_lockholder": true, 
                "lockholder_name": "Imaginary User", 
                "created": "2015-05-12T15:50:38Z"
            }
        }, 
        {
            ".tag": "folder", 
            "name": "math", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
            "path_lower": "/homework/math", 
            "path_display": "/Homework/math", 
            "sharing_info": {
                "read_only": false, 
                "parent_shared_folder_id": "84528192421", 
                "traverse_only": false, 
                "no_access": false
            }, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ]
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Starts returning the contents of a folder. If the result's [ListFolderResult.has_more](#data-types-listfolderresult) field is true, call list_folder/continue with the returned [ListFolderResult.cursor](#data-types-listfolderresult) to retrieve more entries.
If you're using [ListFolderArg.recursive](#data-types-listfolderarg) set to true to keep a local cache of the contents of a Dropbox account, iterate through each entry in order and process them as follows to keep your local state in sync:
For each [FileMetadata](#data-types-filemetadata), store the new entry at the given path in your local state. If the required parent folders don't exist yet, create them. If there's already something else at the given path, replace it and remove all its children.
For each [FolderMetadata](#data-types-foldermetadata), store the new entry at the given path in your local state. If the required parent folders don't exist yet, create them. If there's already something else at the given path, replace it but leave the children as they are. Check the new entry's [FolderSharingInfo.read_only](#data-types-foldersharinginfo) and set all its children's read-only statuses to match.
For each [DeletedMetadata](#data-types-deletedmetadata), if your local state has something at the given path, remove it and all its children. If there's nothing at the given path, ignore this entry.
Note: [auth.RateLimitError](#data-types-auth.ratelimiterror) may be returned if multiple list_folder or list_folder/continue calls with same parameters are made simultaneously by same API app for same user. If your app implements retry logic, please hold off the retry until the previous request finishes.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListFolderArg](#data-types-listfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file.<br>
recursive | Boolean | If true, the list folder operation will be applied recursively to all subfolders and the response will contain contents of all subfolders.<br>
include_media_info | Boolean | Field is deprecated. If true, [FileMetadata.media_info](#data-types-filemetadata) is set for photo and video. This parameter will no longer have an effect starting December 2, 2019.<br>
include_deleted | Boolean | If true, the results will include entries for files and folders that used to exist but were deleted.<br>
include_has_explicit_shared_members | Boolean | If true, the results will include a flag for each file indicating whether or not  that file has any explicit members.<br>
include_mounted_folders | Boolean | If true, the results will include entries under mounted folders which includes app folder, shared folder and team folder.<br>
limit | Optional[UInt32] | The maximum number of results to return per request. Note: This is an approximate number and there can be slightly more entries returned in some cases.<br>
shared_link | Optional[[SharedLink](#data-types-sharedlink)] | A shared link to list the contents of. If the link is password-protected, the password must be provided. If this field is present, [ListFolderArg.path](#data-types-listfolderarg) will be relative to root of the shared link. Only non-recursive mode is supported for shared link.<br>
include_property_groups | Optional[[TemplateFilterBase](#data-types-templatefilterbase)] | If set to a valid list of template IDs, [FileMetadata.property_groups](#data-types-filemetadata) is set if there exists property data associated with the file and each of the listed templates.<br>
include_non_downloadable_files | Boolean | If true, include files that are not downloadable, i.e. Google Docs.<br>
### Return Values
[ListFolderResult](#data-types-listfolderresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[Metadata](#data-types-metadata)] | The files and (direct) subfolders in the folder.<br>
cursor | String | Pass the cursor into [files/list_folder/continue](#files-list_folder-continue) to see what's changed in the folder since your previous query.<br>
has_more | Boolean | If true, then there are more entries available. Pass the cursor to [files/list_folder/continue](#files-list_folder-continue) to retrieve the rest.<br>
### Error Values
[ListFolderError](#data-types-listfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
template_error | [TemplateError](#data-types-templateerror) | 
other | Void | 
## list_folder/continue
```shell
curl -X POST https://api.dropboxapi.com/2/files/list_folder/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            ".tag": "file", 
            "name": "Prime_Numbers.txt", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "client_modified": "2015-05-12T15:50:38Z", 
            "server_modified": "2015-05-12T15:50:38Z", 
            "rev": "a1c10ce0dd78", 
            "size": 7212, 
            "path_lower": "/homework/math/prime_numbers.txt", 
            "path_display": "/Homework/math/Prime_Numbers.txt", 
            "sharing_info": {
                "read_only": true, 
                "parent_shared_folder_id": "84528192421", 
                "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
            }, 
            "is_downloadable": true, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ], 
            "has_explicit_shared_members": false, 
            "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
            "file_lock_info": {
                "is_lockholder": true, 
                "lockholder_name": "Imaginary User", 
                "created": "2015-05-12T15:50:38Z"
            }
        }, 
        {
            ".tag": "folder", 
            "name": "math", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXz", 
            "path_lower": "/homework/math", 
            "path_display": "/Homework/math", 
            "sharing_info": {
                "read_only": false, 
                "parent_shared_folder_id": "84528192421", 
                "traverse_only": false, 
                "no_access": false
            }, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ]
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from list_folder, use this to paginate through all files and retrieve updates to the folder, following the same rules as documented for list_folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListFolderContinueArg](#data-types-listfoldercontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by your last call to [files/list_folder](#files-list_folder) or [files/list_folder/continue](#files-list_folder-continue).<br>
### Return Values
[ListFolderResult](#data-types-listfolderresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[Metadata](#data-types-metadata)] | The files and (direct) subfolders in the folder.<br>
cursor | String | Pass the cursor into [files/list_folder/continue](#files-list_folder-continue) to see what's changed in the folder since your previous query.<br>
has_more | Boolean | If true, then there are more entries available. Pass the cursor to [files/list_folder/continue](#files-list_folder-continue) to retrieve the rest.<br>
### Error Values
[ListFolderContinueError](#data-types-listfoldercontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
reset | Void | Indicates that the cursor has been invalidated. Call [files/list_folder](#files-list_folder) to obtain a new cursor.<br>
other | Void | 
## list_folder/get_latest_cursor
```shell
curl -X POST https://api.dropboxapi.com/2/files/list_folder/get_latest_cursor \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math\",\"recursive\": false,\"include_media_info\": false,\"include_deleted\": false,\"include_has_explicit_shared_members\": false,\"include_mounted_folders\": true,\"include_non_downloadable_files\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
A way to quickly get a cursor for the folder's state. Unlike list_folder, list_folder/get_latest_cursor doesn't return any entries. This endpoint is for app which only needs to know about new files and modifications and doesn't need to know about files that already exist in Dropbox.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListFolderArg](#data-types-listfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file.<br>
recursive | Boolean | If true, the list folder operation will be applied recursively to all subfolders and the response will contain contents of all subfolders.<br>
include_media_info | Boolean | Field is deprecated. If true, [FileMetadata.media_info](#data-types-filemetadata) is set for photo and video. This parameter will no longer have an effect starting December 2, 2019.<br>
include_deleted | Boolean | If true, the results will include entries for files and folders that used to exist but were deleted.<br>
include_has_explicit_shared_members | Boolean | If true, the results will include a flag for each file indicating whether or not  that file has any explicit members.<br>
include_mounted_folders | Boolean | If true, the results will include entries under mounted folders which includes app folder, shared folder and team folder.<br>
limit | Optional[UInt32] | The maximum number of results to return per request. Note: This is an approximate number and there can be slightly more entries returned in some cases.<br>
shared_link | Optional[[SharedLink](#data-types-sharedlink)] | A shared link to list the contents of. If the link is password-protected, the password must be provided. If this field is present, [ListFolderArg.path](#data-types-listfolderarg) will be relative to root of the shared link. Only non-recursive mode is supported for shared link.<br>
include_property_groups | Optional[[TemplateFilterBase](#data-types-templatefilterbase)] | If set to a valid list of template IDs, [FileMetadata.property_groups](#data-types-filemetadata) is set if there exists property data associated with the file and each of the listed templates.<br>
include_non_downloadable_files | Boolean | If true, include files that are not downloadable, i.e. Google Docs.<br>
### Return Values
[ListFolderGetLatestCursorResult](#data-types-listfoldergetlatestcursorresult)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Pass the cursor into [files/list_folder/continue](#files-list_folder-continue) to see what's changed in the folder since your previous query.<br>
### Error Values
[ListFolderError](#data-types-listfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
template_error | [TemplateError](#data-types-templateerror) | 
other | Void | 
## list_folder/longpoll
```shell
curl -X POST https://notify.dropboxapi.com/2/files/list_folder/longpoll \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\",\"timeout\": 30}"
```

> The above command returns JSON structured like this:

```json
{
    "changes": true
}
```

### Description
A longpoll endpoint to wait for changes on an account. In conjunction with list_folder/continue, this call gives you a low-latency way to monitor an account for file changes. The connection will block until there are changes available or a timeout occurs. This endpoint is useful mostly for client-side apps. If you're looking for server-side notifications, check out our [webhooks documentation](https://www.dropbox.com/developers/reference/webhooks).
### Authentication
No Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListFolderLongpollArg](#data-types-listfolderlongpollarg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | A cursor as returned by [files/list_folder](#files-list_folder) or [files/list_folder/continue](#files-list_folder-continue). Cursors retrieved by setting [ListFolderArg.include_media_info](#data-types-listfolderarg) to true are not supported.<br>
timeout | UInt64 | A timeout in seconds. The request will block for at most this length of time, plus up to 90 seconds of random jitter added to avoid the thundering herd problem. Care should be taken when using this parameter, as some network infrastructure does not support long timeouts.<br>
### Return Values
[ListFolderLongpollResult](#data-types-listfolderlongpollresult)

Field Name | Data Type | Description
--------- | ------- | -----------
changes | Boolean | Indicates whether new changes are available. If true, call [files/list_folder/continue](#files-list_folder-continue) to retrieve the changes.<br>
backoff | Optional[UInt64] | If present, backoff for at least this many seconds before calling [files/list_folder/longpoll](#files-list_folder-longpoll) again.<br>
### Error Values
[ListFolderLongpollError](#data-types-listfolderlongpollerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
reset | Void | Indicates that the cursor has been invalidated. Call [files/list_folder](#files-list_folder) to obtain a new cursor.<br>
other | Void | 
## list_revisions
```shell
curl -X POST https://api.dropboxapi.com/2/files/list_revisions \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/root/word.docx\",\"mode\": \"path\",\"limit\": 10}"
```

> The above command returns JSON structured like this:

```json
{
    "is_deleted": false, 
    "entries": [
        {
            "name": "Prime_Numbers.txt", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "client_modified": "2015-05-12T15:50:38Z", 
            "server_modified": "2015-05-12T15:50:38Z", 
            "rev": "a1c10ce0dd78", 
            "size": 7212, 
            "path_lower": "/homework/math/prime_numbers.txt", 
            "path_display": "/Homework/math/Prime_Numbers.txt", 
            "sharing_info": {
                "read_only": true, 
                "parent_shared_folder_id": "84528192421", 
                "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
            }, 
            "is_downloadable": true, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ], 
            "has_explicit_shared_members": false, 
            "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
            "file_lock_info": {
                "is_lockholder": true, 
                "lockholder_name": "Imaginary User", 
                "created": "2015-05-12T15:50:38Z"
            }
        }
    ]
}
```

### Description
Returns revisions for files based on a file path or a file id. The file path or file id is identified from the latest file entry at the given file path or id. This end point allows your app to query either by file path or file id by setting the mode parameter appropriately.
In the [ListRevisionsMode.path](#data-types-listrevisionsmode) (default) mode, all revisions at the same file path as the latest file entry are returned. If revisions with the same file id are desired, then mode must be set to [ListRevisionsMode.id](#data-types-listrevisionsmode). The [ListRevisionsMode.id](#data-types-listrevisionsmode) mode is useful to retrieve revisions for a given file across moves or renames.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListRevisionsArg](#data-types-listrevisionsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to the file you want to see the revisions of.<br>
mode | [ListRevisionsMode](#data-types-listrevisionsmode) | Determines the behavior of the API in listing the revisions for a given file path or id.<br>
limit | UInt64 | The maximum number of revision entries returned.<br>
### Return Values
[ListRevisionsResult](#data-types-listrevisionsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
is_deleted | Boolean | If the file identified by the latest revision in the response is either deleted or moved.<br>
entries | List[[FileMetadata](#data-types-filemetadata)] | The revisions for the file. Only revisions that are not deleted will show up here.<br>
server_deleted | Optional[Timestamp] | The time of deletion if the file was deleted.<br>
### Error Values
[ListRevisionsError](#data-types-listrevisionserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
other | Void | 
## lock_file_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/lock_file_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"path\": \"/John Doe/sample/test.pdf\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }, 
            "lock": {
                "content": {
                    ".tag": "single_user", 
                    "created": "2015-05-12T15:50:38Z", 
                    "lock_holder_account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                    "lock_holder_team_id": "dbtid:1234abcd"
                }
            }
        }
    ]
}
```

### Description
Lock the files at the given paths. A locked file will be writable only by the lock holder. A successful response indicates that the file has been locked. Returns a list of the locked file paths and their metadata after this operation.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[LockFileBatchArg](#data-types-lockfilebatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LockFileArg](#data-types-lockfilearg)] | List of 'entries'. Each 'entry' contains a path of the file which will be locked or queried. Duplicate path arguments in the batch are considered only once.<br>
### Return Values
[LockFileBatchResult](#data-types-lockfilebatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LockFileResultEntry](#data-types-lockfileresultentry)] | Each Entry in the 'entries' will have '.tag' with the operation status (e.g. success), the metadata for the file and the lock state after the operation.<br>
### Error Values
[LockFileError](#data-types-lockfileerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | Could not find the specified resource.<br>
too_many_write_operations | Void | There are too many write operations in user's Dropbox. Please retry this request.<br>
too_many_files | Void | There are too many files in one request. Please retry with fewer files.<br>
no_write_permission | Void | The user does not have permissions to change the lock state or access the file.<br>
cannot_be_locked | Void | Item is a type that cannot be locked.<br>
file_not_shared | Void | Requested file is not currently shared.<br>
lock_conflict | [LockConflictError](#data-types-lockconflicterror) | The user action conflicts with an existing lock on the file.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## move_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/move_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\",\"allow_shared_folder\": false,\"autorename\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "metadata": {
        ".tag": "file", 
        "name": "Prime_Numbers.txt", 
        "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
        "client_modified": "2015-05-12T15:50:38Z", 
        "server_modified": "2015-05-12T15:50:38Z", 
        "rev": "a1c10ce0dd78", 
        "size": 7212, 
        "path_lower": "/homework/math/prime_numbers.txt", 
        "path_display": "/Homework/math/Prime_Numbers.txt", 
        "sharing_info": {
            "read_only": true, 
            "parent_shared_folder_id": "84528192421", 
            "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
        }, 
        "is_downloadable": true, 
        "property_groups": [
            {
                "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                "fields": [
                    {
                        "name": "Security Policy", 
                        "value": "Confidential"
                    }
                ]
            }
        ], 
        "has_explicit_shared_members": false, 
        "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
        "file_lock_info": {
            "is_lockholder": true, 
            "lockholder_name": "Imaginary User", 
            "created": "2015-05-12T15:50:38Z"
        }
    }
}
```

### Description
Move a file or folder to a different location in the user's Dropbox.
If the source path is a folder all its contents will be moved.
Note that we do not currently support case-only renaming.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationArg](#data-types-relocationarg)

Field Name | Data Type | Description
--------- | ------- | -----------
from_path | String | Path in the user's Dropbox to be copied or moved.<br>
to_path | String | Path in the user's Dropbox that is the destination.<br>
allow_shared_folder | Boolean | If true, [files/copy](#files-copy) will copy contents in shared folder, otherwise [RelocationError.cant_copy_shared_folder](#data-types-relocationerror) will be returned if [from_path](#data-types-relocationarg) contains shared folder. This field is always true for [files/move](#files-move).<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the file to avoid the conflict.<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[RelocationResult](#data-types-relocationresult)

Field Name | Data Type | Description
--------- | ------- | -----------
metadata | [Metadata](#data-types-metadata) | Metadata of the relocated object.<br>
### Error Values
[RelocationError](#data-types-relocationerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
from_lookup | [LookupError](#data-types-lookuperror) | 
from_write | [WriteError](#data-types-writeerror) | 
to | [WriteError](#data-types-writeerror) | 
cant_copy_shared_folder | Void | Shared folders can't be copied.<br>
cant_nest_shared_folder | Void | Your move operation would result in nested shared folders.  This is not allowed.<br>
cant_move_folder_into_itself | Void | You cannot move a folder into itself.<br>
too_many_files | Void | The operation would involve more than 10,000 files and folders.<br>
duplicated_or_nested_paths | Void | There are duplicated/nested paths among [RelocationArg.from_path](#data-types-relocationarg) and [RelocationArg.to_path](#data-types-relocationarg).<br>
cant_transfer_ownership | Void | Your move operation would result in an ownership transfer. You may reissue the request with the field [RelocationArg.allow_ownership_transfer](#data-types-relocationarg) to true.<br>
insufficient_quota | Void | The current user does not have enough space to move or copy the files.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
cant_move_shared_folder | Void | Can't move the shared folder to the given destination.<br>
other | Void | 
## move
```shell
curl -X POST https://api.dropboxapi.com/2/files/move \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\",\"allow_shared_folder\": false,\"autorename\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Move a file or folder to a different location in the user's Dropbox.
If the source path is a folder all its contents will be moved.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationArg](#data-types-relocationarg)

Field Name | Data Type | Description
--------- | ------- | -----------
from_path | String | Path in the user's Dropbox to be copied or moved.<br>
to_path | String | Path in the user's Dropbox that is the destination.<br>
allow_shared_folder | Boolean | If true, [files/copy](#files-copy) will copy contents in shared folder, otherwise [RelocationError.cant_copy_shared_folder](#data-types-relocationerror) will be returned if [from_path](#data-types-relocationarg) contains shared folder. This field is always true for [files/move](#files-move).<br>
autorename | Boolean | If there's a conflict, have the Dropbox server try to autorename the file to avoid the conflict.<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[Metadata](#data-types-metadata)

Metadata for a file or folder.

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
### Error Values
[RelocationError](#data-types-relocationerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
from_lookup | [LookupError](#data-types-lookuperror) | 
from_write | [WriteError](#data-types-writeerror) | 
to | [WriteError](#data-types-writeerror) | 
cant_copy_shared_folder | Void | Shared folders can't be copied.<br>
cant_nest_shared_folder | Void | Your move operation would result in nested shared folders.  This is not allowed.<br>
cant_move_folder_into_itself | Void | You cannot move a folder into itself.<br>
too_many_files | Void | The operation would involve more than 10,000 files and folders.<br>
duplicated_or_nested_paths | Void | There are duplicated/nested paths among [RelocationArg.from_path](#data-types-relocationarg) and [RelocationArg.to_path](#data-types-relocationarg).<br>
cant_transfer_ownership | Void | Your move operation would result in an ownership transfer. You may reissue the request with the field [RelocationArg.allow_ownership_transfer](#data-types-relocationarg) to true.<br>
insufficient_quota | Void | The current user does not have enough space to move or copy the files.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
cant_move_shared_folder | Void | Can't move the shared folder to the given destination.<br>
other | Void | 
## move_batch_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/move_batch_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\"}],\"autorename\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "success": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Move multiple files or folders to different locations at once in the user's Dropbox. Note that we do not currently support case-only renaming.
This route will replace move_batch:1. The main difference is this route will return status for each entry, while move_batch:1 raises failure if any entry fails.
This route will either finish synchronously, or return a job ID and do the async move job in background. Please use move_batch/check:2 to check the job status.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[MoveBatchArg](#data-types-movebatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[RelocationPath](#data-types-relocationpath)] | List of entries to be moved or copied. Each entry is [RelocationPath](#data-types-relocationpath).<br>
autorename | Boolean | If there's a conflict with any file, have the Dropbox server try to autorename that file to avoid the conflict.<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[RelocationBatchV2Launch](#data-types-relocationbatchv2launch)

Result returned by [files/copy_batch:2](#files-copy_batch_v2) or [files/move_batch:2](#files-move_batch_v2) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [RelocationBatchV2Result](#data-types-relocationbatchv2result) | 
### Error Values
Void
## move_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/move_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"from_path\": \"/Homework/math\",\"to_path\": \"/Homework/algebra\"}],\"autorename\": false,\"allow_shared_folder\": false,\"allow_ownership_transfer\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Move multiple files or folders to different locations at once in the user's Dropbox.
This route will return job ID immediately and do the async moving job in background. Please use move_batch/check:1 to check the job status.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RelocationBatchArg](#data-types-relocationbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[RelocationPath](#data-types-relocationpath)] | List of entries to be moved or copied. Each entry is [RelocationPath](#data-types-relocationpath).<br>
autorename | Boolean | If there's a conflict with any file, have the Dropbox server try to autorename that file to avoid the conflict.<br>
allow_shared_folder | Boolean | If true, [files/copy_batch](#files-copy_batch) will copy contents in shared folder, otherwise [RelocationError.cant_copy_shared_folder](#data-types-relocationerror) will be returned if [RelocationPath.from_path](#data-types-relocationpath) contains shared folder. This field is always true for [files/move_batch](#files-move_batch).<br>
allow_ownership_transfer | Boolean | Allow moves by owner even if it would result in an ownership transfer for the content being moved. This does not apply to copies.<br>
### Return Values
[RelocationBatchLaunch](#data-types-relocationbatchlaunch)

Result returned by [files/copy_batch](#files-copy_batch) or [files/move_batch](#files-move_batch) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [RelocationBatchResult](#data-types-relocationbatchresult) | 
other | Void | 
### Error Values
Void
## move_batch/check_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/move_batch/check_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "success": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for move_batch:2. It returns list of results for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[RelocationBatchV2JobStatus](#data-types-relocationbatchv2jobstatus)

Result returned by [files/copy_batch/check:2](#files-copy_batch-check_v2) or [files/move_batch/check:2](#files-move_batch-check_v2) that may either be in progress or completed with result for each entry.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [RelocationBatchV2Result](#data-types-relocationbatchv2result) | The copy or move batch job has finished.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## move_batch/check
```shell
curl -X POST https://api.dropboxapi.com/2/files/move_batch/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for move_batch:1. If success, it returns list of results for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[RelocationBatchJobStatus](#data-types-relocationbatchjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [RelocationBatchResult](#data-types-relocationbatchresult) | The copy or move batch job has finished.<br>
failed | [RelocationBatchError](#data-types-relocationbatcherror) | The copy or move batch job has failed with exception.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## permanently_delete
```shell
curl -X POST https://api.dropboxapi.com/2/files/permanently_delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/math/Prime_Numbers.txt\"}"
```

### Description
Permanently delete the file or folder at a given path (see https://www.dropbox.com/en/help/40).
Note: This endpoint is only available for Dropbox Business apps.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.permanent_delete
### Query Parameters
[DeleteArg](#data-types-deletearg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to delete.<br>
parent_rev | Optional[String] | Perform delete if given "rev" matches the existing file's latest "rev". This field does not support deleting a folder.<br>
### Return Values
Void
### Error Values
[DeleteError](#data-types-deleteerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | 
path_write | [WriteError](#data-types-writeerror) | 
too_many_write_operations | Void | There are too many write operations in user's Dropbox. Please retry this request.<br>
too_many_files | Void | There are too many files in one request. Please retry with fewer files.<br>
other | Void | 
## properties/add
```shell
curl -X POST https://api.dropboxapi.com/2/files/properties/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"property_groups\": [{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"fields\": [{\"name\": \"Security Policy\",\"value\": \"Confidential\"}]}]}"
```

### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[AddPropertiesArg](#data-types-addpropertiesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
property_groups | List[[PropertyGroup](#data-types-propertygroup)] | The property groups which are to be added to a Dropbox file. No two groups in the input should  refer to the same template.<br>
### Return Values
Void
### Error Values
[AddPropertiesError](#data-types-addpropertieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_field_too_large | Void | One or more of the supplied property field values is too large.<br>
does_not_fit_template | Void | One or more of the supplied property fields does not conform to the template specifications.<br>
duplicate_property_groups | Void | There are 2 or more property groups referring to the same templates in the input.<br>
property_group_already_exists | Void | A property group associated with this template and file already exists.<br>
## properties/overwrite
```shell
curl -X POST https://api.dropboxapi.com/2/files/properties/overwrite \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"property_groups\": [{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"fields\": [{\"name\": \"Security Policy\",\"value\": \"Confidential\"}]}]}"
```

### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[OverwritePropertyGroupArg](#data-types-overwritepropertygrouparg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
property_groups | List[[PropertyGroup](#data-types-propertygroup)] | The property groups "snapshot" updates to force apply. No two groups in the input should  refer to the same template.<br>
### Return Values
Void
### Error Values
[InvalidPropertyGroupError](#data-types-invalidpropertygrouperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_field_too_large | Void | One or more of the supplied property field values is too large.<br>
does_not_fit_template | Void | One or more of the supplied property fields does not conform to the template specifications.<br>
duplicate_property_groups | Void | There are 2 or more property groups referring to the same templates in the input.<br>
## properties/remove
```shell
curl -X POST https://api.dropboxapi.com/2/files/properties/remove \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"property_template_ids\": [\"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"]}"
```

### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[RemovePropertiesArg](#data-types-removepropertiesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
property_template_ids | List[String] | A list of identifiers for a template created by [files/templates/add_for_user](#files-templates-add_for_user) or [files/templates/add_for_team](#files-templates-add_for_team).<br>
### Return Values
Void
### Error Values
[RemovePropertiesError](#data-types-removepropertieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_group_lookup | [LookUpPropertiesError](#data-types-lookuppropertieserror) | 
## properties/template/get
```shell
curl -X POST https://api.dropboxapi.com/2/files/properties/template/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Security", 
    "description": "These properties describe how confidential this file or folder is.", 
    "fields": [
        {
            "name": "Security Policy", 
            "description": "This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.", 
            "type": {
                ".tag": "string"
            }
        }
    ]
}
```

### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[GetTemplateArg](#data-types-gettemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [files/templates/add_for_user](#files-templates-add_for_user) or [files/templates/add_for_team](#files-templates-add_for_team).<br>
### Return Values
[GetTemplateResult](#data-types-gettemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## properties/template/list
```shell
curl -X POST https://api.dropboxapi.com/2/files/properties/template/list \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "template_ids": [
        "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
    ]
}
```

### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
Void
### Return Values
[ListTemplateResult](#data-types-listtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_ids | List[String] | List of identifiers for templates added by  See [files/templates/add_for_user](#files-templates-add_for_user) or [files/templates/add_for_team](#files-templates-add_for_team).<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## properties/update
```shell
curl -X POST https://api.dropboxapi.com/2/files/properties/update \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/my_awesome/word.docx\",\"update_property_groups\": [{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"add_or_update_fields\": [{\"name\": \"Security Policy\",\"value\": \"Confidential\"}],\"remove_fields\": []}]}"
```

### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[UpdatePropertiesArg](#data-types-updatepropertiesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | A unique identifier for the file or folder.<br>
update_property_groups | List[[PropertyGroupUpdate](#data-types-propertygroupupdate)] | The property groups "delta" updates to apply.<br>
### Return Values
Void
### Error Values
[UpdatePropertiesError](#data-types-updatepropertieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
path | [LookupError](#data-types-lookuperror) | 
unsupported_folder | Void | This folder cannot be tagged. Tagging folders is not supported for team-owned templates.<br>
property_field_too_large | Void | One or more of the supplied property field values is too large.<br>
does_not_fit_template | Void | One or more of the supplied property fields does not conform to the template specifications.<br>
duplicate_property_groups | Void | There are 2 or more property groups referring to the same templates in the input.<br>
property_group_lookup | [LookUpPropertiesError](#data-types-lookuppropertieserror) | 
## restore
```shell
curl -X POST https://api.dropboxapi.com/2/files/restore \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/root/word.docx\",\"rev\": \"a1c10ce0dd78\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Restore a specific revision of a file to the given path.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RestoreArg](#data-types-restorearg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to save the restored file.<br>
rev | String | The revision to restore.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[RestoreError](#data-types-restoreerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | An error occurs when downloading metadata for the file.<br>
path_write | [WriteError](#data-types-writeerror) | An error occurs when trying to restore the file to that path.<br>
invalid_revision | Void | The revision is invalid. It may not exist.<br>
other | Void | 
## save_url
```shell
curl -X POST https://api.dropboxapi.com/2/files/save_url \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/a.txt\",\"url\": \"http://example.com/a.txt\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Save the data from a specified URL into a file in user's Dropbox.
Note that the transfer from the URL must complete within 5 minutes, or the operation will time out and the job will fail.
If the given path already exists, the file will be renamed to avoid the conflict (e.g. myfile (1).txt).
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[SaveUrlArg](#data-types-saveurlarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path in Dropbox where the URL will be saved to.<br>
url | String | The URL to be saved.<br>
### Return Values
[SaveUrlResult](#data-types-saveurlresult)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [FileMetadata](#data-types-filemetadata) | Metadata of the file where the URL is saved to.<br>
### Error Values
[SaveUrlError](#data-types-saveurlerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [WriteError](#data-types-writeerror) | 
download_failed | Void | Failed downloading the given URL. The URL may be  password-protected and the password provided was incorrect,  or the link may be disabled.<br>
invalid_url | Void | The given URL is invalid.<br>
not_found | Void | The file where the URL is saved to no longer exists.<br>
other | Void | 
## save_url/check_job_status
```shell
curl -X POST https://api.dropboxapi.com/2/files/save_url/check_job_status \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "in_progress"
}
```

### Description
Check the status of a save_url job.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[SaveUrlJobStatus](#data-types-saveurljobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [FileMetadata](#data-types-filemetadata) | Metadata of the file where the URL is saved to.<br>
failed | [SaveUrlError](#data-types-saveurlerror) | 
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## search
```shell
curl -X POST https://api.dropboxapi.com/2/files/search \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"\",\"query\": \"prime numbers\",\"start\": 0,\"max_results\": 100,\"mode\": \"filename\"}"
```

> The above command returns JSON structured like this:

```json
{
    "matches": [
        {
            "match_type": {
                ".tag": "content"
            }, 
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }
        }
    ], 
    "more": false, 
    "start": 1
}
```

### Description
Searches for files and folders.
Note: Recent changes will be reflected in search results within a few seconds and older revisions of existing files may still match your query for up to a few days.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[SearchArg](#data-types-searcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path in the user's Dropbox to search. Should probably be a folder.<br>
query | String | The string to search for. Query string may be rewritten to improve relevance of results. The string is split on spaces into multiple tokens. For file name searching, the last token is used for prefix matching (i.e. "bat c" matches "bat cave" but not "batman car").<br>
start | UInt64 | The starting index within the search results (used for paging).<br>
max_results | UInt64 | The maximum number of search results to return.<br>
mode | [SearchMode](#data-types-searchmode) | The search mode (filename, filename_and_content, or deleted_filename). Note that searching file content is only available for Dropbox Business accounts.<br>
### Return Values
[SearchResult](#data-types-searchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
matches | List[[SearchMatch](#data-types-searchmatch)] | A list (possibly empty) of matches for the query.<br>
more | Boolean | Used for paging. If true, indicates there is another page of results available that can be fetched by calling [files/search](#files-search) again.<br>
start | UInt64 | Used for paging. Value to set the start argument to when calling [files/search](#files-search) to fetch the next page of results.<br>
### Error Values
[SearchError](#data-types-searcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
invalid_argument | Optional[String] | 
internal_error | Void | Something went wrong, please try again.<br>
other | Void | 
## search_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/search_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"query\": \"cat\",\"include_highlights\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "matches": [
        {
            "metadata": {
                ".tag": "metadata", 
                "metadata": {
                    ".tag": "file", 
                    "name": "Prime_Numbers.txt", 
                    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                    "client_modified": "2015-05-12T15:50:38Z", 
                    "server_modified": "2015-05-12T15:50:38Z", 
                    "rev": "a1c10ce0dd78", 
                    "size": 7212, 
                    "path_lower": "/homework/math/prime_numbers.txt", 
                    "path_display": "/Homework/math/Prime_Numbers.txt", 
                    "sharing_info": {
                        "read_only": true, 
                        "parent_shared_folder_id": "84528192421", 
                        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                    }, 
                    "is_downloadable": true, 
                    "property_groups": [
                        {
                            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                            "fields": [
                                {
                                    "name": "Security Policy", 
                                    "value": "Confidential"
                                }
                            ]
                        }
                    ], 
                    "has_explicit_shared_members": false, 
                    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                    "file_lock_info": {
                        "is_lockholder": true, 
                        "lockholder_name": "Imaginary User", 
                        "created": "2015-05-12T15:50:38Z"
                    }
                }
            }
        }
    ], 
    "has_more": false
}
```

### Description
Searches for files and folders.
Note: search:2 along with search/continue:2 can only be used to retrieve a maximum of 10,000 matches.
Recent changes may not immediately be reflected in search results due to a short delay in indexing. Duplicate results may be returned across pages. Some results may not be returned.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[SearchV2Arg](#data-types-searchv2arg)

Field Name | Data Type | Description
--------- | ------- | -----------
query | String | The string to search for. May match across multiple fields based on the request arguments. Query string may be rewritten to improve relevance of results.<br>
options | Optional[[SearchOptions](#data-types-searchoptions)] | Options for more targeted search results.<br>
match_field_options | Optional[[SearchMatchFieldOptions](#data-types-searchmatchfieldoptions)] | Options for search results match fields.<br>
include_highlights | Boolean | Field is deprecated. Deprecated and moved this option to SearchMatchFieldOptions.<br>
### Return Values
[SearchV2Result](#data-types-searchv2result)

Field Name | Data Type | Description
--------- | ------- | -----------
matches | List[[SearchMatchV2](#data-types-searchmatchv2)] | A list (possibly empty) of matches for the query.<br>
has_more | Boolean | Used for paging. If true, indicates there is another page of results available that can be fetched by calling [files/search/continue:2](#files-search-continue_v2) with the cursor.<br>
cursor | Optional[String] | Pass the cursor into [files/search/continue:2](#files-search-continue_v2) to fetch the next page of results.<br>
### Error Values
[SearchError](#data-types-searcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
invalid_argument | Optional[String] | 
internal_error | Void | Something went wrong, please try again.<br>
other | Void | 
## search/continue_v2
```shell
curl -X POST https://api.dropboxapi.com/2/files/search/continue_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "matches": [
        {
            "metadata": {
                ".tag": "metadata", 
                "metadata": {
                    ".tag": "file", 
                    "name": "Prime_Numbers.txt", 
                    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                    "client_modified": "2015-05-12T15:50:38Z", 
                    "server_modified": "2015-05-12T15:50:38Z", 
                    "rev": "a1c10ce0dd78", 
                    "size": 7212, 
                    "path_lower": "/homework/math/prime_numbers.txt", 
                    "path_display": "/Homework/math/Prime_Numbers.txt", 
                    "sharing_info": {
                        "read_only": true, 
                        "parent_shared_folder_id": "84528192421", 
                        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                    }, 
                    "is_downloadable": true, 
                    "property_groups": [
                        {
                            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                            "fields": [
                                {
                                    "name": "Security Policy", 
                                    "value": "Confidential"
                                }
                            ]
                        }
                    ], 
                    "has_explicit_shared_members": false, 
                    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                    "file_lock_info": {
                        "is_lockholder": true, 
                        "lockholder_name": "Imaginary User", 
                        "created": "2015-05-12T15:50:38Z"
                    }
                }
            }
        }
    ], 
    "has_more": false
}
```

### Description
Fetches the next page of search results returned from search:2.
Note: search:2 along with search/continue:2 can only be used to retrieve a maximum of 10,000 matches.
Recent changes may not immediately be reflected in search results due to a short delay in indexing. Duplicate results may be returned across pages. Some results may not be returned.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[SearchV2ContinueArg](#data-types-searchv2continuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by your last call to [files/search:2](#files-search_v2). Used to fetch the next page of results.<br>
### Return Values
[SearchV2Result](#data-types-searchv2result)

Field Name | Data Type | Description
--------- | ------- | -----------
matches | List[[SearchMatchV2](#data-types-searchmatchv2)] | A list (possibly empty) of matches for the query.<br>
has_more | Boolean | Used for paging. If true, indicates there is another page of results available that can be fetched by calling [files/search/continue:2](#files-search-continue_v2) with the cursor.<br>
cursor | Optional[String] | Pass the cursor into [files/search/continue:2](#files-search-continue_v2) to fetch the next page of results.<br>
### Error Values
[SearchError](#data-types-searcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
invalid_argument | Optional[String] | 
internal_error | Void | Something went wrong, please try again.<br>
other | Void | 
## unlock_file_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/unlock_file_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"path\": \"/John Doe/sample/test.pdf\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            ".tag": "success", 
            "metadata": {
                ".tag": "file", 
                "name": "Prime_Numbers.txt", 
                "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                "client_modified": "2015-05-12T15:50:38Z", 
                "server_modified": "2015-05-12T15:50:38Z", 
                "rev": "a1c10ce0dd78", 
                "size": 7212, 
                "path_lower": "/homework/math/prime_numbers.txt", 
                "path_display": "/Homework/math/Prime_Numbers.txt", 
                "sharing_info": {
                    "read_only": true, 
                    "parent_shared_folder_id": "84528192421", 
                    "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
                }, 
                "is_downloadable": true, 
                "property_groups": [
                    {
                        "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                        "fields": [
                            {
                                "name": "Security Policy", 
                                "value": "Confidential"
                            }
                        ]
                    }
                ], 
                "has_explicit_shared_members": false, 
                "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
                "file_lock_info": {
                    "is_lockholder": true, 
                    "lockholder_name": "Imaginary User", 
                    "created": "2015-05-12T15:50:38Z"
                }
            }, 
            "lock": {
                "content": {
                    ".tag": "single_user", 
                    "created": "2015-05-12T15:50:38Z", 
                    "lock_holder_account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                    "lock_holder_team_id": "dbtid:1234abcd"
                }
            }
        }
    ]
}
```

### Description
Unlock the files at the given paths. A locked file can only be unlocked by the lock holder or, if a business account, a team admin. A successful response indicates that the file has been unlocked. Returns a list of the unlocked file paths and their metadata after this operation.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[UnlockFileBatchArg](#data-types-unlockfilebatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[UnlockFileArg](#data-types-unlockfilearg)] | List of 'entries'. Each 'entry' contains a path of the file which will be unlocked. Duplicate path arguments in the batch are considered only once.<br>
### Return Values
[LockFileBatchResult](#data-types-lockfilebatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LockFileResultEntry](#data-types-lockfileresultentry)] | Each Entry in the 'entries' will have '.tag' with the operation status (e.g. success), the metadata for the file and the lock state after the operation.<br>
### Error Values
[LockFileError](#data-types-lockfileerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path_lookup | [LookupError](#data-types-lookuperror) | Could not find the specified resource.<br>
too_many_write_operations | Void | There are too many write operations in user's Dropbox. Please retry this request.<br>
too_many_files | Void | There are too many files in one request. Please retry with fewer files.<br>
no_write_permission | Void | The user does not have permissions to change the lock state or access the file.<br>
cannot_be_locked | Void | Item is a type that cannot be locked.<br>
file_not_shared | Void | Requested file is not currently shared.<br>
lock_conflict | [LockConflictError](#data-types-lockconflicterror) | The user action conflicts with an existing lock on the file.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## upload
```shell
curl -X POST https://content.dropboxapi.com/2/files/upload \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"path\": \"/Homework/math/Matrices.txt\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Create a new file with the contents provided in the request.
Do not use this to upload a file larger than 150 MB. Instead, create an upload session with upload_session/start.
Calls to this endpoint will count as data transport calls for any Dropbox Business teams with a limit on the number of data transport calls allowed per month. For more information, see the [Data transport limit page](https://www.dropbox.com/developers/reference/data-transport-limit).
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[CommitInfo](#data-types-commitinfo)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | Path in the user's Dropbox to save the file.<br>
mode | [WriteMode](#data-types-writemode) | Selects what to do if the file already exists.<br>
autorename | Boolean | If there's a conflict, as determined by [mode](#data-types-commitinfo), have the Dropbox server try to autorename the file to avoid conflict.<br>
client_modified | Optional[Timestamp] | The value to store as the [client_modified](#data-types-commitinfo) timestamp. Dropbox automatically records the time at which the file was written to the Dropbox servers. It can also record an additional timestamp, provided by Dropbox desktop clients, mobile clients, and API apps of when the file was actually created or modified.<br>
mute | Boolean | Normally, users are made aware of any file modifications in their Dropbox account via notifications in the client software. If true, this tells the clients that this modification shouldn't result in a user notification.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | List of custom properties to add to file.<br>
strict_conflict | Boolean | Be more strict about how each [WriteMode](#data-types-writemode) detects conflict. For example, always return a conflict error when [mode](#data-types-commitinfo) = [WriteMode.update](#data-types-writemode) and the given "rev" doesn't match the existing file's "rev", even if the existing file has been deleted.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[UploadError](#data-types-uploaderror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [UploadWriteFailed](#data-types-uploadwritefailed) | Unable to save the uploaded contents to a file.<br>
properties_error | [InvalidPropertyGroupError](#data-types-invalidpropertygrouperror) | The supplied property group is invalid. The file has uploaded without property groups.<br>
other | Void | 
## upload_session/append_v2
```shell
curl -X POST https://content.dropboxapi.com/2/files/upload_session/append_v2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"cursor\": {\"session_id\": \"1234faaf0678bcde\",\"offset\": 0},\"close\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

### Description
Append more data to an upload session.
When the parameter close is set, this call will close the session.
A single request should not upload more than 150 MB. The maximum size of a file one can upload to an upload session is 350 GB.
Calls to this endpoint will count as data transport calls for any Dropbox Business teams with a limit on the number of data transport calls allowed per month. For more information, see the [Data transport limit page](https://www.dropbox.com/developers/reference/data-transport-limit).
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[UploadSessionAppendArg](#data-types-uploadsessionappendarg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | [UploadSessionCursor](#data-types-uploadsessioncursor) | Contains the upload session ID and the offset.<br>
close | Boolean | If true, the current session will be closed, at which point you won't be able to call [files/upload_session/append:2](#files-upload_session-append_v2) anymore with the current session.<br>
### Return Values
Void
### Error Values
[UploadSessionLookupError](#data-types-uploadsessionlookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
not_found | Void | The upload session ID was not found or has expired. Upload sessions are valid for 48 hours.<br>
incorrect_offset | [UploadSessionOffsetError](#data-types-uploadsessionoffseterror) | The specified offset was incorrect. See the value for the correct offset. This error may occur when a previous request was received and processed successfully but the client did not receive the response, e.g. due to a network error.<br>
closed | Void | You are attempting to append data to an upload session that has already been closed (i.e. committed).<br>
not_closed | Void | The session must be closed before calling upload_session/finish_batch.<br>
too_large | Void | You can not append to the upload session because the size of a file should not reach the max file size limit (i.e. 350GB).<br>
other | Void | 
## upload_session/append
```shell
curl -X POST https://content.dropboxapi.com/2/files/upload_session/append \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"session_id\": \"1234faaf0678bcde\",\"offset\": 0}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

### Description
Append more data to an upload session.
A single request should not upload more than 150 MB. The maximum size of a file one can upload to an upload session is 350 GB.
Calls to this endpoint will count as data transport calls for any Dropbox Business teams with a limit on the number of data transport calls allowed per month. For more information, see the [Data transport limit page](https://www.dropbox.com/developers/reference/data-transport-limit).
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[UploadSessionCursor](#data-types-uploadsessioncursor)

Field Name | Data Type | Description
--------- | ------- | -----------
session_id | String | The upload session ID (returned by [files/upload_session/start](#files-upload_session-start)).<br>
offset | UInt64 | The amount of data that has been uploaded so far. We use this to make sure upload data isn't lost or duplicated in the event of a network error.<br>
### Return Values
Void
### Error Values
[UploadSessionLookupError](#data-types-uploadsessionlookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
not_found | Void | The upload session ID was not found or has expired. Upload sessions are valid for 48 hours.<br>
incorrect_offset | [UploadSessionOffsetError](#data-types-uploadsessionoffseterror) | The specified offset was incorrect. See the value for the correct offset. This error may occur when a previous request was received and processed successfully but the client did not receive the response, e.g. due to a network error.<br>
closed | Void | You are attempting to append data to an upload session that has already been closed (i.e. committed).<br>
not_closed | Void | The session must be closed before calling upload_session/finish_batch.<br>
too_large | Void | You can not append to the upload session because the size of a file should not reach the max file size limit (i.e. 350GB).<br>
other | Void | 
## upload_session/finish
```shell
curl -X POST https://content.dropboxapi.com/2/files/upload_session/finish \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"cursor\": {\"session_id\": \"1234faaf0678bcde\",\"offset\": 0},\"commit\": {\"path\": \"/Homework/math/Matrices.txt\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "name": "Prime_Numbers.txt", 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "path_display": "/Homework/math/Prime_Numbers.txt", 
    "sharing_info": {
        "read_only": true, 
        "parent_shared_folder_id": "84528192421", 
        "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
    }, 
    "is_downloadable": true, 
    "property_groups": [
        {
            "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
            "fields": [
                {
                    "name": "Security Policy", 
                    "value": "Confidential"
                }
            ]
        }
    ], 
    "has_explicit_shared_members": false, 
    "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
    "file_lock_info": {
        "is_lockholder": true, 
        "lockholder_name": "Imaginary User", 
        "created": "2015-05-12T15:50:38Z"
    }
}
```

### Description
Finish an upload session and save the uploaded data to the given file path.
A single request should not upload more than 150 MB. The maximum size of a file one can upload to an upload session is 350 GB.
Calls to this endpoint will count as data transport calls for any Dropbox Business teams with a limit on the number of data transport calls allowed per month. For more information, see the [Data transport limit page](https://www.dropbox.com/developers/reference/data-transport-limit).
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[UploadSessionFinishArg](#data-types-uploadsessionfinisharg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | [UploadSessionCursor](#data-types-uploadsessioncursor) | Contains the upload session ID and the offset.<br>
commit | [CommitInfo](#data-types-commitinfo) | Contains the path and other optional modifiers for the commit.<br>
### Return Values
[FileMetadata](#data-types-filemetadata)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The last component of the path (including extension). This never contains a slash.<br>
id | String | A unique identifier for the file.<br>
client_modified | Timestamp | For files, this is the modification time set by the desktop client when the file was added to Dropbox. Since this time is not verified (the Dropbox server stores whatever the desktop client sends up), this should only be used for display purposes (such as sorting) and not, for example, to determine if a file has changed or not.<br>
server_modified | Timestamp | The last time the file was modified on Dropbox.<br>
rev | String | A unique identifier for the current revision of a file. This field is the same rev as elsewhere in the API and can be used to detect changes and avoid conflicts.<br>
size | UInt64 | The file size in bytes.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will be null if the file or folder is not mounted.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1, and at least the last path component will have the correct casing. Changes to only the casing of paths won't be returned by [files/list_folder/continue](#files-list_folder-continue). This field will be null if the file or folder is not mounted.<br>
parent_shared_folder_id | Optional[String] | Field is deprecated. Please use [FileSharingInfo.parent_shared_folder_id](#data-types-filesharinginfo) or [FolderSharingInfo.parent_shared_folder_id](#data-types-foldersharinginfo) instead.<br>
media_info | Optional[[MediaInfo](#data-types-mediainfo)] | Additional information if the file is a photo or video. This field will not be set on entries returned by [files/list_folder](#files-list_folder), [files/list_folder/continue](#files-list_folder-continue), or [files/get_thumbnail_batch](#files-get_thumbnail_batch), starting December 2, 2019.<br>
symlink_info | Optional[[SymlinkInfo](#data-types-symlinkinfo)] | Set if this file is a symlink.<br>
sharing_info | Optional[[FileSharingInfo](#data-types-filesharinginfo)] | Set if this file is contained in a shared folder.<br>
is_downloadable | Boolean | If true, file can be downloaded directly; else the file must be exported.<br>
export_info | Optional[[ExportInfo](#data-types-exportinfo)] | Information about format this file can be exported to. This filed must be set if [is_downloadable](#data-types-filemetadata) is set to false.<br>
property_groups | Optional[List[[PropertyGroup](#data-types-propertygroup)]] | Additional information if the file has custom properties with the property template specified.<br>
has_explicit_shared_members | Optional[Boolean] | This flag will only be present if include_has_explicit_shared_members  is true in [files/list_folder](#files-list_folder) or [files/get_metadata](#files-get_metadata). If this  flag is present, it will be true if this file has any explicit shared  members. This is different from sharing_info in that this could be true  in the case where a file has explicit members but is not contained within  a shared folder.<br>
content_hash | Optional[String] | A hash of the file content. This field can be used to verify data integrity. For more information see our [Content hash](https://www.dropbox.com/developers/reference/content-hash) page.<br>
file_lock_info | Optional[[FileLockMetadata](#data-types-filelockmetadata)] | If present, the metadata associated with the file's current lock.<br>
### Error Values
[UploadSessionFinishError](#data-types-uploadsessionfinisherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
lookup_failed | [UploadSessionLookupError](#data-types-uploadsessionlookuperror) | The session arguments are incorrect; the value explains the reason.<br>
path | [WriteError](#data-types-writeerror) | Unable to save the uploaded contents to a file. Data has already been appended to the upload session. Please retry with empty data body and updated offset.<br>
properties_error | [InvalidPropertyGroupError](#data-types-invalidpropertygrouperror) | The supplied property group is invalid. The file has uploaded without property groups.<br>
too_many_shared_folder_targets | Void | Field is deprecated. The batch request commits files into too many different shared folders. Please limit your batch request to files contained in a single shared folder.<br>
too_many_write_operations | Void | There are too many write operations happening in the user's Dropbox. You should retry uploading this file.<br>
other | Void | 
## upload_session/finish_batch
```shell
curl -X POST https://api.dropboxapi.com/2/files/upload_session/finish_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"entries\": [{\"cursor\": {\"session_id\": \"1234faaf0678bcde\",\"offset\": 0},\"commit\": {\"path\": \"/Homework/math/Matrices.txt\",\"mode\": \"add\",\"autorename\": true,\"mute\": false,\"strict_conflict\": false}}]}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "name": "Prime_Numbers.txt", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "client_modified": "2015-05-12T15:50:38Z", 
            "server_modified": "2015-05-12T15:50:38Z", 
            "rev": "a1c10ce0dd78", 
            "size": 7212, 
            "path_lower": "/homework/math/prime_numbers.txt", 
            "path_display": "/Homework/math/Prime_Numbers.txt", 
            "sharing_info": {
                "read_only": true, 
                "parent_shared_folder_id": "84528192421", 
                "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
            }, 
            "is_downloadable": true, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ], 
            "has_explicit_shared_members": false, 
            "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
            "file_lock_info": {
                "is_lockholder": true, 
                "lockholder_name": "Imaginary User", 
                "created": "2015-05-12T15:50:38Z"
            }
        }
    ]
}
```

### Description
This route helps you commit many files at once into a user's Dropbox. Use upload_session/start and upload_session/append:2 to upload file contents. We recommend uploading many files in parallel to increase throughput. Once the file contents have been uploaded, rather than calling upload_session/finish, use this route to finish all your upload sessions in a single request.
[UploadSessionStartArg.close](#data-types-uploadsessionstartarg) or [UploadSessionAppendArg.close](#data-types-uploadsessionappendarg) needs to be true for the last upload_session/start or upload_session/append:2 call. The maximum size of a file one can upload to an upload session is 350 GB.
This route will return a job_id immediately and do the async commit job in background. Use upload_session/finish_batch/check to check the job status.
For the same account, this route should be executed serially. That means you should not start the next job before current job finishes. We allow up to 1000 entries in a single request.
Calls to this endpoint will count as data transport calls for any Dropbox Business teams with a limit on the number of data transport calls allowed per month. For more information, see the [Data transport limit page](https://www.dropbox.com/developers/reference/data-transport-limit).
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[UploadSessionFinishBatchArg](#data-types-uploadsessionfinishbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[UploadSessionFinishArg](#data-types-uploadsessionfinisharg)] | Commit information for each file in the batch.<br>
### Return Values
[UploadSessionFinishBatchLaunch](#data-types-uploadsessionfinishbatchlaunch)

Result returned by [files/upload_session/finish_batch](#files-upload_session-finish_batch) that may either launch an asynchronous job or complete synchronously.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [UploadSessionFinishBatchResult](#data-types-uploadsessionfinishbatchresult) | 
other | Void | 
### Error Values
Void
## upload_session/finish_batch/check
```shell
curl -X POST https://api.dropboxapi.com/2/files/upload_session/finish_batch/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "entries": [
        {
            ".tag": "success", 
            "name": "Prime_Numbers.txt", 
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "client_modified": "2015-05-12T15:50:38Z", 
            "server_modified": "2015-05-12T15:50:38Z", 
            "rev": "a1c10ce0dd78", 
            "size": 7212, 
            "path_lower": "/homework/math/prime_numbers.txt", 
            "path_display": "/Homework/math/Prime_Numbers.txt", 
            "sharing_info": {
                "read_only": true, 
                "parent_shared_folder_id": "84528192421", 
                "modified_by": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc"
            }, 
            "is_downloadable": true, 
            "property_groups": [
                {
                    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa", 
                    "fields": [
                        {
                            "name": "Security Policy", 
                            "value": "Confidential"
                        }
                    ]
                }
            ], 
            "has_explicit_shared_members": false, 
            "content_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", 
            "file_lock_info": {
                "is_lockholder": true, 
                "lockholder_name": "Imaginary User", 
                "created": "2015-05-12T15:50:38Z"
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for upload_session/finish_batch. If success, it returns list of result for each entry.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[UploadSessionFinishBatchJobStatus](#data-types-uploadsessionfinishbatchjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [UploadSessionFinishBatchResult](#data-types-uploadsessionfinishbatchresult) | The [files/upload_session/finish_batch](#files-upload_session-finish_batch) has finished.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## upload_session/start
```shell
curl -X POST https://content.dropboxapi.com/2/files/upload_session/start \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"close\": false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "session_id": "1234faaf0678bcde"
}
```

### Description
Upload sessions allow you to upload a single file in one or more requests, for example where the size of the file is greater than 150 MB.  This call starts a new upload session with the given data. You can then use upload_session/append:2 to add more data and upload_session/finish to save all the data to a file in Dropbox.
A single request should not upload more than 150 MB. The maximum size of a file one can upload to an upload session is 350 GB.
An upload session can be used for a maximum of 48 hours. Attempting to use an [UploadSessionStartResult.session_id](#data-types-uploadsessionstartresult) with upload_session/append:2 or upload_session/finish more than 48 hours after its creation will return a [UploadSessionLookupError.not_found](#data-types-uploadsessionlookuperror).
Calls to this endpoint will count as data transport calls for any Dropbox Business teams with a limit on the number of data transport calls allowed per month. For more information, see the [Data transport limit page](https://www.dropbox.com/developers/reference/data-transport-limit).
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[UploadSessionStartArg](#data-types-uploadsessionstartarg)

Field Name | Data Type | Description
--------- | ------- | -----------
close | Boolean | If true, the current session will be closed, at which point you won't be able to call [files/upload_session/append:2](#files-upload_session-append_v2) anymore with the current session.<br>
### Return Values
[UploadSessionStartResult](#data-types-uploadsessionstartresult)

Field Name | Data Type | Description
--------- | ------- | -----------
session_id | String | A unique identifier for the upload session. Pass this to [files/upload_session/append:2](#files-upload_session-append_v2) and [files/upload_session/finish](#files-upload_session-finish).<br>
### Error Values
Void
# Paper
## docs/archive
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/archive \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\"}"
```

### Description
Marks the given Paper doc as archived.
This action can be performed or undone by anyone with edit permissions to the doc.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
This endpoint will be retired in September 2020. Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for more information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[RefPaperDoc](#data-types-refpaperdoc)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
### Return Values
Void
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/create
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/create \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"import_format\": \"markdown\"}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "doc_id": "uaSvRuxvnkFa12PTkBv5q", 
    "revision": 456736745, 
    "title": "Week one retention"
}
```

### Description
Creates a new Paper doc with the provided content.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
This endpoint will be retired in September 2020. Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for more information.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[PaperDocCreateArgs](#data-types-paperdoccreateargs)

Field Name | Data Type | Description
--------- | ------- | -----------
import_format | [ImportFormat](#data-types-importformat) | The format of provided data.<br>
parent_folder_id | Optional[String] | The Paper folder ID where the Paper document should be created. The API user has to have write access to this folder or error is thrown.<br>
### Return Values
[PaperDocCreateUpdateResult](#data-types-paperdoccreateupdateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | Doc ID of the newly created doc.<br>
revision | Int64 | The Paper doc revision. Simply an ever increasing number.<br>
title | String | The Paper doc title.<br>
### Error Values
[PaperDocCreateError](#data-types-paperdoccreateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
content_malformed | Void | The provided content was malformed and cannot be imported to Paper.<br>
folder_not_found | Void | The specified Paper folder is cannot be found.<br>
doc_length_exceeded | Void | The newly created Paper doc would be too large. Please split the content into multiple docs.<br>
image_size_exceeded | Void | The imported document contains an image that is too large. The current limit is 1MB. This only applies to HTML with data URI.<br>
## docs/download
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/download \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"export_format\": \"markdown\"}"
```

> The above command returns JSON structured like this:

```json
{
    "owner": "james@example.com", 
    "title": "Week one retention", 
    "revision": 456736745, 
    "mime_type": "text/x-markdown"
}
```

### Description
Exports and downloads Paper doc either as HTML or markdown.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
files.content.read
### Query Parameters
[PaperDocExport](#data-types-paperdocexport)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
export_format | [ExportFormat](#data-types-exportformat) | 
### Return Values
[PaperDocExportResult](#data-types-paperdocexportresult)

Field Name | Data Type | Description
--------- | ------- | -----------
owner | String | The Paper doc owner's email address.<br>
title | String | The Paper doc title.<br>
revision | Int64 | The Paper doc revision. Simply an ever increasing number.<br>
mime_type | String | MIME type of the export. This corresponds to [ExportFormat](#data-types-exportformat) specified in the request.<br>
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/folder_users/list
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/folder_users/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "invitees": [
        {
            ".tag": "email", 
            "email": "jessica@example.com"
        }
    ], 
    "users": [
        {
            "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
            "email": "bob@example.com", 
            "display_name": "Robert Smith", 
            "same_team": true, 
            "team_member_id": "dbmid:abcd1234"
        }
    ], 
    "cursor": {
        "value": "zHZvTPBnXilGgm1AmDgVyZ10zf7qb0qznd5sAVQbbIvoteSnWLjUdLU7aR25hb", 
        "expiration": "2016-08-07T14:56:15Z"
    }, 
    "has_more": false
}
```

### Description
Lists the users who are explicitly invited to the Paper folder in which the Paper doc is contained. For private folders all users (including owner) shared on the folder are listed and for team folders all non-team users shared on the folder are returned.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListUsersOnFolderArgs](#data-types-listusersonfolderargs)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
limit | Int32 | Size limit per batch. The maximum number of users that can be retrieved per batch is 1000. Higher value results in invalid arguments error.<br>
### Return Values
[ListUsersOnFolderResponse](#data-types-listusersonfolderresponse)

Field Name | Data Type | Description
--------- | ------- | -----------
invitees | List[[InviteeInfo](#data-types-inviteeinfo)] | List of email addresses that are invited on the Paper folder.<br>
users | List[[UserInfo](#data-types-userinfo)] | List of users that are invited on the Paper folder.<br>
cursor | [Cursor](#data-types-cursor) | Pass the cursor into [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue) to paginate through all users. The cursor preserves all properties as specified in the original call to [paper/docs/folder_users/list](#paper-docs-folder_users-list).<br>
has_more | Boolean | Will be set to True if a subsequent call with the provided cursor to [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue) returns immediately with some results. If set to False please allow some delay before making another call to [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue).<br>
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/folder_users/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/folder_users/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"cursor\": \"U60b6BxT43ySd5sAVQbbIvoteSnWLjUdLU7aR25hbt3ySd5sAVQbbIvoteSnWLjUd\"}"
```

> The above command returns JSON structured like this:

```json
{
    "invitees": [
        {
            ".tag": "email", 
            "email": "jessica@example.com"
        }
    ], 
    "users": [
        {
            "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
            "email": "bob@example.com", 
            "display_name": "Robert Smith", 
            "same_team": true, 
            "team_member_id": "dbmid:abcd1234"
        }
    ], 
    "cursor": {
        "value": "zHZvTPBnXilGgm1AmDgVyZ10zf7qb0qznd5sAVQbbIvoteSnWLjUdLU7aR25hb", 
        "expiration": "2016-08-07T14:56:15Z"
    }, 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from docs/folder_users/list, use this to paginate through all users on the Paper folder.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListUsersOnFolderContinueArgs](#data-types-listusersonfoldercontinueargs)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
cursor | String | The cursor obtained from [paper/docs/folder_users/list](#paper-docs-folder_users-list) or [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue). Allows for pagination.<br>
### Return Values
[ListUsersOnFolderResponse](#data-types-listusersonfolderresponse)

Field Name | Data Type | Description
--------- | ------- | -----------
invitees | List[[InviteeInfo](#data-types-inviteeinfo)] | List of email addresses that are invited on the Paper folder.<br>
users | List[[UserInfo](#data-types-userinfo)] | List of users that are invited on the Paper folder.<br>
cursor | [Cursor](#data-types-cursor) | Pass the cursor into [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue) to paginate through all users. The cursor preserves all properties as specified in the original call to [paper/docs/folder_users/list](#paper-docs-folder_users-list).<br>
has_more | Boolean | Will be set to True if a subsequent call with the provided cursor to [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue) returns immediately with some results. If set to False please allow some delay before making another call to [paper/docs/folder_users/list/continue](#paper-docs-folder_users-list-continue).<br>
### Error Values
[ListUsersCursorError](#data-types-listuserscursorerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
cursor_error | [PaperApiCursorError](#data-types-paperapicursorerror) | 
## docs/get_folder_info
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/get_folder_info \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\"}"
```

> The above command returns JSON structured like this:

```json
{
    "folder_sharing_policy_type": {
        ".tag": "team"
    }, 
    "folders": [
        {
            "id": "e.gGYT6HSafpMej9bUv306oGm60vrHiCHgEFnzziioPGCvHf", 
            "name": "Design docs"
        }
    ]
}
```

### Description
Retrieves folder information for the given Paper doc. This includes:
  - folder sharing policy; permissions for subfolders are set by the top-level folder.
  - full 'filepath', i.e. the list of folders (both folderId and folderName) from     the root folder to the folder directly containing the Paper doc.

If the Paper doc is not in any folder (aka unfiled) the response will be empty.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[RefPaperDoc](#data-types-refpaperdoc)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
### Return Values
[FoldersContainingPaperDoc](#data-types-folderscontainingpaperdoc)

Metadata about Paper folders containing the specififed Paper doc.

Field Name | Data Type | Description
--------- | ------- | -----------
folder_sharing_policy_type | Optional[[FolderSharingPolicyType](#data-types-foldersharingpolicytype)] | The sharing policy of the folder containing the Paper doc.<br>
folders | Optional[List[[Folder](#data-types-folder)]] | The folder path. If present the first folder is the root folder.<br>
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/list
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"filter_by\": \"docs_created\",\"sort_by\": \"modified\",\"sort_order\": \"descending\",\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "doc_ids": [
        "zO1E7coc54sE8IuMdUoxz", 
        "mm1AmDgVyZ10zf7qb0qzn", 
        "dByYHZvTPBnXilGgyc5mm"
    ], 
    "cursor": {
        "value": "zHZvTPBnXilGgm1AmDgVyZ10zf7qb0qznd5sAVQbbIvoteSnWLjUdLU7aR25hb", 
        "expiration": "2016-08-07T14:56:15Z"
    }, 
    "has_more": true
}
```

### Description
Return the list of all Paper docs according to the argument specifications. To iterate over through the full pagination, pass the cursor to docs/list/continue.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListPaperDocsArgs](#data-types-listpaperdocsargs)

Field Name | Data Type | Description
--------- | ------- | -----------
filter_by | [ListPaperDocsFilterBy](#data-types-listpaperdocsfilterby) | Allows user to specify how the Paper docs should be filtered.<br>
sort_by | [ListPaperDocsSortBy](#data-types-listpaperdocssortby) | Allows user to specify how the Paper docs should be sorted.<br>
sort_order | [ListPaperDocsSortOrder](#data-types-listpaperdocssortorder) | Allows user to specify the sort order of the result.<br>
limit | Int32 | Size limit per batch. The maximum number of docs that can be retrieved per batch is 1000. Higher value results in invalid arguments error.<br>
### Return Values
[ListPaperDocsResponse](#data-types-listpaperdocsresponse)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_ids | List[String] | The list of Paper doc IDs that can be used to access the given Paper docs or supplied to other API methods. The list is sorted in the order specified by the initial call to [paper/docs/list](#paper-docs-list).<br>
cursor | [Cursor](#data-types-cursor) | Pass the cursor into [paper/docs/list/continue](#paper-docs-list-continue) to paginate through all files. The cursor preserves all properties as specified in the original call to [paper/docs/list](#paper-docs-list).<br>
has_more | Boolean | Will be set to True if a subsequent call with the provided cursor to [paper/docs/list/continue](#paper-docs-list-continue) returns immediately with some results. If set to False please allow some delay before making another call to [paper/docs/list/continue](#paper-docs-list-continue).<br>
### Error Values
Void
## docs/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"U60b6BxT43ySd5sAVQbbIvoteSnWLjUdLU7aR25hbt3ySd5sAVQbbIvoteSnWLjUd\"}"
```

> The above command returns JSON structured like this:

```json
{
    "doc_ids": [
        "zO1E7coc54sE8IuMdUoxz", 
        "mm1AmDgVyZ10zf7qb0qzn", 
        "dByYHZvTPBnXilGgyc5mm"
    ], 
    "cursor": {
        "value": "zHZvTPBnXilGgm1AmDgVyZ10zf7qb0qznd5sAVQbbIvoteSnWLjUdLU7aR25hb", 
        "expiration": "2016-08-07T14:56:15Z"
    }, 
    "has_more": true
}
```

### Description
Once a cursor has been retrieved from docs/list, use this to paginate through all Paper doc.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.metadata.read
### Query Parameters
[ListPaperDocsContinueArgs](#data-types-listpaperdocscontinueargs)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor obtained from [paper/docs/list](#paper-docs-list) or [paper/docs/list/continue](#paper-docs-list-continue). Allows for pagination.<br>
### Return Values
[ListPaperDocsResponse](#data-types-listpaperdocsresponse)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_ids | List[String] | The list of Paper doc IDs that can be used to access the given Paper docs or supplied to other API methods. The list is sorted in the order specified by the initial call to [paper/docs/list](#paper-docs-list).<br>
cursor | [Cursor](#data-types-cursor) | Pass the cursor into [paper/docs/list/continue](#paper-docs-list-continue) to paginate through all files. The cursor preserves all properties as specified in the original call to [paper/docs/list](#paper-docs-list).<br>
has_more | Boolean | Will be set to True if a subsequent call with the provided cursor to [paper/docs/list/continue](#paper-docs-list-continue) returns immediately with some results. If set to False please allow some delay before making another call to [paper/docs/list/continue](#paper-docs-list-continue).<br>
### Error Values
[ListDocsCursorError](#data-types-listdocscursorerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
cursor_error | [PaperApiCursorError](#data-types-paperapicursorerror) | 
other | Void | 
## docs/permanently_delete
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/permanently_delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\"}"
```

### Description
Permanently deletes the given Paper doc. This operation is final as the doc cannot be recovered.
This action can be performed only by the doc owner.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.permanent_delete
### Query Parameters
[RefPaperDoc](#data-types-refpaperdoc)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
### Return Values
Void
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/sharing_policy/get
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/sharing_policy/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\"}"
```

> The above command returns JSON structured like this:

```json
{
    "public_sharing_policy": {
        ".tag": "people_with_link_can_edit"
    }, 
    "team_sharing_policy": {
        ".tag": "people_with_link_can_edit"
    }
}
```

### Description
Gets the default sharing policy for the given Paper doc.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[RefPaperDoc](#data-types-refpaperdoc)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
### Return Values
[SharingPolicy](#data-types-sharingpolicy)

Sharing policy of Paper doc.

Field Name | Data Type | Description
--------- | ------- | -----------
public_sharing_policy | Optional[[SharingPublicPolicyType](#data-types-sharingpublicpolicytype)] | This value applies to the non-team members.<br>
team_sharing_policy | Optional[[SharingTeamPolicyType](#data-types-sharingteampolicytype)] | This value applies to the team members only. The value is null for all personal accounts.<br>
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/sharing_policy/set
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/sharing_policy/set \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"sharing_policy\": {\"public_sharing_policy\": \"people_with_link_can_edit\",\"team_sharing_policy\": \"people_with_link_can_edit\"}}"
```

### Description
Sets the default sharing policy for the given Paper doc. The default 'team_sharing_policy' can be changed only by teams, omit this field for personal accounts.
The 'public_sharing_policy' policy can't be set to the value 'disabled' because this setting can be changed only via the team admin console.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[PaperDocSharingPolicy](#data-types-paperdocsharingpolicy)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
sharing_policy | [SharingPolicy](#data-types-sharingpolicy) | The default sharing policy to be set for the Paper doc.<br>
### Return Values
Void
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/update
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/update \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"doc_update_policy\": \"overwrite_all\",\"revision\": 12345,\"import_format\": \"html\"}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @local_file.txt
```

> The above command returns JSON structured like this:

```json
{
    "doc_id": "uaSvRuxvnkFa12PTkBv5q", 
    "revision": 456736745, 
    "title": "Week one retention"
}
```

### Description
Updates an existing Paper doc with the provided content.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
This endpoint will be retired in September 2020. Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for more information.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-upload
### Required Scope
files.content.write
### Query Parameters
[PaperDocUpdateArgs](#data-types-paperdocupdateargs)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
doc_update_policy | [PaperDocUpdatePolicy](#data-types-paperdocupdatepolicy) | The policy used for the current update call.<br>
revision | Int64 | The latest doc revision. This value must match the head revision or an error code will be returned. This is to prevent colliding writes.<br>
import_format | [ImportFormat](#data-types-importformat) | The format of provided data.<br>
### Return Values
[PaperDocCreateUpdateResult](#data-types-paperdoccreateupdateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | Doc ID of the newly created doc.<br>
revision | Int64 | The Paper doc revision. Simply an ever increasing number.<br>
title | String | The Paper doc title.<br>
### Error Values
[PaperDocUpdateError](#data-types-paperdocupdateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
content_malformed | Void | The provided content was malformed and cannot be imported to Paper.<br>
revision_mismatch | Void | The provided revision does not match the document head.<br>
doc_length_exceeded | Void | The newly created Paper doc would be too large, split the content into multiple docs.<br>
image_size_exceeded | Void | The imported document contains an image that is too large. The current limit is 1MB. This only applies to HTML with data URI.<br>
doc_archived | Void | This operation is not allowed on archived Paper docs.<br>
doc_deleted | Void | This operation is not allowed on deleted Paper docs.<br>
## docs/users/add
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/users/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"members\": [{\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"},\"permission_level\": \"view_and_comment\"}],\"custom_message\": \"Welcome to Paper.\",\"quiet\": false}"
```

### Description
Allows an owner or editor to add users to a Paper doc or change their permissions using their email address or Dropbox account ID.
The doc owner's permissions cannot be changed.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[AddPaperDocUser](#data-types-addpaperdocuser)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
members | List[[AddMember](#data-types-addmember)] | User which should be added to the Paper doc. Specify only email address or Dropbox account ID.<br>
custom_message | Optional[String] | A personal message that will be emailed to each successfully added member.<br>
quiet | Boolean | Clients should set this to true if no email message shall be sent to added users.<br>
### Return Values
List[[AddPaperDocUserMemberResult](#data-types-addpaperdocusermemberresult)]
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/users/list
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/users/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"limit\": 100,\"filter_by\": \"shared\"}"
```

> The above command returns JSON structured like this:

```json
{
    "invitees": [
        {
            "invitee": {
                ".tag": "email", 
                "email": "jessica@example.com"
            }, 
            "permission_level": {
                ".tag": "edit"
            }
        }
    ], 
    "users": [
        {
            "user": {
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "email": "bob@example.com", 
                "display_name": "Robert Smith", 
                "same_team": true, 
                "team_member_id": "dbmid:abcd1234"
            }, 
            "permission_level": {
                ".tag": "view_and_comment"
            }
        }
    ], 
    "doc_owner": {
        "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
        "email": "bob@example.com", 
        "display_name": "Robert Smith", 
        "same_team": true, 
        "team_member_id": "dbmid:abcd1234"
    }, 
    "cursor": {
        "value": "zHZvTPBnXilGgm1AmDgVyZ10zf7qb0qznd5sAVQbbIvoteSnWLjUdLU7aR25hb", 
        "expiration": "2016-08-07T14:56:15Z"
    }, 
    "has_more": false
}
```

### Description
Lists all users who visited the Paper doc or users with explicit access. This call excludes users who have been removed. The list is sorted by the date of the visit or the share date.
The list will include both users, the explicitly shared ones as well as those who came in using the Paper url link.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListUsersOnPaperDocArgs](#data-types-listusersonpaperdocargs)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
limit | Int32 | Size limit per batch. The maximum number of users that can be retrieved per batch is 1000. Higher value results in invalid arguments error.<br>
filter_by | [UserOnPaperDocFilter](#data-types-useronpaperdocfilter) | Specify this attribute if you want to obtain users that have already accessed the Paper doc.<br>
### Return Values
[ListUsersOnPaperDocResponse](#data-types-listusersonpaperdocresponse)

Field Name | Data Type | Description
--------- | ------- | -----------
invitees | List[[InviteeInfoWithPermissionLevel](#data-types-inviteeinfowithpermissionlevel)] | List of email addresses with their respective permission levels that are invited on the Paper doc.<br>
users | List[[UserInfoWithPermissionLevel](#data-types-userinfowithpermissionlevel)] | List of users with their respective permission levels that are invited on the Paper folder.<br>
doc_owner | [UserInfo](#data-types-userinfo) | The Paper doc owner. This field is populated on every single response.<br>
cursor | [Cursor](#data-types-cursor) | Pass the cursor into [paper/docs/users/list/continue](#paper-docs-users-list-continue) to paginate through all users. The cursor preserves all properties as specified in the original call to [paper/docs/users/list](#paper-docs-users-list).<br>
has_more | Boolean | Will be set to True if a subsequent call with the provided cursor to [paper/docs/users/list/continue](#paper-docs-users-list-continue) returns immediately with some results. If set to False please allow some delay before making another call to [paper/docs/users/list/continue](#paper-docs-users-list-continue).<br>
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## docs/users/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/users/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"cursor\": \"U60b6BxT43ySd5sAVQbbIvoteSnWLjUdLU7aR25hbt3ySd5sAVQbbIvoteSnWLjUd\"}"
```

> The above command returns JSON structured like this:

```json
{
    "invitees": [
        {
            "invitee": {
                ".tag": "email", 
                "email": "jessica@example.com"
            }, 
            "permission_level": {
                ".tag": "edit"
            }
        }
    ], 
    "users": [
        {
            "user": {
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "email": "bob@example.com", 
                "display_name": "Robert Smith", 
                "same_team": true, 
                "team_member_id": "dbmid:abcd1234"
            }, 
            "permission_level": {
                ".tag": "view_and_comment"
            }
        }
    ], 
    "doc_owner": {
        "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
        "email": "bob@example.com", 
        "display_name": "Robert Smith", 
        "same_team": true, 
        "team_member_id": "dbmid:abcd1234"
    }, 
    "cursor": {
        "value": "zHZvTPBnXilGgm1AmDgVyZ10zf7qb0qznd5sAVQbbIvoteSnWLjUdLU7aR25hb", 
        "expiration": "2016-08-07T14:56:15Z"
    }, 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from docs/users/list, use this to paginate through all users on the Paper doc.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListUsersOnPaperDocContinueArgs](#data-types-listusersonpaperdoccontinueargs)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
cursor | String | The cursor obtained from [paper/docs/users/list](#paper-docs-users-list) or [paper/docs/users/list/continue](#paper-docs-users-list-continue). Allows for pagination.<br>
### Return Values
[ListUsersOnPaperDocResponse](#data-types-listusersonpaperdocresponse)

Field Name | Data Type | Description
--------- | ------- | -----------
invitees | List[[InviteeInfoWithPermissionLevel](#data-types-inviteeinfowithpermissionlevel)] | List of email addresses with their respective permission levels that are invited on the Paper doc.<br>
users | List[[UserInfoWithPermissionLevel](#data-types-userinfowithpermissionlevel)] | List of users with their respective permission levels that are invited on the Paper folder.<br>
doc_owner | [UserInfo](#data-types-userinfo) | The Paper doc owner. This field is populated on every single response.<br>
cursor | [Cursor](#data-types-cursor) | Pass the cursor into [paper/docs/users/list/continue](#paper-docs-users-list-continue) to paginate through all users. The cursor preserves all properties as specified in the original call to [paper/docs/users/list](#paper-docs-users-list).<br>
has_more | Boolean | Will be set to True if a subsequent call with the provided cursor to [paper/docs/users/list/continue](#paper-docs-users-list-continue) returns immediately with some results. If set to False please allow some delay before making another call to [paper/docs/users/list/continue](#paper-docs-users-list-continue).<br>
### Error Values
[ListUsersCursorError](#data-types-listuserscursorerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
cursor_error | [PaperApiCursorError](#data-types-paperapicursorerror) | 
## docs/users/remove
```shell
curl -X POST https://api.dropboxapi.com/2/paper/docs/users/remove \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"doc_id\": \"uaSvRuxvnkFa12PTkBv5q\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"}}"
```

### Description
Allows an owner or editor to remove users from a Paper doc using their email address or Dropbox account ID.
The doc owner cannot be removed.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RemovePaperDocUser](#data-types-removepaperdocuser)

Field Name | Data Type | Description
--------- | ------- | -----------
doc_id | String | The Paper doc ID.<br>
member | [MemberSelector](#data-types-memberselector) | User which should be removed from the Paper doc. Specify only email address or Dropbox account ID.<br>
### Return Values
Void
### Error Values
[DocLookupError](#data-types-doclookuperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
doc_not_found | Void | The required doc was not found.<br>
## folders/create
```shell
curl -X POST https://api.dropboxapi.com/2/paper/folders/create \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"name\": \"my new folder\"}"
```

> The above command returns JSON structured like this:

```json
{
    "folder_id": "abcd"
}
```

### Description
Create a new Paper folder with the provided info.
Note that this endpoint will continue to work for content created by users on the older version of Paper. To check which version of Paper a user is on, use /users/features/get_values. If the paper_as_files feature is enabled, then the user is running the new version of Paper.
Refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide) for migration information.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
files.content.write
### Query Parameters
[PaperFolderCreateArg](#data-types-paperfoldercreatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The name of the new Paper folder.<br>
parent_folder_id | Optional[String] | The encrypted Paper folder Id where the new Paper folder should be created. The API user has to have write access to this folder or error is thrown. If not supplied, the new folder will be created at top level.<br>
is_team_folder | Optional[Boolean] | Whether the folder to be created should be a team folder. This value will be ignored if parent_folder_id is supplied, as the new folder will inherit the type (private or team folder) from its parent. We will by default create a top-level private folder if both parent_folder_id and is_team_folder are not supplied.<br>
### Return Values
[PaperFolderCreateResult](#data-types-paperfoldercreateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
folder_id | String | Folder ID of the newly created folder.<br>
### Error Values
[PaperFolderCreateError](#data-types-paperfoldercreateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
insufficient_permissions | Void | Your account does not have permissions to perform this action. This may be due to it only having access to Paper as files in the Dropbox filesystem. For more information, refer to the [Paper Migration Guide](https://www.dropbox.com/lp/developers/reference/paper-migration-guide).<br>
other | Void | 
folder_not_found | Void | The specified parent Paper folder cannot be found.<br>
invalid_folder_id | Void | The folder id cannot be decrypted to valid folder id.<br>
# Sharing
## add_file_member
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/add_file_member \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"members\": [{\".tag\": \"email\",\"email\": \"justin@example.com\"}],\"custom_message\": \"This is a custom message about ACME.doc\",\"quiet\": false,\"access_level\": \"viewer\",\"add_message_as_comment\": false}"
```

### Description
Adds specified members to a file.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[AddFileMemberArgs](#data-types-addfilememberargs)

Arguments for [sharing/add_file_member](#sharing-add_file_member).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | File to which to add members.<br>
members | List[[MemberSelector](#data-types-memberselector)] | Members to add. Note that even an email address is given, this may result in a user being directy added to the membership if that email is the user's main account email.<br>
custom_message | Optional[String] | Message to send to added members in their invitation.<br>
quiet | Boolean | Whether added members should be notified via device notifications of their invitation.<br>
access_level | [AccessLevel](#data-types-accesslevel) | AccessLevel union object, describing what access level we want to give new members.<br>
add_message_as_comment | Boolean | If the custom message should be added as a comment on the file.<br>
### Return Values
List[[FileMemberActionResult](#data-types-filememberactionresult)]
### Error Values
[AddFileMemberError](#data-types-addfilemembererror)

Errors for [sharing/add_file_member](#sharing-add_file_member).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
rate_limit | Void | The user has reached the rate limit for invitations.<br>
invalid_comment | Void | The custom message did not pass comment permissions checks.<br>
other | Void | 
## add_folder_member
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/add_folder_member \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"members\": [{\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"},\"access_level\": \"editor\"},{\"member\": {\".tag\": \"dropbox_id\",\"dropbox_id\": \"dbid:AAEufNrMPSPe0dMQijRP0N_aZtBJRm26W4Q\"},\"access_level\": \"viewer\"}],\"quiet\": false,\"custom_message\": \"Documentation for launch day\"}"
```

### Description
Allows an owner or editor (if the ACL update policy allows) of a shared folder to add another member.
For the new member to get access to all the functionality for this folder, you will need to call mount_folder on their behalf.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[AddFolderMemberArg](#data-types-addfoldermemberarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
members | List[[AddMember](#data-types-addmember)] | The intended list of members to add.  Added members will receive invites to join the shared folder.<br>
quiet | Boolean | Whether added members should be notified via email and device notifications of their invite.<br>
custom_message | Optional[String] | Optional message to display to added members in their invitation.<br>
### Return Values
Void
### Error Values
[AddFolderMemberError](#data-types-addfoldermembererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | Unable to access shared folder.<br>
email_unverified | Void | The current user's e-mail address is unverified.<br>
banned_member | Void | The current user has been banned.<br>
bad_member | [AddMemberSelectorError](#data-types-addmemberselectorerror) | [AddFolderMemberArg.members](#data-types-addfoldermemberarg) contains a bad invitation recipient.<br>
cant_share_outside_team | Void | Your team policy does not allow sharing outside of the team.<br>
too_many_members | UInt64 | The value is the member limit that was reached.<br>
too_many_pending_invites | UInt64 | The value is the pending invite limit that was reached.<br>
rate_limit | Void | The current user has hit the limit of invites they can send per day. Try again in 24 hours.<br>
too_many_invitees | Void | The current user is trying to share with too many people at once.<br>
insufficient_plan | Void | The current user's account doesn't support this action. An example of this is when adding a read-only member. This action can only be performed by users that have upgraded to a Pro or Business plan.<br>
team_folder | Void | This action cannot be performed on a team shared folder.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
invalid_shared_folder | Void | Field is deprecated. Invalid shared folder error will be returned as an access_error.<br>
other | Void | 
## change_file_member_access
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/change_file_member_access \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"},\"access_level\": \"viewer\"}"
```

> The above command returns JSON structured like this:

```json
{
    "member": {
        ".tag": "email", 
        "email": "justin@example.com"
    }, 
    "result": {
        ".tag": "success"
    }
}
```

### Description
Identical to update_file_member but with less information returned.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[ChangeFileMemberAccessArgs](#data-types-changefilememberaccessargs)

Arguments for [sharing/change_file_member_access](#sharing-change_file_member_access).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | File for which we are changing a member's access.<br>
member | [MemberSelector](#data-types-memberselector) | The member whose access we are changing.<br>
access_level | [AccessLevel](#data-types-accesslevel) | The new access level for the member.<br>
### Return Values
[FileMemberActionResult](#data-types-filememberactionresult)

Per-member result for [sharing/add_file_member](#sharing-add_file_member) or [sharing/change_file_member_access](#sharing-change_file_member_access).

Field Name | Data Type | Description
--------- | ------- | -----------
member | [MemberSelector](#data-types-memberselector) | One of specified input members.<br>
result | [FileMemberActionIndividualResult](#data-types-filememberactionindividualresult) | The outcome of the action on this member.<br>
### Error Values
[FileMemberActionError](#data-types-filememberactionerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_member | Void | Specified member was not found.<br>
no_permission | Void | User does not have permission to perform this action on this member.<br>
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | Specified file was invalid or user does not have access.<br>
no_explicit_access | [MemberAccessLevelResult](#data-types-memberaccesslevelresult) | The action cannot be completed because the target member does not have explicit access to the file. The return value is the access that the member has to the file from a parent folder.<br>
other | Void | 
## check_job_status
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/check_job_status \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "in_progress"
}
```

### Description
Returns the status of an asynchronous job.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[JobStatus](#data-types-jobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | Void | The asynchronous job has finished.<br>
failed | [JobError](#data-types-joberror) | The asynchronous job returned an error.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## check_remove_member_job_status
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/check_remove_member_job_status \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Returns the status of an asynchronous job for sharing a folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[RemoveMemberJobStatus](#data-types-removememberjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [MemberAccessLevelResult](#data-types-memberaccesslevelresult) | Removing the folder member has finished. The value is information about whether the member has another form of access.<br>
failed | [RemoveFolderMemberError](#data-types-removefoldermembererror) | 
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## check_share_job_status
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/check_share_job_status \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "access_type": {
        ".tag": "owner"
    }, 
    "is_inside_team_folder": false, 
    "is_team_folder": false, 
    "name": "dir", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
    "shared_folder_id": "84528192421", 
    "time_invited": "2016-01-20T00:00:00Z", 
    "path_lower": "/dir", 
    "link_metadata": {
        "audience_options": [
            {
                ".tag": "public"
            }, 
            {
                ".tag": "team"
            }, 
            {
                ".tag": "members"
            }
        ], 
        "current_audience": {
            ".tag": "public"
        }, 
        "link_permissions": [
            {
                "action": {
                    ".tag": "change_audience"
                }, 
                "allow": true
            }
        ], 
        "password_protected": false, 
        "url": ""
    }, 
    "permissions": [], 
    "access_inheritance": {
        ".tag": "inherit"
    }
}
```

### Description
Returns the status of an asynchronous job for sharing a folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[ShareFolderJobStatus](#data-types-sharefolderjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [SharedFolderMetadata](#data-types-sharedfoldermetadata) | The share job has finished. The value is the metadata for the folder.<br>
failed | [ShareFolderError](#data-types-sharefoldererror) | 
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## create_shared_link
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/create_shared_link \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Homework/Math/Prime_Numbers.txt\",\"short_url\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
    "visibility": {
        ".tag": "public"
    }, 
    "path": "/Homework/Math/Prime_Numbers.txt"
}
```

### Description
Create a shared link.
If a shared link already exists for the given path, that link is returned.
Note that in the returned [PathLinkMetadata](#data-types-pathlinkmetadata), the [PathLinkMetadata.url](#data-types-pathlinkmetadata) field is the shortened URL if [CreateSharedLinkArg.short_url](#data-types-createsharedlinkarg) argument is set to true.
Previously, it was technically possible to break a shared link by moving or renaming the corresponding file or folder. In the future, this will no longer be the case, so your app shouldn't rely on this behavior. Instead, if your app needs to revoke a shared link, use revoke_shared_link.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[CreateSharedLinkArg](#data-types-createsharedlinkarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to share.<br>
short_url | Boolean | Whether to return a shortened URL.<br>
pending_upload | Optional[[PendingUploadMode](#data-types-pendinguploadmode)] | If it's okay to share a path that does not yet exist, set this to either [PendingUploadMode.file](#data-types-pendinguploadmode) or [PendingUploadMode.folder](#data-types-pendinguploadmode) to indicate whether to assume it's a file or folder.<br>
### Return Values
[PathLinkMetadata](#data-types-pathlinkmetadata)

Metadata for a path-based shared link.

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
visibility | [Visibility](#data-types-visibility) | Who can access the link.<br>
path | String | Path in user's Dropbox.<br>
expires | Optional[Timestamp] | Expiration time, if set. By default the link won't expire.<br>
### Error Values
[CreateSharedLinkError](#data-types-createsharedlinkerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
other | Void | 
## create_shared_link_with_settings
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/create_shared_link_with_settings \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/Prime_Numbers.txt\",\"settings\": {\"requested_visibility\": \"public\",\"audience\": \"public\",\"access\": \"viewer\"}}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
    "name": "Prime_Numbers.txt", 
    "link_permissions": {
        "can_revoke": false, 
        "resolved_visibility": {
            ".tag": "public"
        }, 
        "revoke_failure_reason": {
            ".tag": "owner_only"
        }
    }, 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "team_member_info": {
        "team_info": {
            "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
            "name": "Acme, Inc."
        }, 
        "display_name": "Roger Rabbit", 
        "member_id": "dbmid:abcd1234"
    }
}
```

### Description
Create a shared link with custom settings. If no settings are given then the default visibility is [RequestedVisibility.public](#data-types-requestedvisibility) (The resolved visibility, though, may depend on other aspects such as team and shared folder settings).
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[CreateSharedLinkWithSettingsArg](#data-types-createsharedlinkwithsettingsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to be shared by the shared link.<br>
settings | Optional[[SharedLinkSettings](#data-types-sharedlinksettings)] | The requested settings for the newly created shared link.<br>
### Return Values
[SharedLinkMetadata](#data-types-sharedlinkmetadata)

The metadata of a shared link.

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
name | String | The linked file name (including extension). This never contains a slash.<br>
link_permissions | [LinkPermissions](#data-types-linkpermissions) | The link's access permissions.<br>
id | Optional[String] | A unique identifier for the linked file.<br>
expires | Optional[Timestamp] | Expiration time, if set. By default the link won't expire.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will only be present only if the linked file is in the authenticated user's  dropbox.<br>
team_member_info | Optional[[TeamMemberInfo](#data-types-teammemberinfo)] | The team membership information of the link's owner.  This field will only be present  if the link's owner is a team member.<br>
content_owner_team_info | Optional[[Team](#data-types-team)] | The team information of the content's owner. This field will only be present if the content's owner is a team member and the content's owner team is different from the link's owner team.<br>
### Error Values
[CreateSharedLinkWithSettingsError](#data-types-createsharedlinkwithsettingserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
email_not_verified | Void | User's email should be verified.<br>
shared_link_already_exists | Optional[[SharedLinkAlreadyExistsMetadata](#data-types-sharedlinkalreadyexistsmetadata)] | The shared link already exists. You can call [sharing/list_shared_links](#sharing-list_shared_links) to get the  existing link, or use the provided metadata if it is returned.<br>
settings_error | [SharedLinkSettingsError](#data-types-sharedlinksettingserror) | There is an error with the given settings.<br>
access_denied | Void | Access to the requested path is forbidden.<br>
## get_file_metadata
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/get_file_metadata \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"actions\": []}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "id:3kmLmQFnf1AAAAAAAAAAAw", 
    "name": "file.txt", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fi/fir9vjelf", 
    "access_type": {
        ".tag": "viewer"
    }, 
    "owner_display_names": [
        "Jane Doe"
    ], 
    "owner_team": {
        "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
        "name": "Acme, Inc."
    }, 
    "path_display": "/dir/file.txt", 
    "path_lower": "/dir/file.txt", 
    "permissions": [], 
    "time_invited": "2016-01-20T00:00:00Z"
}
```

### Description
Returns shared file metadata.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[GetFileMetadataArg](#data-types-getfilemetadataarg)

Arguments of [sharing/get_file_metadata](#sharing-get_file_metadata).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | The file to query.<br>
actions | Optional[List[[FileAction](#data-types-fileaction)]] | A list of `FileAction`s corresponding to `FilePermission`s that should appear in the  response's [SharedFileMetadata.permissions](#data-types-sharedfilemetadata) field describing the actions the  authenticated user can perform on the file.<br>
### Return Values
[SharedFileMetadata](#data-types-sharedfilemetadata)

Properties of the shared file.

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The ID of the file.<br>
name | String | The name of this file.<br>
policy | [FolderPolicy](#data-types-folderpolicy) | Policies governing this shared file.<br>
preview_url | String | URL for displaying a web preview of the shared file.<br>
access_type | Optional[[AccessLevel](#data-types-accesslevel)] | The current user's access level for this shared file.<br>
expected_link_metadata | Optional[[ExpectedSharedContentLinkMetadata](#data-types-expectedsharedcontentlinkmetadata)] | The expected metadata of the link associated for the file when it is first shared. Absent if the link already exists. This is for an unreleased feature so it may not be returned yet.<br>
link_metadata | Optional[[SharedContentLinkMetadata](#data-types-sharedcontentlinkmetadata)] | The metadata of the link associated for the file. This is for an unreleased feature so it may not be returned yet.<br>
owner_display_names | Optional[List[String]] | The display names of the users that own the file. If the file is part of a team folder, the display names of the team admins are also included. Absent if the owner display names cannot be fetched.<br>
owner_team | Optional[[Team](#data-types-team)] | The team that owns the file. This field is not present if the file is not owned by a team.<br>
parent_shared_folder_id | Optional[String] | The ID of the parent shared folder. This field is present only if the file is contained within a shared folder.<br>
path_display | Optional[String] | The cased path to be used for display purposes only. In rare instances the casing will not correctly match the user's filesystem, but this behavior will match the path provided in the Core API v1. Absent for unmounted files.<br>
path_lower | Optional[String] | The lower-case full path of this file. Absent for unmounted files.<br>
permissions | Optional[List[[FilePermission](#data-types-filepermission)]] | The sharing permissions that requesting user has on this file. This corresponds to the entries given in [GetFileMetadataBatchArg.actions](#data-types-getfilemetadatabatcharg) or [GetFileMetadataArg.actions](#data-types-getfilemetadataarg).<br>
time_invited | Optional[Timestamp] | Timestamp indicating when the current user was invited to this shared file. If the user was not invited to the shared file, the timestamp will indicate when the user was invited to the parent shared folder. This value may be absent.<br>
### Error Values
[GetFileMetadataError](#data-types-getfilemetadataerror)

Error result for [sharing/get_file_metadata](#sharing-get_file_metadata).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
other | Void | 
## get_file_metadata/batch
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/get_file_metadata/batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"files\": [\"id:3kmLmQFnf1AAAAAAAAAAAw\",\"id:VvTaJu2VZzAAAAAAAAAADQ\"],\"actions\": []}"
```

### Description
Returns shared file metadata.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[GetFileMetadataBatchArg](#data-types-getfilemetadatabatcharg)

Arguments of [sharing/get_file_metadata/batch](#sharing-get_file_metadata-batch).

Field Name | Data Type | Description
--------- | ------- | -----------
files | List[String] | The files to query.<br>
actions | Optional[List[[FileAction](#data-types-fileaction)]] | A list of `FileAction`s corresponding to `FilePermission`s that should appear in the  response's [SharedFileMetadata.permissions](#data-types-sharedfilemetadata) field describing the actions the  authenticated user can perform on the file.<br>
### Return Values
List[[GetFileMetadataBatchResult](#data-types-getfilemetadatabatchresult)]
### Error Values
[SharingUserError](#data-types-sharingusererror)

User account had a problem preventing this action.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
email_unverified | Void | The current user must verify the account e-mail address before performing this action.<br>
other | Void | 
## get_folder_metadata
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/get_folder_metadata \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"actions\": []}"
```

> The above command returns JSON structured like this:

```json
{
    "access_type": {
        ".tag": "owner"
    }, 
    "is_inside_team_folder": false, 
    "is_team_folder": false, 
    "name": "dir", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
    "shared_folder_id": "84528192421", 
    "time_invited": "2016-01-20T00:00:00Z", 
    "path_lower": "/dir", 
    "link_metadata": {
        "audience_options": [
            {
                ".tag": "public"
            }, 
            {
                ".tag": "team"
            }, 
            {
                ".tag": "members"
            }
        ], 
        "current_audience": {
            ".tag": "public"
        }, 
        "link_permissions": [
            {
                "action": {
                    ".tag": "change_audience"
                }, 
                "allow": true
            }
        ], 
        "password_protected": false, 
        "url": ""
    }, 
    "permissions": [], 
    "access_inheritance": {
        ".tag": "inherit"
    }
}
```

### Description
Returns shared folder metadata by its folder ID.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[GetMetadataArgs](#data-types-getmetadataargs)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
actions | Optional[List[[FolderAction](#data-types-folderaction)]] | A list of `FolderAction`s corresponding to `FolderPermission`s that should appear in the  response's [SharedFolderMetadata.permissions](#data-types-sharedfoldermetadata) field describing the actions the  authenticated user can perform on the folder.<br>
### Return Values
[SharedFolderMetadata](#data-types-sharedfoldermetadata)

The metadata which includes basic information about the shared folder.

Field Name | Data Type | Description
--------- | ------- | -----------
access_type | [AccessLevel](#data-types-accesslevel) | The current user's access level for this shared folder.<br>
is_inside_team_folder | Boolean | Whether this folder is inside of a team folder.<br>
is_team_folder | Boolean | Whether this folder is a [team folder](https://www.dropbox.com/en/help/986).<br>
name | String | The name of the this shared folder.<br>
policy | [FolderPolicy](#data-types-folderpolicy) | Policies governing this shared folder.<br>
preview_url | String | URL for displaying a web preview of the shared folder.<br>
shared_folder_id | String | The ID of the shared folder.<br>
time_invited | Timestamp | Timestamp indicating when the current user was invited to this shared folder.<br>
owner_display_names | Optional[List[String]] | The display names of the users that own the folder. If the folder is part of a team folder, the display names of the team admins are also included. Absent if the owner display names cannot be fetched.<br>
owner_team | Optional[[Team](#data-types-team)] | The team that owns the folder. This field is not present if the folder is not owned by a team.<br>
parent_shared_folder_id | Optional[String] | The ID of the parent shared folder. This field is present only if the folder is contained within another shared folder.<br>
path_lower | Optional[String] | The lower-cased full path of this shared folder. Absent for unmounted folders.<br>
parent_folder_name | Optional[String] | Display name for the parent folder.<br>
link_metadata | Optional[[SharedContentLinkMetadata](#data-types-sharedcontentlinkmetadata)] | The metadata of the shared content link to this shared folder. Absent if there is no link on the folder. This is for an unreleased feature so it may not be returned yet.<br>
permissions | Optional[List[[FolderPermission](#data-types-folderpermission)]] | Actions the current user may perform on the folder and its contents. The set of permissions corresponds to the FolderActions in the request.<br>
access_inheritance | [AccessInheritance](#data-types-accessinheritance) | Whether the folder inherits its members from its parent.<br>
### Error Values
[SharedFolderAccessError](#data-types-sharedfolderaccesserror)

There is an error accessing the shared folder.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_id | Void | This shared folder ID is invalid.<br>
not_a_member | Void | The user is not a member of the shared folder thus cannot access it.<br>
email_unverified | Void | Field is deprecated. Never set.<br>
unmounted | Void | The shared folder is unmounted.<br>
other | Void | 
## get_shared_link_file
```shell
curl -X POST https://content.dropboxapi.com/2/sharing/get_shared_link_file \
    --header "Authorization: Bearer [access_token]" \
    --header "Dropbox-API-Arg: {\"url\": \"https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0\",\"path\": \"/Prime_Numbers.txt\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
    "name": "Prime_Numbers.txt", 
    "link_permissions": {
        "can_revoke": false, 
        "resolved_visibility": {
            ".tag": "public"
        }, 
        "revoke_failure_reason": {
            ".tag": "owner_only"
        }
    }, 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "team_member_info": {
        "team_info": {
            "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
            "name": "Acme, Inc."
        }, 
        "display_name": "Roger Rabbit", 
        "member_id": "dbmid:abcd1234"
    }
}
```

### Description
Download the shared link's file from a user's Dropbox.
### Authentication
User Authentication
### ENDPOINT FORMAT
Content-download
### Required Scope
sharing.read
### Query Parameters
[GetSharedLinkMetadataArg](#data-types-getsharedlinkmetadataarg)

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
path | Optional[String] | If the shared link is to a folder, this parameter can be used to retrieve the metadata for a specific file or sub-folder in this folder. A relative path should be used.<br>
link_password | Optional[String] | If the shared link has a password, this parameter can be used.<br>
### Return Values
[SharedLinkMetadata](#data-types-sharedlinkmetadata)

The metadata of a shared link.

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
name | String | The linked file name (including extension). This never contains a slash.<br>
link_permissions | [LinkPermissions](#data-types-linkpermissions) | The link's access permissions.<br>
id | Optional[String] | A unique identifier for the linked file.<br>
expires | Optional[Timestamp] | Expiration time, if set. By default the link won't expire.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will only be present only if the linked file is in the authenticated user's  dropbox.<br>
team_member_info | Optional[[TeamMemberInfo](#data-types-teammemberinfo)] | The team membership information of the link's owner.  This field will only be present  if the link's owner is a team member.<br>
content_owner_team_info | Optional[[Team](#data-types-team)] | The team information of the content's owner. This field will only be present if the content's owner is a team member and the content's owner team is different from the link's owner team.<br>
### Error Values
[GetSharedLinkFileError](#data-types-getsharedlinkfileerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
shared_link_not_found | Void | The shared link wasn't found.<br>
shared_link_access_denied | Void | The caller is not allowed to access this shared link.<br>
unsupported_link_type | Void | This type of link is not supported; use [sharing/files.export](#sharing-files.export) instead.<br>
other | Void | 
shared_link_is_directory | Void | Directories cannot be retrieved by this endpoint.<br>
## get_shared_link_metadata
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/get_shared_link_metadata \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"url\": \"https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0\",\"path\": \"/Prime_Numbers.txt\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
    "name": "Prime_Numbers.txt", 
    "link_permissions": {
        "can_revoke": false, 
        "resolved_visibility": {
            ".tag": "public"
        }, 
        "revoke_failure_reason": {
            ".tag": "owner_only"
        }
    }, 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "team_member_info": {
        "team_info": {
            "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
            "name": "Acme, Inc."
        }, 
        "display_name": "Roger Rabbit", 
        "member_id": "dbmid:abcd1234"
    }
}
```

### Description
Get the shared link's metadata.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[GetSharedLinkMetadataArg](#data-types-getsharedlinkmetadataarg)

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
path | Optional[String] | If the shared link is to a folder, this parameter can be used to retrieve the metadata for a specific file or sub-folder in this folder. A relative path should be used.<br>
link_password | Optional[String] | If the shared link has a password, this parameter can be used.<br>
### Return Values
[SharedLinkMetadata](#data-types-sharedlinkmetadata)

The metadata of a shared link.

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
name | String | The linked file name (including extension). This never contains a slash.<br>
link_permissions | [LinkPermissions](#data-types-linkpermissions) | The link's access permissions.<br>
id | Optional[String] | A unique identifier for the linked file.<br>
expires | Optional[Timestamp] | Expiration time, if set. By default the link won't expire.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will only be present only if the linked file is in the authenticated user's  dropbox.<br>
team_member_info | Optional[[TeamMemberInfo](#data-types-teammemberinfo)] | The team membership information of the link's owner.  This field will only be present  if the link's owner is a team member.<br>
content_owner_team_info | Optional[[Team](#data-types-team)] | The team information of the content's owner. This field will only be present if the content's owner is a team member and the content's owner team is different from the link's owner team.<br>
### Error Values
[SharedLinkError](#data-types-sharedlinkerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
shared_link_not_found | Void | The shared link wasn't found.<br>
shared_link_access_denied | Void | The caller is not allowed to access this shared link.<br>
unsupported_link_type | Void | This type of link is not supported; use [sharing/files.export](#sharing-files.export) instead.<br>
other | Void | 
## get_shared_links
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/get_shared_links \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"\"}"
```

> The above command returns JSON structured like this:

```json
{
    "links": [
        {
            ".tag": "path", 
            "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
            "visibility": {
                ".tag": "public"
            }, 
            "path": "/Homework/Math/Prime_Numbers.txt"
        }
    ]
}
```

### Description
Returns a list of [LinkMetadata](#data-types-linkmetadata) objects for this user, including collection links.
If no path is given, returns a list of all shared links for the current user, including collection links, up to a maximum of 1000 links.
If a non-empty path is given, returns a list of all shared links that allow access to the given path.  Collection links are never returned in this case.
Note that the url field in the response is never the shortened URL.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[GetSharedLinksArg](#data-types-getsharedlinksarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | Optional[String] | See [sharing/get_shared_links](#sharing-get_shared_links) description.<br>
### Return Values
[GetSharedLinksResult](#data-types-getsharedlinksresult)

Field Name | Data Type | Description
--------- | ------- | -----------
links | List[[LinkMetadata](#data-types-linkmetadata)] | Shared links applicable to the path argument.<br>
### Error Values
[GetSharedLinksError](#data-types-getsharedlinkserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | Optional[String] | 
other | Void | 
## list_file_members
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_file_members \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"include_inherited\": true,\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "users": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "user": {
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "email": "bob@example.com", 
                "display_name": "Robert Smith", 
                "same_team": true, 
                "team_member_id": "dbmid:abcd1234"
            }, 
            "permissions": [], 
            "is_inherited": false, 
            "time_last_seen": "2016-01-20T00:00:00Z", 
            "platform_type": {
                ".tag": "unknown"
            }
        }
    ], 
    "groups": [
        {
            "access_type": {
                ".tag": "editor"
            }, 
            "group": {
                "group_name": "Test group", 
                "group_id": "g:e2db7665347abcd600000000001a2b3c", 
                "group_management_type": {
                    ".tag": "user_managed"
                }, 
                "group_type": {
                    ".tag": "user_managed"
                }, 
                "is_member": false, 
                "is_owner": false, 
                "same_team": true, 
                "member_count": 10
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "invitees": [
        {
            "access_type": {
                ".tag": "viewer"
            }, 
            "invitee": {
                ".tag": "email", 
                "email": "jessica@example.com"
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ]
}
```

### Description
Use to obtain the members who have been invited to a file, both inherited and uninherited members.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFileMembersArg](#data-types-listfilemembersarg)

Arguments for [sharing/list_file_members](#sharing-list_file_members).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | The file for which you want to see members.<br>
actions | Optional[List[[MemberAction](#data-types-memberaction)]] | The actions for which to return permissions on a member.<br>
include_inherited | Boolean | Whether to include members who only have access from a parent shared folder.<br>
limit | UInt32 | Number of members to return max per query. Defaults to 100 if no limit is specified.<br>
### Return Values
[SharedFileMembers](#data-types-sharedfilemembers)

Shared file user, group, and invitee membership.
Used for the results of [sharing/list_file_members](#sharing-list_file_members) and [sharing/list_file_members/continue](#sharing-list_file_members-continue), and used as part of the results for [sharing/list_file_members/batch](#sharing-list_file_members-batch).

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[UserFileMembershipInfo](#data-types-userfilemembershipinfo)] | The list of user members of the shared file.<br>
groups | List[[GroupMembershipInfo](#data-types-groupmembershipinfo)] | The list of group members of the shared file.<br>
invitees | List[[InviteeMembershipInfo](#data-types-inviteemembershipinfo)] | The list of invited members of a file, but have not logged in and claimed this.<br>
cursor | Optional[String] | Present if there are additional shared file members that have not been returned yet. Pass the cursor into [sharing/list_file_members/continue](#sharing-list_file_members-continue) to list additional members.<br>
### Error Values
[ListFileMembersError](#data-types-listfilememberserror)

Error for [sharing/list_file_members](#sharing-list_file_members).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
other | Void | 
## list_file_members/batch
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_file_members/batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"files\": [\"id:3kmLmQFnf1AAAAAAAAAAAw\",\"id:VvTaJu2VZzAAAAAAAAAADQ\"],\"limit\": 10}"
```

### Description
Get members of multiple files at once. The arguments to this route are more limited, and the limit on query result size per file is more strict. To customize the results more, use the individual file endpoint.
Inherited users and groups are not included in the result, and permissions are not returned for this endpoint.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFileMembersBatchArg](#data-types-listfilemembersbatcharg)

Arguments for [sharing/list_file_members/batch](#sharing-list_file_members-batch).

Field Name | Data Type | Description
--------- | ------- | -----------
files | List[String] | Files for which to return members.<br>
limit | UInt32 | Number of members to return max per query. Defaults to 10 if no limit is specified.<br>
### Return Values
List[[ListFileMembersBatchResult](#data-types-listfilemembersbatchresult)]
### Error Values
[SharingUserError](#data-types-sharingusererror)

User account had a problem preventing this action.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
email_unverified | Void | The current user must verify the account e-mail address before performing this action.<br>
other | Void | 
## list_file_members/continue
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_file_members/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "users": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "user": {
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "email": "bob@example.com", 
                "display_name": "Robert Smith", 
                "same_team": true, 
                "team_member_id": "dbmid:abcd1234"
            }, 
            "permissions": [], 
            "is_inherited": false, 
            "time_last_seen": "2016-01-20T00:00:00Z", 
            "platform_type": {
                ".tag": "unknown"
            }
        }
    ], 
    "groups": [
        {
            "access_type": {
                ".tag": "editor"
            }, 
            "group": {
                "group_name": "Test group", 
                "group_id": "g:e2db7665347abcd600000000001a2b3c", 
                "group_management_type": {
                    ".tag": "user_managed"
                }, 
                "group_type": {
                    ".tag": "user_managed"
                }, 
                "is_member": false, 
                "is_owner": false, 
                "same_team": true, 
                "member_count": 10
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "invitees": [
        {
            "access_type": {
                ".tag": "viewer"
            }, 
            "invitee": {
                ".tag": "email", 
                "email": "jessica@example.com"
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ]
}
```

### Description
Once a cursor has been retrieved from list_file_members or list_file_members/batch, use this to paginate through all shared file members.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFileMembersContinueArg](#data-types-listfilememberscontinuearg)

Arguments for [sharing/list_file_members/continue](#sharing-list_file_members-continue).

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by your last call to [sharing/list_file_members](#sharing-list_file_members), [sharing/list_file_members/continue](#sharing-list_file_members-continue), or [sharing/list_file_members/batch](#sharing-list_file_members-batch).<br>
### Return Values
[SharedFileMembers](#data-types-sharedfilemembers)

Shared file user, group, and invitee membership.
Used for the results of [sharing/list_file_members](#sharing-list_file_members) and [sharing/list_file_members/continue](#sharing-list_file_members-continue), and used as part of the results for [sharing/list_file_members/batch](#sharing-list_file_members-batch).

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[UserFileMembershipInfo](#data-types-userfilemembershipinfo)] | The list of user members of the shared file.<br>
groups | List[[GroupMembershipInfo](#data-types-groupmembershipinfo)] | The list of group members of the shared file.<br>
invitees | List[[InviteeMembershipInfo](#data-types-inviteemembershipinfo)] | The list of invited members of a file, but have not logged in and claimed this.<br>
cursor | Optional[String] | Present if there are additional shared file members that have not been returned yet. Pass the cursor into [sharing/list_file_members/continue](#sharing-list_file_members-continue) to list additional members.<br>
### Error Values
[ListFileMembersContinueError](#data-types-listfilememberscontinueerror)

Error for [sharing/list_file_members/continue](#sharing-list_file_members-continue).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
invalid_cursor | Void | [ListFileMembersContinueArg.cursor](#data-types-listfilememberscontinuearg) is invalid.<br>
other | Void | 
## list_folder_members
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_folder_members \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"actions\": [],\"limit\": 10}"
```

> The above command returns JSON structured like this:

```json
{
    "users": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "user": {
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "email": "bob@example.com", 
                "display_name": "Robert Smith", 
                "same_team": true, 
                "team_member_id": "dbmid:abcd1234"
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "groups": [
        {
            "access_type": {
                ".tag": "editor"
            }, 
            "group": {
                "group_name": "Test group", 
                "group_id": "g:e2db7665347abcd600000000001a2b3c", 
                "group_management_type": {
                    ".tag": "user_managed"
                }, 
                "group_type": {
                    ".tag": "user_managed"
                }, 
                "is_member": false, 
                "is_owner": false, 
                "same_team": true, 
                "member_count": 10
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "invitees": [
        {
            "access_type": {
                ".tag": "viewer"
            }, 
            "invitee": {
                ".tag": "email", 
                "email": "jessica@example.com"
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Returns shared folder membership by its folder ID.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFolderMembersArgs](#data-types-listfoldermembersargs)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
actions | Optional[List[[MemberAction](#data-types-memberaction)]] | This is a list indicating whether each returned member will include a boolean value [MemberPermission.allow](#data-types-memberpermission) that describes whether the current user can perform the MemberAction on the member.<br>
limit | UInt32 | The maximum number of results that include members, groups and invitees to return per request.<br>
### Return Values
[SharedFolderMembers](#data-types-sharedfoldermembers)

Shared folder user and group membership.

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[UserMembershipInfo](#data-types-usermembershipinfo)] | The list of user members of the shared folder.<br>
groups | List[[GroupMembershipInfo](#data-types-groupmembershipinfo)] | The list of group members of the shared folder.<br>
invitees | List[[InviteeMembershipInfo](#data-types-inviteemembershipinfo)] | The list of invitees to the shared folder.<br>
cursor | Optional[String] | Present if there are additional shared folder members that have not been returned yet. Pass the cursor into [sharing/list_folder_members/continue](#sharing-list_folder_members-continue) to list additional members.<br>
### Error Values
[SharedFolderAccessError](#data-types-sharedfolderaccesserror)

There is an error accessing the shared folder.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_id | Void | This shared folder ID is invalid.<br>
not_a_member | Void | The user is not a member of the shared folder thus cannot access it.<br>
email_unverified | Void | Field is deprecated. Never set.<br>
unmounted | Void | The shared folder is unmounted.<br>
other | Void | 
## list_folder_members/continue
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_folder_members/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "users": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "user": {
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "email": "bob@example.com", 
                "display_name": "Robert Smith", 
                "same_team": true, 
                "team_member_id": "dbmid:abcd1234"
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "groups": [
        {
            "access_type": {
                ".tag": "editor"
            }, 
            "group": {
                "group_name": "Test group", 
                "group_id": "g:e2db7665347abcd600000000001a2b3c", 
                "group_management_type": {
                    ".tag": "user_managed"
                }, 
                "group_type": {
                    ".tag": "user_managed"
                }, 
                "is_member": false, 
                "is_owner": false, 
                "same_team": true, 
                "member_count": 10
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "invitees": [
        {
            "access_type": {
                ".tag": "viewer"
            }, 
            "invitee": {
                ".tag": "email", 
                "email": "jessica@example.com"
            }, 
            "permissions": [], 
            "is_inherited": false
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Once a cursor has been retrieved from list_folder_members, use this to paginate through all shared folder members.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFolderMembersContinueArg](#data-types-listfoldermemberscontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by your last call to [sharing/list_folder_members](#sharing-list_folder_members) or [sharing/list_folder_members/continue](#sharing-list_folder_members-continue).<br>
### Return Values
[SharedFolderMembers](#data-types-sharedfoldermembers)

Shared folder user and group membership.

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[UserMembershipInfo](#data-types-usermembershipinfo)] | The list of user members of the shared folder.<br>
groups | List[[GroupMembershipInfo](#data-types-groupmembershipinfo)] | The list of group members of the shared folder.<br>
invitees | List[[InviteeMembershipInfo](#data-types-inviteemembershipinfo)] | The list of invitees to the shared folder.<br>
cursor | Optional[String] | Present if there are additional shared folder members that have not been returned yet. Pass the cursor into [sharing/list_folder_members/continue](#sharing-list_folder_members-continue) to list additional members.<br>
### Error Values
[ListFolderMembersContinueError](#data-types-listfoldermemberscontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
invalid_cursor | Void | [ListFolderMembersContinueArg.cursor](#data-types-listfoldermemberscontinuearg) is invalid.<br>
other | Void | 
## list_folders
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_folders \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100,\"actions\": []}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "is_inside_team_folder": false, 
            "is_team_folder": false, 
            "name": "dir", 
            "policy": {
                "acl_update_policy": {
                    ".tag": "owner"
                }, 
                "shared_link_policy": {
                    ".tag": "anyone"
                }, 
                "member_policy": {
                    ".tag": "anyone"
                }, 
                "resolved_member_policy": {
                    ".tag": "team"
                }
            }, 
            "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
            "shared_folder_id": "84528192421", 
            "time_invited": "2016-01-20T00:00:00Z", 
            "path_lower": "/dir", 
            "link_metadata": {
                "audience_options": [
                    {
                        ".tag": "public"
                    }, 
                    {
                        ".tag": "team"
                    }, 
                    {
                        ".tag": "members"
                    }
                ], 
                "current_audience": {
                    ".tag": "public"
                }, 
                "link_permissions": [
                    {
                        "action": {
                            ".tag": "change_audience"
                        }, 
                        "allow": true
                    }
                ], 
                "password_protected": false, 
                "url": ""
            }, 
            "permissions": [], 
            "access_inheritance": {
                ".tag": "inherit"
            }
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Return the list of all shared folders the current user has access to.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFoldersArgs](#data-types-listfoldersargs)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | The maximum number of results to return per request.<br>
actions | Optional[List[[FolderAction](#data-types-folderaction)]] | A list of `FolderAction`s corresponding to `FolderPermission`s that should appear in the  response's [SharedFolderMetadata.permissions](#data-types-sharedfoldermetadata) field describing the actions the  authenticated user can perform on the folder.<br>
### Return Values
[ListFoldersResult](#data-types-listfoldersresult)

Result for [sharing/list_folders](#sharing-list_folders) or [sharing/list_mountable_folders](#sharing-list_mountable_folders), depending on which endpoint was requested.
Unmounted shared folders can be identified by the absence of [SharedFolderMetadata.path_lower](#data-types-sharedfoldermetadata).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[SharedFolderMetadata](#data-types-sharedfoldermetadata)] | List of all shared folders the authenticated user has access to.<br>
cursor | Optional[String] | Present if there are additional shared folders that have not been returned yet. Pass the cursor into the corresponding continue endpoint (either [sharing/list_folders/continue](#sharing-list_folders-continue) or [sharing/list_mountable_folders/continue](#sharing-list_mountable_folders-continue)) to list additional folders.<br>
### Error Values
Void
## list_folders/continue
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_folders/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "is_inside_team_folder": false, 
            "is_team_folder": false, 
            "name": "dir", 
            "policy": {
                "acl_update_policy": {
                    ".tag": "owner"
                }, 
                "shared_link_policy": {
                    ".tag": "anyone"
                }, 
                "member_policy": {
                    ".tag": "anyone"
                }, 
                "resolved_member_policy": {
                    ".tag": "team"
                }
            }, 
            "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
            "shared_folder_id": "84528192421", 
            "time_invited": "2016-01-20T00:00:00Z", 
            "path_lower": "/dir", 
            "link_metadata": {
                "audience_options": [
                    {
                        ".tag": "public"
                    }, 
                    {
                        ".tag": "team"
                    }, 
                    {
                        ".tag": "members"
                    }
                ], 
                "current_audience": {
                    ".tag": "public"
                }, 
                "link_permissions": [
                    {
                        "action": {
                            ".tag": "change_audience"
                        }, 
                        "allow": true
                    }
                ], 
                "password_protected": false, 
                "url": ""
            }, 
            "permissions": [], 
            "access_inheritance": {
                ".tag": "inherit"
            }
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Once a cursor has been retrieved from list_folders, use this to paginate through all shared folders. The cursor must come from a previous call to list_folders or list_folders/continue.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFoldersContinueArg](#data-types-listfolderscontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by the previous API call specified in the endpoint description.<br>
### Return Values
[ListFoldersResult](#data-types-listfoldersresult)

Result for [sharing/list_folders](#sharing-list_folders) or [sharing/list_mountable_folders](#sharing-list_mountable_folders), depending on which endpoint was requested.
Unmounted shared folders can be identified by the absence of [SharedFolderMetadata.path_lower](#data-types-sharedfoldermetadata).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[SharedFolderMetadata](#data-types-sharedfoldermetadata)] | List of all shared folders the authenticated user has access to.<br>
cursor | Optional[String] | Present if there are additional shared folders that have not been returned yet. Pass the cursor into the corresponding continue endpoint (either [sharing/list_folders/continue](#sharing-list_folders-continue) or [sharing/list_mountable_folders/continue](#sharing-list_mountable_folders-continue)) to list additional folders.<br>
### Error Values
[ListFoldersContinueError](#data-types-listfolderscontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | [ListFoldersContinueArg.cursor](#data-types-listfolderscontinuearg) is invalid.<br>
other | Void | 
## list_mountable_folders
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_mountable_folders \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100,\"actions\": []}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "is_inside_team_folder": false, 
            "is_team_folder": false, 
            "name": "dir", 
            "policy": {
                "acl_update_policy": {
                    ".tag": "owner"
                }, 
                "shared_link_policy": {
                    ".tag": "anyone"
                }, 
                "member_policy": {
                    ".tag": "anyone"
                }, 
                "resolved_member_policy": {
                    ".tag": "team"
                }
            }, 
            "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
            "shared_folder_id": "84528192421", 
            "time_invited": "2016-01-20T00:00:00Z", 
            "path_lower": "/dir", 
            "link_metadata": {
                "audience_options": [
                    {
                        ".tag": "public"
                    }, 
                    {
                        ".tag": "team"
                    }, 
                    {
                        ".tag": "members"
                    }
                ], 
                "current_audience": {
                    ".tag": "public"
                }, 
                "link_permissions": [
                    {
                        "action": {
                            ".tag": "change_audience"
                        }, 
                        "allow": true
                    }
                ], 
                "password_protected": false, 
                "url": ""
            }, 
            "permissions": [], 
            "access_inheritance": {
                ".tag": "inherit"
            }
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Return the list of all shared folders the current user can mount or unmount.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFoldersArgs](#data-types-listfoldersargs)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | The maximum number of results to return per request.<br>
actions | Optional[List[[FolderAction](#data-types-folderaction)]] | A list of `FolderAction`s corresponding to `FolderPermission`s that should appear in the  response's [SharedFolderMetadata.permissions](#data-types-sharedfoldermetadata) field describing the actions the  authenticated user can perform on the folder.<br>
### Return Values
[ListFoldersResult](#data-types-listfoldersresult)

Result for [sharing/list_folders](#sharing-list_folders) or [sharing/list_mountable_folders](#sharing-list_mountable_folders), depending on which endpoint was requested.
Unmounted shared folders can be identified by the absence of [SharedFolderMetadata.path_lower](#data-types-sharedfoldermetadata).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[SharedFolderMetadata](#data-types-sharedfoldermetadata)] | List of all shared folders the authenticated user has access to.<br>
cursor | Optional[String] | Present if there are additional shared folders that have not been returned yet. Pass the cursor into the corresponding continue endpoint (either [sharing/list_folders/continue](#sharing-list_folders-continue) or [sharing/list_mountable_folders/continue](#sharing-list_mountable_folders-continue)) to list additional folders.<br>
### Error Values
Void
## list_mountable_folders/continue
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_mountable_folders/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "access_type": {
                ".tag": "owner"
            }, 
            "is_inside_team_folder": false, 
            "is_team_folder": false, 
            "name": "dir", 
            "policy": {
                "acl_update_policy": {
                    ".tag": "owner"
                }, 
                "shared_link_policy": {
                    ".tag": "anyone"
                }, 
                "member_policy": {
                    ".tag": "anyone"
                }, 
                "resolved_member_policy": {
                    ".tag": "team"
                }
            }, 
            "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
            "shared_folder_id": "84528192421", 
            "time_invited": "2016-01-20T00:00:00Z", 
            "path_lower": "/dir", 
            "link_metadata": {
                "audience_options": [
                    {
                        ".tag": "public"
                    }, 
                    {
                        ".tag": "team"
                    }, 
                    {
                        ".tag": "members"
                    }
                ], 
                "current_audience": {
                    ".tag": "public"
                }, 
                "link_permissions": [
                    {
                        "action": {
                            ".tag": "change_audience"
                        }, 
                        "allow": true
                    }
                ], 
                "password_protected": false, 
                "url": ""
            }, 
            "permissions": [], 
            "access_inheritance": {
                ".tag": "inherit"
            }
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Once a cursor has been retrieved from list_mountable_folders, use this to paginate through all mountable shared folders. The cursor must come from a previous call to list_mountable_folders or list_mountable_folders/continue.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFoldersContinueArg](#data-types-listfolderscontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | The cursor returned by the previous API call specified in the endpoint description.<br>
### Return Values
[ListFoldersResult](#data-types-listfoldersresult)

Result for [sharing/list_folders](#sharing-list_folders) or [sharing/list_mountable_folders](#sharing-list_mountable_folders), depending on which endpoint was requested.
Unmounted shared folders can be identified by the absence of [SharedFolderMetadata.path_lower](#data-types-sharedfoldermetadata).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[SharedFolderMetadata](#data-types-sharedfoldermetadata)] | List of all shared folders the authenticated user has access to.<br>
cursor | Optional[String] | Present if there are additional shared folders that have not been returned yet. Pass the cursor into the corresponding continue endpoint (either [sharing/list_folders/continue](#sharing-list_folders-continue) or [sharing/list_mountable_folders/continue](#sharing-list_mountable_folders-continue)) to list additional folders.<br>
### Error Values
[ListFoldersContinueError](#data-types-listfolderscontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | [ListFoldersContinueArg.cursor](#data-types-listfolderscontinuearg) is invalid.<br>
other | Void | 
## list_received_files
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_received_files \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100,\"actions\": []}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "id": "id:3kmLmQFnf1AAAAAAAAAAAw", 
            "name": "file.txt", 
            "policy": {
                "acl_update_policy": {
                    ".tag": "owner"
                }, 
                "shared_link_policy": {
                    ".tag": "anyone"
                }, 
                "member_policy": {
                    ".tag": "anyone"
                }, 
                "resolved_member_policy": {
                    ".tag": "team"
                }
            }, 
            "preview_url": "https://www.dropbox.com/scl/fi/fir9vjelf", 
            "access_type": {
                ".tag": "viewer"
            }, 
            "owner_display_names": [
                "Jane Doe"
            ], 
            "owner_team": {
                "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
                "name": "Acme, Inc."
            }, 
            "path_display": "/dir/file.txt", 
            "path_lower": "/dir/file.txt", 
            "permissions": [], 
            "time_invited": "2016-01-20T00:00:00Z"
        }
    ], 
    "cursor": "AzJJbGlzdF90eXBdofe9c3RPbGlzdGFyZ3NfYnlfZ2lkMRhcbric7Rdog9cmV2aXNpb24H3Qf6o1fkHxQ"
}
```

### Description
Returns a list of all files shared with current user.
 Does not include files the user has received via shared folders, and does  not include unclaimed invitations.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFilesArg](#data-types-listfilesarg)

Arguments for [sharing/list_received_files](#sharing-list_received_files).

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | Number of files to return max per query. Defaults to 100 if no limit is specified.<br>
actions | Optional[List[[FileAction](#data-types-fileaction)]] | A list of `FileAction`s corresponding to `FilePermission`s that should appear in the  response's [SharedFileMetadata.permissions](#data-types-sharedfilemetadata) field describing the actions the  authenticated user can perform on the file.<br>
### Return Values
[ListFilesResult](#data-types-listfilesresult)

Success results for [sharing/list_received_files](#sharing-list_received_files).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[SharedFileMetadata](#data-types-sharedfilemetadata)] | Information about the files shared with current user.<br>
cursor | Optional[String] | Cursor used to obtain additional shared files.<br>
### Error Values
[SharingUserError](#data-types-sharingusererror)

User account had a problem preventing this action.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
email_unverified | Void | The current user must verify the account e-mail address before performing this action.<br>
other | Void | 
## list_received_files/continue
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_received_files/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"AzJJbGlzdF90eXBdofe9c3RPbGlzdGFyZ3NfYnlfZ2lkMRhcbric7Rdog9emfGRlc2MCRWxpbWl0BGRId\"}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "id": "id:3kmLmQFnf1AAAAAAAAAAAw", 
            "name": "file.txt", 
            "policy": {
                "acl_update_policy": {
                    ".tag": "owner"
                }, 
                "shared_link_policy": {
                    ".tag": "anyone"
                }, 
                "member_policy": {
                    ".tag": "anyone"
                }, 
                "resolved_member_policy": {
                    ".tag": "team"
                }
            }, 
            "preview_url": "https://www.dropbox.com/scl/fi/fir9vjelf", 
            "access_type": {
                ".tag": "viewer"
            }, 
            "owner_display_names": [
                "Jane Doe"
            ], 
            "owner_team": {
                "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
                "name": "Acme, Inc."
            }, 
            "path_display": "/dir/file.txt", 
            "path_lower": "/dir/file.txt", 
            "permissions": [], 
            "time_invited": "2016-01-20T00:00:00Z"
        }
    ], 
    "cursor": "AzJJbGlzdF90eXBdofe9c3RPbGlzdGFyZ3NfYnlfZ2lkMRhcbric7Rdog9cmV2aXNpb24H3Qf6o1fkHxQ"
}
```

### Description
Get more results with a cursor from list_received_files.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListFilesContinueArg](#data-types-listfilescontinuearg)

Arguments for [sharing/list_received_files/continue](#sharing-list_received_files-continue).

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Cursor in [ListFilesResult.cursor](#data-types-listfilesresult).<br>
### Return Values
[ListFilesResult](#data-types-listfilesresult)

Success results for [sharing/list_received_files](#sharing-list_received_files).

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[SharedFileMetadata](#data-types-sharedfilemetadata)] | Information about the files shared with current user.<br>
cursor | Optional[String] | Cursor used to obtain additional shared files.<br>
### Error Values
[ListFilesContinueError](#data-types-listfilescontinueerror)

Error results for [sharing/list_received_files/continue](#sharing-list_received_files-continue).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | User account had a problem.<br>
invalid_cursor | Void | [ListFilesContinueArg.cursor](#data-types-listfilescontinuearg) is invalid.<br>
other | Void | 
## list_shared_links
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/list_shared_links \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "links": [
        {
            ".tag": "file", 
            "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
            "name": "Prime_Numbers.txt", 
            "link_permissions": {
                "can_revoke": false, 
                "resolved_visibility": {
                    ".tag": "public"
                }, 
                "revoke_failure_reason": {
                    ".tag": "owner_only"
                }
            }, 
            "client_modified": "2015-05-12T15:50:38Z", 
            "server_modified": "2015-05-12T15:50:38Z", 
            "rev": "a1c10ce0dd78", 
            "size": 7212, 
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "path_lower": "/homework/math/prime_numbers.txt", 
            "team_member_info": {
                "team_info": {
                    "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
                    "name": "Acme, Inc."
                }, 
                "display_name": "Roger Rabbit", 
                "member_id": "dbmid:abcd1234"
            }
        }
    ], 
    "has_more": true, 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
List shared links of this user.
If no path is given, returns a list of all shared links for the current user.
If a non-empty path is given, returns a list of all shared links that allow access to the given path - direct links to the given path and links to parent folders of the given path. Links to parent folders can be suppressed by setting direct_only to true.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[ListSharedLinksArg](#data-types-listsharedlinksarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | Optional[String] | See [sharing/list_shared_links](#sharing-list_shared_links) description.<br>
cursor | Optional[String] | The cursor returned by your last call to [sharing/list_shared_links](#sharing-list_shared_links).<br>
direct_only | Optional[Boolean] | See [sharing/list_shared_links](#sharing-list_shared_links) description.<br>
### Return Values
[ListSharedLinksResult](#data-types-listsharedlinksresult)

Field Name | Data Type | Description
--------- | ------- | -----------
links | List[[SharedLinkMetadata](#data-types-sharedlinkmetadata)] | Shared links applicable to the path argument.<br>
has_more | Boolean | Is true if there are additional shared links that have not been returned yet. Pass the cursor into [sharing/list_shared_links](#sharing-list_shared_links) to retrieve them.<br>
cursor | Optional[String] | Pass the cursor into [sharing/list_shared_links](#sharing-list_shared_links) to obtain the additional links. Cursor is returned only if no path is given.<br>
### Error Values
[ListSharedLinksError](#data-types-listsharedlinkserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
path | [LookupError](#data-types-lookuperror) | 
reset | Void | Indicates that the cursor has been invalidated. Call [sharing/list_shared_links](#sharing-list_shared_links) to obtain a new cursor.<br>
other | Void | 
## modify_shared_link_settings
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/modify_shared_link_settings \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"url\": \"https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0\",\"settings\": {\"requested_visibility\": \"public\",\"audience\": \"public\",\"access\": \"viewer\"},\"remove_expiration\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "file", 
    "url": "https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0", 
    "name": "Prime_Numbers.txt", 
    "link_permissions": {
        "can_revoke": false, 
        "resolved_visibility": {
            ".tag": "public"
        }, 
        "revoke_failure_reason": {
            ".tag": "owner_only"
        }
    }, 
    "client_modified": "2015-05-12T15:50:38Z", 
    "server_modified": "2015-05-12T15:50:38Z", 
    "rev": "a1c10ce0dd78", 
    "size": 7212, 
    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
    "path_lower": "/homework/math/prime_numbers.txt", 
    "team_member_info": {
        "team_info": {
            "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
            "name": "Acme, Inc."
        }, 
        "display_name": "Roger Rabbit", 
        "member_id": "dbmid:abcd1234"
    }
}
```

### Description
Modify the shared link's settings.
If the requested visibility conflict with the shared links policy of the team or the shared folder (in case the linked file is part of a shared folder) then the [LinkPermissions.resolved_visibility](#data-types-linkpermissions) of the returned [SharedLinkMetadata](#data-types-sharedlinkmetadata) will reflect the actual visibility of the shared link and the [LinkPermissions.requested_visibility](#data-types-linkpermissions) will reflect the requested visibility.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[ModifySharedLinkSettingsArgs](#data-types-modifysharedlinksettingsargs)

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link to change its settings.<br>
settings | [SharedLinkSettings](#data-types-sharedlinksettings) | Set of settings for the shared link.<br>
remove_expiration | Boolean | If set to true, removes the expiration of the shared link.<br>
### Return Values
[SharedLinkMetadata](#data-types-sharedlinkmetadata)

The metadata of a shared link.

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
name | String | The linked file name (including extension). This never contains a slash.<br>
link_permissions | [LinkPermissions](#data-types-linkpermissions) | The link's access permissions.<br>
id | Optional[String] | A unique identifier for the linked file.<br>
expires | Optional[Timestamp] | Expiration time, if set. By default the link won't expire.<br>
path_lower | Optional[String] | The lowercased full path in the user's Dropbox. This always starts with a slash. This field will only be present only if the linked file is in the authenticated user's  dropbox.<br>
team_member_info | Optional[[TeamMemberInfo](#data-types-teammemberinfo)] | The team membership information of the link's owner.  This field will only be present  if the link's owner is a team member.<br>
content_owner_team_info | Optional[[Team](#data-types-team)] | The team information of the content's owner. This field will only be present if the content's owner is a team member and the content's owner team is different from the link's owner team.<br>
### Error Values
[ModifySharedLinkSettingsError](#data-types-modifysharedlinksettingserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
shared_link_not_found | Void | The shared link wasn't found.<br>
shared_link_access_denied | Void | The caller is not allowed to access this shared link.<br>
unsupported_link_type | Void | This type of link is not supported; use [sharing/files.export](#sharing-files.export) instead.<br>
other | Void | 
settings_error | [SharedLinkSettingsError](#data-types-sharedlinksettingserror) | There is an error with the given settings.<br>
email_not_verified | Void | The caller's email should be verified.<br>
## mount_folder
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/mount_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\"}"
```

> The above command returns JSON structured like this:

```json
{
    "access_type": {
        ".tag": "owner"
    }, 
    "is_inside_team_folder": false, 
    "is_team_folder": false, 
    "name": "dir", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
    "shared_folder_id": "84528192421", 
    "time_invited": "2016-01-20T00:00:00Z", 
    "path_lower": "/dir", 
    "link_metadata": {
        "audience_options": [
            {
                ".tag": "public"
            }, 
            {
                ".tag": "team"
            }, 
            {
                ".tag": "members"
            }
        ], 
        "current_audience": {
            ".tag": "public"
        }, 
        "link_permissions": [
            {
                "action": {
                    ".tag": "change_audience"
                }, 
                "allow": true
            }
        ], 
        "password_protected": false, 
        "url": ""
    }, 
    "permissions": [], 
    "access_inheritance": {
        ".tag": "inherit"
    }
}
```

### Description
The current user mounts the designated folder.
Mount a shared folder for a user after they have been added as a member. Once mounted, the shared folder will appear in their Dropbox.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[MountFolderArg](#data-types-mountfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID of the shared folder to mount.<br>
### Return Values
[SharedFolderMetadata](#data-types-sharedfoldermetadata)

The metadata which includes basic information about the shared folder.

Field Name | Data Type | Description
--------- | ------- | -----------
access_type | [AccessLevel](#data-types-accesslevel) | The current user's access level for this shared folder.<br>
is_inside_team_folder | Boolean | Whether this folder is inside of a team folder.<br>
is_team_folder | Boolean | Whether this folder is a [team folder](https://www.dropbox.com/en/help/986).<br>
name | String | The name of the this shared folder.<br>
policy | [FolderPolicy](#data-types-folderpolicy) | Policies governing this shared folder.<br>
preview_url | String | URL for displaying a web preview of the shared folder.<br>
shared_folder_id | String | The ID of the shared folder.<br>
time_invited | Timestamp | Timestamp indicating when the current user was invited to this shared folder.<br>
owner_display_names | Optional[List[String]] | The display names of the users that own the folder. If the folder is part of a team folder, the display names of the team admins are also included. Absent if the owner display names cannot be fetched.<br>
owner_team | Optional[[Team](#data-types-team)] | The team that owns the folder. This field is not present if the folder is not owned by a team.<br>
parent_shared_folder_id | Optional[String] | The ID of the parent shared folder. This field is present only if the folder is contained within another shared folder.<br>
path_lower | Optional[String] | The lower-cased full path of this shared folder. Absent for unmounted folders.<br>
parent_folder_name | Optional[String] | Display name for the parent folder.<br>
link_metadata | Optional[[SharedContentLinkMetadata](#data-types-sharedcontentlinkmetadata)] | The metadata of the shared content link to this shared folder. Absent if there is no link on the folder. This is for an unreleased feature so it may not be returned yet.<br>
permissions | Optional[List[[FolderPermission](#data-types-folderpermission)]] | Actions the current user may perform on the folder and its contents. The set of permissions corresponds to the FolderActions in the request.<br>
access_inheritance | [AccessInheritance](#data-types-accessinheritance) | Whether the folder inherits its members from its parent.<br>
### Error Values
[MountFolderError](#data-types-mountfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
inside_shared_folder | Void | Mounting would cause a shared folder to be inside another, which is disallowed.<br>
insufficient_quota | [InsufficientQuotaAmounts](#data-types-insufficientquotaamounts) | The current user does not have enough space to mount the shared folder.<br>
already_mounted | Void | The shared folder is already mounted.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
not_mountable | Void | The shared folder is not mountable. One example where this can occur is when the shared folder belongs within a team folder in the user's Dropbox.<br>
other | Void | 
## relinquish_file_membership
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/relinquish_file_membership \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\"}"
```

### Description
The current user relinquishes their membership in the designated file. Note that the current user may still have inherited access to this file through the parent folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RelinquishFileMembershipArg](#data-types-relinquishfilemembershiparg)

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | The path or id for the file.<br>
### Return Values
Void
### Error Values
[RelinquishFileMembershipError](#data-types-relinquishfilemembershiperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
group_access | Void | The current user has access to the shared file via a group.  You can't relinquish membership to a file shared via groups.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
other | Void | 
## relinquish_folder_membership
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/relinquish_folder_membership \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"leave_a_copy\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
The current user relinquishes their membership in the designated shared folder and will no longer have access to the folder.  A folder owner cannot relinquish membership in their own folder.
This will run synchronously if leave_a_copy is false, and asynchronously if leave_a_copy is true.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RelinquishFolderMembershipArg](#data-types-relinquishfoldermembershiparg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
leave_a_copy | Boolean | Keep a copy of the folder's contents upon relinquishing membership.<br>
### Return Values
[LaunchEmptyResult](#data-types-launchemptyresult)

Result returned by methods that may either launch an asynchronous job or complete synchronously. Upon synchronous completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | Void | The job finished synchronously and successfully.<br>
### Error Values
[RelinquishFolderMembershipError](#data-types-relinquishfoldermembershiperror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
folder_owner | Void | The current user is the owner of the shared folder. Owners cannot relinquish membership to their own folders. Try unsharing or transferring ownership first.<br>
mounted | Void | The shared folder is currently mounted.  Unmount the shared folder before relinquishing membership.<br>
group_access | Void | The current user has access to the shared folder via a group.  You can't relinquish membership to folders shared via groups.<br>
team_folder | Void | This action cannot be performed on a team shared folder.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
no_explicit_access | Void | The current user only has inherited access to the shared folder.  You can't relinquish inherited membership to folders.<br>
other | Void | 
## remove_file_member
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/remove_file_member \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"}}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "success"
}
```

### Description
Identical to remove_file_member_2 but with less information returned.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RemoveFileMemberArg](#data-types-removefilememberarg)

Arguments for [sharing/remove_file_member_2](#sharing-remove_file_member_2).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | File from which to remove members.<br>
member | [MemberSelector](#data-types-memberselector) | Member to remove from this file. Note that even if an email is specified, it may result in the removal of a user (not an invitee) if the user's main account corresponds to that email address.<br>
### Return Values
[FileMemberActionIndividualResult](#data-types-filememberactionindividualresult)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
success | Optional[[AccessLevel](#data-types-accesslevel)] | Member was successfully removed from this file. If AccessLevel is given, the member still has access via a parent shared folder.<br>
member_error | [FileMemberActionError](#data-types-filememberactionerror) | User was not able to perform this action.<br>
### Error Values
[RemoveFileMemberError](#data-types-removefilemembererror)

Errors for [sharing/remove_file_member_2](#sharing-remove_file_member_2).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
no_explicit_access | [MemberAccessLevelResult](#data-types-memberaccesslevelresult) | This member does not have explicit access to the file and therefore cannot be removed. The return value is the access that a user might have to the file from a parent folder.<br>
other | Void | 
## remove_file_member_2
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/remove_file_member_2 \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"}}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "other"
}
```

### Description
Removes a specified member from the file.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RemoveFileMemberArg](#data-types-removefilememberarg)

Arguments for [sharing/remove_file_member_2](#sharing-remove_file_member_2).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | File from which to remove members.<br>
member | [MemberSelector](#data-types-memberselector) | Member to remove from this file. Note that even if an email is specified, it may result in the removal of a user (not an invitee) if the user's main account corresponds to that email address.<br>
### Return Values
[FileMemberRemoveActionResult](#data-types-filememberremoveactionresult)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
success | [MemberAccessLevelResult](#data-types-memberaccesslevelresult) | Member was successfully removed from this file.<br>
member_error | [FileMemberActionError](#data-types-filememberactionerror) | User was not able to remove this member.<br>
other | Void | 
### Error Values
[RemoveFileMemberError](#data-types-removefilemembererror)

Errors for [sharing/remove_file_member_2](#sharing-remove_file_member_2).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
no_explicit_access | [MemberAccessLevelResult](#data-types-memberaccesslevelresult) | This member does not have explicit access to the file and therefore cannot be removed. The return value is the access that a user might have to the file from a parent folder.<br>
other | Void | 
## remove_folder_member
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/remove_folder_member \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"},\"leave_a_copy\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "async_job_id", 
    "async_job_id": "34g93hh34h04y384084"
}
```

### Description
Allows an owner or editor (if the ACL update policy allows) of a shared folder to remove another member.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RemoveFolderMemberArg](#data-types-removefoldermemberarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
member | [MemberSelector](#data-types-memberselector) | The member to remove from the folder.<br>
leave_a_copy | Boolean | If true, the removed user will keep their copy of the folder after it's unshared, assuming it was mounted. Otherwise, it will be removed from their Dropbox. Also, this must be set to false when kicking a group.<br>
### Return Values
[LaunchResultBase](#data-types-launchresultbase)

Result returned by methods that launch an asynchronous job.
A method who may either launch an asynchronous job, or complete the request synchronously, can use this union by extending it, and adding a 'complete' field with the type of the synchronous response.
See [LaunchEmptyResult](#data-types-launchemptyresult) for an example.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
### Error Values
[RemoveFolderMemberError](#data-types-removefoldermembererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
member_error | [SharedFolderMemberError](#data-types-sharedfoldermembererror) | 
folder_owner | Void | The target user is the owner of the shared folder. You can't remove this user until ownership has been transferred to another member.<br>
group_access | Void | The target user has access to the shared folder via a group.<br>
team_folder | Void | This action cannot be performed on a team shared folder.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
too_many_files | Void | This shared folder has too many files for leaving a copy. You can still remove this user without leaving a copy.<br>
other | Void | 
## revoke_shared_link
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/revoke_shared_link \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"url\": \"https://www.dropbox.com/s/2sn712vy1ovegw8/Prime_Numbers.txt?dl=0\"}"
```

### Description
Revoke a shared link.
Note that even after revoking a shared link to a file, the file may be accessible if there are shared links leading to any of the file parent folders. To list all shared links that enable access to a specific file, you can use the list_shared_links with the file as the [ListSharedLinksArg.path](#data-types-listsharedlinksarg) argument.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[RevokeSharedLinkArg](#data-types-revokesharedlinkarg)

Field Name | Data Type | Description
--------- | ------- | -----------
url | String | URL of the shared link.<br>
### Return Values
Void
### Error Values
[RevokeSharedLinkError](#data-types-revokesharedlinkerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
shared_link_not_found | Void | The shared link wasn't found.<br>
shared_link_access_denied | Void | The caller is not allowed to access this shared link.<br>
unsupported_link_type | Void | This type of link is not supported; use [sharing/files.export](#sharing-files.export) instead.<br>
other | Void | 
shared_link_malformed | Void | Shared link is malformed.<br>
## set_access_inheritance
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/set_access_inheritance \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"access_inheritance\": \"inherit\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "access_type": {
        ".tag": "owner"
    }, 
    "is_inside_team_folder": false, 
    "is_team_folder": false, 
    "name": "dir", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
    "shared_folder_id": "84528192421", 
    "time_invited": "2016-01-20T00:00:00Z", 
    "path_lower": "/dir", 
    "link_metadata": {
        "audience_options": [
            {
                ".tag": "public"
            }, 
            {
                ".tag": "team"
            }, 
            {
                ".tag": "members"
            }
        ], 
        "current_audience": {
            ".tag": "public"
        }, 
        "link_permissions": [
            {
                "action": {
                    ".tag": "change_audience"
                }, 
                "allow": true
            }
        ], 
        "password_protected": false, 
        "url": ""
    }, 
    "permissions": [], 
    "access_inheritance": {
        ".tag": "inherit"
    }
}
```

### Description
Change the inheritance policy of an existing Shared Folder. Only permitted for shared folders in a shared team root.
If a [ShareFolderLaunch.async_job_id](#data-types-sharefolderlaunch) is returned, you'll need to call check_share_job_status until the action completes to get the metadata for the folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[SetAccessInheritanceArg](#data-types-setaccessinheritancearg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
access_inheritance | [AccessInheritance](#data-types-accessinheritance) | The access inheritance settings for the folder.<br>
### Return Values
[ShareFolderLaunch](#data-types-sharefolderlaunch)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [SharedFolderMetadata](#data-types-sharedfoldermetadata) | 
### Error Values
[SetAccessInheritanceError](#data-types-setaccessinheritanceerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | Unable to access shared folder.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
other | Void | 
## share_folder
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/share_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"path\": \"/example/workspace\",\"acl_update_policy\": \"editors\",\"force_async\": false,\"member_policy\": \"team\",\"shared_link_policy\": \"members\",\"access_inheritance\": \"inherit\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "access_type": {
        ".tag": "owner"
    }, 
    "is_inside_team_folder": false, 
    "is_team_folder": false, 
    "name": "dir", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
    "shared_folder_id": "84528192421", 
    "time_invited": "2016-01-20T00:00:00Z", 
    "path_lower": "/dir", 
    "link_metadata": {
        "audience_options": [
            {
                ".tag": "public"
            }, 
            {
                ".tag": "team"
            }, 
            {
                ".tag": "members"
            }
        ], 
        "current_audience": {
            ".tag": "public"
        }, 
        "link_permissions": [
            {
                "action": {
                    ".tag": "change_audience"
                }, 
                "allow": true
            }
        ], 
        "password_protected": false, 
        "url": ""
    }, 
    "permissions": [], 
    "access_inheritance": {
        ".tag": "inherit"
    }
}
```

### Description
Share a folder with collaborators.
Most sharing will be completed synchronously. Large folders will be completed asynchronously. To make testing the async case repeatable, set `ShareFolderArg.force_async`.
If a [ShareFolderLaunch.async_job_id](#data-types-sharefolderlaunch) is returned, you'll need to call check_share_job_status until the action completes to get the metadata for the folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[ShareFolderArg](#data-types-sharefolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
path | String | The path to the folder to share. If it does not exist, then a new one is created.<br>
acl_update_policy | Optional[[AclUpdatePolicy](#data-types-aclupdatepolicy)] | Who can add and remove members of this shared folder.<br>
force_async | Boolean | Whether to force the share to happen asynchronously.<br>
member_policy | Optional[[MemberPolicy](#data-types-memberpolicy)] | Who can be a member of this shared folder. Only applicable if the current user is on a team.<br>
shared_link_policy | Optional[[SharedLinkPolicy](#data-types-sharedlinkpolicy)] | The policy to apply to shared links created for content inside this shared folder.  The current user must be on a team to set this policy to [SharedLinkPolicy.members](#data-types-sharedlinkpolicy).<br>
viewer_info_policy | Optional[[ViewerInfoPolicy](#data-types-viewerinfopolicy)] | Who can enable/disable viewer info for this shared folder.<br>
access_inheritance | [AccessInheritance](#data-types-accessinheritance) | The access inheritance settings for the folder.<br>
actions | Optional[List[[FolderAction](#data-types-folderaction)]] | A list of `FolderAction`s corresponding to `FolderPermission`s that should appear in the  response's [SharedFolderMetadata.permissions](#data-types-sharedfoldermetadata) field describing the actions the  authenticated user can perform on the folder.<br>
link_settings | Optional[[LinkSettings](#data-types-linksettings)] | Settings on the link for this folder.<br>
### Return Values
[ShareFolderLaunch](#data-types-sharefolderlaunch)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [SharedFolderMetadata](#data-types-sharedfoldermetadata) | 
### Error Values
[ShareFolderError](#data-types-sharefoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
email_unverified | Void | The current user's e-mail address is unverified.<br>
bad_path | [SharePathError](#data-types-sharepatherror) | [ShareFolderArg.path](#data-types-sharefolderarg) is invalid.<br>
team_policy_disallows_member_policy | Void | Team policy is more restrictive than [ShareFolderArg.member_policy](#data-types-sharefolderarg).<br>
disallowed_shared_link_policy | Void | The current user's account is not allowed to select the specified [ShareFolderArg.shared_link_policy](#data-types-sharefolderarg).<br>
other | Void | 
no_permission | Void | The current user does not have permission to perform this action.<br>
## transfer_folder
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/transfer_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"to_dropbox_id\": \"dbid:AAEufNrMPSPe0dMQijRP0N_aZtBJRm26W4Q\"}"
```

### Description
Transfer ownership of a shared folder to a member of the shared folder.
User must have [AccessLevel.owner](#data-types-accesslevel) access to the shared folder to perform a transfer.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[TransferFolderArg](#data-types-transferfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
to_dropbox_id | String | A account or team member ID to transfer ownership to.<br>
### Return Values
Void
### Error Values
[TransferFolderError](#data-types-transferfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
invalid_dropbox_id | Void | [TransferFolderArg.to_dropbox_id](#data-types-transferfolderarg) is invalid.<br>
new_owner_not_a_member | Void | The new designated owner is not currently a member of the shared folder.<br>
new_owner_unmounted | Void | The new designated owner has not added the folder to their Dropbox.<br>
new_owner_email_unverified | Void | The new designated owner's e-mail address is unverified.<br>
team_folder | Void | This action cannot be performed on a team shared folder.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
other | Void | 
## unmount_folder
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/unmount_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\"}"
```

### Description
The current user unmounts the designated folder. They can re-mount the folder at a later time using mount_folder.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[UnmountFolderArg](#data-types-unmountfolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
### Return Values
Void
### Error Values
[UnmountFolderError](#data-types-unmountfoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
no_permission | Void | The current user does not have permission to perform this action.<br>
not_unmountable | Void | The shared folder can't be unmounted. One example where this can occur is when the shared folder's parent folder is also a shared folder that resides in the current user's Dropbox.<br>
other | Void | 
## unshare_file
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/unshare_file \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\"}"
```

### Description
Remove all members from this file. Does not remove inherited members.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[UnshareFileArg](#data-types-unsharefilearg)

Arguments for [sharing/unshare_file](#sharing-unshare_file).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | The file to unshare.<br>
### Return Values
Void
### Error Values
[UnshareFileError](#data-types-unsharefileerror)

Error result for [sharing/unshare_file](#sharing-unshare_file).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_error | [SharingUserError](#data-types-sharingusererror) | 
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | 
other | Void | 
## unshare_folder
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/unshare_folder \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"leave_a_copy\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Allows a shared folder owner to unshare the folder.
You'll need to call check_job_status to determine if the action has completed successfully.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[UnshareFolderArg](#data-types-unsharefolderarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
leave_a_copy | Boolean | If true, members of this shared folder will get a copy of this folder after it's unshared. Otherwise, it will be removed from their Dropbox. The current user, who is an owner, will always retain their copy.<br>
### Return Values
[LaunchEmptyResult](#data-types-launchemptyresult)

Result returned by methods that may either launch an asynchronous job or complete synchronously. Upon synchronous completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | Void | The job finished synchronously and successfully.<br>
### Error Values
[UnshareFolderError](#data-types-unsharefoldererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
team_folder | Void | This action cannot be performed on a team shared folder.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
too_many_files | Void | This shared folder has too many files to be unshared.<br>
other | Void | 
## update_file_member
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/update_file_member \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"file\": \"id:3kmLmQFnf1AAAAAAAAAAAw\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"},\"access_level\": \"viewer\"}"
```

### Description
Changes a member's access on a shared file.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[UpdateFileMemberArgs](#data-types-updatefilememberargs)

Arguments for [sharing/update_file_member](#sharing-update_file_member).

Field Name | Data Type | Description
--------- | ------- | -----------
file | String | File for which we are changing a member's access.<br>
member | [MemberSelector](#data-types-memberselector) | The member whose access we are changing.<br>
access_level | [AccessLevel](#data-types-accesslevel) | The new access level for the member.<br>
### Return Values
[MemberAccessLevelResult](#data-types-memberaccesslevelresult)

Contains information about a member's access level to content after an operation.

Field Name | Data Type | Description
--------- | ------- | -----------
access_level | Optional[[AccessLevel](#data-types-accesslevel)] | The member still has this level of access to the content through a parent folder.<br>
warning | Optional[String] | A localized string with additional information about why the user has this access level to the content.<br>
access_details | Optional[List[[ParentFolderAccessInfo](#data-types-parentfolderaccessinfo)]] | The parent folders that a member has access to. The field is present if the user has access to the first parent folder where the member gains access.<br>
### Error Values
[FileMemberActionError](#data-types-filememberactionerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_member | Void | Specified member was not found.<br>
no_permission | Void | User does not have permission to perform this action on this member.<br>
access_error | [SharingFileAccessError](#data-types-sharingfileaccesserror) | Specified file was invalid or user does not have access.<br>
no_explicit_access | [MemberAccessLevelResult](#data-types-memberaccesslevelresult) | The action cannot be completed because the target member does not have explicit access to the file. The return value is the access that the member has to the file from a parent folder.<br>
other | Void | 
## update_folder_member
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/update_folder_member \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"member\": {\".tag\": \"email\",\"email\": \"justin@example.com\"},\"access_level\": \"editor\"}"
```

### Description
Allows an owner or editor of a shared folder to update another member's permissions.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[UpdateFolderMemberArg](#data-types-updatefoldermemberarg)

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
member | [MemberSelector](#data-types-memberselector) | The member of the shared folder to update.  Only the [MemberSelector.dropbox_id](#data-types-memberselector) may be set at this time.<br>
access_level | [AccessLevel](#data-types-accesslevel) | The new access level for [member](#data-types-updatefoldermemberarg). [AccessLevel.owner](#data-types-accesslevel) is disallowed.<br>
### Return Values
[MemberAccessLevelResult](#data-types-memberaccesslevelresult)

Contains information about a member's access level to content after an operation.

Field Name | Data Type | Description
--------- | ------- | -----------
access_level | Optional[[AccessLevel](#data-types-accesslevel)] | The member still has this level of access to the content through a parent folder.<br>
warning | Optional[String] | A localized string with additional information about why the user has this access level to the content.<br>
access_details | Optional[List[[ParentFolderAccessInfo](#data-types-parentfolderaccessinfo)]] | The parent folders that a member has access to. The field is present if the user has access to the first parent folder where the member gains access.<br>
### Error Values
[UpdateFolderMemberError](#data-types-updatefoldermembererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
member_error | [SharedFolderMemberError](#data-types-sharedfoldermembererror) | 
no_explicit_access | [AddFolderMemberError](#data-types-addfoldermembererror) | If updating the access type required the member to be added to the shared folder and there was an error when adding the member.<br>
insufficient_plan | Void | The current user's account doesn't support this action. An example of this is when downgrading a member from editor to viewer. This action can only be performed by users that have upgraded to a Pro or Business plan.<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
other | Void | 
## update_folder_policy
```shell
curl -X POST https://api.dropboxapi.com/2/sharing/update_folder_policy \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"shared_folder_id\": \"84528192421\",\"member_policy\": \"team\",\"acl_update_policy\": \"owner\",\"shared_link_policy\": \"members\"}"
```

> The above command returns JSON structured like this:

```json
{
    "access_type": {
        ".tag": "owner"
    }, 
    "is_inside_team_folder": false, 
    "is_team_folder": false, 
    "name": "dir", 
    "policy": {
        "acl_update_policy": {
            ".tag": "owner"
        }, 
        "shared_link_policy": {
            ".tag": "anyone"
        }, 
        "member_policy": {
            ".tag": "anyone"
        }, 
        "resolved_member_policy": {
            ".tag": "team"
        }
    }, 
    "preview_url": "https://www.dropbox.com/scl/fo/fir9vjelf", 
    "shared_folder_id": "84528192421", 
    "time_invited": "2016-01-20T00:00:00Z", 
    "path_lower": "/dir", 
    "link_metadata": {
        "audience_options": [
            {
                ".tag": "public"
            }, 
            {
                ".tag": "team"
            }, 
            {
                ".tag": "members"
            }
        ], 
        "current_audience": {
            ".tag": "public"
        }, 
        "link_permissions": [
            {
                "action": {
                    ".tag": "change_audience"
                }, 
                "allow": true
            }
        ], 
        "password_protected": false, 
        "url": ""
    }, 
    "permissions": [], 
    "access_inheritance": {
        ".tag": "inherit"
    }
}
```

### Description
Update the sharing policies for a shared folder.
User must have [AccessLevel.owner](#data-types-accesslevel) access to the shared folder to update its policies.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.write
### Query Parameters
[UpdateFolderPolicyArg](#data-types-updatefolderpolicyarg)

If any of the policies are unset, then they retain their current setting.

Field Name | Data Type | Description
--------- | ------- | -----------
shared_folder_id | String | The ID for the shared folder.<br>
member_policy | Optional[[MemberPolicy](#data-types-memberpolicy)] | Who can be a member of this shared folder. Only applicable if the current user is on a team.<br>
acl_update_policy | Optional[[AclUpdatePolicy](#data-types-aclupdatepolicy)] | Who can add and remove members of this shared folder.<br>
viewer_info_policy | Optional[[ViewerInfoPolicy](#data-types-viewerinfopolicy)] | Who can enable/disable viewer info for this shared folder.<br>
shared_link_policy | Optional[[SharedLinkPolicy](#data-types-sharedlinkpolicy)] | The policy to apply to shared links created for content inside this shared folder. The current user must be on a team to set this policy to [SharedLinkPolicy.members](#data-types-sharedlinkpolicy).<br>
link_settings | Optional[[LinkSettings](#data-types-linksettings)] | Settings on the link for this folder.<br>
actions | Optional[List[[FolderAction](#data-types-folderaction)]] | A list of `FolderAction`s corresponding to `FolderPermission`s that should appear in the  response's [SharedFolderMetadata.permissions](#data-types-sharedfoldermetadata) field describing the actions the  authenticated user can perform on the folder.<br>
### Return Values
[SharedFolderMetadata](#data-types-sharedfoldermetadata)

The metadata which includes basic information about the shared folder.

Field Name | Data Type | Description
--------- | ------- | -----------
access_type | [AccessLevel](#data-types-accesslevel) | The current user's access level for this shared folder.<br>
is_inside_team_folder | Boolean | Whether this folder is inside of a team folder.<br>
is_team_folder | Boolean | Whether this folder is a [team folder](https://www.dropbox.com/en/help/986).<br>
name | String | The name of the this shared folder.<br>
policy | [FolderPolicy](#data-types-folderpolicy) | Policies governing this shared folder.<br>
preview_url | String | URL for displaying a web preview of the shared folder.<br>
shared_folder_id | String | The ID of the shared folder.<br>
time_invited | Timestamp | Timestamp indicating when the current user was invited to this shared folder.<br>
owner_display_names | Optional[List[String]] | The display names of the users that own the folder. If the folder is part of a team folder, the display names of the team admins are also included. Absent if the owner display names cannot be fetched.<br>
owner_team | Optional[[Team](#data-types-team)] | The team that owns the folder. This field is not present if the folder is not owned by a team.<br>
parent_shared_folder_id | Optional[String] | The ID of the parent shared folder. This field is present only if the folder is contained within another shared folder.<br>
path_lower | Optional[String] | The lower-cased full path of this shared folder. Absent for unmounted folders.<br>
parent_folder_name | Optional[String] | Display name for the parent folder.<br>
link_metadata | Optional[[SharedContentLinkMetadata](#data-types-sharedcontentlinkmetadata)] | The metadata of the shared content link to this shared folder. Absent if there is no link on the folder. This is for an unreleased feature so it may not be returned yet.<br>
permissions | Optional[List[[FolderPermission](#data-types-folderpermission)]] | Actions the current user may perform on the folder and its contents. The set of permissions corresponds to the FolderActions in the request.<br>
access_inheritance | [AccessInheritance](#data-types-accessinheritance) | Whether the folder inherits its members from its parent.<br>
### Error Values
[UpdateFolderPolicyError](#data-types-updatefolderpolicyerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [SharedFolderAccessError](#data-types-sharedfolderaccesserror) | 
not_on_team | Void | [UpdateFolderPolicyArg.member_policy](#data-types-updatefolderpolicyarg) was set even though user is not on a team.<br>
team_policy_disallows_member_policy | Void | Team policy is more restrictive than [ShareFolderArg.member_policy](#data-types-sharefolderarg).<br>
disallowed_shared_link_policy | Void | The current account is not allowed to select the specified [ShareFolderArg.shared_link_policy](#data-types-sharefolderarg).<br>
no_permission | Void | The current user does not have permission to perform this action.<br>
team_folder | Void | This action cannot be performed on a team shared folder.<br>
other | Void | 
# Team
## devices/list_member_devices
```shell
curl -X POST https://api.dropboxapi.com/2/team/devices/list_member_devices \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_member_id\": \"dbmid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I\",\"include_web_sessions\": true,\"include_desktop_clients\": true,\"include_mobile_clients\": true}"
```

### Description
List all device sessions of a team's member.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.list
### Query Parameters
[ListMemberDevicesArg](#data-types-listmemberdevicesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_member_id | String | The team's member id.<br>
include_web_sessions | Boolean | Whether to list web sessions of the team's member.<br>
include_desktop_clients | Boolean | Whether to list linked desktop devices of the team's member.<br>
include_mobile_clients | Boolean | Whether to list linked mobile devices of the team's member.<br>
### Return Values
[ListMemberDevicesResult](#data-types-listmemberdevicesresult)

Field Name | Data Type | Description
--------- | ------- | -----------
active_web_sessions | Optional[List[[ActiveWebSession](#data-types-activewebsession)]] | List of web sessions made by this team member.<br>
desktop_client_sessions | Optional[List[[DesktopClientSession](#data-types-desktopclientsession)]] | List of desktop clients used by this team member.<br>
mobile_client_sessions | Optional[List[[MobileClientSession](#data-types-mobileclientsession)]] | List of mobile client used by this team member.<br>
### Error Values
[ListMemberDevicesError](#data-types-listmemberdeviceserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
member_not_found | Void | Member not found.<br>
other | Void | 
## devices/list_members_devices
### Description
List all device sessions of a team.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.list
### Query Parameters
[ListMembersDevicesArg](#data-types-listmembersdevicesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | Optional[String] | At the first call to the [team/devices/list_members_devices](#team-devices-list_members_devices) the cursor shouldn't be passed. Then, if the result of the call includes a cursor, the following requests should include the received cursors in order to receive the next sub list of team devices.<br>
include_web_sessions | Boolean | Whether to list web sessions of the team members.<br>
include_desktop_clients | Boolean | Whether to list desktop clients of the team members.<br>
include_mobile_clients | Boolean | Whether to list mobile clients of the team members.<br>
### Return Values
[ListMembersDevicesResult](#data-types-listmembersdevicesresult)

Field Name | Data Type | Description
--------- | ------- | -----------
devices | List[[MemberDevices](#data-types-memberdevices)] | The devices of each member of the team.<br>
has_more | Boolean | If true, then there are more devices available. Pass the cursor to [team/devices/list_members_devices](#team-devices-list_members_devices) to retrieve the rest.<br>
cursor | Optional[String] | Pass the cursor into [team/devices/list_members_devices](#team-devices-list_members_devices) to receive the next sub list of team's devices.<br>
### Error Values
[ListMembersDevicesError](#data-types-listmembersdeviceserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
reset | Void | Indicates that the cursor has been invalidated. Call [team/devices/list_members_devices](#team-devices-list_members_devices) again with an empty cursor to obtain a new cursor.<br>
other | Void | 
## devices/list_team_devices
```shell
curl -X POST https://api.dropboxapi.com/2/team/devices/list_team_devices \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\",\"include_web_sessions\": true,\"include_desktop_clients\": true,\"include_mobile_clients\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "devices": [
        {
            "team_member_id": "dbmid:AAHhy7WsR0x-u4ZCqiDl5Fz5zvuL3kmspwU"
        }
    ], 
    "has_more": false
}
```

### Description
List all device sessions of a team.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[ListTeamDevicesArg](#data-types-listteamdevicesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | Optional[String] | At the first call to the [team/devices/list_team_devices](#team-devices-list_team_devices) the cursor shouldn't be passed. Then, if the result of the call includes a cursor, the following requests should include the received cursors in order to receive the next sub list of team devices.<br>
include_web_sessions | Boolean | Whether to list web sessions of the team members.<br>
include_desktop_clients | Boolean | Whether to list desktop clients of the team members.<br>
include_mobile_clients | Boolean | Whether to list mobile clients of the team members.<br>
### Return Values
[ListTeamDevicesResult](#data-types-listteamdevicesresult)

Field Name | Data Type | Description
--------- | ------- | -----------
devices | List[[MemberDevices](#data-types-memberdevices)] | The devices of each member of the team.<br>
has_more | Boolean | If true, then there are more devices available. Pass the cursor to [team/devices/list_team_devices](#team-devices-list_team_devices) to retrieve the rest.<br>
cursor | Optional[String] | Pass the cursor into [team/devices/list_team_devices](#team-devices-list_team_devices) to receive the next sub list of team's devices.<br>
### Error Values
[ListTeamDevicesError](#data-types-listteamdeviceserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
reset | Void | Indicates that the cursor has been invalidated. Call [team/devices/list_team_devices](#team-devices-list_team_devices) again with an empty cursor to obtain a new cursor.<br>
other | Void | 
## devices/revoke_device_session
```shell
curl -X POST https://api.dropboxapi.com/2/team/devices/revoke_device_session \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\".tag\": \"web_session\",\"session_id\": \"1234faaf0678bcde\",\"team_member_id\": \"dbmid:AAHhy7WsR0x-u4ZCqiDl5Fz5zvuL3kmspwU\"}"
```

### Description
Revoke a device session of a team's member.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.modify
### Query Parameters
[RevokeDeviceSessionArg](#data-types-revokedevicesessionarg)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
web_session | [DeviceSessionArg](#data-types-devicesessionarg) | End an active session.<br>
desktop_client | [RevokeDesktopClientArg](#data-types-revokedesktopclientarg) | Unlink a linked desktop device.<br>
mobile_client | [DeviceSessionArg](#data-types-devicesessionarg) | Unlink a linked mobile device.<br>
### Return Values
Void
### Error Values
[RevokeDeviceSessionError](#data-types-revokedevicesessionerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
device_session_not_found | Void | Device session not found.<br>
member_not_found | Void | Member not found.<br>
other | Void | 
## devices/revoke_device_session_batch
```shell
curl -X POST https://api.dropboxapi.com/2/team/devices/revoke_device_session_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"revoke_devices\": [{\".tag\": \"web_session\",\"session_id\": \"1234faaf0678bcde\",\"team_member_id\": \"dbmid:AAHhy7WsR0x-u4ZCqiDl5Fz5zvuL3kmspwU\"}]}"
```

### Description
Revoke a list of device sessions of team members.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.modify
### Query Parameters
[RevokeDeviceSessionBatchArg](#data-types-revokedevicesessionbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
revoke_devices | List[[RevokeDeviceSessionArg](#data-types-revokedevicesessionarg)] | 
### Return Values
[RevokeDeviceSessionBatchResult](#data-types-revokedevicesessionbatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
revoke_devices_status | List[[RevokeDeviceSessionStatus](#data-types-revokedevicesessionstatus)] | 
### Error Values
[RevokeDeviceSessionBatchError](#data-types-revokedevicesessionbatcherror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## features/get_values
```shell
curl -X POST https://api.dropboxapi.com/2/team/features/get_values \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"features\": [{\".tag\": \"upload_api_rate_limit\"},{\".tag\": \"has_team_shared_dropbox\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "values": [
        {
            ".tag": "upload_api_rate_limit", 
            "upload_api_rate_limit": {
                ".tag": "limit", 
                "limit": 25000
            }
        }, 
        {
            ".tag": "has_team_shared_dropbox", 
            "has_team_shared_dropbox": {
                ".tag": "has_team_shared_dropbox", 
                "has_team_shared_dropbox": false
            }
        }
    ]
}
```

### Description
Get the values for one or more featues. This route allows you to check your account's capability for what feature you can access or what value you have for certain features.
Permission : Team information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
[FeaturesGetValuesBatchArg](#data-types-featuresgetvaluesbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
features | List[[Feature](#data-types-feature)] | A list of features in [Feature](#data-types-feature). If the list is empty, this route will return [FeaturesGetValuesBatchError](#data-types-featuresgetvaluesbatcherror).<br>
### Return Values
[FeaturesGetValuesBatchResult](#data-types-featuresgetvaluesbatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
values | List[[FeatureValue](#data-types-featurevalue)] | 
### Error Values
[FeaturesGetValuesBatchError](#data-types-featuresgetvaluesbatcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
empty_features_list | Void | At least one [Feature](#data-types-feature) must be included in the [FeaturesGetValuesBatchArg](#data-types-featuresgetvaluesbatcharg).features list.<br>
other | Void | 
## get_info
```shell
curl -X POST https://api.dropboxapi.com/2/team/get_info \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Dropbox Inc.", 
    "team_id": "dbtid:1234abcd", 
    "num_licensed_users": 5, 
    "num_provisioned_users": 2, 
    "policies": {
        "sharing": {
            "shared_folder_member_policy": {
                ".tag": "team"
            }, 
            "shared_folder_join_policy": {
                ".tag": "from_anyone"
            }, 
            "shared_link_create_policy": {
                ".tag": "team_only"
            }
        }, 
        "emm_state": {
            ".tag": "disabled"
        }, 
        "office_addin": {
            ".tag": "disabled"
        }
    }
}
```

### Description
Retrieves information about a team.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
Void
### Return Values
[TeamGetInfoResult](#data-types-teamgetinforesult)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | The name of the team.<br>
team_id | String | The ID of the team.<br>
num_licensed_users | UInt32 | The number of licenses available to the team.<br>
num_provisioned_users | UInt32 | The number of accounts that have been invited or are already active members of the team.<br>
policies | [TeamMemberPolicies](#data-types-teammemberpolicies) | 
### Error Values
Void
## groups/create
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/create \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"group_name\": \"Europe sales\",\"add_creator_as_owner\": false,\"group_external_id\": \"group-134\"}"
```

> The above command returns JSON structured like this:

```json
{
    "group_name": "project launch", 
    "group_id": "g:e2db7665347abcd600000000001a2b3c", 
    "group_management_type": {
        ".tag": "user_managed"
    }, 
    "created": 1447255518000, 
    "member_count": 5, 
    "members": [
        {
            "profile": {
                "team_member_id": "dbmid:1234567", 
                "email": "mary@lamb.com", 
                "email_verified": true, 
                "status": {
                    ".tag": "active"
                }, 
                "name": {
                    "given_name": "Franz", 
                    "surname": "Ferdinand", 
                    "familiar_name": "Franz", 
                    "display_name": "Franz Ferdinand (Personal)", 
                    "abbreviated_name": "FF"
                }, 
                "membership_type": {
                    ".tag": "full"
                }, 
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "secondary_emails": [
                    {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }, 
                    {
                        "email": "banana@honeydew.com", 
                        "is_verified": true
                    }, 
                    {
                        "email": "grape@strawberry.com", 
                        "is_verified": false
                    }
                ], 
                "joined_on": "2015-05-12T15:50:38Z", 
                "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
            }, 
            "access_type": {
                ".tag": "member"
            }
        }
    ]
}
```

### Description
Creates a new, empty group, with a requested name.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[GroupCreateArg](#data-types-groupcreatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
group_name | String | Group name.<br>
add_creator_as_owner | Boolean | Automatically add the creator of the group.<br>
group_external_id | Optional[String] | The creator of a team can associate an arbitrary external ID to the group.<br>
group_management_type | Optional[[GroupManagementType](#data-types-groupmanagementtype)] | Whether the team can be managed by selected users, or only by team admins.<br>
### Return Values
[GroupFullInfo](#data-types-groupfullinfo)

Full description of a group.

Field Name | Data Type | Description
--------- | ------- | -----------
group_name | String | 
group_id | String | 
group_management_type | [GroupManagementType](#data-types-groupmanagementtype) | Who is allowed to manage the group.<br>
created | UInt64 | The group creation time as a UTC timestamp in milliseconds since the Unix epoch.<br>
group_external_id | Optional[String] | External ID of group. This is an arbitrary ID that an admin can attach to a group.<br>
member_count | Optional[UInt32] | The number of members in the group.<br>
members | Optional[List[[GroupMemberInfo](#data-types-groupmemberinfo)]] | List of group members.<br>
### Error Values
[GroupCreateError](#data-types-groupcreateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_name_already_used | Void | The requested group name is already being used by another group.<br>
group_name_invalid | Void | Group name is empty or has invalid characters.<br>
external_id_already_in_use | Void | The requested external ID is already being used by another group.<br>
system_managed_group_disallowed | Void | System-managed group cannot be manually created.<br>
other | Void | 
## groups/delete
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\".tag\": \"group_id\",\"group_id\": \"g:e2db7665347abcd600000000001a2b3c\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Deletes a group.
The group is deleted immediately. However the revoking of group-owned resources may take additional time. Use the groups/job_status/get to determine whether this process has completed.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[GroupSelector](#data-types-groupselector)

Argument for selecting a single group, either by group_id or by external group ID.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_id | String | Group ID.<br>
group_external_id | String | External ID of the group.<br>
### Return Values
[LaunchEmptyResult](#data-types-launchemptyresult)

Result returned by methods that may either launch an asynchronous job or complete synchronously. Upon synchronous completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | Void | The job finished synchronously and successfully.<br>
### Error Values
[GroupDeleteError](#data-types-groupdeleteerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_found | Void | No matching group found. No groups match the specified group ID.<br>
other | Void | 
system_managed_group_disallowed | Void | This operation is not supported on system-managed groups.<br>
group_already_deleted | Void | This group has already been deleted.<br>
## groups/get_info
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/get_info \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\".tag\": \"group_ids\",\"group_ids\": [\"g:e2db7665347abcd600000000001a2b3c\",\"g:111111147abcd6000000000222222c\"]}"
```

### Description
Retrieves information about one or more groups. Note that the optional field  [GroupFullInfo.members](#data-types-groupfullinfo) is not returned for system-managed groups.
Permission : Team Information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.read
### Query Parameters
[GroupsSelector](#data-types-groupsselector)

Argument for selecting a list of groups, either by group_ids, or external group IDs.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_ids | List[String] | List of group IDs.<br>
group_external_ids | List[String] | List of external IDs of groups.<br>
### Return Values
List[[GroupsGetInfoItem](#data-types-groupsgetinfoitem)]
### Error Values
[GroupsGetInfoError](#data-types-groupsgetinfoerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_on_team | Void | The group is not on your team.<br>
other | Void | 
## groups/job_status/get
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/job_status/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Once an async_job_id is returned from groups/delete, groups/members/add , or groups/members/remove use this method to poll the status of granting/revoking group members' access to group-owned resources.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[PollEmptyResult](#data-types-pollemptyresult)

Result returned by methods that poll for the status of an asynchronous job. Upon completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | Void | The asynchronous job has completed successfully.<br>
### Error Values
[GroupsPollError](#data-types-groupspollerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
access_denied | Void | You are not allowed to poll this job.<br>
## groups/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "groups": [
        {
            "group_name": "Test group", 
            "group_id": "g:e2db7665347abcd600000000001a2b3c", 
            "group_management_type": {
                ".tag": "user_managed"
            }, 
            "member_count": 10
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Lists groups on a team.
Permission : Team Information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.read
### Query Parameters
[GroupsListArg](#data-types-groupslistarg)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | Number of results to return per call.<br>
### Return Values
[GroupsListResult](#data-types-groupslistresult)

Field Name | Data Type | Description
--------- | ------- | -----------
groups | List[[GroupSummary](#data-types-groupsummary)] | 
cursor | String | Pass the cursor into [team/groups/list/continue](#team-groups-list-continue) to obtain the additional groups.<br>
has_more | Boolean | Is true if there are additional groups that have not been returned yet. An additional call to [team/groups/list/continue](#team-groups-list-continue) can retrieve them.<br>
### Error Values
Void
## groups/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "groups": [
        {
            "group_name": "Test group", 
            "group_id": "g:e2db7665347abcd600000000001a2b3c", 
            "group_management_type": {
                ".tag": "user_managed"
            }, 
            "member_count": 10
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from groups/list, use this to paginate through all groups.
Permission : Team Information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.read
### Query Parameters
[GroupsListContinueArg](#data-types-groupslistcontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of groups.<br>
### Return Values
[GroupsListResult](#data-types-groupslistresult)

Field Name | Data Type | Description
--------- | ------- | -----------
groups | List[[GroupSummary](#data-types-groupsummary)] | 
cursor | String | Pass the cursor into [team/groups/list/continue](#team-groups-list-continue) to obtain the additional groups.<br>
has_more | Boolean | Is true if there are additional groups that have not been returned yet. An additional call to [team/groups/list/continue](#team-groups-list-continue) can retrieve them.<br>
### Error Values
[GroupsListContinueError](#data-types-groupslistcontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | The cursor is invalid.<br>
other | Void | 
## groups/members/add
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/members/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"group\": {\".tag\": \"group_id\",\"group_id\": \"g:e2db7665347abcd600000000001a2b3c\"},\"members\": [{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"access_type\": \"member\"}],\"return_members\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "group_info": {
        "group_name": "project launch", 
        "group_id": "g:e2db7665347abcd600000000001a2b3c", 
        "group_management_type": {
            ".tag": "user_managed"
        }, 
        "created": 1447255518000, 
        "member_count": 5, 
        "members": [
            {
                "profile": {
                    "team_member_id": "dbmid:1234567", 
                    "email": "mary@lamb.com", 
                    "email_verified": true, 
                    "status": {
                        ".tag": "active"
                    }, 
                    "name": {
                        "given_name": "Franz", 
                        "surname": "Ferdinand", 
                        "familiar_name": "Franz", 
                        "display_name": "Franz Ferdinand (Personal)", 
                        "abbreviated_name": "FF"
                    }, 
                    "membership_type": {
                        ".tag": "full"
                    }, 
                    "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                    "secondary_emails": [
                        {
                            "email": "apple@orange.com", 
                            "is_verified": true
                        }, 
                        {
                            "email": "banana@honeydew.com", 
                            "is_verified": true
                        }, 
                        {
                            "email": "grape@strawberry.com", 
                            "is_verified": false
                        }
                    ], 
                    "joined_on": "2015-05-12T15:50:38Z", 
                    "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
                }, 
                "access_type": {
                    ".tag": "member"
                }
            }
        ]
    }, 
    "async_job_id": "99988877733388"
}
```

### Description
Adds members to a group.
The members are added immediately. However the granting of group-owned resources may take additional time. Use the groups/job_status/get to determine whether this process has completed.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[GroupMembersAddArg](#data-types-groupmembersaddarg)

Field Name | Data Type | Description
--------- | ------- | -----------
group | [GroupSelector](#data-types-groupselector) | Group to which users will be added.<br>
members | List[[MemberAccess](#data-types-memberaccess)] | List of users to be added to the group.<br>
return_members | Boolean | Whether to return the list of members in the group.  Note that the default value will cause all the group members  to be returned in the response. This may take a long time for large groups.<br>
### Return Values
[GroupMembersChangeResult](#data-types-groupmemberschangeresult)

Result returned by [team/groups/members/add](#team-groups-members-add) and [team/groups/members/remove](#team-groups-members-remove).

Field Name | Data Type | Description
--------- | ------- | -----------
group_info | [GroupFullInfo](#data-types-groupfullinfo) | The group info after member change operation has been performed.<br>
async_job_id | String | Field is deprecated. For legacy purposes async_job_id will always return one space ' '. Formerly, it was an ID that was used to obtain the status of granting/revoking group-owned resources. It's no longer necessary because the async processing now happens automatically.<br>
### Error Values
[GroupMembersAddError](#data-types-groupmembersadderror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_found | Void | No matching group found. No groups match the specified group ID.<br>
other | Void | 
system_managed_group_disallowed | Void | This operation is not supported on system-managed groups.<br>
duplicate_user | Void | You cannot add duplicate users. One or more of the members you are trying to add is already a member of the group.<br>
group_not_in_team | Void | Group is not in this team. You cannot add members to a group that is outside of your team.<br>
members_not_in_team | List[String] | These members are not part of your team. Currently, you cannot add members to a group if they are not part of your team, though this may change in a subsequent version. To add new members to your Dropbox Business team, use the [team/members/add](#team-members-add) endpoint.<br>
users_not_found | List[String] | These users were not found in Dropbox.<br>
user_must_be_active_to_be_owner | Void | A suspended user cannot be added to a group as [GroupAccessType.owner](#data-types-groupaccesstype).<br>
user_cannot_be_manager_of_company_managed_group | List[String] | A company-managed group cannot be managed by a user.<br>
## groups/members/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/members/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"group\": {\".tag\": \"group_id\",\"group_id\": \"g:e2db7665347abcd600000000001a2b3c\"},\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "members": [], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Lists members of a group.
Permission : Team Information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.read
### Query Parameters
[GroupsMembersListArg](#data-types-groupsmemberslistarg)

Field Name | Data Type | Description
--------- | ------- | -----------
group | [GroupSelector](#data-types-groupselector) | The group whose members are to be listed.<br>
limit | UInt32 | Number of results to return per call.<br>
### Return Values
[GroupsMembersListResult](#data-types-groupsmemberslistresult)

Field Name | Data Type | Description
--------- | ------- | -----------
members | List[[GroupMemberInfo](#data-types-groupmemberinfo)] | 
cursor | String | Pass the cursor into [team/groups/members/list/continue](#team-groups-members-list-continue) to obtain additional group members.<br>
has_more | Boolean | Is true if there are additional group members that have not been returned yet. An additional call to [team/groups/members/list/continue](#team-groups-members-list-continue) can retrieve them.<br>
### Error Values
[GroupSelectorError](#data-types-groupselectorerror)

Error that can be raised when [GroupSelector](#data-types-groupselector) is used.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_found | Void | No matching group found. No groups match the specified group ID.<br>
other | Void | 
## groups/members/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/members/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "members": [], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from groups/members/list, use this to paginate through all members of the group.
Permission : Team information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.read
### Query Parameters
[GroupsMembersListContinueArg](#data-types-groupsmemberslistcontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of groups.<br>
### Return Values
[GroupsMembersListResult](#data-types-groupsmemberslistresult)

Field Name | Data Type | Description
--------- | ------- | -----------
members | List[[GroupMemberInfo](#data-types-groupmemberinfo)] | 
cursor | String | Pass the cursor into [team/groups/members/list/continue](#team-groups-members-list-continue) to obtain additional group members.<br>
has_more | Boolean | Is true if there are additional group members that have not been returned yet. An additional call to [team/groups/members/list/continue](#team-groups-members-list-continue) can retrieve them.<br>
### Error Values
[GroupsMembersListContinueError](#data-types-groupsmemberslistcontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | The cursor is invalid.<br>
other | Void | 
## groups/members/remove
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/members/remove \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"group\": {\".tag\": \"group_id\",\"group_id\": \"g:e2db7665347abcd600000000001a2b3c\"},\"users\": [{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}],\"return_members\": true}"
```

> The above command returns JSON structured like this:

```json
{
    "group_info": {
        "group_name": "project launch", 
        "group_id": "g:e2db7665347abcd600000000001a2b3c", 
        "group_management_type": {
            ".tag": "user_managed"
        }, 
        "created": 1447255518000, 
        "member_count": 5, 
        "members": [
            {
                "profile": {
                    "team_member_id": "dbmid:1234567", 
                    "email": "mary@lamb.com", 
                    "email_verified": true, 
                    "status": {
                        ".tag": "active"
                    }, 
                    "name": {
                        "given_name": "Franz", 
                        "surname": "Ferdinand", 
                        "familiar_name": "Franz", 
                        "display_name": "Franz Ferdinand (Personal)", 
                        "abbreviated_name": "FF"
                    }, 
                    "membership_type": {
                        ".tag": "full"
                    }, 
                    "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                    "secondary_emails": [
                        {
                            "email": "apple@orange.com", 
                            "is_verified": true
                        }, 
                        {
                            "email": "banana@honeydew.com", 
                            "is_verified": true
                        }, 
                        {
                            "email": "grape@strawberry.com", 
                            "is_verified": false
                        }
                    ], 
                    "joined_on": "2015-05-12T15:50:38Z", 
                    "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
                }, 
                "access_type": {
                    ".tag": "member"
                }
            }
        ]
    }, 
    "async_job_id": "99988877733388"
}
```

### Description
Removes members from a group.
The members are removed immediately. However the revoking of group-owned resources may take additional time. Use the groups/job_status/get to determine whether this process has completed.
This method permits removing the only owner of a group, even in cases where this is not possible via the web client.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[GroupMembersRemoveArg](#data-types-groupmembersremovearg)

Field Name | Data Type | Description
--------- | ------- | -----------
group | [GroupSelector](#data-types-groupselector) | Group from which users will be removed.<br>
users | List[[UserSelectorArg](#data-types-userselectorarg)] | List of users to be removed from the group.<br>
return_members | Boolean | Whether to return the list of members in the group.  Note that the default value will cause all the group members  to be returned in the response. This may take a long time for large groups.<br>
### Return Values
[GroupMembersChangeResult](#data-types-groupmemberschangeresult)

Result returned by [team/groups/members/add](#team-groups-members-add) and [team/groups/members/remove](#team-groups-members-remove).

Field Name | Data Type | Description
--------- | ------- | -----------
group_info | [GroupFullInfo](#data-types-groupfullinfo) | The group info after member change operation has been performed.<br>
async_job_id | String | Field is deprecated. For legacy purposes async_job_id will always return one space ' '. Formerly, it was an ID that was used to obtain the status of granting/revoking group-owned resources. It's no longer necessary because the async processing now happens automatically.<br>
### Error Values
[GroupMembersRemoveError](#data-types-groupmembersremoveerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_found | Void | No matching group found. No groups match the specified group ID.<br>
other | Void | 
system_managed_group_disallowed | Void | This operation is not supported on system-managed groups.<br>
member_not_in_group | Void | At least one of the specified users is not a member of the group.<br>
group_not_in_team | Void | Group is not in this team. You cannot remove members from a group that is outside of your team.<br>
members_not_in_team | List[String] | These members are not part of your team.<br>
users_not_found | List[String] | These users were not found in Dropbox.<br>
## groups/members/set_access_type
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/members/set_access_type \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"group\": {\".tag\": \"group_id\",\"group_id\": \"g:e2db7665347abcd600000000001a2b3c\"},\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"access_type\": \"member\",\"return_members\": true}"
```

### Description
Sets a member's access type in a group.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[GroupMembersSetAccessTypeArg](#data-types-groupmemberssetaccesstypearg)

Field Name | Data Type | Description
--------- | ------- | -----------
group | [GroupSelector](#data-types-groupselector) | Specify a group.<br>
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of a user that is a member of [group](#data-types-groupmemberssetaccesstypearg).<br>
access_type | [GroupAccessType](#data-types-groupaccesstype) | New group access type the user will have.<br>
return_members | Boolean | Whether to return the list of members in the group.  Note that the default value will cause all the group members  to be returned in the response. This may take a long time for large groups.<br>
### Return Values
List[[GroupsGetInfoItem](#data-types-groupsgetinfoitem)]
### Error Values
[GroupMemberSetAccessTypeError](#data-types-groupmembersetaccesstypeerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_found | Void | No matching group found. No groups match the specified group ID.<br>
other | Void | 
system_managed_group_disallowed | Void | This operation is not supported on system-managed groups.<br>
member_not_in_group | Void | The specified user is not a member of this group.<br>
user_cannot_be_manager_of_company_managed_group | Void | A company managed group cannot be managed by a user.<br>
## groups/update
```shell
curl -X POST https://api.dropboxapi.com/2/team/groups/update \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"group\": {\".tag\": \"group_id\",\"group_id\": \"g:e2db7665347abcd600000000001a2b3c\"},\"return_members\": true,\"new_group_name\": \"Europe west sales\",\"new_group_external_id\": \"sales-234\",\"new_group_management_type\": \"company_managed\"}"
```

> The above command returns JSON structured like this:

```json
{
    "group_name": "project launch", 
    "group_id": "g:e2db7665347abcd600000000001a2b3c", 
    "group_management_type": {
        ".tag": "user_managed"
    }, 
    "created": 1447255518000, 
    "member_count": 5, 
    "members": [
        {
            "profile": {
                "team_member_id": "dbmid:1234567", 
                "email": "mary@lamb.com", 
                "email_verified": true, 
                "status": {
                    ".tag": "active"
                }, 
                "name": {
                    "given_name": "Franz", 
                    "surname": "Ferdinand", 
                    "familiar_name": "Franz", 
                    "display_name": "Franz Ferdinand (Personal)", 
                    "abbreviated_name": "FF"
                }, 
                "membership_type": {
                    ".tag": "full"
                }, 
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "secondary_emails": [
                    {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }, 
                    {
                        "email": "banana@honeydew.com", 
                        "is_verified": true
                    }, 
                    {
                        "email": "grape@strawberry.com", 
                        "is_verified": false
                    }
                ], 
                "joined_on": "2015-05-12T15:50:38Z", 
                "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
            }, 
            "access_type": {
                ".tag": "member"
            }
        }
    ]
}
```

### Description
Updates a group's name and/or external ID.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
groups.write
### Query Parameters
[GroupUpdateArgs](#data-types-groupupdateargs)

Field Name | Data Type | Description
--------- | ------- | -----------
group | [GroupSelector](#data-types-groupselector) | Specify a group.<br>
return_members | Boolean | Whether to return the list of members in the group.  Note that the default value will cause all the group members  to be returned in the response. This may take a long time for large groups.<br>
new_group_name | Optional[String] | Optional argument. Set group name to this if provided.<br>
new_group_external_id | Optional[String] | Optional argument. New group external ID. If the argument is None, the group's external_id won't be updated. If the argument is empty string, the group's external id will be cleared.<br>
new_group_management_type | Optional[[GroupManagementType](#data-types-groupmanagementtype)] | Set new group management type, if provided.<br>
### Return Values
[GroupFullInfo](#data-types-groupfullinfo)

Full description of a group.

Field Name | Data Type | Description
--------- | ------- | -----------
group_name | String | 
group_id | String | 
group_management_type | [GroupManagementType](#data-types-groupmanagementtype) | Who is allowed to manage the group.<br>
created | UInt64 | The group creation time as a UTC timestamp in milliseconds since the Unix epoch.<br>
group_external_id | Optional[String] | External ID of group. This is an arbitrary ID that an admin can attach to a group.<br>
member_count | Optional[UInt32] | The number of members in the group.<br>
members | Optional[List[[GroupMemberInfo](#data-types-groupmemberinfo)]] | List of group members.<br>
### Error Values
[GroupUpdateError](#data-types-groupupdateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
group_not_found | Void | No matching group found. No groups match the specified group ID.<br>
other | Void | 
system_managed_group_disallowed | Void | This operation is not supported on system-managed groups.<br>
group_name_already_used | Void | The requested group name is already being used by another group.<br>
group_name_invalid | Void | Group name is empty or has invalid characters.<br>
external_id_already_in_use | Void | The requested external ID is already being used by another group.<br>
## legal_holds/create_policy
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/create_policy \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"name\": \"acme cfo policy\",\"members\": [\"dbmid:FDFSVF-DFSDF\"],\"start_date\": \"2016-01-01T00:00:00Z\",\"end_date\": \"2017-12-31T00:00:00Z\"}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "pid_dbhid:abcd1234", 
    "name": "acme cfo policy", 
    "members": {
        "team_member_ids": [
            "dbmid:efgh5678"
        ], 
        "permanently_deleted_users": 2
    }, 
    "status": {
        ".tag": "active"
    }, 
    "start_date": "2016-01-01T00:00:00Z", 
    "activation_time": "2016-01-20T00:00:10Z", 
    "end_date": "2017-12-31T00:00:00Z"
}
```

### Description
Creates new legal hold policy. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsPolicyCreateArg](#data-types-legalholdspolicycreatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Policy name.<br>
members | List[String] | List of team member IDs added to the hold.<br>
description | Optional[String] | A description of the legal hold policy.<br>
start_date | Optional[Timestamp] | start date of the legal hold policy.<br>
end_date | Optional[Timestamp] | end date of the legal hold policy.<br>
### Return Values
[LegalHoldPolicy](#data-types-legalholdpolicy)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold id.<br>
name | String | Policy name.<br>
members | [MembersInfo](#data-types-membersinfo) | Team members IDs and number of permanetly deleted members under hold.<br>
status | [LegalHoldStatus](#data-types-legalholdstatus) | The current state of the hold.<br>
start_date | Timestamp | Start date of the legal hold policy.<br>
description | Optional[String] | A description of the legal hold policy.<br>
activation_time | Optional[Timestamp] | The time at which the legal hold was activated.<br>
end_date | Optional[Timestamp] | End date of the legal hold policy.<br>
### Error Values
[LegalHoldsPolicyCreateError](#data-types-legalholdspolicycreateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
start_date_is_later_than_end_date | Void | Start date must be earlier than end date.<br>
empty_members_list | Void | The users list must have at least one user.<br>
invalid_members | Void | Some members in the members list are not valid to be placed under legal hold.<br>
number_of_users_on_hold_is_greater_than_hold_limitation | Void | You cannot add more than 5 users in a legal hold.<br>
transient_error | Void | Temporary infrastructure failure, please retry.<br>
name_must_be_unique | Void | The name provided is already in use by another legal hold.<br>
team_exceeded_legal_hold_quota | Void | Team exceeded legal hold quota.<br>
## legal_holds/get_policy
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/get_policy \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"pid_dbhid:abcd1234\"}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "pid_dbhid:abcd1234", 
    "name": "acme cfo policy", 
    "members": {
        "team_member_ids": [
            "dbmid:efgh5678"
        ], 
        "permanently_deleted_users": 2
    }, 
    "status": {
        ".tag": "active"
    }, 
    "start_date": "2016-01-01T00:00:00Z", 
    "activation_time": "2016-01-20T00:00:10Z", 
    "end_date": "2017-12-31T00:00:00Z"
}
```

### Description
Gets a legal hold by Id. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsGetPolicyArg](#data-types-legalholdsgetpolicyarg)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold Id.<br>
### Return Values
[LegalHoldPolicy](#data-types-legalholdpolicy)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold id.<br>
name | String | Policy name.<br>
members | [MembersInfo](#data-types-membersinfo) | Team members IDs and number of permanetly deleted members under hold.<br>
status | [LegalHoldStatus](#data-types-legalholdstatus) | The current state of the hold.<br>
start_date | Timestamp | Start date of the legal hold policy.<br>
description | Optional[String] | A description of the legal hold policy.<br>
activation_time | Optional[Timestamp] | The time at which the legal hold was activated.<br>
end_date | Optional[Timestamp] | End date of the legal hold policy.<br>
### Error Values
[LegalHoldsGetPolicyError](#data-types-legalholdsgetpolicyerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
legal_hold_policy_not_found | Void | Legal hold policy does not exist for [LegalHoldsGetPolicyArg.id](#data-types-legalholdsgetpolicyarg).<br>
## legal_holds/list_held_revisions
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/list_held_revisions \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"pid_dbhid:abcd1234\"}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "new_filename": "111_222.pdf", 
            "original_revision_id": "ab2rij4i5ojgfd", 
            "original_file_path": "/a.pdf", 
            "server_modified": "2019-08-12T12:08:52Z", 
            "author_member_id": "dbmid:abcd1234abcd1234abcd1234abcd1234a23", 
            "author_member_status": {
                ".tag": "active"
            }, 
            "author_email": "a@a.com", 
            "file_type": "Document", 
            "size": 3, 
            "content_hash": "abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234"
        }
    ], 
    "has_more": false
}
```

### Description
List the file metadata that's under the hold. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsListHeldRevisionsArg](#data-types-legalholdslistheldrevisionsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold Id.<br>
### Return Values
[LegalHoldsListHeldRevisionResult](#data-types-legalholdslistheldrevisionresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LegalHoldHeldRevisionMetadata](#data-types-legalholdheldrevisionmetadata)] | List of file entries that under the hold.<br>
has_more | Boolean | True if there are more file entries that haven't been returned. You can retrieve them with a call to /legal_holds/list_held_revisions_continue.<br>
cursor | Optional[String] | The cursor idicates where to continue reading file metadata entries for the next API call. When there are no more entries, the cursor will return none.<br>Pass the cursor into /2/team/legal_holds/list_held_revisions/continue.<br>
### Error Values
[LegalHoldsListHeldRevisionsError](#data-types-legalholdslistheldrevisionserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
transient_error | Void | Temporary infrastructure failure, please retry.<br>
legal_hold_still_empty | Void | The legal hold is not holding any revisions yet.<br>
inactive_legal_hold | Void | Trying to list revisions for an inactive legal hold.<br>
## legal_holds/list_held_revisions_continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/list_held_revisions_continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"pid_dbhid:abcd1234\"}"
```

> The above command returns JSON structured like this:

```json
{
    "entries": [
        {
            "new_filename": "111_222.pdf", 
            "original_revision_id": "ab2rij4i5ojgfd", 
            "original_file_path": "/a.pdf", 
            "server_modified": "2019-08-12T12:08:52Z", 
            "author_member_id": "dbmid:abcd1234abcd1234abcd1234abcd1234a23", 
            "author_member_status": {
                ".tag": "active"
            }, 
            "author_email": "a@a.com", 
            "file_type": "Document", 
            "size": 3, 
            "content_hash": "abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234"
        }
    ], 
    "has_more": false
}
```

### Description
Continue listing the file metadata that's under the hold. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsListHeldRevisionsContinueArg](#data-types-legalholdslistheldrevisionscontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold Id.<br>
cursor | Optional[String] | The cursor idicates where to continue reading file metadata entries for the next API call. When there are no more entries, the cursor will return none.<br>
### Return Values
[LegalHoldsListHeldRevisionResult](#data-types-legalholdslistheldrevisionresult)

Field Name | Data Type | Description
--------- | ------- | -----------
entries | List[[LegalHoldHeldRevisionMetadata](#data-types-legalholdheldrevisionmetadata)] | List of file entries that under the hold.<br>
has_more | Boolean | True if there are more file entries that haven't been returned. You can retrieve them with a call to /legal_holds/list_held_revisions_continue.<br>
cursor | Optional[String] | The cursor idicates where to continue reading file metadata entries for the next API call. When there are no more entries, the cursor will return none.<br>Pass the cursor into /2/team/legal_holds/list_held_revisions/continue.<br>
### Error Values
[LegalHoldsListHeldRevisionsError](#data-types-legalholdslistheldrevisionserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
transient_error | Void | Temporary infrastructure failure, please retry.<br>
legal_hold_still_empty | Void | The legal hold is not holding any revisions yet.<br>
inactive_legal_hold | Void | Trying to list revisions for an inactive legal hold.<br>
## legal_holds/list_policies
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/list_policies \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"include_released\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "policies": [
        {
            "id": "pid_dbhid:abcd1234", 
            "name": "acme cfo policy", 
            "members": {
                "team_member_ids": [
                    "dbmid:efgh5678"
                ], 
                "permanently_deleted_users": 2
            }, 
            "status": {
                ".tag": "active"
            }, 
            "start_date": "2016-01-01T00:00:00Z", 
            "activation_time": "2016-01-20T00:00:10Z", 
            "end_date": "2017-12-31T00:00:00Z"
        }
    ]
}
```

### Description
Lists legal holds on a team. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsListPoliciesArg](#data-types-legalholdslistpoliciesarg)

Field Name | Data Type | Description
--------- | ------- | -----------
include_released | Boolean | Whether to return holds that were released.<br>
### Return Values
[LegalHoldsListPoliciesResult](#data-types-legalholdslistpoliciesresult)

Field Name | Data Type | Description
--------- | ------- | -----------
policies | List[[LegalHoldPolicy](#data-types-legalholdpolicy)] | 
### Error Values
[LegalHoldsListPoliciesError](#data-types-legalholdslistpolicieserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
transient_error | Void | Temporary infrastructure failure, please retry.<br>
## legal_holds/release_policy
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/release_policy \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"pid_dbhid:abcd1234\"}"
```

### Description
Releases a legal hold by Id. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsPolicyReleaseArg](#data-types-legalholdspolicyreleasearg)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold Id.<br>
### Return Values
Void
### Error Values
[LegalHoldsPolicyReleaseError](#data-types-legalholdspolicyreleaseerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
legal_hold_performing_another_operation | Void | Legal hold is currently performing another operation.<br>
legal_hold_already_releasing | Void | Legal hold is currently performing a release or is already released.<br>
legal_hold_policy_not_found | Void | Legal hold policy does not exist for [LegalHoldsPolicyReleaseArg.id](#data-types-legalholdspolicyreleasearg).<br>
## legal_holds/update_policy
```shell
curl -X POST https://api.dropboxapi.com/2/team/legal_holds/update_policy \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"id\": \"pid_dbhid:abcd1234\",\"members\": [\"dbmid:FDFSVF-DFSDF\"]}"
```

> The above command returns JSON structured like this:

```json
{
    "id": "pid_dbhid:abcd1234", 
    "name": "acme cfo policy", 
    "members": {
        "team_member_ids": [
            "dbmid:efgh5678"
        ], 
        "permanently_deleted_users": 2
    }, 
    "status": {
        ".tag": "active"
    }, 
    "start_date": "2016-01-01T00:00:00Z", 
    "activation_time": "2016-01-20T00:00:10Z", 
    "end_date": "2017-12-31T00:00:00Z"
}
```

### Description
Updates a legal hold. Note: Legal Holds is a paid add-on. Not all teams have the feature.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[LegalHoldsPolicyUpdateArg](#data-types-legalholdspolicyupdatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold Id.<br>
name | Optional[String] | Policy new name.<br>
description | Optional[String] | Policy new description.<br>
members | Optional[List[String]] | List of team member IDs to apply the policy on.<br>
### Return Values
[LegalHoldPolicy](#data-types-legalholdpolicy)

Field Name | Data Type | Description
--------- | ------- | -----------
id | String | The legal hold id.<br>
name | String | Policy name.<br>
members | [MembersInfo](#data-types-membersinfo) | Team members IDs and number of permanetly deleted members under hold.<br>
status | [LegalHoldStatus](#data-types-legalholdstatus) | The current state of the hold.<br>
start_date | Timestamp | Start date of the legal hold policy.<br>
description | Optional[String] | A description of the legal hold policy.<br>
activation_time | Optional[Timestamp] | The time at which the legal hold was activated.<br>
end_date | Optional[Timestamp] | End date of the legal hold policy.<br>
### Error Values
[LegalHoldsPolicyUpdateError](#data-types-legalholdspolicyupdateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
unknown_legal_hold_error | Void | There has been an unknown legal hold error.<br>
insufficient_permissions | Void | You don't have permissions to perform this action.<br>
other | Void | 
inactive_legal_hold | Void | Trying to release an inactive legal hold.<br>
legal_hold_performing_another_operation | Void | Legal hold is currently performing another operation.<br>
invalid_members | Void | Some members in the members list are not valid to be placed under legal hold.<br>
number_of_users_on_hold_is_greater_than_hold_limitation | Void | You cannot add more than 5 users in a legal hold.<br>
empty_members_list | Void | The users list must have at least one user.<br>
name_must_be_unique | Void | The name provided is already in use by another legal hold.<br>
legal_hold_policy_not_found | Void | Legal hold policy does not exist for [LegalHoldsPolicyUpdateArg.id](#data-types-legalholdspolicyupdatearg).<br>
## linked_apps/list_member_linked_apps
```shell
curl -X POST https://api.dropboxapi.com/2/team/linked_apps/list_member_linked_apps \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_member_id\": \"dbmid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I\"}"
```

### Description
List all linked applications of the team member.
Note, this endpoint does not list any team-linked applications.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.list
### Query Parameters
[ListMemberAppsArg](#data-types-listmemberappsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_member_id | String | The team member id.<br>
### Return Values
[ListMemberAppsResult](#data-types-listmemberappsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
linked_api_apps | List[[ApiApp](#data-types-apiapp)] | List of third party applications linked by this team member.<br>
### Error Values
[ListMemberAppsError](#data-types-listmemberappserror)

Error returned by [team/linked_apps/list_member_linked_apps](#team-linked_apps-list_member_linked_apps).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
member_not_found | Void | Member not found.<br>
other | Void | 
## linked_apps/list_members_linked_apps
### Description
List all applications linked to the team members' accounts.
Note, this endpoint does not list any team-linked applications.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.list
### Query Parameters
[ListMembersAppsArg](#data-types-listmembersappsarg)

Arguments for [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps).

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | Optional[String] | At the first call to the [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps) the cursor shouldn't be passed. Then, if the result of the call includes a cursor, the following requests should include the received cursors in order to receive the next sub list of the team applications.<br>
### Return Values
[ListMembersAppsResult](#data-types-listmembersappsresult)

Information returned by [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps).

Field Name | Data Type | Description
--------- | ------- | -----------
apps | List[[MemberLinkedApps](#data-types-memberlinkedapps)] | The linked applications of each member of the team.<br>
has_more | Boolean | If true, then there are more apps available. Pass the cursor to [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps) to retrieve the rest.<br>
cursor | Optional[String] | Pass the cursor into [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps) to receive the next sub list of team's applications.<br>
### Error Values
[ListMembersAppsError](#data-types-listmembersappserror)

Error returned by [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
reset | Void | Indicates that the cursor has been invalidated. Call [team/linked_apps/list_members_linked_apps](#team-linked_apps-list_members_linked_apps) again with an empty cursor to obtain a new cursor.<br>
other | Void | 
## linked_apps/list_team_linked_apps
### Description
List all applications linked to the team members' accounts.
Note, this endpoint doesn't list any team-linked applications.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[ListTeamAppsArg](#data-types-listteamappsarg)

Arguments for [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps).

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | Optional[String] | At the first call to the [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps) the cursor shouldn't be passed. Then, if the result of the call includes a cursor, the following requests should include the received cursors in order to receive the next sub list of the team applications.<br>
### Return Values
[ListTeamAppsResult](#data-types-listteamappsresult)

Information returned by [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps).

Field Name | Data Type | Description
--------- | ------- | -----------
apps | List[[MemberLinkedApps](#data-types-memberlinkedapps)] | The linked applications of each member of the team.<br>
has_more | Boolean | If true, then there are more apps available. Pass the cursor to [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps) to retrieve the rest.<br>
cursor | Optional[String] | Pass the cursor into [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps) to receive the next sub list of team's applications.<br>
### Error Values
[ListTeamAppsError](#data-types-listteamappserror)

Error returned by [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
reset | Void | Indicates that the cursor has been invalidated. Call [team/linked_apps/list_team_linked_apps](#team-linked_apps-list_team_linked_apps) again with an empty cursor to obtain a new cursor.<br>
other | Void | 
## linked_apps/revoke_linked_app
### Description
Revoke a linked application of the team member.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.modify
### Query Parameters
[RevokeLinkedApiAppArg](#data-types-revokelinkedapiapparg)

Field Name | Data Type | Description
--------- | ------- | -----------
app_id | String | The application's unique id.<br>
team_member_id | String | The unique id of the member owning the device.<br>
keep_app_folder | Boolean | Field is deprecated. This flag is not longer supported, the application dedicated folder (in case the application uses  one) will be kept.<br>
### Return Values
Void
### Error Values
[RevokeLinkedAppError](#data-types-revokelinkedapperror)

Error returned by [team/linked_apps/revoke_linked_app](#team-linked_apps-revoke_linked_app).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
app_not_found | Void | Application not found.<br>
member_not_found | Void | Member not found.<br>
app_folder_removal_not_supported | Void | App folder removal is not supported.<br>
other | Void | 
## linked_apps/revoke_linked_app_batch
### Description
Revoke a list of linked applications of the team members.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sessions.modify
### Query Parameters
[RevokeLinkedApiAppBatchArg](#data-types-revokelinkedapiappbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
revoke_linked_app | List[[RevokeLinkedApiAppArg](#data-types-revokelinkedapiapparg)] | 
### Return Values
[RevokeLinkedAppBatchResult](#data-types-revokelinkedappbatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
revoke_linked_app_status | List[[RevokeLinkedAppStatus](#data-types-revokelinkedappstatus)] | 
### Error Values
[RevokeLinkedAppBatchError](#data-types-revokelinkedappbatcherror)

Error returned by [team/linked_apps/revoke_linked_app_batch](#team-linked_apps-revoke_linked_app_batch).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## member_space_limits/excluded_users/add
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/excluded_users/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"users\": [{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "status": {
        ".tag": "success"
    }
}
```

### Description
Add users to member space limits excluded users list.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[ExcludedUsersUpdateArg](#data-types-excludedusersupdatearg)

Argument of excluded users update operation. Should include a list of users to add/remove (according to endpoint), Maximum size of the list is 1000 users.

Field Name | Data Type | Description
--------- | ------- | -----------
users | Optional[List[[UserSelectorArg](#data-types-userselectorarg)]] | List of users to be added/removed.<br>
### Return Values
[ExcludedUsersUpdateResult](#data-types-excludedusersupdateresult)

Excluded users update result.

Field Name | Data Type | Description
--------- | ------- | -----------
status | [ExcludedUsersUpdateStatus](#data-types-excludedusersupdatestatus) | Update status.<br>
### Error Values
[ExcludedUsersUpdateError](#data-types-excludedusersupdateerror)

Excluded users update error.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
users_not_in_team | Void | At least one of the users is not part of your team.<br>
too_many_users | Void | A maximum of 1000 users for each of addition/removal can be supplied.<br>
other | Void | 
## member_space_limits/excluded_users/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/excluded_users/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "users": [], 
    "has_more": false, 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
List member space limits excluded users.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[ExcludedUsersListArg](#data-types-excludeduserslistarg)

Excluded users list argument.

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | Number of results to return per call.<br>
### Return Values
[ExcludedUsersListResult](#data-types-excludeduserslistresult)

Excluded users list result.

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[MemberProfile](#data-types-memberprofile)] | 
has_more | Boolean | Is true if there are additional excluded users that have not been returned yet. An additional call to [team/member_space_limits/excluded_users/list/continue](#team-member_space_limits-excluded_users-list-continue) can retrieve them.<br>
cursor | Optional[String] | Pass the cursor into [team/member_space_limits/excluded_users/list/continue](#team-member_space_limits-excluded_users-list-continue) to obtain additional excluded users.<br>
### Error Values
[ExcludedUsersListError](#data-types-excludeduserslisterror)

Excluded users list error.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
list_error | Void | An error occurred.<br>
other | Void | 
## member_space_limits/excluded_users/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/excluded_users/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "users": [], 
    "has_more": false, 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu"
}
```

### Description
Continue listing member space limits excluded users.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[ExcludedUsersListContinueArg](#data-types-excludeduserslistcontinuearg)

Excluded users list continue argument.

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of users.<br>
### Return Values
[ExcludedUsersListResult](#data-types-excludeduserslistresult)

Excluded users list result.

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[MemberProfile](#data-types-memberprofile)] | 
has_more | Boolean | Is true if there are additional excluded users that have not been returned yet. An additional call to [team/member_space_limits/excluded_users/list/continue](#team-member_space_limits-excluded_users-list-continue) can retrieve them.<br>
cursor | Optional[String] | Pass the cursor into [team/member_space_limits/excluded_users/list/continue](#team-member_space_limits-excluded_users-list-continue) to obtain additional excluded users.<br>
### Error Values
[ExcludedUsersListContinueError](#data-types-excludeduserslistcontinueerror)

Excluded users list continue error.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | The cursor is invalid.<br>
other | Void | 
## member_space_limits/excluded_users/remove
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/excluded_users/remove \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"users\": [{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "status": {
        ".tag": "success"
    }
}
```

### Description
Remove users from member space limits excluded users list.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[ExcludedUsersUpdateArg](#data-types-excludedusersupdatearg)

Argument of excluded users update operation. Should include a list of users to add/remove (according to endpoint), Maximum size of the list is 1000 users.

Field Name | Data Type | Description
--------- | ------- | -----------
users | Optional[List[[UserSelectorArg](#data-types-userselectorarg)]] | List of users to be added/removed.<br>
### Return Values
[ExcludedUsersUpdateResult](#data-types-excludedusersupdateresult)

Excluded users update result.

Field Name | Data Type | Description
--------- | ------- | -----------
status | [ExcludedUsersUpdateStatus](#data-types-excludedusersupdatestatus) | Update status.<br>
### Error Values
[ExcludedUsersUpdateError](#data-types-excludedusersupdateerror)

Excluded users update error.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
users_not_in_team | Void | At least one of the users is not part of your team.<br>
too_many_users | Void | A maximum of 1000 users for each of addition/removal can be supplied.<br>
other | Void | 
## member_space_limits/get_custom_quota
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/get_custom_quota \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"users\": [{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}]}"
```

### Description
Get users custom quota. Returns none as the custom quota if none was set. A maximum of 1000 members can be specified in a single call.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[CustomQuotaUsersArg](#data-types-customquotausersarg)

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[UserSelectorArg](#data-types-userselectorarg)] | List of users.<br>
### Return Values
List[[CustomQuotaResult](#data-types-customquotaresult)]
### Error Values
[CustomQuotaError](#data-types-customquotaerror)

Error returned when getting member custom quota.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
too_many_users | Void | A maximum of 1000 users can be set for a single call.<br>
other | Void | 
## member_space_limits/remove_custom_quota
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/remove_custom_quota \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"users\": [{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}]}"
```

### Description
Remove users custom quota. A maximum of 1000 members can be specified in a single call.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[CustomQuotaUsersArg](#data-types-customquotausersarg)

Field Name | Data Type | Description
--------- | ------- | -----------
users | List[[UserSelectorArg](#data-types-userselectorarg)] | List of users.<br>
### Return Values
List[[RemoveCustomQuotaResult](#data-types-removecustomquotaresult)]
### Error Values
[CustomQuotaError](#data-types-customquotaerror)

Error returned when getting member custom quota.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
too_many_users | Void | A maximum of 1000 users can be set for a single call.<br>
other | Void | 
## member_space_limits/set_custom_quota
```shell
curl -X POST https://api.dropboxapi.com/2/team/member_space_limits/set_custom_quota \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"users_and_quotas\": [{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"quota_gb\": 30}]}"
```

### Description
Set users custom quota. Custom quota has to be at least 15GB. A maximum of 1000 members can be specified in a single call.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[SetCustomQuotaArg](#data-types-setcustomquotaarg)

Field Name | Data Type | Description
--------- | ------- | -----------
users_and_quotas | List[[UserCustomQuotaArg](#data-types-usercustomquotaarg)] | List of users and their custom quotas.<br>
### Return Values
List[[CustomQuotaResult](#data-types-customquotaresult)]
### Error Values
[SetCustomQuotaError](#data-types-setcustomquotaerror)

Error returned when setting member custom quota.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
too_many_users | Void | A maximum of 1000 users can be set for a single call.<br>
other | Void | 
some_users_are_excluded | Void | Some of the users are on the excluded users list and can't have custom quota set.<br>
## members/add
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"new_members\": [{\"member_email\": \"tom.s@company.com\",\"member_given_name\": \"Tom\",\"member_surname\": \"Silverstone\",\"member_external_id\": \"company_id:342432\",\"send_welcome_email\": true,\"role\": \"member_only\"}],\"force_async\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "complete": [
        {
            ".tag": "success", 
            "profile": {
                "team_member_id": "dbmid:FDFSVF-DFSDF", 
                "email": "tami@seagull.com", 
                "email_verified": false, 
                "status": {
                    ".tag": "active"
                }, 
                "name": {
                    "given_name": "Franz", 
                    "surname": "Ferdinand", 
                    "familiar_name": "Franz", 
                    "display_name": "Franz Ferdinand (Personal)", 
                    "abbreviated_name": "FF"
                }, 
                "membership_type": {
                    ".tag": "full"
                }, 
                "groups": [
                    "g:e2db7665347abcd600000000001a2b3c"
                ], 
                "member_folder_id": "20", 
                "external_id": "244423", 
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "secondary_emails": [
                    {
                        "email": "grape@strawberry.com", 
                        "is_verified": false
                    }, 
                    {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }
                ], 
                "joined_on": "2015-05-12T15:50:38Z", 
                "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
            }, 
            "role": {
                ".tag": "member_only"
            }
        }
    ]
}
```

### Description
Adds members to a team.
Permission : Team member management
A maximum of 20 members can be specified in a single call.
If no Dropbox account exists with the email address specified, a new Dropbox account will be created with the given email address, and that account will be invited to the team.
If a personal Dropbox account exists with the email address specified in the call, this call will create a placeholder Dropbox account for the user on the team and send an email inviting the user to migrate their existing personal account onto the team.
Team member management apps are required to set an initial given_name and surname for a user to use in the team invitation and for 'Perform as team member' actions taken on the user before they become 'active'.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersAddArg](#data-types-membersaddarg)

Field Name | Data Type | Description
--------- | ------- | -----------
new_members | List[[MemberAddArg](#data-types-memberaddarg)] | Details of new members to be added to the team.<br>
force_async | Boolean | Whether to force the add to happen asynchronously.<br>
### Return Values
[MembersAddLaunch](#data-types-membersaddlaunch)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | List[[MemberAddResult](#data-types-memberaddresult)] | 
### Error Values
Void
## members/add/job_status/get
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/add/job_status/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "complete": [
        {
            ".tag": "success", 
            "profile": {
                "team_member_id": "dbmid:FDFSVF-DFSDF", 
                "email": "tami@seagull.com", 
                "email_verified": false, 
                "status": {
                    ".tag": "active"
                }, 
                "name": {
                    "given_name": "Franz", 
                    "surname": "Ferdinand", 
                    "familiar_name": "Franz", 
                    "display_name": "Franz Ferdinand (Personal)", 
                    "abbreviated_name": "FF"
                }, 
                "membership_type": {
                    ".tag": "full"
                }, 
                "groups": [
                    "g:e2db7665347abcd600000000001a2b3c"
                ], 
                "member_folder_id": "20", 
                "external_id": "244423", 
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "secondary_emails": [
                    {
                        "email": "grape@strawberry.com", 
                        "is_verified": false
                    }, 
                    {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }
                ], 
                "joined_on": "2015-05-12T15:50:38Z", 
                "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
            }, 
            "role": {
                ".tag": "member_only"
            }
        }
    ]
}
```

### Description
Once an async_job_id is returned from members/add , use this to poll the status of the asynchronous request.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[MembersAddJobStatus](#data-types-membersaddjobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | List[[MemberAddResult](#data-types-memberaddresult)] | The asynchronous job has finished. For each member that was specified in the parameter [MembersAddArg](#data-types-membersaddarg) that was provided to [team/members/add](#team-members-add), a corresponding item is returned in this list.<br>
failed | String | The asynchronous job returned an error. The string contains an error message.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## members/delete_profile_photo
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/delete_profile_photo \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}}"
```

> The above command returns JSON structured like this:

```json
{
    "profile": {
        "team_member_id": "dbmid:FDFSVF-DFSDF", 
        "email": "tami@seagull.com", 
        "email_verified": false, 
        "status": {
            ".tag": "active"
        }, 
        "name": {
            "given_name": "Franz", 
            "surname": "Ferdinand", 
            "familiar_name": "Franz", 
            "display_name": "Franz Ferdinand (Personal)", 
            "abbreviated_name": "FF"
        }, 
        "membership_type": {
            ".tag": "full"
        }, 
        "groups": [
            "g:e2db7665347abcd600000000001a2b3c"
        ], 
        "member_folder_id": "20", 
        "external_id": "244423", 
        "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
        "secondary_emails": [
            {
                "email": "grape@strawberry.com", 
                "is_verified": false
            }, 
            {
                "email": "apple@orange.com", 
                "is_verified": true
            }
        ], 
        "joined_on": "2015-05-12T15:50:38Z", 
        "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
    }, 
    "role": {
        ".tag": "member_only"
    }
}
```

### Description
Deletes a team member's profile photo.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersDeleteProfilePhotoArg](#data-types-membersdeleteprofilephotoarg)

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of the user whose profile photo will be deleted.<br>
### Return Values
[TeamMemberInfo](#data-types-teammemberinfo)

Information about a team member.

Field Name | Data Type | Description
--------- | ------- | -----------
profile | [TeamMemberProfile](#data-types-teammemberprofile) | Profile of a user as a member of a team.<br>
role | [AdminTier](#data-types-admintier) | The user's role in the team.<br>
### Error Values
[MembersDeleteProfilePhotoError](#data-types-membersdeleteprofilephotoerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
set_profile_disallowed | Void | Modifying deleted users is not allowed.<br>
other | Void | 
## members/get_info
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/get_info \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"members\": [{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}]}"
```

### Description
Returns information about multiple team members.
Permission : Team information
This endpoint will return [MembersGetInfoItem.id_not_found](#data-types-membersgetinfoitem), for IDs (or emails) that cannot be matched to a valid team member.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[MembersGetInfoArgs](#data-types-membersgetinfoargs)

Field Name | Data Type | Description
--------- | ------- | -----------
members | List[[UserSelectorArg](#data-types-userselectorarg)] | List of team members.<br>
### Return Values
List[[MembersGetInfoItem](#data-types-membersgetinfoitem)]
### Error Values
[MembersGetInfoError](#data-types-membersgetinfoerror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## members/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100,\"include_removed\": false}"
```

> The above command returns JSON structured like this:

```json
{
    "members": [
        {
            "profile": {
                "team_member_id": "dbmid:FDFSVF-DFSDF", 
                "email": "tami@seagull.com", 
                "email_verified": false, 
                "status": {
                    ".tag": "active"
                }, 
                "name": {
                    "given_name": "Franz", 
                    "surname": "Ferdinand", 
                    "familiar_name": "Franz", 
                    "display_name": "Franz Ferdinand (Personal)", 
                    "abbreviated_name": "FF"
                }, 
                "membership_type": {
                    ".tag": "full"
                }, 
                "groups": [
                    "g:e2db7665347abcd600000000001a2b3c"
                ], 
                "member_folder_id": "20", 
                "external_id": "244423", 
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "secondary_emails": [
                    {
                        "email": "grape@strawberry.com", 
                        "is_verified": false
                    }, 
                    {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }
                ], 
                "joined_on": "2015-05-12T15:50:38Z", 
                "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
            }, 
            "role": {
                ".tag": "member_only"
            }
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": true
}
```

### Description
Lists members of a team.
Permission : Team information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[MembersListArg](#data-types-memberslistarg)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | Number of results to return per call.<br>
include_removed | Boolean | Whether to return removed members.<br>
### Return Values
[MembersListResult](#data-types-memberslistresult)

Field Name | Data Type | Description
--------- | ------- | -----------
members | List[[TeamMemberInfo](#data-types-teammemberinfo)] | List of team members.<br>
cursor | String | Pass the cursor into [team/members/list/continue](#team-members-list-continue) to obtain the additional members.<br>
has_more | Boolean | Is true if there are additional team members that have not been returned yet. An additional call to [team/members/list/continue](#team-members-list-continue) can retrieve them.<br>
### Error Values
[MembersListError](#data-types-memberslisterror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## members/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "members": [
        {
            "profile": {
                "team_member_id": "dbmid:FDFSVF-DFSDF", 
                "email": "tami@seagull.com", 
                "email_verified": false, 
                "status": {
                    ".tag": "active"
                }, 
                "name": {
                    "given_name": "Franz", 
                    "surname": "Ferdinand", 
                    "familiar_name": "Franz", 
                    "display_name": "Franz Ferdinand (Personal)", 
                    "abbreviated_name": "FF"
                }, 
                "membership_type": {
                    ".tag": "full"
                }, 
                "groups": [
                    "g:e2db7665347abcd600000000001a2b3c"
                ], 
                "member_folder_id": "20", 
                "external_id": "244423", 
                "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
                "secondary_emails": [
                    {
                        "email": "grape@strawberry.com", 
                        "is_verified": false
                    }, 
                    {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }
                ], 
                "joined_on": "2015-05-12T15:50:38Z", 
                "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
            }, 
            "role": {
                ".tag": "member_only"
            }
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": true
}
```

### Description
Once a cursor has been retrieved from members/list, use this to paginate through all team members.
Permission : Team information.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.read
### Query Parameters
[MembersListContinueArg](#data-types-memberslistcontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of members.<br>
### Return Values
[MembersListResult](#data-types-memberslistresult)

Field Name | Data Type | Description
--------- | ------- | -----------
members | List[[TeamMemberInfo](#data-types-teammemberinfo)] | List of team members.<br>
cursor | String | Pass the cursor into [team/members/list/continue](#team-members-list-continue) to obtain the additional members.<br>
has_more | Boolean | Is true if there are additional team members that have not been returned yet. An additional call to [team/members/list/continue](#team-members-list-continue) can retrieve them.<br>
### Error Values
[MembersListContinueError](#data-types-memberslistcontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | The cursor is invalid.<br>
other | Void | 
## members/move_former_member_files
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/move_former_member_files \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"transfer_dest_id\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"transfer_admin_id\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Moves removed member's files to a different member. This endpoint initiates an asynchronous job. To obtain the final result of the job, the client should periodically poll members/move_former_member_files/job_status/check.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersDataTransferArg](#data-types-membersdatatransferarg)

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user to remove/suspend/have their files moved.<br>
transfer_dest_id | [UserSelectorArg](#data-types-userselectorarg) | Files from the deleted member account will be transferred to this user.<br>
transfer_admin_id | [UserSelectorArg](#data-types-userselectorarg) | Errors during the transfer process will be sent via email to this user.<br>
### Return Values
[LaunchEmptyResult](#data-types-launchemptyresult)

Result returned by methods that may either launch an asynchronous job or complete synchronously. Upon synchronous completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | Void | The job finished synchronously and successfully.<br>
### Error Values
[MembersTransferFormerMembersFilesError](#data-types-memberstransferformermembersfileserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
other | Void | 
removed_and_transfer_dest_should_differ | Void | Expected removed user and transfer_dest user to be different.<br>
removed_and_transfer_admin_should_differ | Void | Expected removed user and transfer_admin user to be different.<br>
transfer_dest_user_not_found | Void | No matching user found for the argument transfer_dest_id.<br>
transfer_dest_user_not_in_team | Void | The provided transfer_dest_id does not exist on this team.<br>
transfer_admin_user_not_in_team | Void | The provided transfer_admin_id does not exist on this team.<br>
transfer_admin_user_not_found | Void | No matching user found for the argument transfer_admin_id.<br>
unspecified_transfer_admin_id | Void | The transfer_admin_id argument must be provided when file transfer is requested.<br>
transfer_admin_is_not_admin | Void | Specified transfer_admin user is not a team admin.<br>
recipient_not_verified | Void | The recipient user's email is not verified.<br>
user_data_is_being_transferred | Void | The user's data is being transferred. Please wait some time before retrying.<br>
user_not_removed | Void | No matching removed user found for the argument user.<br>
user_data_cannot_be_transferred | Void | User files aren't transferable anymore.<br>
user_data_already_transferred | Void | User's data has already been transferred to another user.<br>
## members/move_former_member_files/job_status/check
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/move_former_member_files/job_status/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Once an async_job_id is returned from members/move_former_member_files , use this to poll the status of the asynchronous request.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[PollEmptyResult](#data-types-pollemptyresult)

Result returned by methods that poll for the status of an asynchronous job. Upon completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | Void | The asynchronous job has completed successfully.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## members/recover
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/recover \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}}"
```

### Description
Recover a deleted member.
Permission : Team member management
Exactly one of team_member_id, email, or external_id must be provided to identify the user account.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.delete
### Query Parameters
[MembersRecoverArg](#data-types-membersrecoverarg)

Exactly one of team_member_id, email, or external_id must be provided to identify the user account.

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user to recover.<br>
### Return Values
Void
### Error Values
[MembersRecoverError](#data-types-membersrecovererror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_unrecoverable | Void | The user is not recoverable.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
team_license_limit | Void | Team is full. The organization has no available licenses.<br>
other | Void | 
## members/remove
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/remove \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"wipe_data\": true,\"transfer_dest_id\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"transfer_admin_id\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"keep_account\": false,\"retain_team_shares\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Removes a member from a team.
Permission : Team member management
Exactly one of team_member_id, email, or external_id must be provided to identify the user account.
Accounts can be recovered via members/recover for a 7 day period or until the account has been permanently deleted or transferred to another account (whichever comes first). Calling members/add while a user is still recoverable on your team will return with [MemberAddResult.user_already_on_team](#data-types-memberaddresult).
Accounts can have their files transferred via the admin console for a limited time, based on the version history length associated with the team (180 days for most teams).
This endpoint may initiate an asynchronous job. To obtain the final result of the job, the client should periodically poll members/remove/job_status/get.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.delete
### Query Parameters
[MembersRemoveArg](#data-types-membersremovearg)

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user to remove/suspend/have their files moved.<br>
wipe_data | Boolean | If provided, controls if the user's data will be deleted on their linked devices.<br>
transfer_dest_id | Optional[[UserSelectorArg](#data-types-userselectorarg)] | If provided, files from the deleted member account will be transferred to this user.<br>
transfer_admin_id | Optional[[UserSelectorArg](#data-types-userselectorarg)] | If provided, errors during the transfer process will be sent via email to this user. If the transfer_dest_id argument was provided, then this argument must be provided as well.<br>
keep_account | Boolean | Downgrade the member to a Basic account. The user will retain the email address associated with their Dropbox  account and data in their account that is not restricted to team members. In order to keep the account the argument [wipe_data](#data-types-membersremovearg) should be set to false.<br>
retain_team_shares | Boolean | If provided, allows removed users to keep access to Dropbox folders (not Dropbox Paper folders) already explicitly shared with them (not via a group) when they are downgraded to a Basic account. Users will not retain access to folders that do not allow external sharing. In order to keep the sharing relationships, the arguments [wipe_data](#data-types-membersremovearg) should be set to false and [keep_account](#data-types-membersremovearg) should be set to true.<br>
### Return Values
[LaunchEmptyResult](#data-types-launchemptyresult)

Result returned by methods that may either launch an asynchronous job or complete synchronously. Upon synchronous completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | Void | The job finished synchronously and successfully.<br>
### Error Values
[MembersRemoveError](#data-types-membersremoveerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
other | Void | 
removed_and_transfer_dest_should_differ | Void | Expected removed user and transfer_dest user to be different.<br>
removed_and_transfer_admin_should_differ | Void | Expected removed user and transfer_admin user to be different.<br>
transfer_dest_user_not_found | Void | No matching user found for the argument transfer_dest_id.<br>
transfer_dest_user_not_in_team | Void | The provided transfer_dest_id does not exist on this team.<br>
transfer_admin_user_not_in_team | Void | The provided transfer_admin_id does not exist on this team.<br>
transfer_admin_user_not_found | Void | No matching user found for the argument transfer_admin_id.<br>
unspecified_transfer_admin_id | Void | The transfer_admin_id argument must be provided when file transfer is requested.<br>
transfer_admin_is_not_admin | Void | Specified transfer_admin user is not a team admin.<br>
recipient_not_verified | Void | The recipient user's email is not verified.<br>
remove_last_admin | Void | The user is the last admin of the team, so it cannot be removed from it.<br>
cannot_keep_account_and_transfer | Void | Cannot keep account and transfer the data to another user at the same time.<br>
cannot_keep_account_and_delete_data | Void | Cannot keep account and delete the data at the same time. To keep the account the argument wipe_data should be set to false.<br>
email_address_too_long_to_be_disabled | Void | The email address of the user is too long to be disabled.<br>
cannot_keep_invited_user_account | Void | Cannot keep account of an invited user.<br>
cannot_retain_shares_when_data_wiped | Void | Cannot retain team shares when the user's data is marked for deletion on their linked devices. The argument wipe_data should be set to false.<br>
cannot_retain_shares_when_no_account_kept | Void | The user's account must be kept in order to retain team shares. The argument keep_account should be set to true.<br>
cannot_retain_shares_when_team_external_sharing_off | Void | Externally sharing files, folders, and links must be enabled in team settings in order to retain team shares for the user.<br>
cannot_keep_account | Void | Only a team admin, can convert this account to a Basic account.<br>
cannot_keep_account_under_legal_hold | Void | This user content is currently being held. To convert this member's account to a Basic account, you'll first need to remove them from the hold.<br>
cannot_keep_account_required_to_sign_tos | Void | To convert this member to a Basic account, they'll first need to sign in to Dropbox and agree to the terms of service.<br>
## members/remove/job_status/get
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/remove/job_status/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete"
}
```

### Description
Once an async_job_id is returned from members/remove , use this to poll the status of the asynchronous request.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.delete
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[PollEmptyResult](#data-types-pollemptyresult)

Result returned by methods that poll for the status of an asynchronous job. Upon completion of the job, no additional information is returned.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | Void | The asynchronous job has completed successfully.<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## members/secondary_emails/add
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/secondary_emails/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"new_secondary_emails\": [{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"secondary_emails\": [\"bob2@hotmail.com\",\"bob@inst.gov\"]}]}"
```

> The above command returns JSON structured like this:

```json
{
    "results": [
        {
            ".tag": "success", 
            "user": {
                ".tag": "team_member_id", 
                "team_member_id": "dbmid:efgh5678"
            }, 
            "results": [
                {
                    ".tag": "success", 
                    "success": {
                        "email": "apple@orange.com", 
                        "is_verified": true
                    }
                }, 
                {
                    ".tag": "unavailable", 
                    "unavailable": "alice@example.com"
                }
            ]
        }, 
        {
            ".tag": "invalid_user", 
            "invalid_user": {
                ".tag": "team_member_id", 
                "team_member_id": "dbmid:efgh5678"
            }
        }
    ]
}
```

### Description
Add secondary emails to users.
Permission : Team member management.
Emails that are on verified domains will be verified automatically. For each email address not on a verified domain a verification email will be sent.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[AddSecondaryEmailsArg](#data-types-addsecondaryemailsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
new_secondary_emails | List[[UserSecondaryEmailsArg](#data-types-usersecondaryemailsarg)] | List of users and secondary emails to add.<br>
### Return Values
[AddSecondaryEmailsResult](#data-types-addsecondaryemailsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
results | List[[UserAddResult](#data-types-useraddresult)] | List of users and secondary email results.<br>
### Error Values
[AddSecondaryEmailsError](#data-types-addsecondaryemailserror)

Error returned when adding secondary emails fails.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
secondary_emails_disabled | Void | Secondary emails are disabled for the team.<br>
too_many_emails | Void | A maximum of 20 secondary emails can be added in a single call.<br>
other | Void | 
## members/secondary_emails/delete
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/secondary_emails/delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"emails_to_delete\": [{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"secondary_emails\": [\"bob2@hotmail.com\",\"bob@inst.gov\"]}]}"
```

> The above command returns JSON structured like this:

```json
{
    "results": [
        {
            ".tag": "success", 
            "user": {
                ".tag": "team_member_id", 
                "team_member_id": "dbmid:efgh5678"
            }, 
            "results": [
                {
                    ".tag": "success", 
                    "success": "alice@example.com"
                }, 
                {
                    ".tag": "not_found", 
                    "not_found": "alic@example.com"
                }
            ]
        }
    ]
}
```

### Description
Delete secondary emails from users
Permission : Team member management.
Users will be notified of deletions of verified secondary emails at both the secondary email and their primary email.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[DeleteSecondaryEmailsArg](#data-types-deletesecondaryemailsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
emails_to_delete | List[[UserSecondaryEmailsArg](#data-types-usersecondaryemailsarg)] | List of users and their secondary emails to delete.<br>
### Return Values
[DeleteSecondaryEmailsResult](#data-types-deletesecondaryemailsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
results | List[[UserDeleteResult](#data-types-userdeleteresult)] | 
### Error Values
Void
## members/secondary_emails/resend_verification_emails
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/secondary_emails/resend_verification_emails \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"emails_to_resend\": [{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"secondary_emails\": [\"bob2@hotmail.com\",\"bob@inst.gov\"]}]}"
```

> The above command returns JSON structured like this:

```json
{
    "results": [
        {
            ".tag": "success", 
            "user": {
                ".tag": "team_member_id", 
                "team_member_id": "dbmid:efgh5678"
            }, 
            "results": [
                {
                    ".tag": "success", 
                    "success": "alice@example.com"
                }
            ]
        }
    ]
}
```

### Description
Resend secondary email verification emails.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[ResendVerificationEmailArg](#data-types-resendverificationemailarg)

Field Name | Data Type | Description
--------- | ------- | -----------
emails_to_resend | List[[UserSecondaryEmailsArg](#data-types-usersecondaryemailsarg)] | List of users and secondary emails to resend verification emails to.<br>
### Return Values
[ResendVerificationEmailResult](#data-types-resendverificationemailresult)

List of users and resend results.

Field Name | Data Type | Description
--------- | ------- | -----------
results | List[[UserResendResult](#data-types-userresendresult)] | 
### Error Values
Void
## members/send_welcome_email
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/send_welcome_email \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}"
```

### Description
Sends welcome email to pending team member.
Permission : Team member management
Exactly one of team_member_id, email, or external_id must be provided to identify the user account.
No-op if team member is not pending.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[UserSelectorArg](#data-types-userselectorarg)

Argument for selecting a single user, either by team_member_id, external_id or email.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
team_member_id | String | 
external_id | String | 
email | String | 
### Return Values
Void
### Error Values
[MembersSendWelcomeError](#data-types-memberssendwelcomeerror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
other | Void | 
## members/set_admin_permissions
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/set_admin_permissions \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"new_role\": \"member_only\"}"
```

> The above command returns JSON structured like this:

```json
{
    "team_member_id": "dbmid:9978889", 
    "role": {
        ".tag": "member_only"
    }
}
```

### Description
Updates a team member's permissions.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersSetPermissionsArg](#data-types-memberssetpermissionsarg)

Exactly one of team_member_id, email, or external_id must be provided to identify the user account.

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user whose role will be set.<br>
new_role | [AdminTier](#data-types-admintier) | The new role of the member.<br>
### Return Values
[MembersSetPermissionsResult](#data-types-memberssetpermissionsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
team_member_id | String | The member ID of the user to which the change was applied.<br>
role | [AdminTier](#data-types-admintier) | The role after the change.<br>
### Error Values
[MembersSetPermissionsError](#data-types-memberssetpermissionserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
last_admin | Void | Cannot remove the admin setting of the last admin.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
cannot_set_permissions | Void | Cannot remove/grant permissions.<br>
team_license_limit | Void | Team is full. The organization has no available licenses.<br>
other | Void | 
## members/set_profile
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/set_profile \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"new_email\": \"t.smith@domain.com\",\"new_surname\": \"Smith\"}"
```

> The above command returns JSON structured like this:

```json
{
    "profile": {
        "team_member_id": "dbmid:FDFSVF-DFSDF", 
        "email": "tami@seagull.com", 
        "email_verified": false, 
        "status": {
            ".tag": "active"
        }, 
        "name": {
            "given_name": "Franz", 
            "surname": "Ferdinand", 
            "familiar_name": "Franz", 
            "display_name": "Franz Ferdinand (Personal)", 
            "abbreviated_name": "FF"
        }, 
        "membership_type": {
            ".tag": "full"
        }, 
        "groups": [
            "g:e2db7665347abcd600000000001a2b3c"
        ], 
        "member_folder_id": "20", 
        "external_id": "244423", 
        "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
        "secondary_emails": [
            {
                "email": "grape@strawberry.com", 
                "is_verified": false
            }, 
            {
                "email": "apple@orange.com", 
                "is_verified": true
            }
        ], 
        "joined_on": "2015-05-12T15:50:38Z", 
        "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
    }, 
    "role": {
        ".tag": "member_only"
    }
}
```

### Description
Updates a team member's profile.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersSetProfileArg](#data-types-memberssetprofilearg)

Exactly one of team_member_id, email, or external_id must be provided to identify the user account.
At least one of new_email, new_external_id, new_given_name, and/or new_surname must be provided.

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user whose profile will be set.<br>
new_email | Optional[String] | New email for member.<br>
new_external_id | Optional[String] | New external ID for member.<br>
new_given_name | Optional[String] | New given name for member.<br>
new_surname | Optional[String] | New surname for member.<br>
new_persistent_id | Optional[String] | New persistent ID. This field only available to teams using persistent ID SAML configuration.<br>
new_is_directory_restricted | Optional[Boolean] | New value for whether the user is a directory restricted user.<br>
### Return Values
[TeamMemberInfo](#data-types-teammemberinfo)

Information about a team member.

Field Name | Data Type | Description
--------- | ------- | -----------
profile | [TeamMemberProfile](#data-types-teammemberprofile) | Profile of a user as a member of a team.<br>
role | [AdminTier](#data-types-admintier) | The user's role in the team.<br>
### Error Values
[MembersSetProfileError](#data-types-memberssetprofileerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
external_id_and_new_external_id_unsafe | Void | It is unsafe to use both external_id and new_external_id.<br>
no_new_data_specified | Void | None of new_email, new_given_name, new_surname, or new_external_id are specified.<br>
email_reserved_for_other_user | Void | Email is already reserved for another user.<br>
external_id_used_by_other_user | Void | The external ID is already in use by another team member.<br>
set_profile_disallowed | Void | Modifying deleted users is not allowed.<br>
param_cannot_be_empty | Void | Parameter new_email cannot be empty.<br>
persistent_id_disabled | Void | Persistent ID is only available to teams with persistent ID SAML configuration. Please contact Dropbox for more information.<br>
persistent_id_used_by_other_user | Void | The persistent ID is already in use by another team member.<br>
directory_restricted_off | Void | Directory Restrictions option is not available.<br>
other | Void | 
## members/set_profile_photo
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/set_profile_photo \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"photo\": {\".tag\": \"base64_data\",\"base64_data\": \"SW1hZ2UgZGF0YSBpbiBiYXNlNjQtZW5jb2RlZCBieXRlcy4gTm90IGEgdmFsaWQgZXhhbXBsZS4=\"}}"
```

> The above command returns JSON structured like this:

```json
{
    "profile": {
        "team_member_id": "dbmid:FDFSVF-DFSDF", 
        "email": "tami@seagull.com", 
        "email_verified": false, 
        "status": {
            ".tag": "active"
        }, 
        "name": {
            "given_name": "Franz", 
            "surname": "Ferdinand", 
            "familiar_name": "Franz", 
            "display_name": "Franz Ferdinand (Personal)", 
            "abbreviated_name": "FF"
        }, 
        "membership_type": {
            ".tag": "full"
        }, 
        "groups": [
            "g:e2db7665347abcd600000000001a2b3c"
        ], 
        "member_folder_id": "20", 
        "external_id": "244423", 
        "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
        "secondary_emails": [
            {
                "email": "grape@strawberry.com", 
                "is_verified": false
            }, 
            {
                "email": "apple@orange.com", 
                "is_verified": true
            }
        ], 
        "joined_on": "2015-05-12T15:50:38Z", 
        "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
    }, 
    "role": {
        ".tag": "member_only"
    }
}
```

### Description
Updates a team member's profile photo.
Permission : Team member management.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersSetProfilePhotoArg](#data-types-memberssetprofilephotoarg)

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of the user whose profile photo will be set.<br>
photo | [PhotoSourceArg](#data-types-photosourcearg) | Image to set as the member's new profile photo.<br>
### Return Values
[TeamMemberInfo](#data-types-teammemberinfo)

Information about a team member.

Field Name | Data Type | Description
--------- | ------- | -----------
profile | [TeamMemberProfile](#data-types-teammemberprofile) | Profile of a user as a member of a team.<br>
role | [AdminTier](#data-types-admintier) | The user's role in the team.<br>
### Error Values
[MembersSetProfilePhotoError](#data-types-memberssetprofilephotoerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
set_profile_disallowed | Void | Modifying deleted users is not allowed.<br>
photo_error | [SetProfilePhotoError](#data-types-setprofilephotoerror) | 
other | Void | 
## members/suspend
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/suspend \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"},\"wipe_data\": false}"
```

### Description
Suspend a member from a team.
Permission : Team member management
Exactly one of team_member_id, email, or external_id must be provided to identify the user account.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersDeactivateArg](#data-types-membersdeactivatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user to remove/suspend/have their files moved.<br>
wipe_data | Boolean | If provided, controls if the user's data will be deleted on their linked devices.<br>
### Return Values
Void
### Error Values
[MembersSuspendError](#data-types-memberssuspenderror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
other | Void | 
suspend_inactive_user | Void | The user is not active, so it cannot be suspended.<br>
suspend_last_admin | Void | The user is the last admin of the team, so it cannot be suspended.<br>
team_license_limit | Void | Team is full. The organization has no available licenses.<br>
## members/unsuspend
```shell
curl -X POST https://api.dropboxapi.com/2/team/members/unsuspend \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"user\": {\".tag\": \"team_member_id\",\"team_member_id\": \"dbmid:efgh5678\"}}"
```

### Description
Unsuspend a member from a team.
Permission : Team member management
Exactly one of team_member_id, email, or external_id must be provided to identify the user account.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
members.write
### Query Parameters
[MembersUnsuspendArg](#data-types-membersunsuspendarg)

Exactly one of team_member_id, email, or external_id must be provided to identify the user account.

Field Name | Data Type | Description
--------- | ------- | -----------
user | [UserSelectorArg](#data-types-userselectorarg) | Identity of user to unsuspend.<br>
### Return Values
Void
### Error Values
[MembersUnsuspendError](#data-types-membersunsuspenderror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
user_not_found | Void | No matching user found. The provided team_member_id, email, or external_id does not exist on this team.<br>
user_not_in_team | Void | The user is not a member of the team.<br>
other | Void | 
unsuspend_non_suspended_member | Void | The user is unsuspended, so it cannot be unsuspended again.<br>
team_license_limit | Void | Team is full. The organization has no available licenses.<br>
## namespaces/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/namespaces/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 1}"
```

> The above command returns JSON structured like this:

```json
{
    "namespaces": [
        {
            "name": "Marketing", 
            "namespace_id": "123456789", 
            "namespace_type": {
                ".tag": "shared_folder"
            }
        }, 
        {
            "name": "Franz Ferdinand", 
            "namespace_id": "123456789", 
            "namespace_type": {
                ".tag": "team_member_folder"
            }, 
            "team_member_id": "dbmid:1234567"
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Returns a list of all team-accessible namespaces. This list includes team folders, shared folders containing team members, team members' home namespaces, and team members' app folders. Home namespaces and app folders are always owned by this team or members of the team, but shared folders may be owned by other users or other teams. Duplicates may occur in the list.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[TeamNamespacesListArg](#data-types-teamnamespaceslistarg)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | Field is deprecated. Specifying a value here has no effect.<br>
### Return Values
[TeamNamespacesListResult](#data-types-teamnamespaceslistresult)

Result for [team/namespaces/list](#team-namespaces-list).

Field Name | Data Type | Description
--------- | ------- | -----------
namespaces | List[[NamespaceMetadata](#data-types-namespacemetadata)] | List of all namespaces the team can access.<br>
cursor | String | Pass the cursor into [team/namespaces/list/continue](#team-namespaces-list-continue) to obtain additional namespaces. Note that duplicate namespaces may be returned.<br>
has_more | Boolean | Is true if there are additional namespaces that have not been returned yet.<br>
### Error Values
[TeamNamespacesListError](#data-types-teamnamespaceslisterror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_arg | Void | Argument passed in is invalid.<br>
other | Void | 
## namespaces/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/namespaces/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "namespaces": [
        {
            "name": "Marketing", 
            "namespace_id": "123456789", 
            "namespace_type": {
                ".tag": "shared_folder"
            }
        }, 
        {
            "name": "Franz Ferdinand", 
            "namespace_id": "123456789", 
            "namespace_type": {
                ".tag": "team_member_folder"
            }, 
            "team_member_id": "dbmid:1234567"
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from namespaces/list, use this to paginate through all team-accessible namespaces. Duplicates may occur in the list.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.member
### Query Parameters
[TeamNamespacesListContinueArg](#data-types-teamnamespaceslistcontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of team-accessible namespaces.<br>
### Return Values
[TeamNamespacesListResult](#data-types-teamnamespaceslistresult)

Result for [team/namespaces/list](#team-namespaces-list).

Field Name | Data Type | Description
--------- | ------- | -----------
namespaces | List[[NamespaceMetadata](#data-types-namespacemetadata)] | List of all namespaces the team can access.<br>
cursor | String | Pass the cursor into [team/namespaces/list/continue](#team-namespaces-list-continue) to obtain additional namespaces. Note that duplicate namespaces may be returned.<br>
has_more | Boolean | Is true if there are additional namespaces that have not been returned yet.<br>
### Error Values
[TeamNamespacesListContinueError](#data-types-teamnamespaceslistcontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_arg | Void | Argument passed in is invalid.<br>
other | Void | 
invalid_cursor | Void | The cursor is invalid.<br>
## properties/template/add
```shell
curl -X POST https://api.dropboxapi.com/2/team/properties/template/add \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"name\": \"Security\",\"description\": \"These properties describe how confidential this file or folder is.\",\"fields\": [{\"name\": \"Security Policy\",\"description\": \"This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.\",\"type\": \"string\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
}
```

### Description
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[AddTemplateArg](#data-types-addtemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Return Values
[AddTemplateResult](#data-types-addtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by  See [team/templates/add_for_user](#team-templates-add_for_user) or [team/templates/add_for_team](#team-templates-add_for_team).<br>
### Error Values
[ModifyTemplateError](#data-types-modifytemplateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
conflicting_property_names | Void | A property field key with that name already exists in the template.<br>
too_many_properties | Void | There are too many properties in the changed template. The maximum number of properties per template is 32.<br>
too_many_templates | Void | There are too many templates for the team.<br>
template_attribute_too_large | Void | The template name, description or one or more of the property field keys is too large.<br>
## properties/template/get
```shell
curl -X POST https://api.dropboxapi.com/2/team/properties/template/get \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\"}"
```

> The above command returns JSON structured like this:

```json
{
    "name": "Security", 
    "description": "These properties describe how confidential this file or folder is.", 
    "fields": [
        {
            "name": "Security Policy", 
            "description": "This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.", 
            "type": {
                ".tag": "string"
            }
        }
    ]
}
```

### Description
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[GetTemplateArg](#data-types-gettemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [team/templates/add_for_user](#team-templates-add_for_user) or [team/templates/add_for_team](#team-templates-add_for_team).<br>
### Return Values
[GetTemplateResult](#data-types-gettemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Display name for the template. Template names can be up to 256 bytes.<br>
description | String | Description for the template. Template descriptions can be up to 1024 bytes.<br>
fields | List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)] | Definitions of the property fields associated with this template. There can be up to 32 properties in a single template.<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## properties/template/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/properties/template/list \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "template_ids": [
        "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
    ]
}
```

### Description
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
Void
### Return Values
[ListTemplateResult](#data-types-listtemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_ids | List[String] | List of identifiers for templates added by  See [team/templates/add_for_user](#team-templates-add_for_user) or [team/templates/add_for_team](#team-templates-add_for_team).<br>
### Error Values
[TemplateError](#data-types-templateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
## properties/template/update
```shell
curl -X POST https://api.dropboxapi.com/2/team/properties/template/update \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"template_id\": \"ptid:1a5n2i6d3OYEAAAAAAAAAYa\",\"name\": \"New Security Template Name\",\"description\": \"These properties will describe how confidential this file or folder is.\",\"add_fields\": [{\"name\": \"Security Policy\",\"description\": \"This is the security policy of the file or folder described.\nPolicies can be Confidential, Public or Internal.\",\"type\": \"string\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "template_id": "ptid:1a5n2i6d3OYEAAAAAAAAAYa"
}
```

### Description
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Query Parameters
[UpdateTemplateArg](#data-types-updatetemplatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by  See [team/templates/add_for_user](#team-templates-add_for_user) or [team/templates/add_for_team](#team-templates-add_for_team).<br>
name | Optional[String] | A display name for the template. template names can be up to 256 bytes.<br>
description | Optional[String] | Description for the new template. Template descriptions can be up to 1024 bytes.<br>
add_fields | Optional[List[[PropertyFieldTemplate](#data-types-propertyfieldtemplate)]] | Property field templates to be added to the group template. There can be up to 32 properties in a single template.<br>
### Return Values
[UpdateTemplateResult](#data-types-updatetemplateresult)

Field Name | Data Type | Description
--------- | ------- | -----------
template_id | String | An identifier for template added by route  See [team/templates/add_for_user](#team-templates-add_for_user) or [team/templates/add_for_team](#team-templates-add_for_team).<br>
### Error Values
[ModifyTemplateError](#data-types-modifytemplateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
template_not_found | String | Template does not exist for the given identifier.<br>
restricted_content | Void | You do not have permission to modify this template.<br>
other | Void | 
conflicting_property_names | Void | A property field key with that name already exists in the template.<br>
too_many_properties | Void | There are too many properties in the changed template. The maximum number of properties per template is 32.<br>
too_many_templates | Void | There are too many templates for the team.<br>
template_attribute_too_large | Void | The template name, description or one or more of the property field keys is too large.<br>
## reports/get_activity
### Description
Retrieves reporting data about a team's user activity.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
[DateRange](#data-types-daterange)

Input arguments that can be provided for most reports.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | Optional[Timestamp] | Optional starting date (inclusive). If start_date is None or too long ago, this field will  be set to 6 months ago.<br>
end_date | Optional[Timestamp] | Optional ending date (exclusive).<br>
### Return Values
[GetActivityReport](#data-types-getactivityreport)

Activity Report Result. Each of the items in the storage report is an array of values, one value per day. If there is no data for a day, then the value will be None.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | String | First date present in the results as 'YYYY-MM-DD' or None.<br>
adds | List[Optional[UInt64]] | Array of total number of adds by team members.<br>
edits | List[Optional[UInt64]] | Array of number of edits by team members. If the same user edits the same file multiple times this is counted as a single edit.<br>
deletes | List[Optional[UInt64]] | Array of total number of deletes by team members.<br>
active_users_28_day | List[Optional[UInt64]] | Array of the number of users who have been active in the last 28 days.<br>
active_users_7_day | List[Optional[UInt64]] | Array of the number of users who have been active in the last week.<br>
active_users_1_day | List[Optional[UInt64]] | Array of the number of users who have been active in the last day.<br>
active_shared_folders_28_day | List[Optional[UInt64]] | Array of the number of shared folders with some activity in the last 28 days.<br>
active_shared_folders_7_day | List[Optional[UInt64]] | Array of the number of shared folders with some activity in the last week.<br>
active_shared_folders_1_day | List[Optional[UInt64]] | Array of the number of shared folders with some activity in the last day.<br>
shared_links_created | List[Optional[UInt64]] | Array of the number of shared links created.<br>
shared_links_viewed_by_team | List[Optional[UInt64]] | Array of the number of views by team users to shared links created by the team.<br>
shared_links_viewed_by_outside_user | List[Optional[UInt64]] | Array of the number of views by users outside of the team to shared links created by the team.<br>
shared_links_viewed_by_not_logged_in | List[Optional[UInt64]] | Array of the number of views by non-logged-in users to shared links created by the team.<br>
shared_links_viewed_total | List[Optional[UInt64]] | Array of the total number of views to shared links created by the team.<br>
### Error Values
[DateRangeError](#data-types-daterangeerror)

Errors that can originate from problems in input arguments to reports.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## reports/get_devices
### Description
Retrieves reporting data about a team's linked devices.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
[DateRange](#data-types-daterange)

Input arguments that can be provided for most reports.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | Optional[Timestamp] | Optional starting date (inclusive). If start_date is None or too long ago, this field will  be set to 6 months ago.<br>
end_date | Optional[Timestamp] | Optional ending date (exclusive).<br>
### Return Values
[GetDevicesReport](#data-types-getdevicesreport)

Devices Report Result. Contains subsections for different time ranges of activity. Each of the items in each subsection of the storage report is an array of values, one value per day. If there is no data for a day, then the value will be None.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | String | First date present in the results as 'YYYY-MM-DD' or None.<br>
active_1_day | [DevicesActive](#data-types-devicesactive) | Report of the number of devices active in the last day.<br>
active_7_day | [DevicesActive](#data-types-devicesactive) | Report of the number of devices active in the last 7 days.<br>
active_28_day | [DevicesActive](#data-types-devicesactive) | Report of the number of devices active in the last 28 days.<br>
### Error Values
[DateRangeError](#data-types-daterangeerror)

Errors that can originate from problems in input arguments to reports.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## reports/get_membership
### Description
Retrieves reporting data about a team's membership.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
[DateRange](#data-types-daterange)

Input arguments that can be provided for most reports.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | Optional[Timestamp] | Optional starting date (inclusive). If start_date is None or too long ago, this field will  be set to 6 months ago.<br>
end_date | Optional[Timestamp] | Optional ending date (exclusive).<br>
### Return Values
[GetMembershipReport](#data-types-getmembershipreport)

Membership Report Result. Each of the items in the storage report is an array of values, one value per day. If there is no data for a day, then the value will be None.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | String | First date present in the results as 'YYYY-MM-DD' or None.<br>
team_size | List[Optional[UInt64]] | Team size, for each day.<br>
pending_invites | List[Optional[UInt64]] | The number of pending invites to the team, for each day.<br>
members_joined | List[Optional[UInt64]] | The number of members that joined the team, for each day.<br>
suspended_members | List[Optional[UInt64]] | The number of suspended team members, for each day.<br>
licenses | List[Optional[UInt64]] | The total number of licenses the team has, for each day.<br>
### Error Values
[DateRangeError](#data-types-daterangeerror)

Errors that can originate from problems in input arguments to reports.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## reports/get_storage
### Description
Retrieves reporting data about a team's storage usage.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
[DateRange](#data-types-daterange)

Input arguments that can be provided for most reports.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | Optional[Timestamp] | Optional starting date (inclusive). If start_date is None or too long ago, this field will  be set to 6 months ago.<br>
end_date | Optional[Timestamp] | Optional ending date (exclusive).<br>
### Return Values
[GetStorageReport](#data-types-getstoragereport)

Storage Report Result. Each of the items in the storage report is an array of values, one value per day. If there is no data for a day, then the value will be None.

Field Name | Data Type | Description
--------- | ------- | -----------
start_date | String | First date present in the results as 'YYYY-MM-DD' or None.<br>
total_usage | List[Optional[UInt64]] | Sum of the shared, unshared, and datastore usages, for each day.<br>
shared_usage | List[Optional[UInt64]] | Array of the combined size (bytes) of team members' shared folders, for each day.<br>
unshared_usage | List[Optional[UInt64]] | Array of the combined size (bytes) of team members' root namespaces, for each day.<br>
shared_folders | List[Optional[UInt64]] | Array of the number of shared folders owned by team members, for each day.<br>
member_storage_map | List[List[[StorageBucket](#data-types-storagebucket)]] | Array of storage summaries of team members' account sizes. Each storage summary is an array of key, value pairs, where each pair describes a storage bucket. The key indicates the upper bound of the bucket and the value is the number of users in that bucket. There is one such summary per day. If there is no data for a day, the storage summary will be empty.<br>
### Error Values
[DateRangeError](#data-types-daterangeerror)

Errors that can originate from problems in input arguments to reports.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
other | Void | 
## team_folder/activate
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/activate \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_folder_id\": \"123456789\"}"
```

> The above command returns JSON structured like this:

```json
{
    "team_folder_id": "123456789", 
    "name": "Marketing", 
    "status": {
        ".tag": "active"
    }, 
    "is_team_shared_dropbox": false, 
    "sync_setting": {
        ".tag": "default"
    }, 
    "content_sync_settings": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "sync_setting": {
                ".tag": "default"
            }
        }
    ]
}
```

### Description
Sets an archived team folder's status to active.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderIdArg](#data-types-teamfolderidarg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
### Return Values
[TeamFolderMetadata](#data-types-teamfoldermetadata)

Properties of a team folder.

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
name | String | The name of the team folder.<br>
status | [TeamFolderStatus](#data-types-teamfolderstatus) | The status of the team folder.<br>
is_team_shared_dropbox | Boolean | True if this team folder is a shared team root.<br>
sync_setting | [SyncSetting](#data-types-syncsetting) | The sync setting applied to this team folder.<br>
content_sync_settings | List[[ContentSyncSetting](#data-types-contentsyncsetting)] | Sync settings applied to contents of this team folder.<br>
### Error Values
[TeamFolderActivateError](#data-types-teamfolderactivateerror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [TeamFolderAccessError](#data-types-teamfolderaccesserror) | 
status_error | [TeamFolderInvalidStatusError](#data-types-teamfolderinvalidstatuserror) | 
team_shared_dropbox_error | [TeamFolderTeamSharedDropboxError](#data-types-teamfolderteamshareddropboxerror) | 
other | Void | 
## team_folder/archive
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/archive \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_folder_id\": \"123456789\",\"force_async_off\": false}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "team_folder_id": "123456789", 
    "name": "Marketing", 
    "status": {
        ".tag": "active"
    }, 
    "is_team_shared_dropbox": false, 
    "sync_setting": {
        ".tag": "default"
    }, 
    "content_sync_settings": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "sync_setting": {
                ".tag": "default"
            }
        }
    ]
}
```

### Description
Sets an active team folder's status to archived and removes all folder and file members.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderArchiveArg](#data-types-teamfolderarchivearg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
force_async_off | Boolean | Whether to force the archive to happen synchronously.<br>
### Return Values
[TeamFolderArchiveLaunch](#data-types-teamfolderarchivelaunch)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | This response indicates that the processing is asynchronous. The string is an id that can be used to obtain the status of the asynchronous job.<br>
complete | [TeamFolderMetadata](#data-types-teamfoldermetadata) | 
### Error Values
[TeamFolderArchiveError](#data-types-teamfolderarchiveerror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [TeamFolderAccessError](#data-types-teamfolderaccesserror) | 
status_error | [TeamFolderInvalidStatusError](#data-types-teamfolderinvalidstatuserror) | 
team_shared_dropbox_error | [TeamFolderTeamSharedDropboxError](#data-types-teamfolderteamshareddropboxerror) | 
other | Void | 
## team_folder/archive/check
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/archive/check \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"async_job_id\": \"34g93hh34h04y384084\"}"
```

> The above command returns JSON structured like this:

```json
{
    ".tag": "complete", 
    "team_folder_id": "123456789", 
    "name": "Marketing", 
    "status": {
        ".tag": "active"
    }, 
    "is_team_shared_dropbox": false, 
    "sync_setting": {
        ".tag": "default"
    }, 
    "content_sync_settings": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "sync_setting": {
                ".tag": "default"
            }
        }
    ]
}
```

### Description
Returns the status of an asynchronous job for archiving a team folder.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[PollArg](#data-types-pollarg)

Arguments for methods that poll the status of an asynchronous job.

Field Name | Data Type | Description
--------- | ------- | -----------
async_job_id | String | Id of the asynchronous job. This is the value of a response returned from the method that launched the job.<br>
### Return Values
[TeamFolderArchiveJobStatus](#data-types-teamfolderarchivejobstatus)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
in_progress | Void | The asynchronous job is still in progress.<br>
complete | [TeamFolderMetadata](#data-types-teamfoldermetadata) | The archive job has finished. The value is the metadata for the resulting team folder.<br>
failed | [TeamFolderArchiveError](#data-types-teamfolderarchiveerror) | Error occurred while performing an asynchronous job from [team/team_folder/archive](#team-team_folder-archive).<br>
### Error Values
[PollError](#data-types-pollerror)

Error returned by methods for polling the status of asynchronous job.

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_async_job_id | Void | The job ID is invalid.<br>
internal_error | Void | Something went wrong with the job on Dropbox's end. You'll need to verify that the action you were taking succeeded, and if not, try again. This should happen very rarely.<br>
other | Void | 
## team_folder/create
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/create \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"name\": \"Marketing\",\"sync_setting\": \"not_synced\"}"
```

> The above command returns JSON structured like this:

```json
{
    "team_folder_id": "123456789", 
    "name": "Marketing", 
    "status": {
        ".tag": "active"
    }, 
    "is_team_shared_dropbox": false, 
    "sync_setting": {
        ".tag": "default"
    }, 
    "content_sync_settings": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "sync_setting": {
                ".tag": "default"
            }
        }
    ]
}
```

### Description
Creates a new, active, team folder with no members.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderCreateArg](#data-types-teamfoldercreatearg)

Field Name | Data Type | Description
--------- | ------- | -----------
name | String | Name for the new team folder.<br>
sync_setting | Optional[[SyncSettingArg](#data-types-syncsettingarg)] | The sync setting to apply to this team folder. Only permitted if the team has team selective sync enabled.<br>
### Return Values
[TeamFolderMetadata](#data-types-teamfoldermetadata)

Properties of a team folder.

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
name | String | The name of the team folder.<br>
status | [TeamFolderStatus](#data-types-teamfolderstatus) | The status of the team folder.<br>
is_team_shared_dropbox | Boolean | True if this team folder is a shared team root.<br>
sync_setting | [SyncSetting](#data-types-syncsetting) | The sync setting applied to this team folder.<br>
content_sync_settings | List[[ContentSyncSetting](#data-types-contentsyncsetting)] | Sync settings applied to contents of this team folder.<br>
### Error Values
[TeamFolderCreateError](#data-types-teamfoldercreateerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_folder_name | Void | The provided name cannot be used.<br>
folder_name_already_used | Void | There is already a team folder with the provided name.<br>
folder_name_reserved | Void | The provided name cannot be used because it is reserved.<br>
sync_settings_error | [SyncSettingsError](#data-types-syncsettingserror) | An error occurred setting the sync settings.<br>
other | Void | 
## team_folder/get_info
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/get_info \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_folder_ids\": [\"947182\",\"5819424\",\"852307532\"]}"
```

### Description
Retrieves metadata for team folders.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderIdListArg](#data-types-teamfolderidlistarg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_ids | List[String] | The list of team folder IDs.<br>
### Return Values
List[[TeamFolderGetInfoItem](#data-types-teamfoldergetinfoitem)]
### Error Values
Void
## team_folder/list
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/list \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 100}"
```

> The above command returns JSON structured like this:

```json
{
    "team_folders": [
        {
            "team_folder_id": "123456789", 
            "name": "Marketing", 
            "status": {
                ".tag": "active"
            }, 
            "is_team_shared_dropbox": false, 
            "sync_setting": {
                ".tag": "default"
            }, 
            "content_sync_settings": [
                {
                    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                    "sync_setting": {
                        ".tag": "default"
                    }
                }
            ]
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Lists all team folders.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderListArg](#data-types-teamfolderlistarg)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | The maximum number of results to return per request.<br>
### Return Values
[TeamFolderListResult](#data-types-teamfolderlistresult)

Result for [team/team_folder/list](#team-team_folder-list) and [team/team_folder/list/continue](#team-team_folder-list-continue).

Field Name | Data Type | Description
--------- | ------- | -----------
team_folders | List[[TeamFolderMetadata](#data-types-teamfoldermetadata)] | List of all team folders in the authenticated team.<br>
cursor | String | Pass the cursor into [team/team_folder/list/continue](#team-team_folder-list-continue) to obtain additional team folders.<br>
has_more | Boolean | Is true if there are additional team folders that have not been returned yet. An additional call to [team/team_folder/list/continue](#team-team_folder-list-continue) can retrieve them.<br>
### Error Values
[TeamFolderListError](#data-types-teamfolderlisterror)

Field Name | Data Type | Description
--------- | ------- | -----------
access_error | [TeamFolderAccessError](#data-types-teamfolderaccesserror) | 
## team_folder/list/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/list/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "team_folders": [
        {
            "team_folder_id": "123456789", 
            "name": "Marketing", 
            "status": {
                ".tag": "active"
            }, 
            "is_team_shared_dropbox": false, 
            "sync_setting": {
                ".tag": "default"
            }, 
            "content_sync_settings": [
                {
                    "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
                    "sync_setting": {
                        ".tag": "default"
                    }
                }
            ]
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from team_folder/list, use this to paginate through all team folders.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderListContinueArg](#data-types-teamfolderlistcontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of team folders.<br>
### Return Values
[TeamFolderListResult](#data-types-teamfolderlistresult)

Result for [team/team_folder/list](#team-team_folder-list) and [team/team_folder/list/continue](#team-team_folder-list-continue).

Field Name | Data Type | Description
--------- | ------- | -----------
team_folders | List[[TeamFolderMetadata](#data-types-teamfoldermetadata)] | List of all team folders in the authenticated team.<br>
cursor | String | Pass the cursor into [team/team_folder/list/continue](#team-team_folder-list-continue) to obtain additional team folders.<br>
has_more | Boolean | Is true if there are additional team folders that have not been returned yet. An additional call to [team/team_folder/list/continue](#team-team_folder-list-continue) can retrieve them.<br>
### Error Values
[TeamFolderListContinueError](#data-types-teamfolderlistcontinueerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
invalid_cursor | Void | The cursor is invalid.<br>
other | Void | 
## team_folder/permanently_delete
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/permanently_delete \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_folder_id\": \"123456789\"}"
```

### Description
Permanently deletes an archived team folder.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderIdArg](#data-types-teamfolderidarg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
### Return Values
Void
### Error Values
[TeamFolderPermanentlyDeleteError](#data-types-teamfolderpermanentlydeleteerror)



The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [TeamFolderAccessError](#data-types-teamfolderaccesserror) | 
status_error | [TeamFolderInvalidStatusError](#data-types-teamfolderinvalidstatuserror) | 
team_shared_dropbox_error | [TeamFolderTeamSharedDropboxError](#data-types-teamfolderteamshareddropboxerror) | 
other | Void | 
## team_folder/rename
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/rename \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_folder_id\": \"123456789\",\"name\": \"Sales\"}"
```

> The above command returns JSON structured like this:

```json
{
    "team_folder_id": "123456789", 
    "name": "Marketing", 
    "status": {
        ".tag": "active"
    }, 
    "is_team_shared_dropbox": false, 
    "sync_setting": {
        ".tag": "default"
    }, 
    "content_sync_settings": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "sync_setting": {
                ".tag": "default"
            }
        }
    ]
}
```

### Description
Changes an active team folder's name.
Permission : Team member file access.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderRenameArg](#data-types-teamfolderrenamearg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
name | String | New team folder name.<br>
### Return Values
[TeamFolderMetadata](#data-types-teamfoldermetadata)

Properties of a team folder.

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
name | String | The name of the team folder.<br>
status | [TeamFolderStatus](#data-types-teamfolderstatus) | The status of the team folder.<br>
is_team_shared_dropbox | Boolean | True if this team folder is a shared team root.<br>
sync_setting | [SyncSetting](#data-types-syncsetting) | The sync setting applied to this team folder.<br>
content_sync_settings | List[[ContentSyncSetting](#data-types-contentsyncsetting)] | Sync settings applied to contents of this team folder.<br>
### Error Values
[TeamFolderRenameError](#data-types-teamfolderrenameerror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [TeamFolderAccessError](#data-types-teamfolderaccesserror) | 
status_error | [TeamFolderInvalidStatusError](#data-types-teamfolderinvalidstatuserror) | 
team_shared_dropbox_error | [TeamFolderTeamSharedDropboxError](#data-types-teamfolderteamshareddropboxerror) | 
other | Void | 
invalid_folder_name | Void | The provided folder name cannot be used.<br>
folder_name_already_used | Void | There is already a team folder with the same name.<br>
folder_name_reserved | Void | The provided name cannot be used because it is reserved.<br>
## team_folder/update_sync_settings
```shell
curl -X POST https://api.dropboxapi.com/2/team/team_folder/update_sync_settings \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"team_folder_id\": \"123456789\",\"sync_setting\": \"not_synced\",\"content_sync_settings\": [{\"id\": \"id:a4ayc_80_OEAAAAAAAAAXw\",\"sync_setting\": \"not_synced\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "team_folder_id": "123456789", 
    "name": "Marketing", 
    "status": {
        ".tag": "active"
    }, 
    "is_team_shared_dropbox": false, 
    "sync_setting": {
        ".tag": "default"
    }, 
    "content_sync_settings": [
        {
            "id": "id:a4ayc_80_OEAAAAAAAAAXw", 
            "sync_setting": {
                ".tag": "default"
            }
        }
    ]
}
```

### Description
Updates the sync settings on a team folder or its contents.  Use of this endpoint requires that the team has team selective sync enabled.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_data.team_space
### Query Parameters
[TeamFolderUpdateSyncSettingsArg](#data-types-teamfolderupdatesyncsettingsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
sync_setting | Optional[[SyncSettingArg](#data-types-syncsettingarg)] | Sync setting to apply to the team folder itself. Only meaningful if the team folder is not a shared team root.<br>
content_sync_settings | Optional[List[[ContentSyncSettingArg](#data-types-contentsyncsettingarg)]] | Sync settings to apply to contents of this team folder.<br>
### Return Values
[TeamFolderMetadata](#data-types-teamfoldermetadata)

Properties of a team folder.

Field Name | Data Type | Description
--------- | ------- | -----------
team_folder_id | String | The ID of the team folder.<br>
name | String | The name of the team folder.<br>
status | [TeamFolderStatus](#data-types-teamfolderstatus) | The status of the team folder.<br>
is_team_shared_dropbox | Boolean | True if this team folder is a shared team root.<br>
sync_setting | [SyncSetting](#data-types-syncsetting) | The sync setting applied to this team folder.<br>
content_sync_settings | List[[ContentSyncSetting](#data-types-contentsyncsetting)] | Sync settings applied to contents of this team folder.<br>
### Error Values
[TeamFolderUpdateSyncSettingsError](#data-types-teamfolderupdatesyncsettingserror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
access_error | [TeamFolderAccessError](#data-types-teamfolderaccesserror) | 
status_error | [TeamFolderInvalidStatusError](#data-types-teamfolderinvalidstatuserror) | 
team_shared_dropbox_error | [TeamFolderTeamSharedDropboxError](#data-types-teamfolderteamshareddropboxerror) | 
other | Void | 
sync_settings_error | [SyncSettingsError](#data-types-syncsettingserror) | An error occurred setting the sync settings.<br>
## token/get_authenticated_admin
```shell
curl -X POST https://api.dropboxapi.com/2/team/token/get_authenticated_admin \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "admin_profile": {
        "team_member_id": "dbmid:FDFSVF-DFSDF", 
        "email": "tami@seagull.com", 
        "email_verified": false, 
        "status": {
            ".tag": "active"
        }, 
        "name": {
            "given_name": "Franz", 
            "surname": "Ferdinand", 
            "familiar_name": "Franz", 
            "display_name": "Franz Ferdinand (Personal)", 
            "abbreviated_name": "FF"
        }, 
        "membership_type": {
            ".tag": "full"
        }, 
        "groups": [
            "g:e2db7665347abcd600000000001a2b3c"
        ], 
        "member_folder_id": "20", 
        "external_id": "244423", 
        "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
        "secondary_emails": [
            {
                "email": "grape@strawberry.com", 
                "is_verified": false
            }, 
            {
                "email": "apple@orange.com", 
                "is_verified": true
            }
        ], 
        "joined_on": "2015-05-12T15:50:38Z", 
        "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
    }
}
```

### Description
Returns the member profile of the admin who generated the team access token used to make the call.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
team_info.read
### Query Parameters
Void
### Return Values
[TokenGetAuthenticatedAdminResult](#data-types-tokengetauthenticatedadminresult)

Results for [team/token/get_authenticated_admin](#team-token-get_authenticated_admin).

Field Name | Data Type | Description
--------- | ------- | -----------
admin_profile | [TeamMemberProfile](#data-types-teammemberprofile) | The admin who authorized the token.<br>
### Error Values
[TokenGetAuthenticatedAdminError](#data-types-tokengetauthenticatedadminerror)

Error returned by [team/token/get_authenticated_admin](#team-token-get_authenticated_admin).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
mapping_not_found | Void | The current token is not associated with a team admin, because mappings were not recorded when the token was created. Consider re-authorizing a new access token to record its authenticating admin.<br>
admin_not_active | Void | Either the team admin that authorized this token is no longer an active member of the team or no longer a team admin.<br>
other | Void | 
# Team_log
## get_events
```shell
curl -X POST https://api.dropboxapi.com/2/team_log/get_events \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"limit\": 50,\"category\": \"groups\",\"event_type\": \"login_success\"}"
```

> The above command returns JSON structured like this:

```json
{
    "events": [
        {
            "timestamp": "2017-01-25T15:51:30Z", 
            "event_category": {
                ".tag": "tfa"
            }, 
            "event_type": {
                ".tag": "shared_content_download", 
                "description": "(sharing) Downloaded shared file/folder"
            }, 
            "details": {
                ".tag": "shared_content_download_details", 
                "shared_content_link": "abc", 
                "shared_content_access_level": {
                    ".tag": "viewer_no_comment"
                }, 
                "shared_content_owner": {
                    ".tag": "team_member", 
                    "account_id": "dbid:AAHgR8xsQP48a5DQUGPo-Vxsrjd0OByVmho", 
                    "display_name": "John Smith", 
                    "email": "john_smith@acmecorp.com", 
                    "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                    "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1224", 
                    "team": {
                        "display_name": "A Team"
                    }
                }
            }, 
            "actor": {
                ".tag": "user", 
                "user": {
                    ".tag": "team_member", 
                    "account_id": "dbid:AAHgR8xsQP48a5DQUGPo-Vxsrjd0OByVmho", 
                    "display_name": "John Smith", 
                    "email": "john_smith@acmecorp.com", 
                    "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                    "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1224", 
                    "team": {
                        "display_name": "A Team"
                    }
                }
            }, 
            "origin": {
                "access_method": {
                    ".tag": "end_user", 
                    "end_user": {
                        ".tag": "web", 
                        "session_id": "dbwsid:123456789012345678901234567890123456789"
                    }
                }, 
                "geo_location": {
                    "ip_address": "45.56.78.100", 
                    "city": "San Francisco", 
                    "region": "California", 
                    "country": "US"
                }
            }, 
            "involve_non_team_member": true, 
            "context": {
                ".tag": "team_member", 
                "account_id": "dbid:AAHgR8xsQP48a5DQUGPo-Vxsrjd0OByVmho", 
                "display_name": "John Smith", 
                "email": "john_smith@acmecorp.com", 
                "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1224", 
                "team": {
                    "display_name": "A Team"
                }
            }, 
            "participants": [
                {
                    ".tag": "user", 
                    "user": {
                        ".tag": "team_member", 
                        "account_id": "dbid:AAGx4oiLtHdvRdNxUpvvJBXYgR4BS19c9kw", 
                        "display_name": "Jane Smith", 
                        "email": "jane_smith@acmecorp.com", 
                        "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                        "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1225", 
                        "team": {
                            "display_name": "A Team"
                        }
                    }
                }
            ], 
            "assets": [
                {
                    ".tag": "file", 
                    "path": {
                        "namespace_relative": {
                            "ns_id": "1234", 
                            "relative_path": "/Contract Work/Draft", 
                            "is_shared_namespace": false
                        }, 
                        "contextual": "/Contract Work/Draft"
                    }, 
                    "display_name": "reports.xls", 
                    "file_id": "id:jQKLsZFQImAAAAAAEZAAQt", 
                    "file_size": 4
                }
            ]
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Retrieves team events. If the result's [GetTeamEventsResult.has_more](#data-types-getteameventsresult) field is true, call get_events/continue with the returned cursor to retrieve more entries. If end_time is not specified in your request, you may use the returned cursor to poll get_events/continue for new events.
Many attributes note 'may be missing due to historical data gap'.
Note that the file_operations category and & analogous paper events are not available on all Dropbox Business [plans](/business/plans-comparison). Use [features/get_values](/developers/documentation/http/teams#team-features-get_values) to check for this feature.
Permission : Team Auditing.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
events.read
### Query Parameters
[GetTeamEventsArg](#data-types-getteameventsarg)

Field Name | Data Type | Description
--------- | ------- | -----------
limit | UInt32 | The maximal number of results to return per call. Note that some calls may not return [limit](#data-types-getteameventsarg) number of events, and may even return no events, even with `has_more` set to true. In this case, callers should fetch again using [team_log/get_events/continue](#team_log-get_events-continue).<br>
account_id | Optional[String] | Filter the events by account ID. Return only events with this account_id as either Actor, Context, or Participants.<br>
time | Optional[[TimeRange](#data-types-timerange)] | Filter by time range.<br>
category | Optional[[EventCategory](#data-types-eventcategory)] | Filter the returned events to a single category.<br>
event_type | Optional[[EventTypeArg](#data-types-eventtypearg)] | Filter the returned events to a single event type. Note that event_type shouldn't be provided together with category.<br>
### Return Values
[GetTeamEventsResult](#data-types-getteameventsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
events | List[[TeamEvent](#data-types-teamevent)] | List of events. Note that events are not guaranteed to be sorted by their timestamp value.<br>
cursor | String | Pass the cursor into [team_log/get_events/continue](#team_log-get_events-continue) to obtain additional events.<br>The value of [cursor](#data-types-getteameventsresult) may change for each response from [team_log/get_events/continue](#team_log-get_events-continue), regardless of the value of [has_more](#data-types-getteameventsresult); older cursor strings may expire.<br>Thus, callers should ensure that they update their cursor based on the latest value of [cursor](#data-types-getteameventsresult) after each call, and poll regularly if they wish to poll for new events.<br>Callers should handle reset exceptions for expired cursors.<br>
has_more | Boolean | Is true if there may be additional events that have not been returned yet. An additional call to [team_log/get_events/continue](#team_log-get_events-continue) can retrieve them. Note that [has_more](#data-types-getteameventsresult) may be true, even if [events](#data-types-getteameventsresult) is empty.<br>
### Error Values
[GetTeamEventsError](#data-types-getteameventserror)

Errors that can be raised when calling [team_log/get_events](#team_log-get_events).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
account_id_not_found | Void | No user found matching the provided account_id.<br>
invalid_time_range | Void | Invalid time range.<br>
invalid_filters | Void | Invalid filters. event_type and category should not be provided together.<br>
other | Void | 
## get_events/continue
```shell
curl -X POST https://api.dropboxapi.com/2/team_log/get_events/continue \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"cursor\": \"ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu\"}"
```

> The above command returns JSON structured like this:

```json
{
    "events": [
        {
            "timestamp": "2017-01-25T15:51:30Z", 
            "event_category": {
                ".tag": "tfa"
            }, 
            "event_type": {
                ".tag": "shared_content_download", 
                "description": "(sharing) Downloaded shared file/folder"
            }, 
            "details": {
                ".tag": "shared_content_download_details", 
                "shared_content_link": "abc", 
                "shared_content_access_level": {
                    ".tag": "viewer_no_comment"
                }, 
                "shared_content_owner": {
                    ".tag": "team_member", 
                    "account_id": "dbid:AAHgR8xsQP48a5DQUGPo-Vxsrjd0OByVmho", 
                    "display_name": "John Smith", 
                    "email": "john_smith@acmecorp.com", 
                    "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                    "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1224", 
                    "team": {
                        "display_name": "A Team"
                    }
                }
            }, 
            "actor": {
                ".tag": "user", 
                "user": {
                    ".tag": "team_member", 
                    "account_id": "dbid:AAHgR8xsQP48a5DQUGPo-Vxsrjd0OByVmho", 
                    "display_name": "John Smith", 
                    "email": "john_smith@acmecorp.com", 
                    "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                    "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1224", 
                    "team": {
                        "display_name": "A Team"
                    }
                }
            }, 
            "origin": {
                "access_method": {
                    ".tag": "end_user", 
                    "end_user": {
                        ".tag": "web", 
                        "session_id": "dbwsid:123456789012345678901234567890123456789"
                    }
                }, 
                "geo_location": {
                    "ip_address": "45.56.78.100", 
                    "city": "San Francisco", 
                    "region": "California", 
                    "country": "US"
                }
            }, 
            "involve_non_team_member": true, 
            "context": {
                ".tag": "team_member", 
                "account_id": "dbid:AAHgR8xsQP48a5DQUGPo-Vxsrjd0OByVmho", 
                "display_name": "John Smith", 
                "email": "john_smith@acmecorp.com", 
                "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1224", 
                "team": {
                    "display_name": "A Team"
                }
            }, 
            "participants": [
                {
                    ".tag": "user", 
                    "user": {
                        ".tag": "team_member", 
                        "account_id": "dbid:AAGx4oiLtHdvRdNxUpvvJBXYgR4BS19c9kw", 
                        "display_name": "Jane Smith", 
                        "email": "jane_smith@acmecorp.com", 
                        "team_member_id": "dbmid:AAFoi-tmvRuQR0jU-3fN4B-9nZo6nHcDO9Q", 
                        "member_external_id": "ADSYNC S-1-5-21-1004296348-1135238915-682003432-1225", 
                        "team": {
                            "display_name": "A Team"
                        }
                    }
                }
            ], 
            "assets": [
                {
                    ".tag": "file", 
                    "path": {
                        "namespace_relative": {
                            "ns_id": "1234", 
                            "relative_path": "/Contract Work/Draft", 
                            "is_shared_namespace": false
                        }, 
                        "contextual": "/Contract Work/Draft"
                    }, 
                    "display_name": "reports.xls", 
                    "file_id": "id:jQKLsZFQImAAAAAAEZAAQt", 
                    "file_size": 4
                }
            ]
        }
    ], 
    "cursor": "ZtkX9_EHj3x7PMkVuFIhwKYXEpwpLwyxp9vMKomUhllil9q7eWiAu", 
    "has_more": false
}
```

### Description
Once a cursor has been retrieved from get_events, use this to paginate through all events.
Permission : Team Auditing.
### Authentication
Team Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
events.read
### Query Parameters
[GetTeamEventsContinueArg](#data-types-getteameventscontinuearg)

Field Name | Data Type | Description
--------- | ------- | -----------
cursor | String | Indicates from what point to get the next set of events.<br>
### Return Values
[GetTeamEventsResult](#data-types-getteameventsresult)

Field Name | Data Type | Description
--------- | ------- | -----------
events | List[[TeamEvent](#data-types-teamevent)] | List of events. Note that events are not guaranteed to be sorted by their timestamp value.<br>
cursor | String | Pass the cursor into [team_log/get_events/continue](#team_log-get_events-continue) to obtain additional events.<br>The value of [cursor](#data-types-getteameventsresult) may change for each response from [team_log/get_events/continue](#team_log-get_events-continue), regardless of the value of [has_more](#data-types-getteameventsresult); older cursor strings may expire.<br>Thus, callers should ensure that they update their cursor based on the latest value of [cursor](#data-types-getteameventsresult) after each call, and poll regularly if they wish to poll for new events.<br>Callers should handle reset exceptions for expired cursors.<br>
has_more | Boolean | Is true if there may be additional events that have not been returned yet. An additional call to [team_log/get_events/continue](#team_log-get_events-continue) can retrieve them. Note that [has_more](#data-types-getteameventsresult) may be true, even if [events](#data-types-getteameventsresult) is empty.<br>
### Error Values
[GetTeamEventsContinueError](#data-types-getteameventscontinueerror)

Errors that can be raised when calling [team_log/get_events/continue](#team_log-get_events-continue).

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
bad_cursor | Void | Bad cursor.<br>
reset | Timestamp | Cursors are intended to be used quickly. Individual cursor values are normally valid for days, but in rare cases may be reset sooner.<br>Cursor reset errors should be handled by fetching a new cursor from [team_log/get_events](#team_log-get_events).<br>The associated value is the approximate timestamp of the most recent event returned by the cursor. This should be used as a resumption point when calling [team_log/get_events](#team_log-get_events) to obtain a new cursor.<br>
other | Void | 
# Users
## features/get_values
```shell
curl -X POST https://api.dropboxapi.com/2/users/features/get_values \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"features\": [{\".tag\": \"paper_as_files\"},{\".tag\": \"file_locking\"}]}"
```

> The above command returns JSON structured like this:

```json
{
    "values": [
        {
            ".tag": "paper_as_files", 
            "paper_as_files": {
                ".tag": "enabled", 
                "enabled": true
            }
        }
    ]
}
```

### Description
Get a list of feature values that may be configured for the current account.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
account_info.read
### Query Parameters
[UserFeaturesGetValuesBatchArg](#data-types-userfeaturesgetvaluesbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
features | List[[UserFeature](#data-types-userfeature)] | A list of features in [UserFeature](#data-types-userfeature). If the list is empty, this route will return [UserFeaturesGetValuesBatchError](#data-types-userfeaturesgetvaluesbatcherror).<br>
### Return Values
[UserFeaturesGetValuesBatchResult](#data-types-userfeaturesgetvaluesbatchresult)

Field Name | Data Type | Description
--------- | ------- | -----------
values | List[[UserFeatureValue](#data-types-userfeaturevalue)] | 
### Error Values
[UserFeaturesGetValuesBatchError](#data-types-userfeaturesgetvaluesbatcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
empty_features_list | Void | At least one [UserFeature](#data-types-userfeature) must be included in the [UserFeaturesGetValuesBatchArg](#data-types-userfeaturesgetvaluesbatcharg).features list.<br>
other | Void | 
## get_account
```shell
curl -X POST https://api.dropboxapi.com/2/users/get_account \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"account_id\": \"dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc\"}"
```

> The above command returns JSON structured like this:

```json
{
    "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
    "name": {
        "given_name": "Franz", 
        "surname": "Ferdinand", 
        "familiar_name": "Franz", 
        "display_name": "Franz Ferdinand (Personal)", 
        "abbreviated_name": "FF"
    }, 
    "email": "franz@dropbox.com", 
    "email_verified": true, 
    "disabled": false, 
    "is_teammate": false, 
    "profile_photo_url": "https://dl-web.dropbox.com/account_photo/get/dbaphid%3AAAHWGmIXV3sUuOmBfTz0wPsiqHUpBWvv3ZA?vers=1556069330102&size=128x128"
}
```

### Description
Get information about a user's account.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[GetAccountArg](#data-types-getaccountarg)

Field Name | Data Type | Description
--------- | ------- | -----------
account_id | String | A user's account identifier.<br>
### Return Values
[BasicAccount](#data-types-basicaccount)

Basic information about any account.

Field Name | Data Type | Description
--------- | ------- | -----------
account_id | String | The user's unique Dropbox ID.<br>
name | [Name](#data-types-name) | Details of a user's name.<br>
email | String | The user's e-mail address. Do not rely on this without checking the [email_verified](#data-types-basicaccount) field. Even then, it's possible that the user has since lost access to their e-mail.<br>
email_verified | Boolean | Whether the user has verified their e-mail address.<br>
disabled | Boolean | Whether the user has been disabled.<br>
is_teammate | Boolean | Whether this user is a teammate of the current user. If this account is the current user's account, then this will be true.<br>
profile_photo_url | Optional[String] | URL for the photo representing the user, if one is set.<br>
team_member_id | Optional[String] | The user's unique team member id. This field will only be present if the user is part of a team and [is_teammate](#data-types-basicaccount) is true.<br>
### Error Values
[GetAccountError](#data-types-getaccounterror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
no_account | Void | The specified [GetAccountArg.account_id](#data-types-getaccountarg) does not exist.<br>
other | Void | 
## get_account_batch
```shell
curl -X POST https://api.dropboxapi.com/2/users/get_account_batch \
    --header "Authorization: Bearer [access_token]" \
    --header "Content-Type: application/json" \
    --data "{\"account_ids\": [\"dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc\",\"dbid:AAH1Vcz-DVoRDeixtr_OA8oUGgiqhs4XPOQ\"]}"
```

### Description
Get information about multiple user accounts.  At most 300 accounts may be queried per request.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
sharing.read
### Query Parameters
[GetAccountBatchArg](#data-types-getaccountbatcharg)

Field Name | Data Type | Description
--------- | ------- | -----------
account_ids | List[String] | List of user account identifiers.  Should not contain any duplicate account IDs.<br>
### Return Values
List[[BasicAccount](#data-types-basicaccount)]
### Error Values
[GetAccountBatchError](#data-types-getaccountbatcherror)

The value will be one of the following datatypes.

Tag Name | Data Type | Description
--------- | ------- | -----------
no_account | String | The value is an account ID specified in [GetAccountBatchArg.account_ids](#data-types-getaccountbatcharg) that does not exist.<br>
other | Void | 
## get_current_account
```shell
curl -X POST https://api.dropboxapi.com/2/users/get_current_account \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "account_id": "dbid:AAH4f99T0taONIb-OurWxbNQ6ywGRopQngc", 
    "name": {
        "given_name": "Franz", 
        "surname": "Ferdinand", 
        "familiar_name": "Franz", 
        "display_name": "Franz Ferdinand (Personal)", 
        "abbreviated_name": "FF"
    }, 
    "email": "franz@dropbox.com", 
    "email_verified": true, 
    "disabled": false, 
    "locale": "en", 
    "referral_link": "https://db.tt/ZITNuhtI", 
    "is_paired": true, 
    "account_type": {
        ".tag": "business"
    }, 
    "root_info": {
        ".tag": "user", 
        "root_namespace_id": "3235641", 
        "home_namespace_id": "3235641"
    }, 
    "country": "US", 
    "team": {
        "id": "dbtid:AAFdgehTzw7WlXhZJsbGCLePe8RvQGYDr-I", 
        "name": "Acme, Inc.", 
        "sharing_policies": {
            "shared_folder_member_policy": {
                ".tag": "team"
            }, 
            "shared_folder_join_policy": {
                ".tag": "from_anyone"
            }, 
            "shared_link_create_policy": {
                ".tag": "team_only"
            }
        }, 
        "office_addin_policy": {
            ".tag": "disabled"
        }
    }, 
    "team_member_id": "dbmid:AAHhy7WsR0x-u4ZCqiDl5Fz5zvuL3kmspwU"
}
```

### Description
Get information about the current user's account.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
account_info.read
### Query Parameters
Void
### Return Values
[FullAccount](#data-types-fullaccount)

Detailed information about the current user's account.

Field Name | Data Type | Description
--------- | ------- | -----------
account_id | String | The user's unique Dropbox ID.<br>
name | [Name](#data-types-name) | Details of a user's name.<br>
email | String | The user's e-mail address. Do not rely on this without checking the [email_verified](#data-types-fullaccount) field. Even then, it's possible that the user has since lost access to their e-mail.<br>
email_verified | Boolean | Whether the user has verified their e-mail address.<br>
disabled | Boolean | Whether the user has been disabled.<br>
locale | String | The language that the user specified. Locale tags will be [IETF language tags](http://en.wikipedia.org/wiki/IETF_language_tag).<br>
referral_link | String | The user's [referral link](https://www.dropbox.com/referrals).<br>
is_paired | Boolean | Whether the user has a personal and work account. If the current account is personal, then [team](#data-types-fullaccount) will always be null, but [is_paired](#data-types-fullaccount) will indicate if a work account is linked.<br>
account_type | [AccountType](#data-types-accounttype) | What type of account this user has.<br>
root_info | [RootInfo](#data-types-rootinfo) | The root info for this account.<br>
profile_photo_url | Optional[String] | URL for the photo representing the user, if one is set.<br>
country | Optional[String] | The user's two-letter country code, if available. Country codes are based on [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1).<br>
team | Optional[[FullTeam](#data-types-fullteam)] | If this account is a member of a team, information about that team.<br>
team_member_id | Optional[String] | This account's unique team member id. This field will only be present if [team](#data-types-fullaccount) is present.<br>
### Error Values
Void
## get_space_usage
```shell
curl -X POST https://api.dropboxapi.com/2/users/get_space_usage \
    --header "Authorization: Bearer [access_token]"
```

> The above command returns JSON structured like this:

```json
{
    "used": 314159265, 
    "allocation": {
        ".tag": "individual", 
        "allocated": 10000000000
    }
}
```

### Description
Get the space usage information for the current user's account.
### Authentication
User Authentication
### ENDPOINT FORMAT
RPC
### Required Scope
account_info.read
### Query Parameters
Void
### Return Values
[SpaceUsage](#data-types-spaceusage)

Information about a user's space usage and quota.

Field Name | Data Type | Description
--------- | ------- | -----------
used | UInt64 | The user's total space usage (bytes).<br>
allocation | [SpaceAllocation](#data-types-spaceallocation) | The user's space allocation.<br>
### Error Values
Void
