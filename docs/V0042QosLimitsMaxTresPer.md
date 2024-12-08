# V0042QosLimitsMaxTresPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**job** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**node** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 
**user** | [**List[V0042Tres]**](V0042Tres.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0042_qos_limits_max_tres_per import V0042QosLimitsMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosLimitsMaxTresPer from a JSON string
v0042_qos_limits_max_tres_per_instance = V0042QosLimitsMaxTresPer.from_json(json)
# print the JSON string representation of the object
print(V0042QosLimitsMaxTresPer.to_json())

# convert the object into a dict
v0042_qos_limits_max_tres_per_dict = v0042_qos_limits_max_tres_per_instance.to_dict()
# create an instance of V0042QosLimitsMaxTresPer from a dict
v0042_qos_limits_max_tres_per_from_dict = V0042QosLimitsMaxTresPer.from_dict(v0042_qos_limits_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


