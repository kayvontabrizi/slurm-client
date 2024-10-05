# V0039JobsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**V0039Meta**](V0039Meta.md) |  | [optional] 
**errors** | [**List[V0039Error]**](V0039Error.md) | Slurm errors | [optional] 
**warnings** | [**List[V0039Warning]**](V0039Warning.md) | Slurm warnings | [optional] 
**jobs** | [**List[V0039JobInfo]**](V0039JobInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0039_jobs_response import V0039JobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V0039JobsResponse from a JSON string
v0039_jobs_response_instance = V0039JobsResponse.from_json(json)
# print the JSON string representation of the object
print(V0039JobsResponse.to_json())

# convert the object into a dict
v0039_jobs_response_dict = v0039_jobs_response_instance.to_dict()
# create an instance of V0039JobsResponse from a dict
v0039_jobs_response_from_dict = V0039JobsResponse.from_dict(v0039_jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

