import oci
from oci_recommendation import functions as fn


class oci_client:
    def __init__(self, config_file_path):
        self.config = oci.config.from_file(config_file_path)

    get_recommendations = fn.get_recommendations
    del_idle_instances = fn.del_idle_instance_recommendation
    purge_unattached_boot_volume = fn.purge_unattached_boot_volume
    purge_unattached_volume = fn.purge_unattached_volume
    enable_monitoring_for_instances = fn.enable_monitoring_for_instances
    enable_olm = fn.enable_olm
    enable_performance_auto_tuning_for_boot_vol = fn.enable_performance_auto_tuning_for_boot_vol
    enable_performance_auto_tuning_for_block_vol = fn.enable_performance_auto_tuning_for_block_vol

    # list_instances = fn.list_instances
    # list_boot_volumes = fn.list_boot_volumes
    # list_block_volumes = fn.list_volumes


# end of the code
