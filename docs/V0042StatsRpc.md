# V0042StatsRpc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rpc** | **str** | RPC type | [optional] 
**count** | **int** | Number of RPCs processed | [optional] 
**time** | [**V0042StatsRpcTime**](V0042StatsRpcTime.md) |  | [optional] 

## Example

```python
from slurm_client.models.v0042_stats_rpc import V0042StatsRpc

# TODO update the JSON string below
json = "{}"
# create an instance of V0042StatsRpc from a JSON string
v0042_stats_rpc_instance = V0042StatsRpc.from_json(json)
# print the JSON string representation of the object
print(V0042StatsRpc.to_json())

# convert the object into a dict
v0042_stats_rpc_dict = v0042_stats_rpc_instance.to_dict()
# create an instance of V0042StatsRpc from a dict
v0042_stats_rpc_from_dict = V0042StatsRpc.from_dict(v0042_stats_rpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


