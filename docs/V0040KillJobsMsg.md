# V0040KillJobsMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Filter jobs to a specific account | [optional] 
**flags** | **List[str]** | Filter jobs according to flags | [optional] 
**job_name** | **str** | Filter jobs to a specific name | [optional] 
**jobs** | **List[str]** |  | [optional] 
**partition** | **str** | Filter jobs to a specific partition | [optional] 
**qos** | **str** | Filter jobs to a specific QOS | [optional] 
**reservation** | **str** | Filter jobs to a specific reservation | [optional] 
**signal** | **str** | Signal to send to jobs | [optional] 
**job_state** | **List[str]** | Filter jobs to a specific state | [optional] 
**user_id** | **str** | Filter jobs to a specific numeric user id | [optional] 
**user_name** | **str** | Filter jobs to a specific user name | [optional] 
**wckey** | **str** | Filter jobs to a specific wckey | [optional] 
**nodes** | **List[str]** |  | [optional] 

## Example

```python
from slurm_client.models.v0040_kill_jobs_msg import V0040KillJobsMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0040KillJobsMsg from a JSON string
v0040_kill_jobs_msg_instance = V0040KillJobsMsg.from_json(json)
# print the JSON string representation of the object
print(V0040KillJobsMsg.to_json())

# convert the object into a dict
v0040_kill_jobs_msg_dict = v0040_kill_jobs_msg_instance.to_dict()
# create an instance of V0040KillJobsMsg from a dict
v0040_kill_jobs_msg_from_dict = V0040KillJobsMsg.from_dict(v0040_kill_jobs_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


