# V0041JobDescMsg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Account associated with the job | [optional] 
**account_gather_frequency** | **str** | Job accounting and profiling sampling intervals in seconds | [optional] 
**admin_comment** | **str** | Arbitrary comment made by administrator | [optional] 
**allocation_node_list** | **str** | Local node making the resource allocation | [optional] 
**allocation_node_port** | **int** | Port to send allocation confirmation to | [optional] 
**argv** | **List[str]** | Arguments to the script | [optional] 
**array** | **str** | Job array index value specification | [optional] 
**batch_features** | **str** | Features required for batch script&#39;s node | [optional] 
**begin_time** | [**V0041JobDescMsgBeginTime**](V0041JobDescMsgBeginTime.md) |  | [optional] 
**flags** | **List[str]** | Job flags | [optional] 
**burst_buffer** | **str** | Burst buffer specifications | [optional] 
**clusters** | **str** | Clusters that a federated job can run on | [optional] 
**cluster_constraint** | **str** | Required features that a federated cluster must have to have a sibling job submitted to it | [optional] 
**comment** | **str** | Arbitrary comment made by user | [optional] 
**contiguous** | **bool** | True if job requires contiguous nodes | [optional] 
**container** | **str** | Absolute path to OCI container bundle | [optional] 
**container_id** | **str** | OCI container ID | [optional] 
**core_specification** | **int** | Specialized core count | [optional] 
**thread_specification** | **int** | Specialized thread count | [optional] 
**cpu_binding** | **str** | Method for binding tasks to allocated CPUs | [optional] 
**cpu_binding_flags** | **List[str]** | Flags for CPU binding | [optional] 
**cpu_frequency** | **str** | Requested CPU frequency range &lt;p1&gt;[-p2][:p3] | [optional] 
**cpus_per_tres** | **str** | Semicolon delimited list of TRES&#x3D;# values values indicating how many CPUs should be allocated for each specified TRES (currently only used for gres/gpu) | [optional] 
**crontab** | [**V0041JobDescMsgCrontab**](V0041JobDescMsgCrontab.md) |  | [optional] 
**deadline** | **int** | Latest time that the job may start (UNIX timestamp) | [optional] 
**delay_boot** | **int** | Number of seconds after job eligible start that nodes will be rebooted to satisfy feature specification | [optional] 
**dependency** | **str** | Other jobs that must meet certain criteria before this job can start | [optional] 
**end_time** | **int** | Expected end time (UNIX timestamp) | [optional] 
**environment** | **List[str]** | Environment variables to be set for the job | [optional] 
**rlimits** | [**V0041JobDescMsgRlimits**](V0041JobDescMsgRlimits.md) |  | [optional] 
**excluded_nodes** | **List[str]** | Comma separated list of nodes that may not be used | [optional] 
**extra** | **str** | Arbitrary string used for node filtering if extra constraints are enabled | [optional] 
**constraints** | **str** | Comma separated list of features that are required | [optional] 
**group_id** | **str** | Group ID of the user that owns the job | [optional] 
**hetjob_group** | **int** | Unique sequence number applied to this component of the heterogeneous job | [optional] 
**immediate** | **bool** | If true, exit if resources are not available within the time period specified | [optional] 
**job_id** | **int** | Job ID | [optional] 
**kill_on_node_fail** | **bool** | If true, kill job on node failure | [optional] 
**licenses** | **str** | License(s) required by the job | [optional] 
**mail_type** | **List[str]** | Mail event type(s) | [optional] 
**mail_user** | **str** | User to receive email notifications | [optional] 
**mcs_label** | **str** | Multi-Category Security label on the job | [optional] 
**memory_binding** | **str** | Binding map for map/mask_cpu | [optional] 
**memory_binding_type** | **List[str]** | Method for binding tasks to memory | [optional] 
**memory_per_tres** | **str** | Semicolon delimited list of TRES&#x3D;# values indicating how much memory in megabytes should be allocated for each specified TRES (currently only used for gres/gpu) | [optional] 
**name** | **str** | Job name | [optional] 
**network** | **str** | Network specs for job step | [optional] 
**nice** | **int** | Requested job priority change | [optional] 
**tasks** | **int** | Number of tasks | [optional] 
**open_mode** | **List[str]** | Open mode used for stdout and stderr files | [optional] 
**reserve_ports** | **int** | Port to send various notification msg to | [optional] 
**overcommit** | **bool** | Overcommit resources | [optional] 
**partition** | **str** | Partition assigned to the job | [optional] 
**distribution_plane_size** | [**V0041JobDescMsgDistributionPlaneSize**](V0041JobDescMsgDistributionPlaneSize.md) |  | [optional] 
**power_flags** | **List[object]** |  | [optional] 
**prefer** | **str** | Comma separated list of features that are preferred but not required | [optional] 
**hold** | **bool** | Hold (true) or release (false) job | [optional] 
**priority** | [**V0041JobDescMsgPriority**](V0041JobDescMsgPriority.md) |  | [optional] 
**profile** | **List[str]** | Profile used by the acct_gather_profile plugin | [optional] 
**qos** | **str** | Quality of Service assigned to the job | [optional] 
**reboot** | **bool** | Node reboot requested before start | [optional] 
**required_nodes** | **List[str]** | Comma separated list of required nodes | [optional] 
**requeue** | **bool** | Determines whether the job may be requeued | [optional] 
**reservation** | **str** | Name of reservation to use | [optional] 
**resv_mpi_ports** | **int** | Number of reserved communication ports; can only be used if slurmstepd step manager is enabled | [optional] 
**script** | **str** | Job batch script; only the first component in a HetJob is populated or honored | [optional] 
**shared** | **List[str]** | How the job can share resources with other jobs, if at all | [optional] 
**exclusive** | **List[str]** |  | [optional] 
**oversubscribe** | **bool** |  | [optional] 
**site_factor** | **int** | Site-specific priority factor | [optional] 
**spank_environment** | **List[str]** | Environment variables for job prolog/epilog scripts as set by SPANK plugins | [optional] 
**distribution** | **str** | Layout | [optional] 
**time_limit** | [**V0041JobDescMsgTimeLimit**](V0041JobDescMsgTimeLimit.md) |  | [optional] 
**time_minimum** | [**V0041JobDescMsgTimeMinimum**](V0041JobDescMsgTimeMinimum.md) |  | [optional] 
**tres_bind** | **str** | Task to TRES binding directives | [optional] 
**tres_freq** | **str** | TRES frequency directives | [optional] 
**tres_per_job** | **str** | Comma separated list of TRES&#x3D;# values to be allocated for every job | [optional] 
**tres_per_node** | **str** | Comma separated list of TRES&#x3D;# values to be allocated for every node | [optional] 
**tres_per_socket** | **str** | Comma separated list of TRES&#x3D;# values to be allocated for every socket | [optional] 
**tres_per_task** | **str** | Comma separated list of TRES&#x3D;# values to be allocated for every task | [optional] 
**user_id** | **str** | User ID that owns the job | [optional] 
**wait_all_nodes** | **bool** | If true, wait to start until after all nodes have booted | [optional] 
**kill_warning_flags** | **List[str]** | Flags related to job signals | [optional] 
**kill_warning_signal** | **str** | Signal to send when approaching end time (e.g. \&quot;10\&quot; or \&quot;USR1\&quot;) | [optional] 
**kill_warning_delay** | [**V0041JobDescMsgKillWarningDelay**](V0041JobDescMsgKillWarningDelay.md) |  | [optional] 
**current_working_directory** | **str** | Working directory to use for the job | [optional] 
**cpus_per_task** | **int** | Number of CPUs required by each task | [optional] 
**minimum_cpus** | **int** | Minimum number of CPUs required | [optional] 
**maximum_cpus** | **int** | Maximum number of CPUs required | [optional] 
**nodes** | **str** | Node count range specification (e.g. 1-15:4) | [optional] 
**minimum_nodes** | **int** | Minimum node count | [optional] 
**maximum_nodes** | **int** | Maximum node count | [optional] 
**minimum_boards_per_node** | **int** | Boards per node required | [optional] 
**minimum_sockets_per_board** | **int** | Sockets per board required | [optional] 
**sockets_per_node** | **int** | Sockets per node required | [optional] 
**threads_per_core** | **int** | Threads per core required | [optional] 
**tasks_per_node** | **int** | Number of tasks to invoke on each node | [optional] 
**tasks_per_socket** | **int** | Number of tasks to invoke on each socket | [optional] 
**tasks_per_core** | **int** | Number of tasks to invoke on each core | [optional] 
**tasks_per_board** | **int** | Number of tasks to invoke on each board | [optional] 
**ntasks_per_tres** | **int** | Number of tasks that can access each GPU | [optional] 
**minimum_cpus_per_node** | **int** | Minimum number of CPUs per node | [optional] 
**memory_per_cpu** | [**V0041JobDescMsgMemoryPerCpu**](V0041JobDescMsgMemoryPerCpu.md) |  | [optional] 
**memory_per_node** | [**V0041JobDescMsgMemoryPerCpu**](V0041JobDescMsgMemoryPerCpu.md) |  | [optional] 
**temporary_disk_per_node** | **int** | Minimum tmp disk space required per node | [optional] 
**selinux_context** | **str** | SELinux context | [optional] 
**required_switches** | [**V0041JobDescMsgRequiredSwitches**](V0041JobDescMsgRequiredSwitches.md) |  | [optional] 
**segment_size** | [**V0041JobDescMsgSegmentSize**](V0041JobDescMsgSegmentSize.md) |  | [optional] 
**standard_error** | **str** | Path to stderr file | [optional] 
**standard_input** | **str** | Path to stdin file | [optional] 
**standard_output** | **str** | Path to stdout file | [optional] 
**wait_for_switch** | **int** | Maximum time to wait for switches in seconds | [optional] 
**wckey** | **str** | Workload characterization key | [optional] 
**x11** | **List[str]** | X11 forwarding options | [optional] 
**x11_magic_cookie** | **str** | Magic cookie for X11 forwarding | [optional] 
**x11_target_host** | **str** | Hostname or UNIX socket if x11_target_port&#x3D;0 | [optional] 
**x11_target_port** | **int** | TCP port | [optional] 

## Example

```python
from openapi_client.models.v0041_job_desc_msg import V0041JobDescMsg

# TODO update the JSON string below
json = "{}"
# create an instance of V0041JobDescMsg from a JSON string
v0041_job_desc_msg_instance = V0041JobDescMsg.from_json(json)
# print the JSON string representation of the object
print(V0041JobDescMsg.to_json())

# convert the object into a dict
v0041_job_desc_msg_dict = v0041_job_desc_msg_instance.to_dict()
# create an instance of V0041JobDescMsg from a dict
v0041_job_desc_msg_from_dict = V0041JobDescMsg.from_dict(v0041_job_desc_msg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

