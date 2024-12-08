# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount

MaxJobsPerAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxJobsActiveJobsPerAccount.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_jobs_active_jobs_per_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


