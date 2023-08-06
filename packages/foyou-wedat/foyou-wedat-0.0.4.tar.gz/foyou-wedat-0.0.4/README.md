# foyou-wedat
微信 dat 文件解密

## 快速入门

[![python version](https://img.shields.io/pypi/pyversions/foyou-wedat)](https://pypi.org/project/foyou-wedat)  [![Downloads](https://static.pepy.tech/personalized-badge/foyou-wedat?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/foyou-wedat)

安装

```shell
pip install -U foyou-wedat
```

> 关于库名：因为这属于偏向个人的库，为了尽可能不占用公共资源，所有库名看上去有些啰嗦。以后我开发的类似库，都会添加 **foyou-** 前缀。

安装完成后，会有一个 `wedat` 命令行命令供调用

```shell
wedat --version 打印版本信息

wedat --help 显示帮助信息

wedat <file1.dat> <file2.dat> ... [-o/--out <输出目录>(默认 .)]

wedat -d/--dir <源目录> [-o/--out <输出目录>(默认 ., 只处理 .dat 文件)]
```