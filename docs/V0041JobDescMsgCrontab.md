# V0041JobDescMsgCrontab

Specification for scrontab job

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **List[str]** | Flags | [optional] 
**minute** | **str** | Ranged string specifying eligible minute values (e.g. 0-10,50) | [optional] 
**hour** | **str** | Ranged string specifying eligible hour values (e.g. 0-5,23) | [optional] 
**day_of_month** | **str** | Ranged string specifying eligible day of month values (e.g. 0-10,29) | [optional] 
**month** | **str** | Ranged string specifying eligible month values (e.g. 0-5,12) | [optional] 
**day_of_week** | **str** | Ranged string specifying eligible day of week values (e.g.0-3,7) | [optional] 
**specification** | **str** | Time specification (* means valid for all allowed values) - minute hour day_of_month month day_of_week | [optional] 
**command** | **str** | Command to run | [optional] 
**line** | [**V0041JobDescMsgCrontabLine**](V0041JobDescMsgCrontabLine.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0041_job_desc_msg_crontab import V0041JobDescMsgCrontab

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsgCrontab from a JSON string
v0041_job_desc_msg_crontab_instance = V0041JobDescMsgCrontab.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsgCrontab.to_json())

# convert the object into a dict
v0041_job_desc_msg_crontab_dict = v0041_job_desc_msg_crontab_instance.to_dict()
# create an instance of V0041JobDescMsgCrontab from a dict
v0041_job_desc_msg_crontab_from_dict = V0041JobDescMsgCrontab.from_dict(v0041_job_desc_msg_crontab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


