import nmap


def get_network_info(target):
    # 创建一个 Nmap 对象
    nm = nmap.PortScanner(nmap_search_path=('nmap', r"D:\Download_tools\Nmap\nmap.exe"))
    nm.scan(hosts=target, arguments='-sL')

    network_interfaces = {}

    for host in nm.all_hosts():
        if 'addresses' in nm[host]:
            interfaces = nm[host]['addresses']
            network_interfaces[host] = interfaces

    # 打印输出信息
    for host, interfaces in network_interfaces.items():
        print(f"主机 {host} 的网络接口信息：{interfaces}")





