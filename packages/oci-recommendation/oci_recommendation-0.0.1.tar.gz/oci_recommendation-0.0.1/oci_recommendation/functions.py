# Enters details to res
import datetime

import oci.core
from dateutil.relativedelta import relativedelta

# contains the description messages for recommendations
r_msgs = {
    'del_instance': "CPU Utilization of instance is less than 3% from last 7 days",
    'purge boot vol': "The Boot Volume is unattached, can be purged",
    'purge vol': "The volume is unattached, can be purged",
    'enable monitoring': "Monitoring is not enabled in Instance, should be enabled ",
    'enable olm': 'The Enable object lifecycle management recommendation indicates that no lifecycle policy rules exist for a Object Storage bucket in your tenancy. Object versioning increases your storage costs because the resource includes multiple versions of the same object. Consider using Object Lifecycle Management to help manage object versions automatically.',
    'enable tuning': 'The Enable performance auto-tuning for boot volumes recommendation indicates that a boot volume is using suboptimal performance settings. Implementing this recommendation improves performance of the volume. The auto-tune feature automatically shifts performance between lower cost, balanced, and higher performance as necessary to optimize utilization of each volume. With the auto-tune feature enabled, you do not need to continually manage volume resources.',

}


# inserts the data into the provided list
def insert_to_res(res: list, Id: str, r_type: str, recommendation: str, datapoints=None, description=None) -> list:
    res.append(
        {
            'Resource Id': Id,
            'Resource Type': r_type,
            'Recommendation': recommendation,
            'Description': description,
            'Datapoints': datapoints
        }
    )
    return res


# returns the list of instances
def list_instances(self, compartment_id: str) -> list:
    instance_lst = []
    core_client = oci.core.ComputeClient(self.config)

    list_instances_response = core_client.list_instances(
        compartment_id=compartment_id,
        sort_by="TIMECREATED"
    )

    for item in list_instances_response.data:
        temp = {
            'id': item.id,
            'tags': item.defined_tags,
            'display_name': item.display_name,
            'region': item.region,
            'time_created': item.time_created
        }
        instance_lst.append(temp)

    return instance_lst


# returns the list of boot volumes
def list_boot_volumes(self, compartment_id: str) -> list:
    core_client = oci.core.BlockstorageClient(self.config)
    boot_volumes = []

    list_boot_volumes_response = core_client.list_boot_volumes(
        compartment_id=compartment_id
    )
    for item in list_boot_volumes_response.data:
        temp = {
            'id': item.id,
            'tags': item.defined_tags,
            'display_name': item.display_name,
            'time_created': item.time_created,
            'availability_domain': item.availability_domain,
            'is_auto_tune_enabled': item.is_auto_tune_enabled
        }
        boot_volumes.append(temp)
    return boot_volumes


def list_volumes(self, compartment_id: str) -> list:
    core_client = oci.core.BlockstorageClient(self.config)
    volumes = []

    list_volumes_response = core_client.list_volumes(
        compartment_id=compartment_id
    )
    for item in list_volumes_response.data:
        temp = {
            'id': item.id,
            'tags': item.defined_tags,
            'display_name': item.display_name,
            'time_created': item.time_created,
            'availability_domain': item.availability_domain,
            'is_auto_tune_enabled': item.is_auto_tune_enabled
        }
        volumes.append(temp)
    return volumes


# return the memory utilization datapoints of instances
def get_memory_datapoints(self, compartment_id: str, namespace: str) -> list:
    datapoints = []
    start_time = datetime.datetime.now()
    start_time = start_time - relativedelta(days=7)
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

    end_time = datetime.datetime.now()
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)

    MonitoringClient = oci.monitoring.MonitoringClient(self.config)

    summarize_metrics_data_response = MonitoringClient.summarize_metrics_data(
        compartment_id=compartment_id,
        summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
            namespace=namespace,
            query="(MemoryUtilization[24h].avg())",
            start_time=start_time,
            end_time=end_time
        ),
        compartment_id_in_subtree=False
    )

    for st in summarize_metrics_data_response.data:
        temp = {
            'id': st.dimensions['resourceId'],
            'datapoints': st.aggregated_datapoints,
            'region': st.dimensions['region']
        }
        datapoints.append(temp)
    return datapoints


# returns cpu utilization datapoints of instances
def get_cpu_datapoints(self, compartment_id: str, namespace: str) -> list:
    datapoints = []
    start_time = datetime.datetime.now()
    start_time = start_time - relativedelta(days=7)
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

    end_time = datetime.datetime.now()
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)

    MonitoringClient = oci.monitoring.MonitoringClient(self.config)

    summarize_metrics_data_response = MonitoringClient.summarize_metrics_data(
        compartment_id=compartment_id,
        summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
            namespace=namespace,
            query="(CpuUtilization[24h].avg())",
            start_time=start_time,
            end_time=end_time
        ),
        compartment_id_in_subtree=False
    )

    for st in summarize_metrics_data_response.data:
        temp = {
            'id': st.dimensions['resourceId'],
            'datapoints': st.aggregated_datapoints,
            'region': st.dimensions['region']
        }
        datapoints.append(temp)
    return datapoints


# provides the recommendations for deleting the idle instances
def del_idle_instance_recommendation(self, compId: str, namespace: str) -> list:
    res = []
    response_cpu = get_cpu_datapoints(self, compId, namespace)
    # response_mem = get_memory_datapoints(self, compId, namespace)
    # print(response_mem)

    for item in response_cpu:
        if len(item['datapoints']) < 7:
            continue

        recommend_flag = True
        for dp in item['datapoints']:
            if dp.value > 3:
                recommend_flag = False
                break

        if recommend_flag:
            res = insert_to_res(
                res, item['id'], "Compute Instance",
                "Delete Idle Compute Instance",
                str('cpu datapoints:' + item['datapoints']),
                r_msgs['del_instance']
            )

    return res


