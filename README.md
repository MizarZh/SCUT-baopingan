# SCUT-baopingan
## 华工报平安脚本
## 使用方法
### 配置python及环境
安装python，并在python中安装requests,bs4,pyexecjs库。
```bash
# 命令行中运行，其他库的安装以此类推
pip install requests
# 如果使用python3，其他库的安装以此类推
pip3 install requests
```

### 配置信息
可以使用记事本或者各种文本编辑器打开json文件。
在config.json中输入自己的账号密码信息。
脚本将自动获取报平安信息

### windows每日自动执行
1. win + R，输入compmgmt.msc
2. 打开任务计划程序栏，创建基本任务
3. 输入名称和描述，设置每天某个时间点运行，操作为启动程序
4. 最重要的一步：程序或脚本输入python.exe，添加参数为.py文件所在位置，起始于为python.exe的位置（添加到了PATH的话应该不需要填写这项）
mac或者其他系统可以自己查找文档配置。