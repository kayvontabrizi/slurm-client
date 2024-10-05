# V0040PartitionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**V0041OpenapiPartitionRespPartitionsInnerNodes**](V0041OpenapiPartitionRespPartitionsInnerNodes.md) |  | [optional] 
**accounts** | [**V0041OpenapiPartitionRespPartitionsInnerAccounts**](V0041OpenapiPartitionRespPartitionsInnerAccounts.md) |  | [optional] 
**groups** | [**V0041OpenapiPartitionRespPartitionsInnerGroups**](V0041OpenapiPartitionRespPartitionsInnerGroups.md) |  | [optional] 
**qos** | [**V0041OpenapiPartitionRespPartitionsInnerQos**](V0041OpenapiPartitionRespPartitionsInnerQos.md) |  | [optional] 
**alternate** | **str** | Alternate | [optional] 
**tres** | [**V0041OpenapiPartitionRespPartitionsInnerTres**](V0041OpenapiPartitionRespPartitionsInnerTres.md) |  | [optional] 
**cluster** | **str** | Cluster name | [optional] 
**cpus** | [**V0041OpenapiPartitionRespPartitionsInnerCpus**](V0041OpenapiPartitionRespPartitionsInnerCpus.md) |  | [optional] 
**defaults** | [**V0040PartitionInfoDefaults**](V0040PartitionInfoDefaults.md) |  | [optional] 
**grace_time** | **int** | GraceTime | [optional] 
**maximums** | [**V0040PartitionInfoMaximums**](V0040PartitionInfoMaximums.md) |  | [optional] 
**minimums** | [**V0041OpenapiPartitionRespPartitionsInnerMinimums**](V0041OpenapiPartitionRespPartitionsInnerMinimums.md) |  | [optional] 
**name** | **str** | PartitionName | [optional] 
**node_sets** | **str** | NodeSets | [optional] 
**priority** | [**V0041OpenapiPartitionRespPartitionsInnerPriority**](V0041OpenapiPartitionRespPartitionsInnerPriority.md) |  | [optional] 
**timeouts** | [**V0040PartitionInfoTimeouts**](V0040PartitionInfoTimeouts.md) |  | [optional] 
**partition** | [**V0041OpenapiPartitionRespPartitionsInnerPartition**](V0041OpenapiPartitionRespPartitionsInnerPartition.md) |  | [optional] 
**suspend_time** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  | [optional] 

## Example

```python
from openapi_client.models.v0040_partition_info import V0040PartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V0040PartitionInfo from a JSON string
v0040_partition_info_instance = V0040PartitionInfo.from_json(json)
# print the JSON string representation of the object
print(V0040PartitionInfo.to_json())

# convert the object into a dict
v0040_partition_info_dict = v0040_partition_info_instance.to_dict()
# create an instance of V0040PartitionInfo from a dict
v0040_partition_info_from_dict = V0040PartitionInfo.from_dict(v0040_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


