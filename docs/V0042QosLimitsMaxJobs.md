# V0042QosLimitsMaxJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional] 
**active_jobs** | [**V0042QosLimitsMaxJobsActiveJobs**](V0042QosLimitsMaxJobsActiveJobs.md) |  | [optional] 
**per** | [**V0042QosLimitsMaxJobsActiveJobsPer**](V0042QosLimitsMaxJobsActiveJobsPer.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0042_qos_limits_max_jobs import V0042QosLimitsMaxJobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMaxJobs from a JSON string
v0042_qos_limits_max_jobs_instance = V0042QosLimitsMaxJobs.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMaxJobs.to_json())

# convert the object into a dict
v0042_qos_limits_max_jobs_dict = v0042_qos_limits_max_jobs_instance.to_dict()
# create an instance of V0042QosLimitsMaxJobs from a dict
v0042_qos_limits_max_jobs_from_dict = V0042QosLimitsMaxJobs.from_dict(v0042_qos_limits_max_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

