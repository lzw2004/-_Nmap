import nmap


def scan_active_hosts(target_subnet):

    print("正在探测活动主机...")

    nm = nmap.PortScanner(nmap_search_path=('nmap', r"D:\Download_tools\Nmap\nmap.exe"))

    # 设置扫描参数，这里使用Ping扫描
    nm.scan(hosts=target_subnet, arguments='-sn')

    # 遍历扫描结果，获取活跃主机的信息
    active_hosts = []
    for host in nm.all_hosts():
        if nm[host]['status']['state'] == 'up':
            active_hosts.append(host)

    # 遍历输出活跃主机
    print("活跃主机列表：")
    for host in active_hosts:
        print(host)
    print(f"共有 {len(active_hosts)} 台主机是活跃的。")

    # 返回值为列表
    return active_hosts


# 指定目标子网，例如 '192.168.1.0/24'
# target_subnet = '192.168.0.1/24'
# active_hosts(target_subnet)
#
