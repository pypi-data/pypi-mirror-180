# NexusInsightsApiV1SoftwareManagementPrevalidationsGet200ResponseEntriesInner

Response entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Config ID for a previous run of pre-validation check | [optional] 
**devices** | [**[NexusInsightsApiV1SoftwareManagementPrevalidationsGet200ResponseEntriesInnerDevicesInner]**](NexusInsightsApiV1SoftwareManagementPrevalidationsGet200ResponseEntriesInnerDevicesInner.md) | List of devices | [optional] 
**end_time** | **str** | End timestamp of validation check | [optional] 
**fabric_name** | **str** | Name of the site | [optional] 
**failed_validation_count** | **float** | No. of validation checks failed | [optional] 
**instance_id** | **str** | Instance ID for a previous run of pre-validation check | [optional] 
**job_name** | **str** | Name of the job | [optional] 
**last_update_time** | **str** | Last timestamp updated | [optional] 
**passed_validation_count** | **float** | No. of validation checks passed | [optional] 
**recommendation_id** | **str** | Recommendation ID | [optional] 
**site_name** | **str** | Name of the site | [optional] 
**start_time** | **str** | Start timestamp of validation check | [optional] 
**status** | **str** | Status of validation check | [optional] 
**target_version** | **str** | Target version to upgrade to | [optional] 
**user_name** | **str** | Username | [optional] 
**validation_results** | [**[NexusInsightsApiV1SoftwareManagementPrevalidationsGet200ResponseEntriesInnerValidationResultsInner]**](NexusInsightsApiV1SoftwareManagementPrevalidationsGet200ResponseEntriesInnerValidationResultsInner.md) | Validation results | [optional] 
**validation_type** | **str** | Type of validation check | [optional] 
**vendor** | **str** | Vendor | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


