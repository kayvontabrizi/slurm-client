# V0041OpenapiJobInfoRespJobsInnerEndTime

End time, real or expected (UNIX timestamp)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_end_time import V0041OpenapiJobInfoRespJobsInnerEndTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiJobInfoRespJobsInnerEndTime from a JSON string
v0041_openapi_job_info_resp_jobs_inner_end_time_instance = V0041OpenapiJobInfoRespJobsInnerEndTime.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiJobInfoRespJobsInnerEndTime.to_json())

# convert the object into a dict
v0041_openapi_job_info_resp_jobs_inner_end_time_dict = v0041_openapi_job_info_resp_jobs_inner_end_time_instance.to_dict()
# create an instance of V0041OpenapiJobInfoRespJobsInnerEndTime from a dict
v0041_openapi_job_info_resp_jobs_inner_end_time_from_dict = V0041OpenapiJobInfoRespJobsInnerEndTime.from_dict(v0041_openapi_job_info_resp_jobs_inner_end_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

