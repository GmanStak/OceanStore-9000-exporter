from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry

REGISTRY = CollectorRegistry(auto_describe=False)

# 集群系统基本信息
hw_cluster_info = Gauge("cluster_info","集群系统基本信息",['id','name','manageIPs','version'],registry=REGISTRY)
hw_cluster_health_status = Gauge("cluster_health_status",
                                 "系统健康状态。参数取值：0：未知1：正常2：故障4：部分损坏5：降级",
                                 ['id','name'],registry=REGISTRY)
hw_cluster_running_status = Gauge("cluster_running_status",
                                  "系统运行状态。参数取值：1：正常2：运行3：未运行6：正在启动28：离线47：正在下电51：正在升级",
                                  ['id','name'],registry=REGISTRY)
hw_cluster_system_capacity = Gauge("cluster_system_capacity","系统总的可用容量.单位：MB",['id','name'],registry=REGISTRY)
hw_cluster_system_used_capacity = Gauge("cluster_system_used_capacity","系统已使用容量.单位：MB",['id','name'],registry=REGISTRY)
hw_cluster_preAvailiableCapacity = Gauge("cluster_preAvailiableCapacity","预测可用容量.单位：MB",['id','name'],registry=REGISTRY)
hw_cluster_bandwidth = Gauge("cluster_bandwidth","集群带宽：（KB/s）",['id','name'],registry=REGISTRY)
hw_cluster_read_bandwidth = Gauge("cluster_read_bandwidth","集群读带宽：（KB/s）",['id','name'],registry=REGISTRY)
hw_cluster_write_bandwidth = Gauge("cluster_write_bandwidth","集群写带宽：（KB/s）",['id','name'],registry=REGISTRY)
hw_cluster_ops = Gauge("cluster_ops","集群OPS：（个/s）",['id','name'],registry=REGISTRY)
hw_cluster_read_ops = Gauge("cluster_read_ops","集群读OPS：（个/s）",['id','name'],registry=REGISTRY)
hw_cluster_write_ops = Gauge("cluster_write_ops","集群写OPS：（个/s）",['id','name'],registry=REGISTRY)


# 集群节点信息
hw_node_info =  Gauge("node_info","集群节点基本信息",['id','associateObjID','devSn','manIP','parentID','name','slotNum','devType','role','time'],registry=REGISTRY)
hw_node_health_status =  Gauge("node_health_status","健康状态。参数取值：0：未知1：正常2：故障4：部分损坏",['id','associateObjID','name','parentID'],registry=REGISTRY)
hw_node_running_staus = Gauge("node_running_staus","运行状态。参数取值：2：运行6：正在启动27：在线28：离线55：在线禁用56：离线禁用57：在线冻结58：离线冻结59：已关闭",
                              ['id','associateObjID','name','parentID'],registry=REGISTRY)
hw_node_bandwidth = Gauge("node_bandwidth","节点读带宽：（KB/s）",['id','associateObjID','name','parentID'],registry=REGISTRY)
hw_node_read_bandwidth = Gauge("node_read_bandwidth","节点读带宽：（KB/s）",['id','associateObjID','name','parentID'],registry=REGISTRY)
hw_node_write_bandwidth = Gauge("node_write_bandwidth","节点写带宽：（KB/s）",['id','associateObjID','name','parentID'],registry=REGISTRY)

# 节点池信息
hw_nodepool_info = Gauge("nodepool_info","节点池信息",['id','name','capThrehold','readOnlyThrehold','recoverValue','recoverReadOnlyValue'],registry=REGISTRY)
hw_nodepool_total_hdd_cap = Gauge("nodepool_total_hdd_cap","HDD总容量。单位：MB",['id','name'],registry=REGISTRY)
hw_nodepool_used_hdd_cap = Gauge("nodepool_used_hdd_cap","HDD已用容量。单位：MB",['id','name'],registry=REGISTRY)
hw_nodepool_total_ssd_cap = Gauge("nodepool_total_ssd_cap","SSD总容量。单位：MB",['id','name'],registry=REGISTRY)
hw_nodepool_used_ssd_cap = Gauge("nodepool_used_ssd_cap","SSD已用容量。单位：MB",['id','name'],registry=REGISTRY)

