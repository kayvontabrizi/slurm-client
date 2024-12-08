# V0042CronEntryLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | Start of this entry in file | [optional] 
**end** | **int** | End of this entry in file | [optional] 

## Example

```python
from slurm_client.models.v0042_cron_entry_line import V0042CronEntryLine

# TODO update the JSON string below
json = "{}"
# create an instance of V0042CronEntryLine from a JSON string
v0042_cron_entry_line_instance = V0042CronEntryLine.from_json(json)
# print the JSON string representation of the object
print(V0042CronEntryLine.to_json())

# convert the object into a dict
v0042_cron_entry_line_dict = v0042_cron_entry_line_instance.to_dict()
# create an instance of V0042CronEntryLine from a dict
v0042_cron_entry_line_from_dict = V0042CronEntryLine.from_dict(v0042_cron_entry_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


