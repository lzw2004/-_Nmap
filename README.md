# 小志 Nmap （win基础版）

### 要想使用此工具需要进行以下操作

1. 安装 [Nmap](https://nmap.org/download.html)

2. 安装[python](https://www.python.org/)

3. 安装python-nmap
   ```python
    pip install -r requirements.txt
   ```
   或者
   ```python
   pip install python-nmap
   ```

环境搭建完后就可以克隆了呦
```python
git clone https://github.com/lzw2004/XiaoZhi_Nmap.git
```

最后一步的操作就是配置 Nmap 工具的路径，在 **main.py** 文件里边进行修改(7-11行)

```python
# 设置 Nmap 的路径
# nmap_path = " 你的nmap路径 "
nmap_path = r"D:\Download_tools\Nmap\nmap.exe"
```
我的路径是 "D:\Download_tools\Nmap\nmap.exe" 改成你的就好啦

全部操作完就得到了一个简易版的Nmap网络扫描小工具

直接运行 main.py 或者 运行 小志Nmap探测.cmd都可以

Image文件夹下放了 nmap.ico 图标文件

## 小白自学大神勿喷
工具仅供参考学习使用，出现任何问题后果自负
