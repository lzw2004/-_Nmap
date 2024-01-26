import nmap


def get_os_info(host_for_os_info, nmap_path):

    # nm = nmap.PortScanner(nmap_search_path=('nmap', r"D:\Download_tools\Nmap\nmap.exe"))
    # nmap_path = r"D:\Download_tools\Nmap\nmap.exe"

    nm = nmap.PortScanner(nmap_search_path=(nmap_path,))
    # 使用 Nmap 对象进行操作系统信息检测
    nm.scan(hosts=host_for_os_info, arguments='-O')

    # 遍历扫描结果，获取操作系统信息
    for host in nm.all_hosts():
        print("------------------------------------------")
        print(f"主机：{host}")

        if 'osmatch' in nm[host]:
            os_matches = nm[host]['osmatch']
            for os_match in os_matches:
                print(f"操作系统匹配名称: {os_match['name']} \n准确度: {os_match['accuracy']}%")

        elif 'osclass' in nm[host]:
            os_classes = nm[host]['osclass']
            for os_class in os_classes:
                print(f"操作系统类别: {os_class['osfamily']} {os_class['osgen']} \n 准确度: {os_class['accuracy']}%")
        else:
            print(f"IP：{host}")

#
# target_host = "192.168.0.1/24"
# get_os_info(target_host)