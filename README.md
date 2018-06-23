# MSFvenom-NG

```
           ___
 _____ ___|  _|_ _ ___ ___ ___ _____
|     |_ -|  _| | | -_|   | . |     |
|_|_|_|___|_|  \_/|___|_|_|___|_|_|_|
         	MSFvenom-NG
```

## Introduction

MSFvenom-NG 是一款交互式 Windows (EXE/DLL Powershell) 后门生成工具

支持自定义编码规则 Bypass 杀毒软件

## Usage

`python3 main.py`

程序第一次运行会进行初始化 (创建 `tmp` 目录并生成 `config.py` `rules.json`)

```
[*] Initializing
[+] Initialized successfully

    	   ___
 _____ ___|  _|_ _ ___ ___ ___ _____
|     |_ -|  _| | | -_|   | . |     |
|_|_|_|___|_|  \_/|___|_|_|___|_|_|_|
         	MSFvenom-NG
         		Ver: 1.1
    	

        (E)XE/DLL Backdoor
        (P)owershell Backdoor
        (S)tart msf Listener
        (C)ustom Settings
        (Q)uit
        
MSFvenom-NG>:
```

## Enc

编码规则位于 `rules.json` 中

```
{
"x86": {
	"test_rule": "S1"
	}
}
```

格式: 字母+数字 (编码器 编码次数)

字母对应的编码器位于 `lib/enc.py` 中

```
x64:

	X x64/xor
	Z: x64/zutto_dekiru

x86:

	F: x86/add_sub
	H: x86/alpha_mixed
	E: x86/alpha_upper
	R: x86/avoid_underscore_tolower
	U: x86/avoid_utf8_tolower
	X: x86/bloxor
	B: x86/bmp_polyglot
	C: x86/call4_dword_xor
	P: x86/context_cpuid
	T: x86/context_stat
	I: x86/context_time
	D: x86/countdown
	M: x86/fnstenv_mov
	J: x86/jmp_call_additive
	K: x86/nonalpha
	L: x86/nonupper
	O: x86/opt_sub
	V: x86/service
	S: x86/shikata_ga_nai
	G: x86/single_static_bit
	Y: x86/unicode_mixed
	N: x86/unicode_upper
```

Ex: S5D3E2 (x86/shikata_ga_nai x5 x86/countdown x3 x86/alpha_upper x3)

*Powershell 默认使用 cmd/powershell_base64 编码器*

## CHANGELOG

```
2018-06-23 Updated Ver:1.1 重构代码,只针对 Windows 平台,支持 encoder,254行代码
2018-02-24 Released Ver:1.0 多平台 payload 生成,38行代码
```

## TODO

免杀 Meterpreter 监听流量

一键启动 metasploit 并开启 handler

自定义设置 (指定 msf 路径 默认参数...)
