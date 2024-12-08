# V0042StepTimeSystem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**seconds** | **int** | System CPU time used by the step in seconds | [optional] 
**microseconds** | **int** | System CPU time used by the step in microseconds | [optional] 

## Example

```python
from slurm_client.models.v0042_step_time_system import V0042StepTimeSystem

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StepTimeSystem from a JSON string
v0042_step_time_system_instance = V0042StepTimeSystem.from_json(json)
# print the JSON string representation of the object
print(V0042StepTimeSystem.to_json())

# convert the object into a dict
v0042_step_time_system_dict = v0042_step_time_system_instance.to_dict()
# create an instance of V0042StepTimeSystem from a dict
v0042_step_time_system_from_dict = V0042StepTimeSystem.from_dict(v0042_step_time_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


