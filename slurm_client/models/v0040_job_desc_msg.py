# coding: utf-8

"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.11.0&openapi/slurmctld&openapi/slurmdbd
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from slurm_client.models.v0040_cron_entry import V0040CronEntry
from slurm_client.models.v0040_job_desc_msg_rlimits import V0040JobDescMsgRlimits
from slurm_client.models.v0040_uint16_no_val import V0040Uint16NoVal
from slurm_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from slurm_client.models.v0040_uint64_no_val import V0040Uint64NoVal
from typing import Optional, Set
from typing_extensions import Self

class V0040JobDescMsg(BaseModel):
    """
    V0040JobDescMsg
    """ # noqa: E501
    account: Optional[StrictStr] = Field(default=None, description="Account associated with the job")
    account_gather_frequency: Optional[StrictStr] = Field(default=None, description="Job accounting and profiling sampling intervals in seconds")
    admin_comment: Optional[StrictStr] = Field(default=None, description="Arbitrary comment made by administrator")
    allocation_node_list: Optional[StrictStr] = Field(default=None, description="Local node making the resource allocation")
    allocation_node_port: Optional[StrictInt] = Field(default=None, description="Port to send allocation confirmation to")
    argv: Optional[List[StrictStr]] = None
    array: Optional[StrictStr] = Field(default=None, description="Job array index value specification")
    batch_features: Optional[StrictStr] = Field(default=None, description="Features required for batch script's node")
    begin_time: Optional[V0040Uint64NoVal] = None
    flags: Optional[List[StrictStr]] = None
    burst_buffer: Optional[StrictStr] = Field(default=None, description="Burst buffer specifications")
    clusters: Optional[StrictStr] = Field(default=None, description="Clusters that a federated job can run on")
    cluster_constraint: Optional[StrictStr] = Field(default=None, description="Required features that a federated cluster must have to have a sibling job submitted to it")
    comment: Optional[StrictStr] = Field(default=None, description="Arbitrary comment made by user")
    contiguous: Optional[StrictBool] = Field(default=None, description="True if job requires contiguous nodes")
    container: Optional[StrictStr] = Field(default=None, description="Absolute path to OCI container bundle")
    container_id: Optional[StrictStr] = Field(default=None, description="OCI container ID")
    cores_per_socket: Optional[StrictInt] = Field(default=None, description="Cores per socket required")
    core_specification: Optional[StrictInt] = Field(default=None, description="Specialized core count")
    thread_specification: Optional[StrictInt] = Field(default=None, description="Specialized thread count")
    cpu_binding: Optional[StrictStr] = Field(default=None, description="Method for binding tasks to allocated CPUs")
    cpu_binding_flags: Optional[List[StrictStr]] = None
    cpu_frequency: Optional[StrictStr] = Field(default=None, description="Requested CPU frequency range <p1>[-p2][:p3]")
    cpus_per_tres: Optional[StrictStr] = Field(default=None, description="Semicolon delimited list of TRES=# values values indicating how many CPUs should be allocated for each specified TRES (currently only used for gres/gpu)")
    crontab: Optional[V0040CronEntry] = None
    deadline: Optional[StrictInt] = Field(default=None, description="Latest time that the job may start (UNIX timestamp)")
    delay_boot: Optional[StrictInt] = Field(default=None, description="Number of seconds after job eligible start that nodes will be rebooted to satisfy feature specification")
    dependency: Optional[StrictStr] = Field(default=None, description="Other jobs that must meet certain criteria before this job can start")
    end_time: Optional[StrictInt] = Field(default=None, description="Expected end time (UNIX timestamp)")
    environment: Optional[List[StrictStr]] = None
    rlimits: Optional[V0040JobDescMsgRlimits] = None
    excluded_nodes: Optional[List[StrictStr]] = None
    extra: Optional[StrictStr] = Field(default=None, description="Arbitrary string used for node filtering if extra constraints are enabled")
    constraints: Optional[StrictStr] = Field(default=None, description="Comma separated list of features that are required")
    group_id: Optional[StrictStr] = Field(default=None, description="Group ID of the user that owns the job")
    hetjob_group: Optional[StrictInt] = Field(default=None, description="Unique sequence number applied to this component of the heterogeneous job")
    immediate: Optional[StrictBool] = Field(default=None, description="If true, exit if resources are not available within the time period specified")
    job_id: Optional[StrictInt] = Field(default=None, description="Job ID")
    kill_on_node_fail: Optional[StrictBool] = Field(default=None, description="If true, kill job on node failure")
    licenses: Optional[StrictStr] = Field(default=None, description="License(s) required by the job")
    mail_type: Optional[List[StrictStr]] = None
    mail_user: Optional[StrictStr] = Field(default=None, description="User to receive email notifications")
    mcs_label: Optional[StrictStr] = Field(default=None, description="Multi-Category Security label on the job")
    memory_binding: Optional[StrictStr] = Field(default=None, description="Binding map for map/mask_cpu")
    memory_binding_type: Optional[List[StrictStr]] = None
    memory_per_tres: Optional[StrictStr] = Field(default=None, description="Semicolon delimited list of TRES=# values indicating how much memory in megabytes should be allocated for each specified TRES (currently only used for gres/gpu)")
    name: Optional[StrictStr] = Field(default=None, description="Job name")
    network: Optional[StrictStr] = Field(default=None, description="Network specs for job step")
    nice: Optional[StrictInt] = Field(default=None, description="Requested job priority change")
    tasks: Optional[StrictInt] = Field(default=None, description="Number of tasks")
    open_mode: Optional[List[StrictStr]] = None
    reserve_ports: Optional[StrictInt] = Field(default=None, description="Port to send various notification msg to")
    overcommit: Optional[StrictBool] = Field(default=None, description="Overcommit resources")
    partition: Optional[StrictStr] = Field(default=None, description="Partition assigned to the job")
    distribution_plane_size: Optional[StrictInt] = Field(default=None, description="Plane size specification when distribution specifies plane")
    power_flags: Optional[List[Any]] = Field(default=None, description="removed field")
    prefer: Optional[StrictStr] = Field(default=None, description="Comma separated list of features that are preferred but not required")
    hold: Optional[StrictBool] = Field(default=None, description="Job held")
    priority: Optional[V0040Uint32NoVal] = None
    profile: Optional[List[StrictStr]] = None
    qos: Optional[StrictStr] = Field(default=None, description="Quality of Service assigned to the job")
    reboot: Optional[StrictBool] = Field(default=None, description="Node reboot requested before start")
    required_nodes: Optional[List[StrictStr]] = None
    requeue: Optional[StrictBool] = Field(default=None, description="Determines whether the job may be requeued")
    reservation: Optional[StrictStr] = Field(default=None, description="Name of reservation to use")
    script: Optional[StrictStr] = Field(default=None, description="Job batch script; only the first component in a HetJob is populated or honored")
    shared: Optional[List[StrictStr]] = None
    exclusive: Optional[List[StrictStr]] = None
    oversubscribe: Optional[StrictBool] = None
    site_factor: Optional[StrictInt] = Field(default=None, description="Site-specific priority factor")
    spank_environment: Optional[List[StrictStr]] = None
    distribution: Optional[StrictStr] = Field(default=None, description="Layout")
    time_limit: Optional[V0040Uint32NoVal] = None
    time_minimum: Optional[V0040Uint32NoVal] = None
    tres_bind: Optional[StrictStr] = Field(default=None, description="Task to TRES binding directives")
    tres_freq: Optional[StrictStr] = Field(default=None, description="TRES frequency directives")
    tres_per_job: Optional[StrictStr] = Field(default=None, description="Comma separated list of TRES=# values to be allocated for every job")
    tres_per_node: Optional[StrictStr] = Field(default=None, description="Comma separated list of TRES=# values to be allocated for every node")
    tres_per_socket: Optional[StrictStr] = Field(default=None, description="Comma separated list of TRES=# values to be allocated for every socket")
    tres_per_task: Optional[StrictStr] = Field(default=None, description="Comma separated list of TRES=# values to be allocated for every task")
    user_id: Optional[StrictStr] = Field(default=None, description="User ID that owns the job")
    wait_all_nodes: Optional[StrictBool] = Field(default=None, description="If true, wait to start until after all nodes have booted")
    kill_warning_flags: Optional[List[StrictStr]] = None
    kill_warning_signal: Optional[StrictStr] = Field(default=None, description="Signal to send when approaching end time (e.g. \"10\" or \"USR1\")")
    kill_warning_delay: Optional[V0040Uint16NoVal] = None
    current_working_directory: Optional[StrictStr] = Field(default=None, description="Working directory to use for the job")
    cpus_per_task: Optional[StrictInt] = Field(default=None, description="Number of CPUs required by each task")
    minimum_cpus: Optional[StrictInt] = Field(default=None, description="Minimum number of CPUs required")
    maximum_cpus: Optional[StrictInt] = Field(default=None, description="Maximum number of CPUs required")
    nodes: Optional[StrictStr] = Field(default=None, description="Node count range specification (e.g. 1-15:4)")
    minimum_nodes: Optional[StrictInt] = Field(default=None, description="Minimum node count")
    maximum_nodes: Optional[StrictInt] = Field(default=None, description="Maximum node count")
    minimum_boards_per_node: Optional[StrictInt] = Field(default=None, description="Boards per node required")
    minimum_sockets_per_board: Optional[StrictInt] = Field(default=None, description="Sockets per board required")
    sockets_per_node: Optional[StrictInt] = Field(default=None, description="Sockets per node required")
    threads_per_core: Optional[StrictInt] = Field(default=None, description="Threads per core required")
    tasks_per_node: Optional[StrictInt] = Field(default=None, description="Number of tasks to invoke on each node")
    tasks_per_socket: Optional[StrictInt] = Field(default=None, description="Number of tasks to invoke on each socket")
    tasks_per_core: Optional[StrictInt] = Field(default=None, description="Number of tasks to invoke on each core")
    tasks_per_board: Optional[StrictInt] = Field(default=None, description="Number of tasks to invoke on each board")
    ntasks_per_tres: Optional[StrictInt] = Field(default=None, description="Number of tasks that can access each GPU")
    minimum_cpus_per_node: Optional[StrictInt] = Field(default=None, description="Minimum number of CPUs per node")
    memory_per_cpu: Optional[V0040Uint64NoVal] = None
    memory_per_node: Optional[V0040Uint64NoVal] = None
    temporary_disk_per_node: Optional[StrictInt] = Field(default=None, description="Minimum tmp disk space required per node")
    selinux_context: Optional[StrictStr] = Field(default=None, description="SELinux context")
    required_switches: Optional[V0040Uint32NoVal] = None
    standard_error: Optional[StrictStr] = Field(default=None, description="Path to stderr file")
    standard_input: Optional[StrictStr] = Field(default=None, description="Path to stdin file")
    standard_output: Optional[StrictStr] = Field(default=None, description="Path to stdout file")
    wait_for_switch: Optional[StrictInt] = Field(default=None, description="Maximum time to wait for switches in seconds")
    wckey: Optional[StrictStr] = Field(default=None, description="Workload characterization key")
    x11: Optional[List[StrictStr]] = None
    x11_magic_cookie: Optional[StrictStr] = Field(default=None, description="Magic cookie for X11 forwarding")
    x11_target_host: Optional[StrictStr] = Field(default=None, description="Hostname or UNIX socket if x11_target_port=0")
    x11_target_port: Optional[StrictInt] = Field(default=None, description="TCP port")
    __properties: ClassVar[List[str]] = ["account", "account_gather_frequency", "admin_comment", "allocation_node_list", "allocation_node_port", "argv", "array", "batch_features", "begin_time", "flags", "burst_buffer", "clusters", "cluster_constraint", "comment", "contiguous", "container", "container_id", "cores_per_socket", "core_specification", "thread_specification", "cpu_binding", "cpu_binding_flags", "cpu_frequency", "cpus_per_tres", "crontab", "deadline", "delay_boot", "dependency", "end_time", "environment", "rlimits", "excluded_nodes", "extra", "constraints", "group_id", "hetjob_group", "immediate", "job_id", "kill_on_node_fail", "licenses", "mail_type", "mail_user", "mcs_label", "memory_binding", "memory_binding_type", "memory_per_tres", "name", "network", "nice", "tasks", "open_mode", "reserve_ports", "overcommit", "partition", "distribution_plane_size", "power_flags", "prefer", "hold", "priority", "profile", "qos", "reboot", "required_nodes", "requeue", "reservation", "script", "shared", "exclusive", "oversubscribe", "site_factor", "spank_environment", "distribution", "time_limit", "time_minimum", "tres_bind", "tres_freq", "tres_per_job", "tres_per_node", "tres_per_socket", "tres_per_task", "user_id", "wait_all_nodes", "kill_warning_flags", "kill_warning_signal", "kill_warning_delay", "current_working_directory", "cpus_per_task", "minimum_cpus", "maximum_cpus", "nodes", "minimum_nodes", "maximum_nodes", "minimum_boards_per_node", "minimum_sockets_per_board", "sockets_per_node", "threads_per_core", "tasks_per_node", "tasks_per_socket", "tasks_per_core", "tasks_per_board", "ntasks_per_tres", "minimum_cpus_per_node", "memory_per_cpu", "memory_per_node", "temporary_disk_per_node", "selinux_context", "required_switches", "standard_error", "standard_input", "standard_output", "wait_for_switch", "wckey", "x11", "x11_magic_cookie", "x11_target_host", "x11_target_port"]

    @field_validator('flags')
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['KILL_INVALID_DEPENDENCY', 'NO_KILL_INVALID_DEPENDENCY', 'HAS_STATE_DIRECTORY', 'TESTING_BACKFILL', 'GRES_BINDING_ENFORCED', 'TEST_NOW_ONLY', 'SEND_JOB_ENVIRONMENT', 'SPREAD_JOB', 'PREFER_MINIMUM_NODE_COUNT', 'JOB_KILL_HURRY', 'SKIP_TRES_STRING_ACCOUNTING', 'SIBLING_CLUSTER_UPDATE_ONLY', 'HETEROGENEOUS_JOB', 'EXACT_TASK_COUNT_REQUESTED', 'EXACT_CPU_COUNT_REQUESTED', 'TESTING_WHOLE_NODE_BACKFILL', 'TOP_PRIORITY_JOB', 'ACCRUE_COUNT_CLEARED', 'GRES_BINDING_DISABLED', 'JOB_WAS_RUNNING', 'JOB_ACCRUE_TIME_RESET', 'CRON_JOB', 'EXACT_MEMORY_REQUESTED', 'USING_DEFAULT_ACCOUNT', 'USING_DEFAULT_PARTITION', 'USING_DEFAULT_QOS', 'USING_DEFAULT_WCKEY', 'DEPENDENT', 'MAGNETIC', 'PARTITION_ASSIGNED', 'BACKFILL_ATTEMPTED', 'SCHEDULING_ATTEMPTED', 'SAVE_BATCH_SCRIPT', 'GRES_ONE_TASK_PER_SHARING', 'GRES_MULTIPLE_TASKS_PER_SHARING', 'GRES_ALLOW_TASK_SHARING']):
                raise ValueError("each list item must be one of ('KILL_INVALID_DEPENDENCY', 'NO_KILL_INVALID_DEPENDENCY', 'HAS_STATE_DIRECTORY', 'TESTING_BACKFILL', 'GRES_BINDING_ENFORCED', 'TEST_NOW_ONLY', 'SEND_JOB_ENVIRONMENT', 'SPREAD_JOB', 'PREFER_MINIMUM_NODE_COUNT', 'JOB_KILL_HURRY', 'SKIP_TRES_STRING_ACCOUNTING', 'SIBLING_CLUSTER_UPDATE_ONLY', 'HETEROGENEOUS_JOB', 'EXACT_TASK_COUNT_REQUESTED', 'EXACT_CPU_COUNT_REQUESTED', 'TESTING_WHOLE_NODE_BACKFILL', 'TOP_PRIORITY_JOB', 'ACCRUE_COUNT_CLEARED', 'GRES_BINDING_DISABLED', 'JOB_WAS_RUNNING', 'JOB_ACCRUE_TIME_RESET', 'CRON_JOB', 'EXACT_MEMORY_REQUESTED', 'USING_DEFAULT_ACCOUNT', 'USING_DEFAULT_PARTITION', 'USING_DEFAULT_QOS', 'USING_DEFAULT_WCKEY', 'DEPENDENT', 'MAGNETIC', 'PARTITION_ASSIGNED', 'BACKFILL_ATTEMPTED', 'SCHEDULING_ATTEMPTED', 'SAVE_BATCH_SCRIPT', 'GRES_ONE_TASK_PER_SHARING', 'GRES_MULTIPLE_TASKS_PER_SHARING', 'GRES_ALLOW_TASK_SHARING')")
        return value

    @field_validator('cpu_binding_flags')
    def cpu_binding_flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['CPU_BIND_TO_THREADS', 'CPU_BIND_TO_CORES', 'CPU_BIND_TO_SOCKETS', 'CPU_BIND_TO_LDOMS', 'CPU_BIND_NONE', 'CPU_BIND_RANK', 'CPU_BIND_MAP', 'CPU_BIND_MASK', 'CPU_BIND_LDRANK', 'CPU_BIND_LDMAP', 'CPU_BIND_LDMASK', 'VERBOSE', 'CPU_BIND_ONE_THREAD_PER_CORE']):
                raise ValueError("each list item must be one of ('CPU_BIND_TO_THREADS', 'CPU_BIND_TO_CORES', 'CPU_BIND_TO_SOCKETS', 'CPU_BIND_TO_LDOMS', 'CPU_BIND_NONE', 'CPU_BIND_RANK', 'CPU_BIND_MAP', 'CPU_BIND_MASK', 'CPU_BIND_LDRANK', 'CPU_BIND_LDMAP', 'CPU_BIND_LDMASK', 'VERBOSE', 'CPU_BIND_ONE_THREAD_PER_CORE')")
        return value

    @field_validator('mail_type')
    def mail_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['BEGIN', 'END', 'FAIL', 'REQUEUE', 'TIME=100%', 'TIME=90%', 'TIME=80%', 'TIME=50%', 'STAGE_OUT', 'ARRAY_TASKS', 'INVALID_DEPENDENCY']):
                raise ValueError("each list item must be one of ('BEGIN', 'END', 'FAIL', 'REQUEUE', 'TIME=100%', 'TIME=90%', 'TIME=80%', 'TIME=50%', 'STAGE_OUT', 'ARRAY_TASKS', 'INVALID_DEPENDENCY')")
        return value

    @field_validator('memory_binding_type')
    def memory_binding_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NONE', 'RANK', 'MAP', 'MASK', 'LOCAL', 'VERBOSE', 'SORT', 'PREFER']):
                raise ValueError("each list item must be one of ('NONE', 'RANK', 'MAP', 'MASK', 'LOCAL', 'VERBOSE', 'SORT', 'PREFER')")
        return value

    @field_validator('open_mode')
    def open_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['APPEND', 'TRUNCATE']):
                raise ValueError("each list item must be one of ('APPEND', 'TRUNCATE')")
        return value

    @field_validator('profile')
    def profile_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['NOT_SET', 'NONE', 'ENERGY', 'LUSTRE', 'NETWORK', 'TASK']):
                raise ValueError("each list item must be one of ('NOT_SET', 'NONE', 'ENERGY', 'LUSTRE', 'NETWORK', 'TASK')")
        return value

    @field_validator('shared')
    def shared_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['none', 'oversubscribe', 'user', 'mcs']):
                raise ValueError("each list item must be one of ('none', 'oversubscribe', 'user', 'mcs')")
        return value

    @field_validator('exclusive')
    def exclusive_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['true', 'false', 'user', 'mcs']):
                raise ValueError("each list item must be one of ('true', 'false', 'user', 'mcs')")
        return value

    @field_validator('kill_warning_flags')
    def kill_warning_flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['BATCH_JOB', 'ARRAY_TASK', 'FULL_STEPS_ONLY', 'FULL_JOB', 'FEDERATION_REQUEUE', 'HURRY', 'OUT_OF_MEMORY', 'NO_SIBLING_JOBS', 'RESERVATION_JOB', 'NO_CRON_JOBS', 'VERBOSE', 'CRON_JOBS', 'WARNING_SENT']):
                raise ValueError("each list item must be one of ('BATCH_JOB', 'ARRAY_TASK', 'FULL_STEPS_ONLY', 'FULL_JOB', 'FEDERATION_REQUEUE', 'HURRY', 'OUT_OF_MEMORY', 'NO_SIBLING_JOBS', 'RESERVATION_JOB', 'NO_CRON_JOBS', 'VERBOSE', 'CRON_JOBS', 'WARNING_SENT')")
        return value

    @field_validator('x11')
    def x11_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['FORWARD_ALL_NODES', 'BATCH_NODE', 'FIRST_NODE', 'LAST_NODE']):
                raise ValueError("each list item must be one of ('FORWARD_ALL_NODES', 'BATCH_NODE', 'FIRST_NODE', 'LAST_NODE')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V0040JobDescMsg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of begin_time
        if self.begin_time:
            _dict['begin_time'] = self.begin_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of crontab
        if self.crontab:
            _dict['crontab'] = self.crontab.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rlimits
        if self.rlimits:
            _dict['rlimits'] = self.rlimits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of priority
        if self.priority:
            _dict['priority'] = self.priority.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_limit
        if self.time_limit:
            _dict['time_limit'] = self.time_limit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_minimum
        if self.time_minimum:
            _dict['time_minimum'] = self.time_minimum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of kill_warning_delay
        if self.kill_warning_delay:
            _dict['kill_warning_delay'] = self.kill_warning_delay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory_per_cpu
        if self.memory_per_cpu:
            _dict['memory_per_cpu'] = self.memory_per_cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory_per_node
        if self.memory_per_node:
            _dict['memory_per_node'] = self.memory_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of required_switches
        if self.required_switches:
            _dict['required_switches'] = self.required_switches.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040JobDescMsg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account": obj.get("account"),
            "account_gather_frequency": obj.get("account_gather_frequency"),
            "admin_comment": obj.get("admin_comment"),
            "allocation_node_list": obj.get("allocation_node_list"),
            "allocation_node_port": obj.get("allocation_node_port"),
            "argv": obj.get("argv"),
            "array": obj.get("array"),
            "batch_features": obj.get("batch_features"),
            "begin_time": V0040Uint64NoVal.from_dict(obj["begin_time"]) if obj.get("begin_time") is not None else None,
            "flags": obj.get("flags"),
            "burst_buffer": obj.get("burst_buffer"),
            "clusters": obj.get("clusters"),
            "cluster_constraint": obj.get("cluster_constraint"),
            "comment": obj.get("comment"),
            "contiguous": obj.get("contiguous"),
            "container": obj.get("container"),
            "container_id": obj.get("container_id"),
            "cores_per_socket": obj.get("cores_per_socket"),
            "core_specification": obj.get("core_specification"),
            "thread_specification": obj.get("thread_specification"),
            "cpu_binding": obj.get("cpu_binding"),
            "cpu_binding_flags": obj.get("cpu_binding_flags"),
            "cpu_frequency": obj.get("cpu_frequency"),
            "cpus_per_tres": obj.get("cpus_per_tres"),
            "crontab": V0040CronEntry.from_dict(obj["crontab"]) if obj.get("crontab") is not None else None,
            "deadline": obj.get("deadline"),
            "delay_boot": obj.get("delay_boot"),
            "dependency": obj.get("dependency"),
            "end_time": obj.get("end_time"),
            "environment": obj.get("environment"),
            "rlimits": V0040JobDescMsgRlimits.from_dict(obj["rlimits"]) if obj.get("rlimits") is not None else None,
            "excluded_nodes": obj.get("excluded_nodes"),
            "extra": obj.get("extra"),
            "constraints": obj.get("constraints"),
            "group_id": obj.get("group_id"),
            "hetjob_group": obj.get("hetjob_group"),
            "immediate": obj.get("immediate"),
            "job_id": obj.get("job_id"),
            "kill_on_node_fail": obj.get("kill_on_node_fail"),
            "licenses": obj.get("licenses"),
            "mail_type": obj.get("mail_type"),
            "mail_user": obj.get("mail_user"),
            "mcs_label": obj.get("mcs_label"),
            "memory_binding": obj.get("memory_binding"),
            "memory_binding_type": obj.get("memory_binding_type"),
            "memory_per_tres": obj.get("memory_per_tres"),
            "name": obj.get("name"),
            "network": obj.get("network"),
            "nice": obj.get("nice"),
            "tasks": obj.get("tasks"),
            "open_mode": obj.get("open_mode"),
            "reserve_ports": obj.get("reserve_ports"),
            "overcommit": obj.get("overcommit"),
            "partition": obj.get("partition"),
            "distribution_plane_size": obj.get("distribution_plane_size"),
            "power_flags": obj.get("power_flags"),
            "prefer": obj.get("prefer"),
            "hold": obj.get("hold"),
            "priority": V0040Uint32NoVal.from_dict(obj["priority"]) if obj.get("priority") is not None else None,
            "profile": obj.get("profile"),
            "qos": obj.get("qos"),
            "reboot": obj.get("reboot"),
            "required_nodes": obj.get("required_nodes"),
            "requeue": obj.get("requeue"),
            "reservation": obj.get("reservation"),
            "script": obj.get("script"),
            "shared": obj.get("shared"),
            "exclusive": obj.get("exclusive"),
            "oversubscribe": obj.get("oversubscribe"),
            "site_factor": obj.get("site_factor"),
            "spank_environment": obj.get("spank_environment"),
            "distribution": obj.get("distribution"),
            "time_limit": V0040Uint32NoVal.from_dict(obj["time_limit"]) if obj.get("time_limit") is not None else None,
            "time_minimum": V0040Uint32NoVal.from_dict(obj["time_minimum"]) if obj.get("time_minimum") is not None else None,
            "tres_bind": obj.get("tres_bind"),
            "tres_freq": obj.get("tres_freq"),
            "tres_per_job": obj.get("tres_per_job"),
            "tres_per_node": obj.get("tres_per_node"),
            "tres_per_socket": obj.get("tres_per_socket"),
            "tres_per_task": obj.get("tres_per_task"),
            "user_id": obj.get("user_id"),
            "wait_all_nodes": obj.get("wait_all_nodes"),
            "kill_warning_flags": obj.get("kill_warning_flags"),
            "kill_warning_signal": obj.get("kill_warning_signal"),
            "kill_warning_delay": V0040Uint16NoVal.from_dict(obj["kill_warning_delay"]) if obj.get("kill_warning_delay") is not None else None,
            "current_working_directory": obj.get("current_working_directory"),
            "cpus_per_task": obj.get("cpus_per_task"),
            "minimum_cpus": obj.get("minimum_cpus"),
            "maximum_cpus": obj.get("maximum_cpus"),
            "nodes": obj.get("nodes"),
            "minimum_nodes": obj.get("minimum_nodes"),
            "maximum_nodes": obj.get("maximum_nodes"),
            "minimum_boards_per_node": obj.get("minimum_boards_per_node"),
            "minimum_sockets_per_board": obj.get("minimum_sockets_per_board"),
            "sockets_per_node": obj.get("sockets_per_node"),
            "threads_per_core": obj.get("threads_per_core"),
            "tasks_per_node": obj.get("tasks_per_node"),
            "tasks_per_socket": obj.get("tasks_per_socket"),
            "tasks_per_core": obj.get("tasks_per_core"),
            "tasks_per_board": obj.get("tasks_per_board"),
            "ntasks_per_tres": obj.get("ntasks_per_tres"),
            "minimum_cpus_per_node": obj.get("minimum_cpus_per_node"),
            "memory_per_cpu": V0040Uint64NoVal.from_dict(obj["memory_per_cpu"]) if obj.get("memory_per_cpu") is not None else None,
            "memory_per_node": V0040Uint64NoVal.from_dict(obj["memory_per_node"]) if obj.get("memory_per_node") is not None else None,
            "temporary_disk_per_node": obj.get("temporary_disk_per_node"),
            "selinux_context": obj.get("selinux_context"),
            "required_switches": V0040Uint32NoVal.from_dict(obj["required_switches"]) if obj.get("required_switches") is not None else None,
            "standard_error": obj.get("standard_error"),
            "standard_input": obj.get("standard_input"),
            "standard_output": obj.get("standard_output"),
            "wait_for_switch": obj.get("wait_for_switch"),
            "wckey": obj.get("wckey"),
            "x11": obj.get("x11"),
            "x11_magic_cookie": obj.get("x11_magic_cookie"),
            "x11_target_host": obj.get("x11_target_host"),
            "x11_target_port": obj.get("x11_target_port")
        })
        return _obj


