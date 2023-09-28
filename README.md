# OceanStore-9000-exporter
# 说明：
    基于python Flask创建的exporter，集中采集华为OceanStore 9000存储API，删除后生成Metrics
# 参数说明
    “--address” 指定集中采集器的外部访问IP地址，即配置在哪个服务器上就写该服务器IP地址，（默认：0.0  .0 .0）；
    “--port” 指定采集器的外部访问端口，（默认：9099）
# 配置文件：config.ini说明
    添加的内容为存储的连接地址，连接端口，有访问权限的用户名、密码。