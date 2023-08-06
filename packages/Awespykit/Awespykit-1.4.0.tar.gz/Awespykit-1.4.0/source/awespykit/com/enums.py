# coding: utf-8

from enum import Enum, IntEnum


class Accept(Enum):
    """
    供一些需要接收区分'文件'或'目录'参数的函数、方法使用
    """

    File = "file"  # 接受文件
    Dir = "dir"  # 接受目录
    Both = "both"  # 全都接受


class AppStyle(IntEnum):
    Native = 0  # 原生风格
    Fusion = 1  # Fusion 风格
    Windows = 2  # 经典风格


class Linkage(IntEnum):
    """枚举：输出窗口的哪一侧吸附在主窗口上"""

    NoLink = 0  # 子窗口没有吸附在主窗口上
    Top = 1  # 子窗口顶部吸附在主窗口底部
    Left = 2  # 子窗口左侧吸附在主窗口右侧
    Right = 3  # 子窗口右侧吸附在主窗口左侧


class QMode(IntEnum):
    """包管理器的查询面板查询模式设置"""

    NotSPCF = 0  # 未指定查询方式
    Pkg2Imp = 1  # 以包名查导入名
    Imp2Pkg = 2  # 以导入名查包名
