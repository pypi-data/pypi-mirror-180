# NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200ResponseEntriesInner

Response entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str** | Config ID for a previous run of pre-validation check | [optional] 
**delta_date1** | **str** | Delta start timestamp | [optional] 
**delta_date2** | **str** | Delta end timestamp | [optional] 
**delta_ts1** | **str** | Delta start timestamp | [optional] 
**delta_ts2** | **str** | Delta end timestamp | [optional] 
**devices** | [**[NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200ResponseEntriesInnerDevicesInner]**](NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200ResponseEntriesInnerDevicesInner.md) | List of devices | [optional] 
**end_time** | **str** | End timestamp of epoch | [optional] 
**epoch_snapshot1** | **str** | Snapshot of fabric run time state | [optional] 
**error_message** | **str** | Error message | [optional] 
**expiry_time** | **str** | Validation expiry timestamp | [optional] 
**fabric_name** | **str** | Name of the site | [optional] 
**failed_validation_count** | **float** | No. of validation checks failed | [optional] 
**failed_validations_count** | **int** | No. of validation checks failed | [optional] 
**instance_id** | **str** | Instance ID for a previous run of pre-validation check | [optional] 
**job_name** | **str** | Name of the job | [optional] 
**last_update_time** | **str** | Timestamp of last update | [optional] 
**latest_pre_validation_date** | **str** | Latest timestamp of pre-validation checks | [optional] 
**latest_pre_validation_ts** | **str** | Latest timestamp of pre-validation checks | [optional] 
**passed_validation_count** | **float** | No. of validation checks passed | [optional] 
**passed_validations_count** | **int** | No. of validation checks passed | [optional] 
**recommendation_id** | **str** | Recommendation ID | [optional] 
**sensei_job_id** | **str** | Sensei job ID | [optional] 
**site_name** | **str** | Name of the site | [optional] 
**start_time** | **str** | Start timestamp of epoch | [optional] 
**status** | **str** | Status of the job | [optional] 
**target_version** | **str** | Target version to upgrade to | [optional] 
**user_name** | **str** | Username | [optional] 
**validation_expiry_time** | **str** | Timestamp of validation expiry | [optional] 
**validation_job_status** | **str** | Validation job status | [optional] 
**validation_results** | [**[NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200ResponseEntriesInnerValidationResultsInner]**](NexusInsightsApiV1SoftwareManagementPostvalidationDetailsGet200ResponseEntriesInnerValidationResultsInner.md) | Validation results | [optional] 
**validation_type** | **str** | Type of validation check | [optional] 
**vendor** | **str** | Vendor | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


