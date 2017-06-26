#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
日志级别:
    Level	Numeric value
    CRITICAL	50
    ERROR	40
    WARNING	30   默认
    INFO	20
    DEBUG	10
    NOTSET	0

日志的输出: 1、控制台  2、日志文件
"""

import logging

"""输出控制台: basicConfig 对日志的输出格式以及输出级别做相关配置"""
# logging.basicConfig(level=logging.WARNING,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

"""输出到文件: 输出到文件"""
logging.basicConfig(level=logging.WARNING,
                    filename='log.txt',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

# logging.debug("DEBUG")
# logging.info("INFO")
# logging.warning("WARNING")
# logging.error("ERROR")
# logging.critical("CRITICAL")

"""日志的输出: 既要输出到控制台又需要保存到文件
1、创建 logger
2、创建handler 用于写入日志文件
3、再创建一个handler 用于输出到控制台
4、定义handler的输出格式
5、在logger里面添加到handler
"""
logger = logging.getLogger() #1
logger.setLevel(logging.INFO)

fh = logging.FileHandler("log.txt",mode='w')#2
fh.setLevel(logging.WARNING)

ch = logging.StreamHandler()#2
ch.setLevel(logging.CRITICAL)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")#4
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)#5
logger.addHandler(ch)

logging.debug("DEBUG")
logging.info("INFO")
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL")