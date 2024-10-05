# V0039MetaSlurm

Slurm information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**V0039MetaSlurmVersion**](V0039MetaSlurmVersion.md) |  | [optional] 
**release** | **str** | version specifier | [optional] 

## Example

```python
from openapi_client.models.v0039_meta_slurm import V0039MetaSlurm

# TODO update the JSON string below
json = "{}"
# create an instance of V0039MetaSlurm from a JSON string
v0039_meta_slurm_instance = V0039MetaSlurm.from_json(json)
# print the JSON string representation of the object
print(V0039MetaSlurm.to_json())

# convert the object into a dict
v0039_meta_slurm_dict = v0039_meta_slurm_instance.to_dict()
# create an instance of V0039MetaSlurm from a dict
v0039_meta_slurm_from_dict = V0039MetaSlurm.from_dict(v0039_meta_slurm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


