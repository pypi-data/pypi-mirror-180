# File upload to AWS S3

This packge can be used to upload file in s3 and get file generated url.

## Steps to use package

1. Install package with `pip install fileUploadS3_x21182787`
2. import package in python and use it

```
>> from fileUploadS3_x21182787 import uploadGenrateUrl

>> uploadGenrateUrl.s3UploadGenURL("b64EncodedData","filename.ext","bucket_name")
```

## Funcation Description

`s3UploadGenURL(b64EncodedData, s3_file, bucket_name)` will take 3 parameters

1. b64EncodedData - Data should be in `base64 encoded` formate.
2. s3_file - File name in which data to be stored eg. abc.jpg, file.doc etc...
3. bucket_name - S3 bucket name file to be store.

## Example

```python
import json
from fileUploadS3_x21182787 import uploadGenerateUrl

response = uploadGenrateUrl.s3UploadGenURL("b64EncodedData","filename.ext","bucket_name")

print(json.loads(response)) # {"img_url": "s3_file_url"}

print(json.loads(response)[img_url]) # will print s3_file_url
```

##### Note:

```
Before using the response convert it to json `json.loads(response)`. because package returing stringified json.
```
