# V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor

UsageFactor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **float** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurm_client.models.v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor import V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor from a JSON string
v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor_instance = V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor_dict = v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor from a dict
v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor_from_dict = V0041OpenapiSlurmdbdConfigRespQosInnerUsageFactor.from_dict(v0041_openapi_slurmdbd_config_resp_qos_inner_usage_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

