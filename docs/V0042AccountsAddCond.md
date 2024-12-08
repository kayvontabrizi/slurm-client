# V0042AccountsAddCond


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **List[str]** |  | 
**association** | [**V0042AssocRecSet**](V0042AssocRecSet.md) |  | [optional] 
**clusters** | **List[str]** |  | [optional] 

## Example

```python
from slurm_client.models.v0042_accounts_add_cond import V0042AccountsAddCond

# TODO update the JSON string below
json = "{}"
# create an instance of V0042AccountsAddCond from a JSON string
v0042_accounts_add_cond_instance = V0042AccountsAddCond.from_json(json)
# print the JSON string representation of the object
print(V0042AccountsAddCond.to_json())

# convert the object into a dict
v0042_accounts_add_cond_dict = v0042_accounts_add_cond_instance.to_dict()
# create an instance of V0042AccountsAddCond from a dict
v0042_accounts_add_cond_from_dict = V0042AccountsAddCond.from_dict(v0042_accounts_add_cond_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


