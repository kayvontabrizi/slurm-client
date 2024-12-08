# V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob

MaxWallDurationPerJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job import V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job_instance = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


