# V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs

Maximum number of jobs which can be in a pending or running state at any time in this association and its children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional] 
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional] 
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional] 

## Example

```python
from slurm_client.models.v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs import V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs from a JSON string
v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs_instance = V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs.to_json())

# convert the object into a dict
v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs_dict = v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs_instance.to_dict()
# create an instance of V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs from a dict
v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs_from_dict = V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs.from_dict(v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


