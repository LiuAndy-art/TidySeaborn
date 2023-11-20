# 1. 声明包的命名空间
# 2. 初始化包级变量或常量：定义包级别的变量、常量或函数，这些可以在包中的各个模块中共享。
# 3. 执行包级别的初始化代码：当包需要在被引入时执行的一些初始化代码，存放在此
# 4. 自动加载模块：如果你希望在引入包时自动加载包内的某些模块，在此导入。
# 5. 提供包的文档：编写包的文档字符串，以提供关于包的概述、用法和示例。
from .MatplotlibDiy import MatplotlibDiy
from .GetSeabornData import GetSeabornData
from .TidySeabornFlexible import TidySeabornFlexible
import matplotlib as mpl
# 正确显示负号
mpl.rcParams['axes.unicode_minus'] = False
