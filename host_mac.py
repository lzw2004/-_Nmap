import nmap


def get_host_mac(target):
    # 请将以下路径替换为你的 Nmap 可执行文件路径
    nmap_path = r"D:\Download_tools\Nmap\nmap.exe"

    nm = nmap.PortScanner(nmap_search_path=(nmap_path,))
    nm.scan(hosts=target, arguments='-sn')

    mac_addresses = {}

    for host in nm.all_hosts():
        if 'addresses' in nm[host] and 'mac' in nm[host]['addresses']:
            mac_addresses[host] = nm[host]['addresses']['mac']
        else:
            mac_addresses[host] = "Unknown MAC"

    for host, mac in mac_addresses.items():
        print(f"主机 {host} 的MAC地址：{mac}")

# target_subnet = '192.168.0.1/24'
# get_mac_addresses(target_subnet)



