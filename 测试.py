import nmap

def get_bug(host_get_bug,nmap_path):
    nm = nmap.PortScanner(nmap_search_path=(nmap_path,))
    nm.scan(hosts=host_get_bug, arguments='-O')

    # print(json.dumps(re, indent=4))
    for host in nm.all_hosts():
        print("------------------------------------------")
        print(f"主机：{host}")
        # os_matches = nm[host]['osmatch']
        if 'osmatch' in nm[host]:
            if  nm[host]['osmatch'] == []:
                print(f"操作系统匹配名称：匹配失败 \n准确度：0%")
            else:
                os_matches = nm[host]['osmatch']
                for os_match in os_matches:
                    print(f"操作系统匹配名称: {os_match['name']} \n准确度: {os_match['accuracy']}%")

        elif 'osclass' in nm[host]:
            if nm[host]['osclass'] == []:
                print(f"操作系统类别：匹配失败 \n准确度：0%")
            else:
                os_classes = nm[host]['osclass']
                for os_class in os_classes:
                        print(f"操作系统类别: {os_class['osfamily']} {os_class['osgen']} \n 准确度: {os_class['accuracy']}%")



nmap_path = r"D:\Download_tools\Nmap\nmap.exe"
host_get_bug = "192.168.0.1/24"
get_bug(host_get_bug,nmap_path)