# V0042StatsRpcTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **int** | Average RPC processing time in microseconds | [optional] 
**total** | **int** | Total RPC processing time in microseconds | [optional] 

## Example

```python
from slurm_client.models.v0042_stats_rpc_time import V0042StatsRpcTime

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsRpcTime from a JSON string
v0042_stats_rpc_time_instance = V0042StatsRpcTime.from_json(json)
# print the JSON string representation of the object
print(V0042StatsRpcTime.to_json())

# convert the object into a dict
v0042_stats_rpc_time_dict = v0042_stats_rpc_time_instance.to_dict()
# create an instance of V0042StatsRpcTime from a dict
v0042_stats_rpc_time_from_dict = V0042StatsRpcTime.from_dict(v0042_stats_rpc_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


