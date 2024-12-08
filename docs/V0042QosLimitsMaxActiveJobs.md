# V0042QosLimitsMaxActiveJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accruing** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**count** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0042_qos_limits_max_active_jobs import V0042QosLimitsMaxActiveJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMaxActiveJobs from a JSON string
v0042_qos_limits_max_active_jobs_instance = V0042QosLimitsMaxActiveJobs.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMaxActiveJobs.to_json())

# convert the object into a dict
v0042_qos_limits_max_active_jobs_dict = v0042_qos_limits_max_active_jobs_instance.to_dict()
# create an instance of V0042QosLimitsMaxActiveJobs from a dict
v0042_qos_limits_max_active_jobs_from_dict = V0042QosLimitsMaxActiveJobs.from_dict(v0042_qos_limits_max_active_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


