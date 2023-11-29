from prom_metrics import *
from meticsapi import *
from arguments import get_config,get_args

args = get_args()
config_path = args.config
host, port, username, password, parentID_list = get_config(config_path)

def metics():
    clear_metrics()
    Storage = OceanStor(host=host, port=port, username=username, password=password, timeout=10)
    Storage.login()
    cpu = Storage.get_cpu()
    for cpu_info in cpu['data']:
        hw_cpu_info.labels(id=cpu_info['id'],
                           healthStatus=cpu_info['healthStatus'],
                           coreTemp=cpu_info['coreTemp'], volts=cpu_info['volts'],
                           workFrequency=cpu_info['workFrequency'],
                           currentFrequency=cpu_info['currentFrequency'], frequencySwitch=cpu_info['frequencySwitch'],
                           coreNum=cpu_info['coreNum'], model=cpu_info['model'], cacheSize=cpu_info['cacheSize']).set(1)
    memory = Storage.get_memory()
    for memory_info in memory['data']:
        hw_memory_info.labels(id=memory_info['id'], SN=memory_info['SN'], capacity=memory_info['capacity'],
                              vendor=memory_info['vendor']).set(1)
    disk = Storage.get_disk()
    for disk_info in disk['data']:
        hw_disk_health_status.labels(id=disk_info['id'], diskType=disk_info['diskType']).set(
            int(disk_info['healthStatus']))
        hw_disk_running_status.labels(id=disk_info['id'], diskType=disk_info['diskType']).set(
            int(disk_info['runningStatus']))
        hw_disk_sectors_num.labels(id=disk_info['id'], diskType=disk_info['diskType']).set(int(disk_info['sectors']))
        hw_disk_sectors_size.labels(id=disk_info['id'], diskType=disk_info['diskType']).set(
            float(disk_info['sectorSize']))
        hw_disk_temperature.labels(id=disk_info['id'], diskType=disk_info['diskType']).set(
            float(disk_info['temperature']))
        hw_disk_bandwidth.labels(id=disk_info['id'], diskType=disk_info['diskType']).set(float(disk_info['bandwidth']))
    cluster = Storage.get_cluster_info()
    for cluster_info in cluster['data']:
        hw_cluster_info.labels(id=cluster_info['id'], name=cluster_info['name'], manageIPs=cluster_info['manageIPs'],
                               version=cluster_info['version']).set(1)
        hw_cluster_health_status.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            int(cluster_info['healthStatus']))
        hw_cluster_running_status.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            int(cluster_info['runningStatus']))
        hw_cluster_system_capacity.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            float(cluster_info['systemCapacity']))
        hw_cluster_system_used_capacity.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            float(cluster_info['systemUsedCapacity']))
        hw_cluster_preAvailiableCapacity.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            float(cluster_info['preAvailiableCapacity']))

        cluster_ops_info = Storage.get_global_api(type_id=cluster_info['type'], device_id=cluster_info['id'],
                                                  metric_id="182")
        cluster_ops = cluster_ops_info['data'][0]['CMO_STATISTIC_DATA']
        hw_cluster_ops.labels(id=cluster_info['id'], name=cluster_info['name']).set(int(cluster_ops))

        cluster_read_ops_info = Storage.get_global_api(type_id=cluster_info['type'], device_id=cluster_info['id'],
                                                       metric_id="232")
        cluster_read_ops = cluster_read_ops_info['data'][0]['CMO_STATISTIC_DATA']
        hw_cluster_read_ops.labels(id=cluster_info['id'], name=cluster_info['name']).set(int(cluster_read_ops))

        cluster_write_ops_info = Storage.get_global_api(type_id=cluster_info['type'], device_id=cluster_info['id'],
                                                        metric_id="233")
        cluster_write_ops = cluster_write_ops_info['data'][0]['CMO_STATISTIC_DATA']
        hw_cluster_write_ops.labels(id=cluster_info['id'], name=cluster_info['name']).set(int(cluster_write_ops))

        cluster_bandwidth_info = Storage.get_global_api(type_id=cluster_info['type'], device_id=cluster_info['id'],
                                                        metric_id="236")
        cluster_bandwidth = cluster_bandwidth_info['data'][0]['CMO_STATISTIC_DATA']
        hw_cluster_bandwidth.labels(id=cluster_info['id'], name=cluster_info['name']).set(int(cluster_bandwidth))

        cluster_read_bandwidth_info = Storage.get_global_api(type_id=cluster_info['type'], device_id=cluster_info['id'],
                                                             metric_id="123")
        cluster_read_bandwidth = cluster_read_bandwidth_info['data'][0]['CMO_STATISTIC_DATA']
        hw_cluster_read_bandwidth.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            int(cluster_read_bandwidth))

        cluster_write_bandwidth_info = Storage.get_global_api(type_id=cluster_info['type'],
                                                              device_id=cluster_info['id'], metric_id="123")
        cluster_write_bandwidth = cluster_write_bandwidth_info['data'][0]['CMO_STATISTIC_DATA']
        hw_cluster_write_bandwidth.labels(id=cluster_info['id'], name=cluster_info['name']).set(
            int(cluster_write_bandwidth))

    node = Storage.get_sys_node()
    for node_info in node['data']:
        hw_node_info.labels(id=node_info['id'], associateObjID=node_info['associateObjID'],
                            devSn=node_info['devSn'], manIP=node_info['manIP'], parentID=node_info['parentID'],
                            name=node_info['name'], slotNum=node_info['slotNum'], devType=node_info['devType'],
                            role=['role'], time=node_info['time']).set(1)
        hw_node_health_status.labels(id=node_info['id'], associateObjID=node_info['associateObjID'],
                                     parentID=node_info['parentID'], name=node_info['name']).set(
            int(node_info['healthStatus']))
        hw_node_running_staus.labels(id=node_info['id'], associateObjID=node_info['associateObjID'],
                                     parentID=node_info['parentID'], name=node_info['name']).set(
            int(node_info['runningStatus']))

        node_bind_info = Storage.get_global_api(type_id=node_info['type'], device_id=node_info['id'], metric_id="236")
        node_bind = node_bind_info['data'][0]['CMO_STATISTIC_DATA']
        hw_node_bandwidth.labels(id=node_info['id'], associateObjID=node_info['associateObjID'],
                                 parentID=node_info['parentID'], name=node_info['name']).set(int(node_bind))

        node_read_bind_info = Storage.get_global_api(type_id=node_info['type'], device_id=node_info['id'],
                                                     metric_id="123")
        node_read_bind = node_read_bind_info['data'][0]['CMO_STATISTIC_DATA']
        hw_node_read_bandwidth.labels(id=node_info['id'], associateObjID=node_info['associateObjID'],
                                      parentID=node_info['parentID'], name=node_info['name']).set(int(node_read_bind))

        node_write_bind_info = Storage.get_global_api(type_id=node_info['type'], device_id=node_info['id'],
                                                      metric_id="124")
        node_write_bind = node_write_bind_info['data'][0]['CMO_STATISTIC_DATA']
        hw_node_write_bandwidth.labels(id=node_info['id'], associateObjID=node_info['associateObjID'],
                                       parentID=node_info['parentID'], name=node_info['name']).set(int(node_write_bind))
    nodepool_info = Storage.get_nodePool()
    for nodepool in nodepool_info['data']:
        hw_nodepool_info.labels(id=nodepool['id'], name=nodepool['name'], capThrehold=nodepool['capThrehold'],
                                readOnlyThrehold=nodepool['readOnlyThrehold'], recoverValue=nodepool['recoverValue'],
                                recoverReadOnlyValue=nodepool['recoverReadOnlyValue']).set(1)
        hw_nodepool_total_hdd_cap.labels(id=nodepool['id'], name=nodepool['name']).set(float(nodepool['totalHDDCap']))
        hw_nodepool_used_hdd_cap.labels(id=nodepool['id'], name=nodepool['name']).set(float(nodepool['usedHDDCap']))
        hw_nodepool_used_ssd_cap.labels(id=nodepool['id'], name=nodepool['name']).set(float(nodepool['usedSSDCap']))
        hw_nodepool_total_ssd_cap.labels(id=nodepool['id'], name=nodepool['name']).set(float(nodepool['totalSSDCap']))

    node_fs_info = Storage.get_node_fs_service()
    for node_fs in node_fs_info['data']:
        hw_node_fs_health_status.labels(id=node_fs['id'], name=node_fs['name']).set(int(node_fs['healthStatus']))
        hw_node_fs_running_status.labels(id=node_fs['id'], name=node_fs['name']).set(int(node_fs['runningStatus']))
        hw_node_fs_capacity.labels(id=node_fs['id'], name=node_fs['name']).set(int(node_fs['capacity']))
        hw_node_fs_used_capacity.labels(id=node_fs['id'], name=node_fs['name']).set(int(node_fs['usedCapacity']))

    fsquota_info = Storage.get_fsquota()
    for fsquota in fsquota_info['data']:
        hw_fsquota_info.labels(id=fsquota['id'], parentID=fsquota['parentID'], active=fsquota['active'],
                               treeName=fsquota['treeName'],
                               quotaType=fsquota['quotaType'], fileSystemID=fsquota['fileSystemID']).set(1)
        hardLimit = fsquota['hardLimit'].replace("[", "").replace("]", "")
        softLimit = fsquota['softLimit'].replace("[", "").replace("]", "")
        amountUsed = fsquota['amountUsed'].replace("[", "").replace("]", "")
        adviseLimit = fsquota['adviseLimit'].replace("[", "").replace("]", "")
        hw_fsquota_hardLimit.labels(id=fsquota['id'], parentID=fsquota['parentID'], treeName=fsquota['treeName']).set(
            int(hardLimit))
        hw_fsquota_softLimit.labels(id=fsquota['id'], parentID=fsquota['parentID'], treeName=fsquota['treeName']).set(
            int(softLimit))
        hw_fsquota_amountUsed.labels(id=fsquota['id'], parentID=fsquota['parentID'], treeName=fsquota['treeName']).set(
            float(amountUsed))
        hw_fsquota_adviseLimit.labels(id=fsquota['id'], parentID=fsquota['parentID'], treeName=fsquota['treeName']).set(
            float(adviseLimit))
    for parentID in parentID_list:
        account_info = Storage.get_allfsquota(parentID)
        for account in account_info['data']:
            quotaCapacity = account['quotaCapacity']
            hw_account_quotaCapacity.labels(id=account['parentID']).set(quotaCapacity)

    Storage.logout()
