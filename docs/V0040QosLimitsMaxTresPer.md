# V0040QosLimitsMaxTresPer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**job** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**node** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 
**user** | [**List[V0040Tres]**](V0040Tres.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0040_qos_limits_max_tres_per import V0040QosLimitsMaxTresPer

# TODO update the JSON string below
json = "{}"
# create an instance of V0040QosLimitsMaxTresPer from a JSON string
v0040_qos_limits_max_tres_per_instance = V0040QosLimitsMaxTresPer.from_json(json)
# print the JSON string representation of the object
print(V0040QosLimitsMaxTresPer.to_json())

# convert the object into a dict
v0040_qos_limits_max_tres_per_dict = v0040_qos_limits_max_tres_per_instance.to_dict()
# create an instance of V0040QosLimitsMaxTresPer from a dict
v0040_qos_limits_max_tres_per_from_dict = V0040QosLimitsMaxTresPer.from_dict(v0040_qos_limits_max_tres_per_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

