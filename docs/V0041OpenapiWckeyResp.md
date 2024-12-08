# V0041OpenapiWckeyResp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wckeys** | [**List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]**](V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.md) | wckeys | 
**meta** | [**V0041OpenapiSharesRespMeta**](V0041OpenapiSharesRespMeta.md) |  | [optional] 
**errors** | [**List[V0041OpenapiSharesRespErrorsInner]**](V0041OpenapiSharesRespErrorsInner.md) | Query errors | [optional] 
**warnings** | [**List[V0041OpenapiSharesRespWarningsInner]**](V0041OpenapiSharesRespWarningsInner.md) | Query warnings | [optional] 

## Example

```python
from slurm_client.models.v0041_openapi_wckey_resp import V0041OpenapiWckeyResp

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiWckeyResp from a JSON string
v0041_openapi_wckey_resp_instance = V0041OpenapiWckeyResp.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiWckeyResp.to_json())

# convert the object into a dict
v0041_openapi_wckey_resp_dict = v0041_openapi_wckey_resp_instance.to_dict()
# create an instance of V0041OpenapiWckeyResp from a dict
v0041_openapi_wckey_resp_from_dict = V0041OpenapiWckeyResp.from_dict(v0041_openapi_wckey_resp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


