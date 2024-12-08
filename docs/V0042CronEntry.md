# V0042CronEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** |  | [optional] 
**minute** | **str** | Ranged string specifying eligible minute values (e.g. 0-10,50) | [optional] 
**hour** | **str** | Ranged string specifying eligible hour values (e.g. 0-5,23) | [optional] 
**day_of_month** | **str** | Ranged string specifying eligible day of month values (e.g. 0-10,29) | [optional] 
**month** | **str** | Ranged string specifying eligible month values (e.g. 0-5,12) | [optional] 
**day_of_week** | **str** | Ranged string specifying eligible day of week values (e.g.0-3,7) | [optional] 
**specification** | **str** | Complete time specification (* means valid for all allowed values) - minute hour day_of_month month day_of_week | [optional] 
**command** | **str** | Command to run | [optional] 
**line** | [**V0042CronEntryLine**](V0042CronEntryLine.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0042_cron_entry import V0042CronEntry

# TODO update the JSON string below
json = "{}"
# create an instance of V0042CronEntry from a JSON string
v0042_cron_entry_instance = V0042CronEntry.from_json(json)
# print the JSON string representation of the object
print(V0042CronEntry.to_json())

# convert the object into a dict
v0042_cron_entry_dict = v0042_cron_entry_instance.to_dict()
# create an instance of V0042CronEntry from a dict
v0042_cron_entry_from_dict = V0042CronEntry.from_dict(v0042_cron_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

