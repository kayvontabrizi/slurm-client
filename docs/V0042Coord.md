# V0042Coord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | User name | 
**direct** | **bool** | Indicates whether the coordinator was directly assigned to this account | [optional] 

## Example

```python
from slurm_client.models.v0042_coord import V0042Coord

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Coord from a JSON string
v0042_coord_instance = V0042Coord.from_json(json)
# print the JSON string representation of the object
print(V0042Coord.to_json())

# convert the object into a dict
v0042_coord_dict = v0042_coord_instance.to_dict()
# create an instance of V0042Coord from a dict
v0042_coord_from_dict = V0042Coord.from_dict(v0042_coord_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

