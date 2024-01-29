import nmap
import concurrent.futures

def scan_open_ports(host_to_scan, nmap_path):
    # 创建一个 Nmap 对象
    # nm = nmap.PortScanner(nmap_search_path=('nmap', r"D:\Download_tools\Nmap\nmap.exe"))
    # nmap_path = r"D:\Download_tools\Nmap\nmap.exe"
    nm = nmap.PortScanner(nmap_search_path=(nmap_path,))
    # 使用 Nmap 对象进行扫描，指定扫描参数，这里使用默认的 SYN 扫描
    nm.scan(hosts=host_to_scan, arguments='-p 1-65535 --open')

    # 遍历扫描结果，获取开放端口信息
    for host in nm.all_hosts():
        print("----------------------------------------------------")
        print(f"主机：{host}")

        # 遍历主机的所有协议（例如，TCP、UDP）
        for proto in nm[host].all_protocols():
            print(f"协议: {proto}")

            # 获取每个协议下的端口信息
            ports = nm[host][proto].keys()
            for port in ports:
                print(
                    f"端口: {port} \t 状态: {nm[host][proto][port]['state']} \t 服务: {nm[host][proto][port]['name']}")
        print("----------------------------------------------------")


# nmap_path = r"D:\Download_tools\Nmap\nmap.exe"
#
# scan_open_ports('192.168.0.114', nmap_path)