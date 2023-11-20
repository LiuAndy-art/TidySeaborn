# TidySeaborn
使用Seaborn库绘图的简洁程序库，纯代码封装不含任何技术含量。

## 使用示例

```python
# 导入模块
>>> from TidySeaborn import TidySeabornFlexible
>>> import matplotlib.pyplot as plt
>>> from TidySeaborn import GetSeabornData
>>> import numpy as np
>>> iris = GetSeabornData("iris")
>>> tips = GetSeabornData("tips")
>>> penguins = GetSeabornData("penguins")
>>> planets = GetSeabornData("planets")
>>> flights = GetSeabornData("flights")
>>> titanic = GetSeabornData("titanic")
>>> diamonds = GetSeabornData("diamonds")
>>> geyser = GetSeabornData("geyser")
>>> fmri = GetSeabornData("fmri")
>>> mpg = GetSeabornData("mpg")
>>> glue = GetSeabornData("glue")
```

```python
>>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", savefilename="./image/直方图.pdf", block=False)
```

