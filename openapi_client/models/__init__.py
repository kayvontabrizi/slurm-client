# coding: utf-8

# flake8: noqa
"""
    Slurm REST API

    API to access and control Slurm

    The version of the OpenAPI document: Slurm-24.05.3&openapi/v0.0.39&openapi/dbv0.0.39&openapi/slurmdbd&openapi/slurmctld
    Contact: sales@schedmd.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.dbv0039_account_info import Dbv0039AccountInfo
from openapi_client.models.dbv0039_associations_info import Dbv0039AssociationsInfo
from openapi_client.models.dbv0039_clusters_info import Dbv0039ClustersInfo
from openapi_client.models.dbv0039_config_info import Dbv0039ConfigInfo
from openapi_client.models.dbv0039_diag import Dbv0039Diag
from openapi_client.models.dbv0039_error import Dbv0039Error
from openapi_client.models.dbv0039_job_info import Dbv0039JobInfo
from openapi_client.models.dbv0039_meta import Dbv0039Meta
from openapi_client.models.dbv0039_qos_info import Dbv0039QosInfo
from openapi_client.models.dbv0039_response_associations_delete import Dbv0039ResponseAssociationsDelete
from openapi_client.models.dbv0039_set_config import Dbv0039SetConfig
from openapi_client.models.dbv0039_tres_info import Dbv0039TresInfo
from openapi_client.models.dbv0039_tres_update import Dbv0039TresUpdate
from openapi_client.models.dbv0039_update_qos import Dbv0039UpdateQos
from openapi_client.models.dbv0039_update_users import Dbv0039UpdateUsers
from openapi_client.models.dbv0039_user_info import Dbv0039UserInfo
from openapi_client.models.dbv0039_warning import Dbv0039Warning
from openapi_client.models.dbv0039_wckey_info import Dbv0039WckeyInfo
from openapi_client.models.status import Status
from openapi_client.models.v0039_account import V0039Account
from openapi_client.models.v0039_accounting import V0039Accounting
from openapi_client.models.v0039_accounting_allocated import V0039AccountingAllocated
from openapi_client.models.v0039_acct_gather_energy import V0039AcctGatherEnergy
from openapi_client.models.v0039_assoc import V0039Assoc
from openapi_client.models.v0039_assoc_default import V0039AssocDefault
from openapi_client.models.v0039_assoc_max import V0039AssocMax
from openapi_client.models.v0039_assoc_max_jobs import V0039AssocMaxJobs
from openapi_client.models.v0039_assoc_max_jobs_per import V0039AssocMaxJobsPer
from openapi_client.models.v0039_assoc_max_per import V0039AssocMaxPer
from openapi_client.models.v0039_assoc_max_per_account import V0039AssocMaxPerAccount
from openapi_client.models.v0039_assoc_max_tres import V0039AssocMaxTres
from openapi_client.models.v0039_assoc_max_tres_group import V0039AssocMaxTresGroup
from openapi_client.models.v0039_assoc_max_tres_minutes import V0039AssocMaxTresMinutes
from openapi_client.models.v0039_assoc_max_tres_minutes_per import V0039AssocMaxTresMinutesPer
from openapi_client.models.v0039_assoc_max_tres_per import V0039AssocMaxTresPer
from openapi_client.models.v0039_assoc_min import V0039AssocMin
from openapi_client.models.v0039_assoc_short import V0039AssocShort
from openapi_client.models.v0039_assoc_usage import V0039AssocUsage
from openapi_client.models.v0039_cluster_rec import V0039ClusterRec
from openapi_client.models.v0039_cluster_rec_associations import V0039ClusterRecAssociations
from openapi_client.models.v0039_cluster_rec_controller import V0039ClusterRecController
from openapi_client.models.v0039_controller_ping import V0039ControllerPing
from openapi_client.models.v0039_coord import V0039Coord
from openapi_client.models.v0039_cron_entry import V0039CronEntry
from openapi_client.models.v0039_cron_entry_line import V0039CronEntryLine
from openapi_client.models.v0039_diag import V0039Diag
from openapi_client.models.v0039_error import V0039Error
from openapi_client.models.v0039_float64_no_val import V0039Float64NoVal
from openapi_client.models.v0039_job import V0039Job
from openapi_client.models.v0039_job_array import V0039JobArray
from openapi_client.models.v0039_job_array_limits import V0039JobArrayLimits
from openapi_client.models.v0039_job_array_limits_max import V0039JobArrayLimitsMax
from openapi_client.models.v0039_job_array_limits_max_running import V0039JobArrayLimitsMaxRunning
from openapi_client.models.v0039_job_array_response_msg_inner import V0039JobArrayResponseMsgInner
from openapi_client.models.v0039_job_comment import V0039JobComment
from openapi_client.models.v0039_job_desc_msg import V0039JobDescMsg
from openapi_client.models.v0039_job_exit_code import V0039JobExitCode
from openapi_client.models.v0039_job_exit_code_signal import V0039JobExitCodeSignal
from openapi_client.models.v0039_job_het import V0039JobHet
from openapi_client.models.v0039_job_info import V0039JobInfo
from openapi_client.models.v0039_job_info_power import V0039JobInfoPower
from openapi_client.models.v0039_job_mcs import V0039JobMcs
from openapi_client.models.v0039_job_required import V0039JobRequired
from openapi_client.models.v0039_job_res import V0039JobRes
from openapi_client.models.v0039_job_reservation import V0039JobReservation
from openapi_client.models.v0039_job_state import V0039JobState
from openapi_client.models.v0039_job_submission import V0039JobSubmission
from openapi_client.models.v0039_job_submission_response import V0039JobSubmissionResponse
from openapi_client.models.v0039_job_time import V0039JobTime
from openapi_client.models.v0039_job_time_system import V0039JobTimeSystem
from openapi_client.models.v0039_job_tres import V0039JobTres
from openapi_client.models.v0039_job_update_response import V0039JobUpdateResponse
from openapi_client.models.v0039_jobs_response import V0039JobsResponse
from openapi_client.models.v0039_license import V0039License
from openapi_client.models.v0039_licenses_info import V0039LicensesInfo
from openapi_client.models.v0039_meta import V0039Meta
from openapi_client.models.v0039_meta_plugin import V0039MetaPlugin
from openapi_client.models.v0039_meta_slurm import V0039MetaSlurm
from openapi_client.models.v0039_meta_slurm_version import V0039MetaSlurmVersion
from openapi_client.models.v0039_node import V0039Node
from openapi_client.models.v0039_nodes_response import V0039NodesResponse
from openapi_client.models.v0039_partition_info import V0039PartitionInfo
from openapi_client.models.v0039_partition_info_accounts import V0039PartitionInfoAccounts
from openapi_client.models.v0039_partition_info_cpus import V0039PartitionInfoCpus
from openapi_client.models.v0039_partition_info_defaults import V0039PartitionInfoDefaults
from openapi_client.models.v0039_partition_info_groups import V0039PartitionInfoGroups
from openapi_client.models.v0039_partition_info_maximums import V0039PartitionInfoMaximums
from openapi_client.models.v0039_partition_info_minimums import V0039PartitionInfoMinimums
from openapi_client.models.v0039_partition_info_nodes import V0039PartitionInfoNodes
from openapi_client.models.v0039_partition_info_priority import V0039PartitionInfoPriority
from openapi_client.models.v0039_partition_info_qos import V0039PartitionInfoQos
from openapi_client.models.v0039_partition_info_timeouts import V0039PartitionInfoTimeouts
from openapi_client.models.v0039_partition_info_tres import V0039PartitionInfoTres
from openapi_client.models.v0039_partitions_response import V0039PartitionsResponse
from openapi_client.models.v0039_pings import V0039Pings
from openapi_client.models.v0039_qos import V0039Qos
from openapi_client.models.v0039_qos_limits import V0039QosLimits
from openapi_client.models.v0039_qos_limits_max import V0039QosLimitsMax
from openapi_client.models.v0039_qos_limits_max_active_jobs import V0039QosLimitsMaxActiveJobs
from openapi_client.models.v0039_qos_limits_max_jobs import V0039QosLimitsMaxJobs
from openapi_client.models.v0039_qos_limits_max_jobs_active_jobs import V0039QosLimitsMaxJobsActiveJobs
from openapi_client.models.v0039_qos_limits_max_jobs_active_jobs_per import V0039QosLimitsMaxJobsActiveJobsPer
from openapi_client.models.v0039_qos_limits_max_tres import V0039QosLimitsMaxTres
from openapi_client.models.v0039_qos_limits_max_tres_minutes import V0039QosLimitsMaxTresMinutes
from openapi_client.models.v0039_qos_limits_max_tres_minutes_per import V0039QosLimitsMaxTresMinutesPer
from openapi_client.models.v0039_qos_limits_max_tres_per import V0039QosLimitsMaxTresPer
from openapi_client.models.v0039_qos_limits_max_wall_clock import V0039QosLimitsMaxWallClock
from openapi_client.models.v0039_qos_limits_max_wall_clock_per import V0039QosLimitsMaxWallClockPer
from openapi_client.models.v0039_qos_limits_min import V0039QosLimitsMin
from openapi_client.models.v0039_qos_limits_min_tres import V0039QosLimitsMinTres
from openapi_client.models.v0039_qos_preempt import V0039QosPreempt
from openapi_client.models.v0039_reservation_core_spec import V0039ReservationCoreSpec
from openapi_client.models.v0039_reservation_info import V0039ReservationInfo
from openapi_client.models.v0039_reservation_info_purge_completed import V0039ReservationInfoPurgeCompleted
from openapi_client.models.v0039_reservations_response import V0039ReservationsResponse
from openapi_client.models.v0039_rollup_stats_inner import V0039RollupStatsInner
from openapi_client.models.v0039_slurm_step_id import V0039SlurmStepId
from openapi_client.models.v0039_stats_msg import V0039StatsMsg
from openapi_client.models.v0039_stats_rec import V0039StatsRec
from openapi_client.models.v0039_stats_rpc import V0039StatsRpc
from openapi_client.models.v0039_stats_rpc_time import V0039StatsRpcTime
from openapi_client.models.v0039_stats_user import V0039StatsUser
from openapi_client.models.v0039_step import V0039Step
from openapi_client.models.v0039_step_cpu import V0039StepCPU
from openapi_client.models.v0039_step_cpu_requested_frequency import V0039StepCPURequestedFrequency
from openapi_client.models.v0039_step_nodes import V0039StepNodes
from openapi_client.models.v0039_step_statistics import V0039StepStatistics
from openapi_client.models.v0039_step_statistics_cpu import V0039StepStatisticsCPU
from openapi_client.models.v0039_step_statistics_energy import V0039StepStatisticsEnergy
from openapi_client.models.v0039_step_step import V0039StepStep
from openapi_client.models.v0039_step_task import V0039StepTask
from openapi_client.models.v0039_step_tasks import V0039StepTasks
from openapi_client.models.v0039_step_time import V0039StepTime
from openapi_client.models.v0039_step_time_system import V0039StepTimeSystem
from openapi_client.models.v0039_step_tres import V0039StepTres
from openapi_client.models.v0039_step_tres_consumed import V0039StepTresConsumed
from openapi_client.models.v0039_step_tres_requested import V0039StepTresRequested
from openapi_client.models.v0039_tres import V0039Tres
from openapi_client.models.v0039_uint16_no_val import V0039Uint16NoVal
from openapi_client.models.v0039_uint32_no_val import V0039Uint32NoVal
from openapi_client.models.v0039_uint64_no_val import V0039Uint64NoVal
from openapi_client.models.v0039_update_node_msg import V0039UpdateNodeMsg
from openapi_client.models.v0039_user import V0039User
from openapi_client.models.v0039_user_default import V0039UserDefault
from openapi_client.models.v0039_warning import V0039Warning
from openapi_client.models.v0039_wckey import V0039Wckey
from openapi_client.models.v0039_wckey_tag import V0039WckeyTag
from openapi_client.models.v0040_acct_gather_energy import V0040AcctGatherEnergy
from openapi_client.models.v0040_assoc_shares_obj_wrap import V0040AssocSharesObjWrap
from openapi_client.models.v0040_assoc_shares_obj_wrap_tres import V0040AssocSharesObjWrapTres
from openapi_client.models.v0040_bf_exit_fields import V0040BfExitFields
from openapi_client.models.v0040_controller_ping import V0040ControllerPing
from openapi_client.models.v0040_cron_entry import V0040CronEntry
from openapi_client.models.v0040_float64_no_val import V0040Float64NoVal
from openapi_client.models.v0040_job_array_response_msg_entry import V0040JobArrayResponseMsgEntry
from openapi_client.models.v0040_job_desc_msg import V0040JobDescMsg
from openapi_client.models.v0040_job_desc_msg_rlimits import V0040JobDescMsgRlimits
from openapi_client.models.v0040_job_info import V0040JobInfo
from openapi_client.models.v0040_job_info_power import V0040JobInfoPower
from openapi_client.models.v0040_job_res import V0040JobRes
from openapi_client.models.v0040_job_submit_req import V0040JobSubmitReq
from openapi_client.models.v0040_job_submit_response_msg import V0040JobSubmitResponseMsg
from openapi_client.models.v0040_kill_jobs_msg import V0040KillJobsMsg
from openapi_client.models.v0040_kill_jobs_resp_job import V0040KillJobsRespJob
from openapi_client.models.v0040_license import V0040License
from openapi_client.models.v0040_node import V0040Node
from openapi_client.models.v0040_openapi_diag_resp import V0040OpenapiDiagResp
from openapi_client.models.v0040_openapi_error import V0040OpenapiError
from openapi_client.models.v0040_openapi_job_info_resp import V0040OpenapiJobInfoResp
from openapi_client.models.v0040_openapi_job_post_response import V0040OpenapiJobPostResponse
from openapi_client.models.v0040_openapi_job_submit_response import V0040OpenapiJobSubmitResponse
from openapi_client.models.v0040_openapi_kill_jobs_resp import V0040OpenapiKillJobsResp
from openapi_client.models.v0040_openapi_licenses_resp import V0040OpenapiLicensesResp
from openapi_client.models.v0040_openapi_meta import V0040OpenapiMeta
from openapi_client.models.v0040_openapi_nodes_resp import V0040OpenapiNodesResp
from openapi_client.models.v0040_openapi_partition_resp import V0040OpenapiPartitionResp
from openapi_client.models.v0040_openapi_ping_array_resp import V0040OpenapiPingArrayResp
from openapi_client.models.v0040_openapi_reservation_resp import V0040OpenapiReservationResp
from openapi_client.models.v0040_openapi_resp import V0040OpenapiResp
from openapi_client.models.v0040_openapi_shares_resp import V0040OpenapiSharesResp
from openapi_client.models.v0040_openapi_warning import V0040OpenapiWarning
from openapi_client.models.v0040_partition_info import V0040PartitionInfo
from openapi_client.models.v0040_partition_info_defaults import V0040PartitionInfoDefaults
from openapi_client.models.v0040_partition_info_maximums import V0040PartitionInfoMaximums
from openapi_client.models.v0040_partition_info_timeouts import V0040PartitionInfoTimeouts
from openapi_client.models.v0040_process_exit_code_verbose import V0040ProcessExitCodeVerbose
from openapi_client.models.v0040_process_exit_code_verbose_signal import V0040ProcessExitCodeVerboseSignal
from openapi_client.models.v0040_reservation_core_spec import V0040ReservationCoreSpec
from openapi_client.models.v0040_reservation_info import V0040ReservationInfo
from openapi_client.models.v0040_reservation_info_purge_completed import V0040ReservationInfoPurgeCompleted
from openapi_client.models.v0040_schedule_exit_fields import V0040ScheduleExitFields
from openapi_client.models.v0040_shares_float128_tres import V0040SharesFloat128Tres
from openapi_client.models.v0040_shares_resp_msg import V0040SharesRespMsg
from openapi_client.models.v0040_shares_uint64_tres import V0040SharesUint64Tres
from openapi_client.models.v0040_stats_msg import V0040StatsMsg
from openapi_client.models.v0040_stats_msg_rpcs_by_type_inner import V0040StatsMsgRpcsByTypeInner
from openapi_client.models.v0040_stats_msg_rpcs_by_user_inner import V0040StatsMsgRpcsByUserInner
from openapi_client.models.v0040_uint16_no_val import V0040Uint16NoVal
from openapi_client.models.v0040_uint32_no_val import V0040Uint32NoVal
from openapi_client.models.v0040_uint64_no_val import V0040Uint64NoVal
from openapi_client.models.v0040_update_node_msg import V0040UpdateNodeMsg
from openapi_client.models.v0041_job_alloc_req import V0041JobAllocReq
from openapi_client.models.v0041_job_desc_msg import V0041JobDescMsg
from openapi_client.models.v0041_job_desc_msg_begin_time import V0041JobDescMsgBeginTime
from openapi_client.models.v0041_job_desc_msg_crontab import V0041JobDescMsgCrontab
from openapi_client.models.v0041_job_desc_msg_crontab_line import V0041JobDescMsgCrontabLine
from openapi_client.models.v0041_job_desc_msg_distribution_plane_size import V0041JobDescMsgDistributionPlaneSize
from openapi_client.models.v0041_job_desc_msg_kill_warning_delay import V0041JobDescMsgKillWarningDelay
from openapi_client.models.v0041_job_desc_msg_memory_per_cpu import V0041JobDescMsgMemoryPerCpu
from openapi_client.models.v0041_job_desc_msg_priority import V0041JobDescMsgPriority
from openapi_client.models.v0041_job_desc_msg_required_switches import V0041JobDescMsgRequiredSwitches
from openapi_client.models.v0041_job_desc_msg_rlimits import V0041JobDescMsgRlimits
from openapi_client.models.v0041_job_desc_msg_rlimits_as import V0041JobDescMsgRlimitsAs
from openapi_client.models.v0041_job_desc_msg_rlimits_core import V0041JobDescMsgRlimitsCore
from openapi_client.models.v0041_job_desc_msg_rlimits_cpu import V0041JobDescMsgRlimitsCpu
from openapi_client.models.v0041_job_desc_msg_rlimits_data import V0041JobDescMsgRlimitsData
from openapi_client.models.v0041_job_desc_msg_rlimits_fsize import V0041JobDescMsgRlimitsFsize
from openapi_client.models.v0041_job_desc_msg_rlimits_memlock import V0041JobDescMsgRlimitsMemlock
from openapi_client.models.v0041_job_desc_msg_rlimits_nofile import V0041JobDescMsgRlimitsNofile
from openapi_client.models.v0041_job_desc_msg_rlimits_nproc import V0041JobDescMsgRlimitsNproc
from openapi_client.models.v0041_job_desc_msg_rlimits_rss import V0041JobDescMsgRlimitsRss
from openapi_client.models.v0041_job_desc_msg_rlimits_stack import V0041JobDescMsgRlimitsStack
from openapi_client.models.v0041_job_desc_msg_segment_size import V0041JobDescMsgSegmentSize
from openapi_client.models.v0041_job_desc_msg_time_limit import V0041JobDescMsgTimeLimit
from openapi_client.models.v0041_job_desc_msg_time_minimum import V0041JobDescMsgTimeMinimum
from openapi_client.models.v0041_job_submit_req import V0041JobSubmitReq
from openapi_client.models.v0041_kill_jobs_msg import V0041KillJobsMsg
from openapi_client.models.v0041_openapi_diag_resp import V0041OpenapiDiagResp
from openapi_client.models.v0041_openapi_diag_resp_statistics import V0041OpenapiDiagRespStatistics
from openapi_client.models.v0041_openapi_diag_resp_statistics_bf_exit import V0041OpenapiDiagRespStatisticsBfExit
from openapi_client.models.v0041_openapi_diag_resp_statistics_bf_when_last_cycle import V0041OpenapiDiagRespStatisticsBfWhenLastCycle
from openapi_client.models.v0041_openapi_diag_resp_statistics_job_states_ts import V0041OpenapiDiagRespStatisticsJobStatesTs
from openapi_client.models.v0041_openapi_diag_resp_statistics_pending_rpcs_by_hostlist_inner import V0041OpenapiDiagRespStatisticsPendingRpcsByHostlistInner
from openapi_client.models.v0041_openapi_diag_resp_statistics_pending_rpcs_inner import V0041OpenapiDiagRespStatisticsPendingRpcsInner
from openapi_client.models.v0041_openapi_diag_resp_statistics_req_time import V0041OpenapiDiagRespStatisticsReqTime
from openapi_client.models.v0041_openapi_diag_resp_statistics_req_time_start import V0041OpenapiDiagRespStatisticsReqTimeStart
from openapi_client.models.v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner import V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner
from openapi_client.models.v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time import V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime
from openapi_client.models.v0041_openapi_diag_resp_statistics_rpcs_by_user_inner import V0041OpenapiDiagRespStatisticsRpcsByUserInner
from openapi_client.models.v0041_openapi_diag_resp_statistics_schedule_exit import V0041OpenapiDiagRespStatisticsScheduleExit
from openapi_client.models.v0041_openapi_job_alloc_resp import V0041OpenapiJobAllocResp
from openapi_client.models.v0041_openapi_job_info_resp import V0041OpenapiJobInfoResp
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner import V0041OpenapiJobInfoRespJobsInner
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_accrue_time import V0041OpenapiJobInfoRespJobsInnerAccrueTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_array_job_id import V0041OpenapiJobInfoRespJobsInnerArrayJobId
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_array_max_tasks import V0041OpenapiJobInfoRespJobsInnerArrayMaxTasks
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_array_task_id import V0041OpenapiJobInfoRespJobsInnerArrayTaskId
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_billable_tres import V0041OpenapiJobInfoRespJobsInnerBillableTres
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cores_per_socket import V0041OpenapiJobInfoRespJobsInnerCoresPerSocket
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cpu_frequency_governor import V0041OpenapiJobInfoRespJobsInnerCpuFrequencyGovernor
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cpu_frequency_maximum import V0041OpenapiJobInfoRespJobsInnerCpuFrequencyMaximum
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cpu_frequency_minimum import V0041OpenapiJobInfoRespJobsInnerCpuFrequencyMinimum
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cpus import V0041OpenapiJobInfoRespJobsInnerCpus
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_cpus_per_task import V0041OpenapiJobInfoRespJobsInnerCpusPerTask
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_deadline import V0041OpenapiJobInfoRespJobsInnerDeadline
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_delay_boot import V0041OpenapiJobInfoRespJobsInnerDelayBoot
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_derived_exit_code import V0041OpenapiJobInfoRespJobsInnerDerivedExitCode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_return_code import V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeReturnCode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_signal import V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeSignal
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_derived_exit_code_signal_id import V0041OpenapiJobInfoRespJobsInnerDerivedExitCodeSignalId
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_eligible_time import V0041OpenapiJobInfoRespJobsInnerEligibleTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_end_time import V0041OpenapiJobInfoRespJobsInnerEndTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_exit_code import V0041OpenapiJobInfoRespJobsInnerExitCode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_het_job_id import V0041OpenapiJobInfoRespJobsInnerHetJobId
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_het_job_offset import V0041OpenapiJobInfoRespJobsInnerHetJobOffset
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources import V0041OpenapiJobInfoRespJobsInnerJobResources
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodes
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInner
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_cpus import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerCpus
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_memory import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerMemory
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_sockets_inner import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerSocketsInner
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_nodes_allocation_inner_sockets_inner_cores_inner import V0041OpenapiJobInfoRespJobsInnerJobResourcesNodesAllocationInnerSocketsInnerCoresInner
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_job_resources_threads_per_core import V0041OpenapiJobInfoRespJobsInnerJobResourcesThreadsPerCore
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_last_sched_evaluation import V0041OpenapiJobInfoRespJobsInnerLastSchedEvaluation
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_max_cpus import V0041OpenapiJobInfoRespJobsInnerMaxCpus
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_max_nodes import V0041OpenapiJobInfoRespJobsInnerMaxNodes
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_memory_per_node import V0041OpenapiJobInfoRespJobsInnerMemoryPerNode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_minimum_cpus_per_node import V0041OpenapiJobInfoRespJobsInnerMinimumCpusPerNode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_minimum_tmp_disk_per_node import V0041OpenapiJobInfoRespJobsInnerMinimumTmpDiskPerNode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_node_count import V0041OpenapiJobInfoRespJobsInnerNodeCount
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_power import V0041OpenapiJobInfoRespJobsInnerPower
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_pre_sus_time import V0041OpenapiJobInfoRespJobsInnerPreSusTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_preempt_time import V0041OpenapiJobInfoRespJobsInnerPreemptTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_preemptable_time import V0041OpenapiJobInfoRespJobsInnerPreemptableTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_resize_time import V0041OpenapiJobInfoRespJobsInnerResizeTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_sockets_per_node import V0041OpenapiJobInfoRespJobsInnerSocketsPerNode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_start_time import V0041OpenapiJobInfoRespJobsInnerStartTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_submit_time import V0041OpenapiJobInfoRespJobsInnerSubmitTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_suspend_time import V0041OpenapiJobInfoRespJobsInnerSuspendTime
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_tasks import V0041OpenapiJobInfoRespJobsInnerTasks
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_tasks_per_board import V0041OpenapiJobInfoRespJobsInnerTasksPerBoard
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_tasks_per_core import V0041OpenapiJobInfoRespJobsInnerTasksPerCore
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_tasks_per_node import V0041OpenapiJobInfoRespJobsInnerTasksPerNode
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_tasks_per_socket import V0041OpenapiJobInfoRespJobsInnerTasksPerSocket
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_tasks_per_tres import V0041OpenapiJobInfoRespJobsInnerTasksPerTres
from openapi_client.models.v0041_openapi_job_info_resp_jobs_inner_threads_per_core import V0041OpenapiJobInfoRespJobsInnerThreadsPerCore
from openapi_client.models.v0041_openapi_job_info_resp_last_backfill import V0041OpenapiJobInfoRespLastBackfill
from openapi_client.models.v0041_openapi_job_info_resp_last_update import V0041OpenapiJobInfoRespLastUpdate
from openapi_client.models.v0041_openapi_job_post_response import V0041OpenapiJobPostResponse
from openapi_client.models.v0041_openapi_job_post_response_results_inner import V0041OpenapiJobPostResponseResultsInner
from openapi_client.models.v0041_openapi_job_submit_response import V0041OpenapiJobSubmitResponse
from openapi_client.models.v0041_openapi_job_submit_response_result import V0041OpenapiJobSubmitResponseResult
from openapi_client.models.v0041_openapi_kill_jobs_resp import V0041OpenapiKillJobsResp
from openapi_client.models.v0041_openapi_kill_jobs_resp_status_inner import V0041OpenapiKillJobsRespStatusInner
from openapi_client.models.v0041_openapi_kill_jobs_resp_status_inner_error import V0041OpenapiKillJobsRespStatusInnerError
from openapi_client.models.v0041_openapi_kill_jobs_resp_status_inner_federation import V0041OpenapiKillJobsRespStatusInnerFederation
from openapi_client.models.v0041_openapi_kill_jobs_resp_status_inner_job_id import V0041OpenapiKillJobsRespStatusInnerJobId
from openapi_client.models.v0041_openapi_licenses_resp import V0041OpenapiLicensesResp
from openapi_client.models.v0041_openapi_licenses_resp_last_update import V0041OpenapiLicensesRespLastUpdate
from openapi_client.models.v0041_openapi_licenses_resp_licenses_inner import V0041OpenapiLicensesRespLicensesInner
from openapi_client.models.v0041_openapi_nodes_resp import V0041OpenapiNodesResp
from openapi_client.models.v0041_openapi_nodes_resp_last_update import V0041OpenapiNodesRespLastUpdate
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner import V0041OpenapiNodesRespNodesInner
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_boot_time import V0041OpenapiNodesRespNodesInnerBootTime
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_energy import V0041OpenapiNodesRespNodesInnerEnergy
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_energy_current_watts import V0041OpenapiNodesRespNodesInnerEnergyCurrentWatts
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_free_mem import V0041OpenapiNodesRespNodesInnerFreeMem
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_last_busy import V0041OpenapiNodesRespNodesInnerLastBusy
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_reason_changed_at import V0041OpenapiNodesRespNodesInnerReasonChangedAt
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_resume_after import V0041OpenapiNodesRespNodesInnerResumeAfter
from openapi_client.models.v0041_openapi_nodes_resp_nodes_inner_slurmd_start_time import V0041OpenapiNodesRespNodesInnerSlurmdStartTime
from openapi_client.models.v0041_openapi_partition_resp import V0041OpenapiPartitionResp
from openapi_client.models.v0041_openapi_partition_resp_last_update import V0041OpenapiPartitionRespLastUpdate
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner import V0041OpenapiPartitionRespPartitionsInner
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_accounts import V0041OpenapiPartitionRespPartitionsInnerAccounts
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_cpus import V0041OpenapiPartitionRespPartitionsInnerCpus
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_defaults import V0041OpenapiPartitionRespPartitionsInnerDefaults
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_defaults_partition_memory_per_cpu import V0041OpenapiPartitionRespPartitionsInnerDefaultsPartitionMemoryPerCpu
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_defaults_partition_memory_per_node import V0041OpenapiPartitionRespPartitionsInnerDefaultsPartitionMemoryPerNode
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_defaults_time import V0041OpenapiPartitionRespPartitionsInnerDefaultsTime
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_groups import V0041OpenapiPartitionRespPartitionsInnerGroups
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums import V0041OpenapiPartitionRespPartitionsInnerMaximums
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_cpus_per_node import V0041OpenapiPartitionRespPartitionsInnerMaximumsCpusPerNode
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_cpus_per_socket import V0041OpenapiPartitionRespPartitionsInnerMaximumsCpusPerSocket
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_nodes import V0041OpenapiPartitionRespPartitionsInnerMaximumsNodes
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_over_time_limit import V0041OpenapiPartitionRespPartitionsInnerMaximumsOverTimeLimit
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_oversubscribe import V0041OpenapiPartitionRespPartitionsInnerMaximumsOversubscribe
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_cpu import V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerCpu
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node import V0041OpenapiPartitionRespPartitionsInnerMaximumsPartitionMemoryPerNode
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_maximums_time import V0041OpenapiPartitionRespPartitionsInnerMaximumsTime
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_minimums import V0041OpenapiPartitionRespPartitionsInnerMinimums
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_nodes import V0041OpenapiPartitionRespPartitionsInnerNodes
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_partition import V0041OpenapiPartitionRespPartitionsInnerPartition
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_priority import V0041OpenapiPartitionRespPartitionsInnerPriority
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_qos import V0041OpenapiPartitionRespPartitionsInnerQos
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_suspend_time import V0041OpenapiPartitionRespPartitionsInnerSuspendTime
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_timeouts import V0041OpenapiPartitionRespPartitionsInnerTimeouts
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_timeouts_resume import V0041OpenapiPartitionRespPartitionsInnerTimeoutsResume
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_timeouts_suspend import V0041OpenapiPartitionRespPartitionsInnerTimeoutsSuspend
from openapi_client.models.v0041_openapi_partition_resp_partitions_inner_tres import V0041OpenapiPartitionRespPartitionsInnerTres
from openapi_client.models.v0041_openapi_ping_array_resp import V0041OpenapiPingArrayResp
from openapi_client.models.v0041_openapi_ping_array_resp_pings_inner import V0041OpenapiPingArrayRespPingsInner
from openapi_client.models.v0041_openapi_reservation_resp import V0041OpenapiReservationResp
from openapi_client.models.v0041_openapi_reservation_resp_last_update import V0041OpenapiReservationRespLastUpdate
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner import V0041OpenapiReservationRespReservationsInner
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_core_specializations_inner import V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_end_time import V0041OpenapiReservationRespReservationsInnerEndTime
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_purge_completed import V0041OpenapiReservationRespReservationsInnerPurgeCompleted
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_purge_completed_time import V0041OpenapiReservationRespReservationsInnerPurgeCompletedTime
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_start_time import V0041OpenapiReservationRespReservationsInnerStartTime
from openapi_client.models.v0041_openapi_reservation_resp_reservations_inner_watts import V0041OpenapiReservationRespReservationsInnerWatts
from openapi_client.models.v0041_openapi_resp import V0041OpenapiResp
from openapi_client.models.v0041_openapi_shares_resp import V0041OpenapiSharesResp
from openapi_client.models.v0041_openapi_shares_resp_errors_inner import V0041OpenapiSharesRespErrorsInner
from openapi_client.models.v0041_openapi_shares_resp_meta import V0041OpenapiSharesRespMeta
from openapi_client.models.v0041_openapi_shares_resp_meta_client import V0041OpenapiSharesRespMetaClient
from openapi_client.models.v0041_openapi_shares_resp_meta_plugin import V0041OpenapiSharesRespMetaPlugin
from openapi_client.models.v0041_openapi_shares_resp_meta_slurm import V0041OpenapiSharesRespMetaSlurm
from openapi_client.models.v0041_openapi_shares_resp_meta_slurm_version import V0041OpenapiSharesRespMetaSlurmVersion
from openapi_client.models.v0041_openapi_shares_resp_shares import V0041OpenapiSharesRespShares
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner import V0041OpenapiSharesRespSharesSharesInner
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_fairshare import V0041OpenapiSharesRespSharesSharesInnerFairshare
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_shares import V0041OpenapiSharesRespSharesSharesInnerShares
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_shares_normalized import V0041OpenapiSharesRespSharesSharesInnerSharesNormalized
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_tres import V0041OpenapiSharesRespSharesSharesInnerTres
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner import V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInner
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_tres_run_seconds_inner_value import V0041OpenapiSharesRespSharesSharesInnerTresRunSecondsInnerValue
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_tres_usage_inner import V0041OpenapiSharesRespSharesSharesInnerTresUsageInner
from openapi_client.models.v0041_openapi_shares_resp_shares_shares_inner_usage_normalized import V0041OpenapiSharesRespSharesSharesInnerUsageNormalized
from openapi_client.models.v0041_openapi_shares_resp_warnings_inner import V0041OpenapiSharesRespWarningsInner
from openapi_client.models.v0041_update_node_msg import V0041UpdateNodeMsg
from openapi_client.models.v0041_update_node_msg_resume_after import V0041UpdateNodeMsgResumeAfter
from openapi_client.models.v0041_update_node_msg_weight import V0041UpdateNodeMsgWeight