# 节点文件系统服务信息
hw_node_fs_health_status = Gauge("node_fs_health_status","健康状态。参数取值：0：未知1：正常2：故障",['id','name'],registry=REGISTRY)
hw_node_fs_running_status = Gauge("node_fs_running_status","运行状态。参数取值：1：正常2：运行3：未运行",['id','name'],registry=REGISTRY)
hw_node_fs_capacity = Gauge("node_fs_capacity","系统提供总的可用容量(未计算RAID)。单位：MB",['id','name'],registry=REGISTRY)
hw_node_fs_used_capacity = Gauge("node_fs_used_capacity","系统已用容量（未计算RAID）。单位：MB",['id','name'],registry=REGISTRY)

# CPU信息
hw_cpu_info = Gauge("cpu_info","CPU信息",['id','healthStatus','coreTemp','volts','workFrequency','currentFrequency','frequencySwitch','coreNum','model','cacheSize'],registry=REGISTRY)

# 内存信息
hw_memory_info = Gauge("memory_info","内存信息",['id','SN','capacity','vendor'],registry=REGISTRY)

# 硬盘全局信息
hw_disk_global_info = Gauge("disk_global_info","硬盘全局信息:单位字节",['diskType','capacity'],registry=REGISTRY)

# 硬盘信息
hw_disk_info = Gauge("disk_info","硬盘信息",['id','diskType','model','firmwareVer','manufacturer','serialNumber','runTime','logicType','remainLife','speedRPM'],registry=REGISTRY)
hw_disk_health_status = Gauge("disk_heath_status","健康状态。参数取值：0：未知1：正常2：故障",['id','diskType'],registry=REGISTRY)
hw_disk_running_status = Gauge("disk_running_status","运行状态。参数取值：0：未知4：不存在27：在线",['id','diskType'],registry=REGISTRY)
hw_disk_sectors_num = Gauge("disk_sectors_num","扇区数量。",['id','diskType'],registry=REGISTRY)
hw_disk_sectors_size = Gauge("disk_sectors_size","扇区大小。单位：Byte",['id','diskType'],registry=REGISTRY)
hw_disk_temperature = Gauge("disk_temperature","温度。单位：℃",['id','diskType'],registry=REGISTRY)
hw_disk_bandwidth = Gauge("disk_bandwidth","接口带宽。单位：MB/s",['id','diskType'],registry=REGISTRY)


# 目录配额信息
hw_fsquota_info = Gauge("fsquota_info","目录配额信息",['id','parentID','active','treeName','quotaType','fileSystemID'],registry=REGISTRY)
hw_fsquota_hardLimit = Gauge("fsquota_hardLimit","硬阈值备注：数组元素取值与ResourceType对应(容量、文件数)，其中容量单位为GB，文件数单位为千。",['id','parentID','treeName'],registry=REGISTRY)
hw_fsquota_softLimit = Gauge("fsquota_softLimit","软阈值备注：数组元素取值与ResourceType对应(容量、文件数)，其中容量单位为GB，文件数单位为千。",['id','parentID','treeName'],registry=REGISTRY)
hw_fsquota_amountUsed = Gauge("fsquota_amountUsed","已使用的配额数量备注：取值与ResourceType对应(容量、文件数) ，其中容量单位为MB，文件数单位为个。",['id','parentID','treeName'],registry=REGISTRY)
hw_fsquota_adviseLimit = Gauge("fsquota_adviseLimit","建议阈值备注：数组元素取值与ResourceType对应(容量、文件数)，其中容量单位为GB，文件数单位为千。",['id','parentID','treeName'],registry=REGISTRY)
