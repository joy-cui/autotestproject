"""
存放公共的变量
"""

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
import os

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
print("BASE_PATH %s" % BASE_PATH)
CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'config.yml')
# 测试数据
TEST_DATA_CONFIG_FILE = os.path.join(BASE_PATH, 'config', 'test_data.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')

driver = None