# provide recommendation for purging the unattached boot volumes
def purge_unattached_boot_volume(self, compId: str) -> list:
    res = []
    boot_volumes = list_boot_volumes(self, compId)
    # print(boot_volumes)

    core_client = oci.core.ComputeClient(self.config)

    for boot_vol in boot_volumes:
        list_boot_volume_attachments_response = core_client.list_boot_volume_attachments(
            availability_domain=boot_vol['availability_domain'],
            compartment_id=compId,
            # limit=584,
            # page="EXAMPLE-page-Value",
            # instance_id="ocid1.test.oc1..<unique_ID>EXAMPLE-instanceId-Value",
            boot_volume_id=boot_vol['id']
        )

        # Get the data from response
        # print(list_boot_volume_attachments_response.data)

        if len(list_boot_volume_attachments_response.data) <= 0:
            res = insert_to_res(
                res, boot_vol['id'], "Boot Volume",
                "Purge Unattached boot volume",
                description=r_msgs['purge boot vol']
            )
    return res


# purge unattached volume
def purge_unattached_volume(self, compId: str) -> list:
    res = []
    volumes = list_volumes(self, compId)
    # print(volumes)

    core_client = oci.core.ComputeClient(self.config)

    for boot_vol in volumes:
        list_volume_attachments_response = core_client.list_volume_attachments(
            # availability_domain=boot_vol['availability_domain'],
            compartment_id=compId,
            # limit=584,
            # page="EXAMPLE-page-Value",
            # instance_id="ocid1.test.oc1..<unique_ID>EXAMPLE-instanceId-Value",
            boot_volume_id=boot_vol['id']
        )

        # Get the data from response
        # print(list_volume_attachments_response.data)

        if len(list_volume_attachments_response.data) <= 0:
            res = insert_to_res(
                res, boot_vol['id'], "Volume",
                "Purge Unattached volume",
                description=r_msgs['purge vol']
            )
    return res


# generates recommendation for enabling monitoring on compute instances
def enable_monitoring_for_instances(self, compId: str) -> list:
    res = []
    instance_lst = list_instances(self, compId)
    # print(instance_lst)

    core_client = oci.core.ComputeClient(self.config)
    for instance in instance_lst:
        get_instance_response = core_client.get_instance(
            instance_id=instance['id']
        )
        flag = get_instance_response.data.agent_config.is_monitoring_disabled

        if not flag:
            res = insert_to_res(
                res, instance['id'], "Compute Instance",
                "Enable Monitoring",
                description=r_msgs['enable monitoring']
            )
    return res


# generates recommendation for enable object lifecycle management on buckets
def enable_olm(self, compId: str) -> list:
    res = []

    start_time = datetime.datetime.now()
    start_time = start_time - relativedelta(days=1)
    start_time = start_time.replace(hour=0, minute=0, second=0, microsecond=0)

    end_time = datetime.datetime.now()
    end_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)

    monitoring_client = oci.monitoring.MonitoringClient(self.config)
    summarize_metrics_data_response = monitoring_client.summarize_metrics_data(
        compartment_id=compId,
        summarize_metrics_data_details=oci.monitoring.models.SummarizeMetricsDataDetails(
            namespace='oci_objectstorage',
            query="(EnabledOLM[24h].avg())",
            start_time=start_time,
            end_time=end_time
        ),
        compartment_id_in_subtree=False
    )
    for item in summarize_metrics_data_response.data:
        try:
            dp = item.aggregated_datapoints[1].value
        except:
            try:
                dp = item.aggregated_datapoints[0].value
            except:
                continue
        if dp == 0:
            res = insert_to_res(
                res, item.dimensions['resourceID'], "Bucket",
                "Enable Object Lifecycle Management",
                description=r_msgs['enable olm']
            )
    return res


# generates recommendation for enable performance auto-tuning for boot volumes
def enable_performance_auto_tuning_for_boot_vol(self, compId: str) -> list:
    res = []
    boot_volumes = list_boot_volumes(self, compId)
    # print(boot_volumes)

    core_client = oci.core.ComputeClient(self.config)

    for boot_vol in boot_volumes:
        if not boot_vol['is_auto_tune_enabled']:
            res = insert_to_res(
                res, boot_vol['id'], "Boot Volume",
                "Enable performance auto-tuning",
                description=r_msgs['enable tuning']
            )
    return res


# generates recommendation for enable performance auto-tuning for block volumes
def enable_performance_auto_tuning_for_block_vol(self, compId: str) -> list:
    res = []
    block_volumes = list_volumes(self, compId)
    # print(boot_volumes)

    core_client = oci.core.ComputeClient(self.config)

    for block_vol in block_volumes:
        if not block_vol['is_auto_tune_enabled']:
            res = insert_to_res(
                res, block_vol['id'], "Block Volume",
                "Enable performance auto-tuning",
                description=r_msgs['enable tuning'].replace('boot','block')
            )
    return res


# aggregates all the recommendations
def get_recommendations(self, compId: str, namespace: str) -> list:
    res = []
    res.extend(purge_unattached_boot_volume(self, compId))
    res.extend(del_idle_instance_recommendation(self, compId, namespace))
    res.extend(purge_unattached_volume(self, compId))
    res.extend(enable_monitoring_for_instances(self, compId))
    res.extend(enable_olm(self, compId))
    res.extend(enable_performance_auto_tuning_for_block_vol(self, compId))
    res.extend(enable_performance_auto_tuning_for_boot_vol(self, compId))

    return res
# end of the code
