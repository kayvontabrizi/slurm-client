# V0042JobArray


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **int** | Job ID of job array, or 0 if N/A | [optional] 
**limits** | [**V0042JobArrayLimits**](V0042JobArrayLimits.md) |  | [optional] 
**task_id** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**task** | **str** | String expression of task IDs in this record | [optional] 

## Example

```python
from slurm_client.models.v0042_job_array import V0042JobArray

# TODO update the JSON string below
json = "{}"
# create an instance of V0042JobArray from a JSON string
v0042_job_array_instance = V0042JobArray.from_json(json)
# print the JSON string representation of the object
print(V0042JobArray.to_json())

# convert the object into a dict
v0042_job_array_dict = v0042_job_array_instance.to_dict()
# create an instance of V0042JobArray from a dict
v0042_job_array_from_dict = V0042JobArray.from_dict(v0042_job_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


