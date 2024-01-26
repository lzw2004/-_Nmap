import sys
from active_host import scan_active_hosts
from os_info import get_os_info
from open_ports import scan_open_ports
from host_mac import get_host_mac
from network_info import get_network_info

def main(num):
    num = num.lower()
    # 探测活跃主机
    if num == "1":
        host_active_hosts = input("请输入IP地址或网段：")
        scan_active_hosts(host_active_hosts)
    # 扫描开放端口
    elif num == "2":
        host_to_scan = input("请输入IP地址或网段：")
        scan_open_ports(host_to_scan)
    # 获取主机系统信息
    elif num == "3":
        host_for_os_info = input("请输入IP地址或网段：")
        get_os_info(host_for_os_info)
    # 获取主机MAC地址
    elif num == "4":
        host_for_mac = input("请输入IP地址或网段：")
        get_host_mac(host_for_mac)
    # 获取主机的网络接口信息
    elif num == "5":
        host_network_info = input("请输入IP地址或网段：")
        get_network_info(host_network_info)
    # 退出
    elif num ==  "6" or num == "q" or num == "exit":
        sys.exit("感谢使用，再见！")
    elif  num == "h" or num == ("help"):
        help()
    else:
        print("无效的选项，请重新输入。")
        main(input("请输入选项："))
    print("\n")

def help():
    print("------------------------------------------")
    print("| 1. 探测活主机 (active hosts)")
    print("| 2. 扫描开放端口 (scan open ports)")
    print("| 3. 获取主机的系统信息 (host os info)")
    print("| 4. 获取主机的MAC地址 (host mac addresses)")
    print("| 5. 获取主机的网络接口信息 (host network interfaces)")
    print("| H. 帮助 (help)")
    print("| Q. 退出 (exit)")
    print("------------------------------------------")


if __name__ == "__main__":
    print("欢迎使用小志探测，请选择要执行的操作：")
    help()
    num = input("请输入选项：")
    main(num)
    while True:
        num = input("请输入选项(H-帮助)：")
        main(num)
