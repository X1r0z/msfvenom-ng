# Msfvenom Payload Generator

```
           ___
 _____ ___|  _|_ _ ___ ___ ___ _____
|     |_ -|  _| | | -_|   | . |     |
|_|_|_|___|_|  \_/|___|_|_|___|_|_|_|
         msfvenom payload generator
```
**交互式 msfvenom 后门生成工具**

支持自定义 payload

## usage

交互式操作

只需输入编号 再按程序要求输入监听地址 端口 格式 文件名

自动生成对应的 msfvenom 命令并执行

RHOST 目标地址 RPORT 目标端口

LHOST 监听地址 LPORT 监听端口

FORMAT 格式 exe dll elf apk

FILENAME 保存路径&文件名 test.exe /tmp/test.exe

## custom

编辑 payloads.py

格式 os (dict) -- payload (dict) -- config (list)

config 保存需要设置的参数

`'android':{'android/shell/reverse_tcp':['LHOST','LPORT']}`
