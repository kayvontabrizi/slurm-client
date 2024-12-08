# V0042Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** | Computer architecture | [optional] 
**burstbuffer_network_address** | **str** | Alternate network path to be used for sbcast network traffic | [optional] 
**boards** | **int** | Number of Baseboards in nodes with a baseboard controller | [optional] 
**boot_time** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**cluster_name** | **str** | Cluster name (only set in federated environments) | [optional] 
**cores** | **int** | Number of cores in a single physical processor socket | [optional] 
**specialized_cores** | **int** | Number of cores reserved for system use | [optional] 
**cpu_binding** | **int** | Default method for binding tasks to allocated CPUs | [optional] 
**cpu_load** | **int** | CPU load as reported by the OS | [optional] 
**free_mem** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**cpus** | **int** | Total CPUs, including cores and threads | [optional] 
**effective_cpus** | **int** | Number of effective CPUs (excluding specialized CPUs) | [optional] 
**specialized_cpus** | **str** | Abstract CPU IDs on this node reserved for exclusive use by slurmd and slurmstepd | [optional] 
**energy** | [**V0042AcctGatherEnergy**](V0042AcctGatherEnergy.md) |  | [optional] 
**external_sensors** | **object** |  | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**power** | **object** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**active_features** | **List[str]** |  | [optional] 
**gpu_spec** | **str** | CPU cores reserved for jobs that also use a GPU | [optional] 
**gres** | **str** | Generic resources | [optional] 
**gres_drained** | **str** | Drained generic resources | [optional] 
**gres_used** | **str** | Generic resources currently in use | [optional] 
**instance_id** | **str** | Cloud instance ID | [optional] 
**instance_type** | **str** | Cloud instance type | [optional] 
**last_busy** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**mcs_label** | **str** | Multi-Category Security label | [optional] 
**specialized_memory** | **int** | Combined memory limit, in MB, for Slurm compute node daemons | [optional] 
**name** | **str** | NodeName | [optional] 
**next_state_after_reboot** | **List[str]** |  | [optional] 
**address** | **str** | NodeAddr, used to establish a communication path | [optional] 
**hostname** | **str** | NodeHostname | [optional] 
**state** | **List[str]** |  | [optional] 
**operating_system** | **str** | Operating system reported by the node | [optional] 
**owner** | **str** | User allowed to run jobs on this node (unset if no restriction) | [optional] 
**partitions** | **List[str]** |  | [optional] 
**port** | **int** | TCP port number of the slurmd | [optional] 
**real_memory** | **int** | Total memory in MB on the node | [optional] 
**res_cores_per_gpu** | **int** | Number of CPU cores per GPU restricted to GPU jobs | [optional] 
**comment** | **str** | Arbitrary comment | [optional] 
**reason** | **str** | Describes why the node is in a \&quot;DOWN\&quot;, \&quot;DRAINED\&quot;, \&quot;DRAINING\&quot;, \&quot;FAILING\&quot; or \&quot;FAIL\&quot; state | [optional] 
**reason_changed_at** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**reason_set_by_user** | **str** | User who set the reason | [optional] 
**resume_after** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**reservation** | **str** | Name of reservation containing this node | [optional] 
**alloc_memory** | **int** | Total memory in MB currently allocated for jobs | [optional] 
**alloc_cpus** | **int** | Total number of CPUs currently allocated for jobs | [optional] 
**alloc_idle_cpus** | **int** | Total number of idle CPUs | [optional] 
**tres_used** | **str** | Trackable resources currently allocated for jobs | [optional] 
**tres_weighted** | **float** | Weighted number of billable trackable resources allocated | [optional] 
**slurmd_start_time** | [**V0042Uint64NoValStruct**](V0042Uint64NoValStruct.md) |  | [optional] 
**sockets** | **int** | Number of physical processor sockets/chips on the node | [optional] 
**threads** | **int** | Number of logical threads in a single physical core | [optional] 
**temporary_disk** | **int** | Total size in MB of temporary disk storage in TmpFS | [optional] 
**weight** | **int** | Weight of the node for scheduling purposes | [optional] 
**tres** | **str** | Configured trackable resources | [optional] 
**version** | **str** | Slurmd version | [optional] 

## Example

```python
from slurm_client.models.v0042_node import V0042Node

# TODO update the JSON string below
json = "{}"
# create an instance of V0042Node from a JSON string
v0042_node_instance = V0042Node.from_json(json)
# print the JSON string representation of the object
print(V0042Node.to_json())

# convert the object into a dict
v0042_node_dict = v0042_node_instance.to_dict()
# create an instance of V0042Node from a dict
v0042_node_from_dict = V0042Node.from_dict(v0042_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

