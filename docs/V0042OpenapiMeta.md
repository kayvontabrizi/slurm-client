# V0042OpenapiMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugin** | [**V0042OpenapiMetaPlugin**](V0042OpenapiMetaPlugin.md) |  | [optional] 
**client** | [**V0042OpenapiMetaClient**](V0042OpenapiMetaClient.md) |  | [optional] 
**command** | **List[str]** |  | [optional] 
**slurm** | [**V0042OpenapiMetaSlurm**](V0042OpenapiMetaSlurm.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0042_openapi_meta import V0042OpenapiMeta

# TODO update the JSON string below
json = "{}"
# create an instance of V0042OpenapiMeta from a JSON string
v0042_openapi_meta_instance = V0042OpenapiMeta.from_json(json)
# print the JSON string representation of the object
print(V0042OpenapiMeta.to_json())

# convert the object into a dict
v0042_openapi_meta_dict = v0042_openapi_meta_instance.to_dict()
# create an instance of V0042OpenapiMeta from a dict
v0042_openapi_meta_from_dict = V0042OpenapiMeta.from_dict(v0042_openapi_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


