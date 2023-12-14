import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import seaborn as sns
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def TidySeabornFlexible(
        df=None,
        plottype=None,
        xvarname=None,
        yvarname=None,
        groupby=None,
        xlabel=None,
        ylabel=None,
        title=None,
        xlabelsize=12,
        ylabelsize=12,
        titlesize=12,
        xticklabelsize=12,
        yticklabelsize=12,
        xticklabelrotation=0,
        yticklabelrotation=0,
        colormap=None,
        alpha=None,
        fig_length=6.4,
        fig_width=4.8,
        layout="tight",
        hue_order=None,
        order=None,
        fontfamily="华文楷体",
        isshowplot=1,
        savefilename=None,
        snsstyle="darkgrid",
        removeleftspine=0,
        removerightspine=1,
        removetopspine=1,
        removebottomspine=0,
        offset=None,
        trim=0,
        contextstyle="notebook",
        matplotlibstyle=None,
        histparamsdict={
            "bins": "auto",
            "iskde": 0,
            "iscumulative": 0,
            "element": "bars",
            "col": None,
            "multiple": "layer",
            "isfill": 1,
            "stat": "count",
            "binwidth": None,
            "bw_adjust": 1,
            "shrink": 1,
            "islog": 0,
            "islegend": 1,
            "iscommon_norm": 0},
    barparamsdict={
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "n_boot": 1000,
            "seed": None,
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "width": 0.8,
            "dodge": "auto",
            "gap": 0,
            "islog": 0,
            "legend": "auto",
            "capsize": 0,
            "isshowdatalabel": 0,
            "datalabelsize": 10,
            "datalabelformat": "%g",
            "datalabelcolor": "black",
            "errorbar_linewidth": 1,
            "errorbar_linecolor": "black",
            "errorbar_linestyle": "-"},
        boxparamsdict={
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "dodge": "auto",
            "width": 0.8,
            "gap": 0,
            "whis": 1.5,
            "linecolor": "auto",
            "linewidth": None,
            "fliersize": None,
            "islog": 0,
            "legend": "auto",
            "isnotch": 0,
            "isshowmean": 0,
            "isshowfliers": 1,
            "meanlinecolor": "red",
            "meanlinewidth": 1},
        kdeparamsdict={
            "color": None,
            "isfill": 0,
            "multiple": "layer",
            "iscumulative": 0,
            "bw_adjust": 1,
            "islog": 0,
            "level": 10,
            "thresh": 0.5,
            "islegend": 1,
            "iscommon_norm": 0},
        countparamsdict={
            "orient": None,
            "color": None,
            "isfill": 1,
            "saturation": 0.75,
            "stat": "count",
            "width": 0.8,
            "dodge": "auto",
            "gap": 0,
            "islog": 0,
            "legend": "auto"},
        ecdfparamsdict={
            "stat": "proportion",
            "iscomplementary": 0,
            "islog": None,
            "islegend": 1},
        fitparamsdict={
            "col": None,
            "row": None,
            "marker": 'o',
            "col_order": None,
            "row_order": None,
            "islegend": 1,
            "isscatter": 1,
            "isreg": 1,
            "ci": 95,
            "order": 1,
            "islogistic": 0,
            "islowess": 0,
            "isrobust": 0,
            "issharex": 1,
            "issharey": 1,
            "islegendout": 1,
            "subplot_kws": None,
            "title": None},
        lineparamsdict={
            "sizegroup": None,
            "stylegroup": None,
            "size_order": None,
            "style_order": None,
            "orient": "x",
            "issort": 1,
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "markers": None,
            "dashes": 1,
            "err_style": "band"},
        pointparamsdict={
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "n_boot": 1000,
            "orient": "v",
            "color": None,
            "markers": "o",
            "linestyles": "-",
            "dodge": 0,
            "islog": 0,
            "legend": "auto",
            "capsize": 0,
            "errorbar_linewidth": 2,
            "errorbar_linestyle": "-",
            "errorbar_linecolor": "black",
            "markersize": 9},
        scatterparamsdict={
            "sizegroup": None,
            "stylegroup": None,
            "size_order": None,
            "style_order": None,
            "markers": True,
            "legend": "auto",
            "sizes": None},
        jitterparamsdict={
            "jitter": 1,
            "isdodge": 0,
            "orient": None,
            "color": None,
            "size": 5,
            "legend": "auto"},
        violinparamsdict={
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "dodge": "auto",
            "width": 0.8,
            "gap": 0,
            "linecolor": "auto",
            "linewidth": None,
            "islog": 0,
            "legend": "auto",
            "bw_adjust": 1,
            "density_norm": "area",
            "inner": "box",
            "issplit": 0},
        matrixparamsdict={
            "vars": None,
            "x_vars": None,
            "y_vars": None,
            "iscorner": 0,
            "mainwhichplot": None,
            "subwhichplot": None,
            "upperwhichplot": None,
            "lowerwhichplot": None,
            "islegend": 0,
            "title": None,
            "issharediagy": 1},
        jointparamsdict={
            "margin_plottype": "hist",
            "margin_x_plottype": None,
            "margin_y_plottype": None,
            "space": 0.2,
            "isdropna": 0,
            "xlim": None,
            "ylim": None,
            "isshowmargin_ticks": 0,
            "title": None},
        residparamsdict={
            "islowess": 0,
            "isrobust": 0,
            "order": 1,
            "label": None,
            "color": None},
        heatparamsdict={
            "vmin": None,
            "vmax": None,
            "isannot": None,
            "annot": None,
            "fmt": ".2g",
            "annot_size": None,
            "linewidths": 0,
            "linecolor": "white",
            "iscolorbar": 1,
            "issquare": 0,
            "xticklabels": "auto",
            "yticklabels": "auto"},
        facetparamsdict={
            "col": None,
            "row": None,
            "col_order": None,
            "row_order": None,
            "issharex": 1,
            "issharey": 1,
            "islegend_out": 1,
            "xlim": None,
            "ylim": None,
            "isshowmargin_titles": 0,
            "islegend": 0,
            "whichplot": "hist",
            "subplot_kws": None,
            "title": None,
            "col_wrap": None},
        **kwargs):
    """
    这是一个Seaborn绘图函数的文档字符串。

    参数:
    df (pd.DataFrame object): dataframe。
    plottype (str): 绘图类型{"hist", "bar", "box", "kde", "count", "ecdf", "fit", "line", "point", "scatter", "jitter", "violin", "matrix", "joint", "resid", "heat", "facet"}。
    xvarname (str): X轴变量名。
    yvarname (str): Y轴变量名。
    groupby (str): 分组变量名。
    xlabel (str): X轴标签。
    ylabel (str): Y轴标签。
    title (str): 图形标题。
    xlabelsize (numeric): X轴标签字体大小。
    ylabelsize (numeric): Y轴标签字体大小。
    titlesize (numeric): 图形标题字体大小。
    xticklabelsize (numeric): X轴刻度标签字体大小。
    yticklabelsize (numeric): Y轴刻度标签字体大小。
    xticklabelrotation (numeric): X轴刻度标签旋转角度。
    yticklabelrotation (numeric): Y轴刻度标签旋转角度。
    colormap (str): 颜色映射名称。
    alpha (numeric): 颜色透明度。
    fig_length (numeric): 图形长度。
    fig_width (numeric): 图形宽度。
    layout (str ; None): 图形在画布上的布局机制{"constrained", "compressed", "tight", None}。
    hue_order (list or array-like): 分组变量的顺序。
    order (list or array-like): 图形主体的顺序。
    fontfamily (str): 支持的中英文字体名称{"方正舒体", "方正姚体", "仿宋", "黑体", "华文彩云", "华文仿宋", "华文琥珀", "华文楷体", "华文隶书", "华文宋体", "华文细黑", "华文新魏", "华文行楷", "华文中宋", "楷体", "隶书", "宋体", "微软雅黑", "新宋体", "幼圆", "TimesNewRoman", "Arial"}。
    isshowplot (binary): 是否显示图形{1,0}。
    savefilename (str): 保存的图形文件名（带后缀）{".pdf", ".png", ".jpg"}。
    snsstyle (str): seaborn绘图风格样式{"darkgrid", "whitegrid", "dark", "white", "ticks"}。
    isremoveleftspine (binary): 是否移除左轴线{1,0}。
    isremoverightspine (binary): 是否移除右轴线{1,0}。
    isremovetopspine (binary): 是否移除上轴线{1,0}。
    isremovebottomspine (binary): 是否移除下轴线{1,0}。
    offset (numeric): 轴线距离图形的距离。
    trim (binary): 是否设置R风格轴线{1,0}。
    contextstyle (str): 图形元素大小风格调整{"paper", "notebook", "talk", "poster"}。
    matplotlibstyle (str): matplotlib支持的绘图风格{"Solarize_Light2", "_classic_test_patch", "_mpl-gallery", "_mpl-gallery-nogrid", "bmh", "classic", "dark_background", "fast", "fivethirtyeight", "ggplot", "grayscale", "seaborn-v0_8", "seaborn-v0_8-bright", "seaborn-v0_8-colorblind", "seaborn-v0_8-dark", "seaborn-v0_8-dark-palette", "seaborn-v0_8-darkgrid", "seaborn-v0_8-deep", "seaborn-v0_8-muted", "seaborn-v0_8-notebook", "seaborn-v0_8-paper", "seaborn-v0_8-pastel", "seaborn-v0_8-poster", "seaborn-v0_8-talk", "seaborn-v0_8-ticks", "seaborn-v0_8-white", "seaborn-v0_8-whitegrid", "tableau-colorblind10"}。
    histparamsdict (dict): 控制直方图的参数字典。
    {
        isfill (binary): 是否对直方图进行填充{1,0}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 柱子的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        multiple (str): 分组情况下的直方图排列方式{"layer", "stack", "fill", "dodge"}。
        stat (str): 直方图Y轴含义{"count", "frequency", "probability", "percent", "density"}。
        bins (numeric): 组数。
        binwidth (numeric): 组距。
        element (str): 直方图的表现形式{"bars", "step", "poly"}。
        iskde (binary): 是否添加核密度估计曲线{1,0}。
        iscumulative (binary): 是否绘制累积直方图{1,0}。
        bw_adjust (numeric): 核密度估计的窗宽。
        shrink (numeric): 柱子之间的间距放缩比例，小于1表示间距拉大。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制直方图{1,0}或者是对数的底数。
        islegend (binary): 是否显示图例{1,0}。
        iscommon_norm (binary): 分组情况下是否将总数作为计算直方图的方式{1,0}。
    }
    barparamsdict (dict): 控制柱状误差图的参数字典。
    {
        estimator (str or callable): 估计量或者是用于估计每个分类下的统计函数{"mean", "median", "max", "min", "var", "std", "sum", callback}。
        errorbar (str): 误差估计量{"ci", "pi", "se", "sd", None}。
        n_boot (int): 计算置信区间误差估计量时使用到Bootstrap样本的数量。
        seed (int): Bootstrap估计时的随机数种子。
        orient (str): 柱状图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 柱子的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        saturation (float): 颜色透明度。
        isfill (binary): 是否填充颜色{1,0}。
        width (numeric): 柱子的宽度。
        dodge (binary): 是否设置分组柱状图的排列方式为并排排列{1,0}。
        gap (numeric): 分组柱状图的排列方式为并排排列时柱子之间的间隔。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制柱状图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        capsize (numeric): 误差条上短横线相对于柱子的宽度。
        isshowdatalabel (binary): 是否显示柱子高度或者长度的数据标签值{1,0}。
        datalabelsize (numeric): 数据标签字体大小。
        datalabelformat (str): 格式化数据标签值{"{:.2f}", "%g"}。
        datalabelcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 数据标签的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        errorbar_linewidth (numeric): errorbar线宽。
        errorbar_linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): errorbar线条的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        errorbar_linestyle (str): errorbar线条的样式{"-", "--", "-.", ":"}。
    }
    boxparamsdict (dict): 控制箱线图的参数字典
    {
        orient (str): 箱线图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 箱子的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        saturation (float): 颜色透明度。
        isfill (binary): 是否填充颜色{1,0}。
        dodge (str or binary): 是否设置分组箱线图的排列方式为并排排列{"auto", 1, 0}。
        width (numeric): 箱子的宽度。
        gap (numeric): 分组箱线图的排列方式为并排排列时箱子之间的间隔。
        whis (numeric): 用于控制多少倍IQR以外作为异常值或者是正常值范围元组。
        linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 线条颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        linewidth (numeric): 线宽。
        fliersize (numeric): 异常值点的大小。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        isnotch (binary): 是否绘制有缺口的箱线图{1,0}。
        isshowmean (binary): 是否显示均值线{1,0}。
        isshowfliers (binary): 是否显示异常值点{1,0}。
        meanlinecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 均值线颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        meanlinewidth (numeric): 均值线条宽度。
    }
    kdeparamsdict (dict): 控制核密度估计曲线的参数。
    {
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 核密度曲线的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        isfill (binary): 是否填充颜色{1,0}。
        multiple (str): 分组情况下的核密度曲线排列方式{"layer", "stack", "fill"}。
        iscumulative (binary): 是否估计累积分布函数{1,0}。
        bw_adjust (numeric): 窗宽。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        level (numeric): 等高线等值水平线的数量。
        thresh (numeric): 等值线之间最低比例。
        islegend (binary): 是否显示图例{1,0}。
        iscommon_norm (binary): 分组情况下是否将总数作为计算核密度曲线的方式{1,0}。
    }
    countparamsdict (dict): 控制分类变量计数柱状图的参数。
    {
        orient (str): 柱状图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 柱子的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        isfill (binary): 是否填充颜色{1,0}。
        saturation (float): 颜色透明度。
        stat (str): 柱子的含义{"count", "percent", "proportion", "probability"}。
        width (numeric): 柱子的宽度。
        dodge (str or binary): 是否设置分组柱状图的排列方式为并排排列{"auto", 1, 0}。
        gap (numeric): 分组柱状图的排列方式为并排排列时柱子之间的间隔。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
    }
    ecdfparamsdict (dict): 控制经验分布函数的参数。
    {
        stat (str): Y轴的含义{"count", "percent", "proportion"}。
        iscomplementary (binary): 是否绘制经验生存函数{1,0}。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        islegend (binary): 是否显示图例{1,0}。
    }
    fitparamsdict (dict): 控制函数拟合图的参数。
    {
        col (str): 列分组变量。
        row (str): 行分组变量。
        marker (str): 散点样式。
        col_order (list of str): 列分组变量的顺序。
        row_order (list of str): 行分组变量的顺序。
        islegend (binary): 是否显示图例{1,0}。
        isscatter (binary): 是否绘制散点{1,0}。
        isreg (binary): 是否绘制回归拟合曲线{1,0}。
        ci (numeric or None): 置信度[0,100]。
        order (numeric): 多项式回归的阶数。
        islogistic (binary): 是否拟合逻辑回归{1,0}。
        islowess (binary): 是否拟合局部多项式回归{1,0}。
        isrobust (binary): 是否拟合稳健回归{1,0}。
        issharex (binary): 是否共享X轴坐标{1,0}。
        issharey (binary): 是否共享Y轴坐标{1,0}。
        islegendout (binary): 是否将图例放到图形外面{1,0}。
        subplot_kws (dict): 控制子图的相关参数字典。
        {
            (xy)label_(i) (str): 从左到右从上到下第i个子图的xy轴标签。
            title_(i) (str): 从左到右从上到下第i个子图的图形标题。
            (xy)labelsize_(i) (numeric): 从左到右从上到下第i个子图的xy轴标签字体大小。
            titlesize (numeric): 从左到右从上到下第i个子图的图形标题字体大小。
            (xy)ticklabelsize_(i) (numeric): 从左到右从上到下第i个子图的xy轴刻度标签字体大小。
            (xy)ticklabelrotation_i (numeric): 从左到右从上到下第i个子图的xy轴刻度标签旋转角度。
        }
        title (str): 图形标题。
    }
    lineparamsdict (dict): 控制线图的参数字典。
    {
        sizegroup (str): 线条宽度分组变量。
        stylegroup (str): 线条样式分组变量。
        size_order (list of str): 线条宽度分组变量顺序。
        style_order (list of str): 线条样式分组变量顺序。
        orient (str): 水平还是竖直线图{"x","y"}。
        issort (binary): 是否按照x对数据集排序{1,0}。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        estimator (str or callable): 当x存在重复值时，对y的聚合计算估计量{"mean", "median", "max", "min", "var", "std", "sum", callback}。
        errorbar (str): 误差估计量{"ci", "pi", "se", "sd", None}。
        markers (binary or list): 是否添加散点标记{1,0}。
        dashes (binary or list): 是否绘制虚线{1,0}。
        err_style (str): 误差的样式{"band", "bars"}。
    }
    pointparamsdict (dict): 控制点状误差图的参数字典。
    {
        estimator (str or callable): 估计量或者是用于估计每个分类下的统计函数{"mean", "median", "max", "min", "var", "std", "sum", callback}。
        errorbar (str): 误差估计量{"ci", "pi", "se", "sd", None}。
        n_boot (int): 计算置信区间误差估计量时使用到Bootstrap样本的数量。
        orient (str): 点状图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 点的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        markers (str or list of str): 散点样式。
        linestyles (str or list of str): 线条样式，"none"为不显示线条。
        dodge (numeric or binary): 是否设置分组柱状图的排列方式为并排排列{numeric, 1, 0}。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        capsize (numeric): 误差条上短横线相对于柱子的宽度。
        errorbar_linewidth (numeric): errorbar线宽。
        errorbar_linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): errorbar线条的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        errorbar_linestyle (str): errorbar线条的样式{"-", "--", "-.", ":"}。
        markersize (numeric): 散点大小。
    }
    scatterparamsdict (dict): 控制散点图的参数字典。
    {
        sizegroup (str): 散点大小分组变量。
        stylegroup (str): 散点样式分组变量。
        size_order (list of str): 散点大小分组变量顺序。
        style_order (list of str): 散点样式分组变量顺序。
        markers (str or list of str or dict): 多类别的散点样式。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        sizes (tuple): 散点大小的上下界。
    }
    jitterparamsdict (dict): 控制抖动图的参数字典。
    {
        jitter (binary or numeric): 是否设置抖动{1,0}或者抖动大小。
        isdodge (binary): 是否设置分组抖动图的排列方式为并排排列{1, 0}。
        orient (str): 抖动图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 散点填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        size (numeric): 散点大小。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
    }
    violinparamsdict (dict): 控制小提琴图的参数字典。
    {
        orient (str): 小提琴图的方向{"v", "h"}。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 小提琴的填充颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        saturation (float): 颜色透明度。
        isfill (binary): 是否填充颜色{1,0}。
        inner (str): 内部数据呈现方式{"box", "quart", "point", "stick", None}。
        dodge (str or binary): 是否设置分组小提琴图的排列方式为并排排列{"auto", 1, 0}。
        width (numeric): 小提琴的宽度。
        gap (numeric): 分组小提琴图的排列方式为并排排列时小提琴之间的间隔。
        linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 线条颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
        linewidth (numeric): 线宽。
        islog (binary or positive numeric): 是否对数化(以10为底)后再绘制箱线图{1,0}或者是对数的底数。
        legend (str): 指定图例的样式{"auto", "brief", "full", False}。
        bw_adjust (numeric): 带宽。
        density_norm: 分组密度的归一化方式{"area", "count", "width"}。
        issplit (binary): 是否对分组箱线图分隔，各取一半拼接为一个整小提琴图{1,0}。
    }
    matrixparamsdict (dict): 控制矩阵图的参数字典。
    {
        vars (list or str): 矩阵图中要展示的变量信息。
        x_vars (list of str): 行变量。
        y_vars (list of str): 列变量。
        iscorner (binary): 是否绘制下三角矩阵图。
        mainwhichplot (str): 非主对角线上绘制什么图形{"scatter", "kde"}。
        subwhichplot (str): 主对角线上绘制什么图形{"hist", "kde", "box", "violin", "jitter", "ecdf"}。
        upperwhichplot (str): 上三角绘制什么图形{"scatter", "kde"}。
        lowerwhichplot (str): 下三角绘制什么图形{"scatter", "kde"}。
        islegend (binary): 是否绘制图例{1,0}。
        title (str): 图形总标题。
        issharediagy (binary): 是否共享对角线上图形的Y轴坐标{1,0}。
    }
    jointparamsdict (dict): 控制联合边际图的参数字典。
    {
        margin_plottype (str): 边际图的类型{"hist", "box", "violin", "jitter", "kde", "ecdf"}。
        margin_x_plottype (str): 投影到X轴上的边际图的类型{"hist", "box", "violin", "jitter", "kde", "ecdf"}。
        margin_y_plottype (str): 投影到Y轴上边际图的类型{"hist", "box", "violin", "jitter", "kde", "ecdf"}。
        space (numeric): 联合图和边际图之间的间距。
        isdropna (binary): 是否删除缺失值再画图{1,0}。
        xlim (tuple): X轴范围。
        ylim (tuple): Y轴范围。
        isshowmargin_ticks (binary): 是否显示边际图的刻度{1,0}。
        title (str): 图形总标题。
    }
    residparamsdict (dict): 控制残差图的参数字典。
    {
        islowess (binary): 是否拟合局部多项式回归{1,0}。
        isrobust (binary): 是否拟合稳健回归{1,0}。
        order (int): 拟合多项式回归的阶数。
        label (str): 图例标题。
        color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 散点和线条的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    }
    heatparamsdict (dict): 控制热图的参数字典。
    {
        vmin (numeric): 用来计算最小颜色值。
        vmax (numeric): 用来计算最大颜色值。
        isannot (binary): 是否显示数据标签{1,0}。
        annot (2D-arraylike): 数据标签。
        fmt (str): 数据标签的格式{".2f", ".2g"}。
        annot_color (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 数据标签的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。:
        annot_size (numeric): 数据标签的大小。
        linewidths (numeric): 分割小方形的线条宽度。
        linecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 分隔小方格线条的颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。:
        iscolorbar (binary): 是否显示颜色条{1,0}。
        issquare (binary): 是否设置图形为正方形{1,0}。
        xticklabels (list of str): X轴刻度标签。
        yticklabels (list of str): Y轴刻度标签。
    }
    facetparamsdict (dict): 控制子图的参数字典。
    {
        row (str): 用于对行分类的行变量名。
        col (str): 用于对列分类的列变量名。
        whichplot (str): 绘制什么图形{"hist", "bar", "box", "kde", "count", "ecdf", "fit", "line", "point", "scatter", "jitter", "violin", "matrix", "joint", "resid", "heat"}。
        col_wrap (int): 每一列排放多少个变量。
        issharex (binary): 是否共享X轴的坐标{1,0}。
        issharey (binary): 是否共享Y轴的坐标{1,0}。
        row_order (list of str): 行变量取值顺序。
        col_order (list of str): 列变量取值顺序。
        islegend_out (binary): 是否将图例添加到图形的外面{1,0}。
        isshowmargin_titles (binary): 是否显示边际标题{1,0}。
        xlim (tuple): X轴范围。
        ylim (tuple): Y轴范围。
        islegend (binary): 是否添加图例{1,0}。
        subplot_kws (dict): 控制子图的相关参数字典。
        {
            (xy)label_(i) (str): 从左到右从上到下第i个子图的xy轴标签。
            title_(i) (str): 从左到右从上到下第i个子图的图形标题。
            (xy)labelsize_(i) (numeric): 从左到右从上到下第i个子图的xy轴标签字体大小。
            titlesize (numeric): 从左到右从上到下第i个子图的图形标题字体大小。
            (xy)ticklabelsize_(i) (numeric): 从左到右从上到下第i个子图的xy轴刻度标签字体大小。
            (xy)ticklabelrotation_i (numeric): 从左到右从上到下第i个子图的xy轴刻度标签旋转角度。
        }
        title (str): 图形标题。
    }

    返回值：
    Axes对象或者是Axes构成的二维数组

    示例：
    ===============================================================================0
    导入模块
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
    测试直方图参数
    ===============================================================================1
    测试基本参数
    ===============================================================================2
    竖直直方图
    >>> ax = TidySeabornFlexible(iris, "hist", "sepal_length", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================3
    水平直方图
    >>> ax = TidySeabornFlexible(iris, "hist", yvarname="sepal_length", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================4
    设置组距
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", histparamsdict={"binwidth": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================5
    设置组数
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", histparamsdict={"bins": 30}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================6
    添加核密度估计曲线
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", histparamsdict={"iskde": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================7
    设置核密度估计的带宽
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", histparamsdict={"iskde": 1, "bw_adjust": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================8
    绘制整个dataframe中数值变量的直方图
    >>> ax = TidySeabornFlexible(iris, "hist", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================9
    分组直方图
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================10
    设置分组方式
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"multiple": "stack"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"multiple": "layer"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"multiple": "fill"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================11
    设置直方图的表现形式
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"element": "step"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"element": "bars"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"element": "poly"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================12
    设置直方图的含义
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"stat": "density"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"stat": "count"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"stat": "frequency"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"stat": "probability"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"stat": "percent"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================13
    离散型柱状图
    >>> ax = TidySeabornFlexible(tips, "hist", xvarname="size", histparamsdict={"binwidth": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================14
    柱子添加间隙
    >>> ax = TidySeabornFlexible(tips, "hist", xvarname="day", histparamsdict={"binwidth": 1, "shrink": 0.8}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================15
    分组直方图
    >>> ax = TidySeabornFlexible(tips, "hist", xvarname="day", groupby="sex", histparamsdict={"binwidth": 1, "shrink": 0.8, "multiple": "dodge"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"iscommon_norm": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"iscommon_norm": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================16
    对数处理
    >>> ax = TidySeabornFlexible(planets, "hist", xvarname="distance", histparamsdict={"islog": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(planets, "hist", xvarname="distance", histparamsdict={"islog": np.exp(1)}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================17
    不填充颜色
    >>> ax = TidySeabornFlexible(planets, "hist", xvarname="distance", histparamsdict={"islog": 1, "isfill": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================18
    不显示图例
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", histparamsdict={"islegend": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================19
    经验分布函数，累积密度直方图
    >>> ax = TidySeabornFlexible(planets, "hist", xvarname="distance", groupby="method", hue_order=["Radial Velocity", "Transit"], histparamsdict={"islog": 1, "isfill": 0, "iscumulative": 1, "element": "step", "stat": "density"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(planets, "hist", xvarname="distance", groupby="method", hue_order=["Radial Velocity", "Transit"], histparamsdict={"islog": 1, "isfill": 0, "iscumulative": 1, "element": "step", "stat": "density", "iscommon_norm": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================20
    二维直方图
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", yvarname="sepal_width", groupby="species", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================21
    直方图填充颜色
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", histparamsdict={"color": "pink"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================22
    测试一般绘图的标签参数
    ===============================================================================23
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, colormap="Set2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================24
    测试一般绘图的字体参数
    ===============================================================================25
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="隶书", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================26
    测试一般绘图的文件保存参数
    ===============================================================================27
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", savefilename="./image/直方图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================28
    测试一般绘图参数的绘图风格参数
    ===============================================================================29
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================30
    测试一般绘图参数的matplotlib绘图风格参数
    ===============================================================================31
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(iris, "hist", xvarname="sepal_length", groupby="species", xlabel="数量", ylabel="个数", title="分组直方图", colormap="Set2", fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================32
    测试柱状误差图参数
    ===============================================================================33
    竖直柱状图
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================34
    水平柱状图
    >>> ax = TidySeabornFlexible(penguins, "bar", yvarname="island", xvarname="body_mass_g", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================35
    分组不带图例柱状图，有颜色区分
    >>> ax = TidySeabornFlexible(penguins, "bar", yvarname="island", xvarname="body_mass_g", groupby="island", barparamsdict={"legend": False}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================36
    整个dataframe的所有列绘制柱状误差图
    >>> flights_wide = flights.pivot(index="year", columns="month", values="passengers")
    >>> print(flights_wide)
    >>> ax = TidySeabornFlexible(flights_wide, "bar", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================37
    某列的柱状误差图
    >>> ax = TidySeabornFlexible(flights_wide["Jun"], "bar", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================38
    分组柱状误差图
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================39
    指定误差
    >>> ax = TidySeabornFlexible(penguins, "bar", yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "sd"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "ci"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "se"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", yvarname="island", xvarname="body_mass_g", barparamsdict={"errorbar": "pi"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================40
    不显示误差，显示数据标签
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================41
    当xy都是数值变量时存在歧义，显示指定水平柱状误差图
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="passengers", yvarname="year", barparamsdict={"errorbar": "sd", "orient": "h"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================42
    颜色饱和度
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================43
    估计量
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "median", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "max", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "min", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "var", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "std", "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> r = lambda x: x.max()-x.min()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": r, "isshowdatalabel": 1, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================44
    Bootstrap样本数
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": "ci", "estimator": "mean", "isshowdatalabel": 1, "saturation": 0.2, "n_boot": 2000}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================45
    Bootstrap估计的随机数种子
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": "ci", "estimator": "mean", "isshowdatalabel": 1, "saturation": 0.2, "n_boot": 500, "seed": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================46
    柱子的填充颜色
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "saturation": 0.2, "color": "red"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================47
    不填充颜色
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "isfill": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================48
    设置柱子宽度
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "isfill": 0, "width": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================49
    设置分组柱状图的排列方式
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "dodge": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "dodge": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================50
    设置分组柱子之间的间距
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "dodge": 1, "gap": 0.3}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================51
    数据对数化
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "islog": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "islog": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "islog": np.exp(1)}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================52
    指定图例样式
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "legend": "auto"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "legend": "brief"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "legend": "full"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": None, "estimator": "mean", "isshowdatalabel": 1, "legend": False}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================53
    误差条上短横线相对于柱子的宽度
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": "sd", "estimator": "mean", "isshowdatalabel": 1, "capsize": 0.3}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================54
    数据标签格式
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": "sd", "estimator": "mean", "isshowdatalabel": 1, "capsize": 0.3, "datalabelsize": 8, "datalabelformat": "{:.1f}", "datalabelcolor": "purple"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================55
    errorbar样式
    >>> ax = TidySeabornFlexible(penguins, "bar", xvarname="island", yvarname="body_mass_g", groupby="sex", barparamsdict={"errorbar": "sd", "estimator": "mean", "capsize": 0.3, "errorbar_linestyle": "-.", "errorbar_linecolor": "purple", "errorbar_linewidth": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================56
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================57
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================58
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/柱状图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================59
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================60
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "bar", xvarname="year", yvarname="passengers", barparamsdict={"errorbar": None, "estimator": "sum", "isshowdatalabel": 1}, xlabel="年份", ylabel="乘客", title="柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================61
    测试箱线图参数
    ===============================================================================62
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="age", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================63
    分组箱线图
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="age", yvarname="class", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================64
    二分组箱线图
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="age", yvarname="class", groupby="alive", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================65
    不填充颜色
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================66
    增加分组之间的间距
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0, "gap": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================67
    分组排列方式
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0, "gap": 0.2, "dodge": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="class", yvarname="age", groupby="alive", boxparamsdict={"isfill": 0, "gap": 0.2, "dodge": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================68
    异常值范围
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"whis": (0, 100)}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"whis": 2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================69
    箱子宽度
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"width": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================70
    箱子样式
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"color": "0.8", "linecolor": "#137", "linewidth": 0.75}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================71
    异常值点大小
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="fare", yvarname="age", groupby="alive", boxparamsdict={"fliersize": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================72
    颜色饱和度
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", boxparamsdict={"saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================73
    指定图例样式
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.2, "legend": "auto"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.4, "legend": "full"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.7, "legend": "brief"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.9, "legend": False}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================74
    设置有缺口的箱线图
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", groupby="alive", boxparamsdict={"saturation": 0.1, "isnotch": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================75
    显示均值线
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", boxparamsdict={"isshowmean": 1, "meanlinecolor": "green", "meanlinewidth": 1.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================76
    显示异常值点
    >>> ax = TidySeabornFlexible(titanic, "box", xvarname="deck", yvarname="age", boxparamsdict={"isshowfliers": 1, "whis": (0, 50)}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================77
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================78
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================79
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/箱线图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================80
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================81
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights, "box", xvarname="year", yvarname="passengers", xlabel="年份", ylabel="乘客", title="箱线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================82
    测试核密度估计参数
    ===============================================================================83
    竖直密度估计图
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================84
    水平密度估计图
    >>> ax = TidySeabornFlexible(tips, "kde", yvarname="total_bill", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================85
    整个dataframe绘制多个数据
    >>> ax = TidySeabornFlexible(iris, "kde", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(plottype="kde", xvarname=iris["sepal_length"], block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================86
    调整窗宽
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", kdeparamsdict={"bw_adjust": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================87
    分组核密度估计
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================88
    分组排列方式
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "stack"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "fill"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "layer"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================89
    填充颜色
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "fill", "isfill": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 1, "multiple": "stack", "isfill": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================90
    累积概率分布
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", kdeparamsdict={"iscommon_norm": 0, "multiple": "layer", "isfill": 1, "iscumulative": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================91
    对数处理
    >>> ax = TidySeabornFlexible(diamonds, "kde", xvarname="price", kdeparamsdict={"islog": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================92
    等高线图（二维核密度估计）
    >>> ax = TidySeabornFlexible(geyser, "kde", xvarname="waiting", yvarname="duration", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(geyser, "kde", xvarname="waiting", yvarname="duration", groupby="kind", kdeparamsdict={"isfill": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(geyser, "kde", xvarname="waiting", yvarname="duration", groupby="kind", kdeparamsdict={"isfill": 1, "level": 15, "thresh": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================93
    不显示图例
    >>> ax = TidySeabornFlexible(iris, "kde", xvarname="sepal_length", groupby="species", kdeparamsdict={"islegend": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================94
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================95
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================96
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/核密度估计图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================97
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================98
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "kde", xvarname="total_bill", groupby="time", xlabel="账单费用", ylabel="密度", title="核密度曲线", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================99
    测试分类变量柱状图
    ===============================================================================100
    竖直分类变量柱状图
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================101
    分组分类变量柱状图
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================102
    设置Y轴含义
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"stat": "count"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"stat": "percent"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"stat": "proportion"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"stat": "probability"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================103
    水平分类变量柱状图
    >>> ax = TidySeabornFlexible(titanic, "count", yvarname="class", countparamsdict={"stat": "probability"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================104
    改变柱子颜色
    >>> ax = TidySeabornFlexible(titanic, "count", yvarname="class", countparamsdict={"color": "green"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================105
    设置饱和度
    >>> ax = TidySeabornFlexible(titanic, "count", yvarname="class", countparamsdict={"color": "green", "saturation": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================106
    不填充颜色
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", countparamsdict={"isfill": 0, "saturation": 0.4}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================107
    柱子宽度
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", countparamsdict={"width": 0.4, "saturation": 0.2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================108
    分组排列方式
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": "auto"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================109
    并排排列柱子之间的距离
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 1, "gap": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================110
    图例设置样式
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 1, "legend": "auto"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 1, "legend": "brief"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 1, "legend": "full"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", countparamsdict={"dodge": 1, "legend": False}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================111
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================112
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================113
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/分类变量柱状图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================114
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================115
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "count", xvarname="class", groupby="survived", xlabel="阶层", ylabel="人数", title="分组分类变量柱状图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================116
    测试经验分布函数参数
    ===============================================================================117
    竖直经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="flipper_length_mm", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================118
    水平经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "ecdf", yvarname="flipper_length_mm", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================119
    分组经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================120
    改变Y轴含义
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", ecdfparamsdict={"stat": "count"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", ecdfparamsdict={"stat": "proportion"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", ecdfparamsdict={"stat": "percent"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================121
    绘制经验生存函数
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", ecdfparamsdict={"stat": "percent", "iscomplementary": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================122
    不显示图例
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", ecdfparamsdict={"stat": "percent", "iscomplementary": 1, "islegend": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================123
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================124
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================125
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/经验分布函数图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================126
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================127
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "ecdf", xvarname="bill_length_mm", groupby="species", xlabel="嘴巴长度（毫米）", ylabel="经验分布函数值", title="分组经验分布函数图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================128
    测试函数拟合图
    ===============================================================================129
    单个函数拟合
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================130
    分组函数拟合
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================131
    指定列分组
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", fitparamsdict={"col": "sex"}, fig_width=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================132
    指定列分组和行分组
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species"}, fig_width=3, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================133
    不共享xy轴坐标
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "issharex": 0, "issharey": 0}, fig_width=3, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================134
    散点样式
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "marker": "^"}, fig_width=2.5, fig_length=3, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================135
    列分组变量的顺序
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "col_order": ["Chinstrap", "Gentoo", "Adelie"]}, fig_width=2.5, fig_length=3, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================136
    行分组变量的顺序
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "col_order": ["Chinstrap", "Gentoo", "Adelie"], "row_order": ["Female", "Male"]}, fig_width=2.5, fig_length=3, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================137
    不显示图例
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "islegend": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================138
    不绘制散点
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "islegend": 0, "isscatter": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================139
    不绘制拟合回归线
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "isreg": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================140
    指定置信区间的置信度
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "ci": 90}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================141
    多项式回归
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "order": 2}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================142
    局部多项式回归
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "islowess": 1}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================143
    稳健回归
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", fitparamsdict={"row": "sex", "col": "species", "isrobust": 1}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================144
    图例设置到图形外面
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"row": "species", "islegendout": 1}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"row": "species", "islegendout": 0}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================145
    子图控制
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================146
    总标题
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "title": "总标题"}, fig_width=4, fig_length=4, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================147
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================148
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", savefilename="./image/函数拟合图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================149
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================150
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "fit", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="sex",  fitparamsdict={"col": "species", "subplot_kws": {"xlabel_1": "第1个图形的X轴标签", "xlabel_2": "第2个图形的X轴标签", "xlabel_3": "第3个图形的X轴标签", "ylabel_1": "第1个图形的Y轴标签", "ylabel_2": "第2个图形的Y轴标签", "ylabel_3": "第3个图形的Y轴标签", "xlabelsize_3": 15, "ylabelsize_1": 9, "title_1": "标题1", "title_3": "标题3"}}, fig_width=4, fig_length=4, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================151
    测试线图参数
    ===============================================================================152
    单个线图
    >>> ax = TidySeabornFlexible(flights.query("month == 'May'"), "line", xvarname="year", yvarname="passengers", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================153
    多个线图
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "line", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================154
    x重复值下的单个线图
    >>> ax = TidySeabornFlexible(flights, "line", xvarname="year", yvarname="passengers", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================155
    分组线图
    >>> ax = TidySeabornFlexible(flights, "line", xvarname="year", yvarname="passengers", groupby="month", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================156
    线条样式分组线图
    >>> ax = TidySeabornFlexible(flights, "line", xvarname="year", yvarname="passengers", groupby="month", lineparamsdict={"stylegroup": "month"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================157
    线条宽度分组线图
    >>> ax = TidySeabornFlexible(flights, "line", xvarname="year", yvarname="passengers", groupby="month", lineparamsdict={"stylegroup": "month", "sizegroup": "month"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================158
    水平线图
    >>> ax = TidySeabornFlexible(flights, "line", xvarname="passengers", yvarname="year", groupby="month", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================159
    分组线图x多个重复值
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="event", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================160
    线条样式分组
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================161
    添加散点线条样式分组
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event", "markers": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================162
    误差样式线条样式分组
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event", "markers": 1, "err_style": "bars"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================163
    不按照顺序绘图
    >>> x, y = np.random.normal(size=(2, 5000)).cumsum(axis=1)
    >>> ax = TidySeabornFlexible(plottype="line", xvarname=x, yvarname=y, lineparamsdict={"issort": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(plottype="line", xvarname=x, yvarname=y, lineparamsdict={"issort": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================164
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================165
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================166
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/线图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================167
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================168
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(fmri, "line", xvarname="timepoint", yvarname="signal", groupby="region", lineparamsdict={"stylegroup": "event"}, xlabel="时间点", ylabel="信号值", title="时间序列线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================169
    测试点状误差图参数
    ===============================================================================170
    简单点状误差图
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="island", yvarname="body_mass_g", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================171
    分组点状误差图
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="island", yvarname="body_mass_g", groupby="sex", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================172
    指定散点样式
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="island", yvarname="body_mass_g", groupby="sex", pointparamsdict={"markers": ["o", "s"], "linestyles": ["-", "--"]}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================173
    指定误差类型
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="island", yvarname="body_mass_g", groupby="sex", pointparamsdict={"markers": ["o", "s"], "linestyles": ["-", "--"], "errorbar": "sd"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================174
    水平点状误差图
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="body_mass_g", yvarname="island", pointparamsdict={"markers": "D", "color": "0.5", "errorbar": "pi", "capsize": 0.4, "orient": "h"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================175
    分组排列方式
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="sex", yvarname="bill_depth_mm", groupby="species", pointparamsdict={"dodge": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="sex", yvarname="bill_depth_mm", groupby="species", pointparamsdict={"dodge": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================176
    不显示误差，不显示连接线条
    >>> ax = TidySeabornFlexible(penguins, "point", xvarname="species", yvarname="bill_depth_mm", groupby="sex", pointparamsdict={"dodge": 0.4, "errorbar": None, "markers": "_", "linestyles": "none"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================177
    绘制整个数据的点状误差图
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================178
    指定估计量
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": "median"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": "max"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": "min"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": "var"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": "std"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": "sum"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> f = lambda x: x.max()-x.min()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"estimator": f}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================179
    误差估计量
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"errorbar": "sd"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"errorbar": "ci"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"errorbar": "pi"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"errorbar": "se"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"errorbar": None}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================180
    控制点和连线颜色
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", pointparamsdict={"color": "green"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================181
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================182
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================183
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/点状误差图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================184
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================185
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(flights.pivot(index="year", columns="month", values="passengers"), "point", xlabel="X轴", ylabel="Y轴", title="点状误差线图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================186
    散点图参数测试
    ===============================================================================187
    单个散点图
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================188
    分组散点图
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="time", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================189
    大小，样式分组散点图
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="time", scatterparamsdict={"stylegroup": "time", "sizegroup": "time"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================190
    气泡图
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================191
    指定散点
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size", "marker": "s"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================192
    大小分组变量顺序散点图
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="time", scatterparamsdict={"sizegroup": "time", "size_order": ["Dinner", "Lunch"]}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================193
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================194
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================195
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/散点图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================196
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================197
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "scatter", xvarname="total_bill", yvarname="tip", groupby="size", scatterparamsdict={"sizes": (20,200), "sizegroup": "size"}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================198
    测试抖动图参数
    ===============================================================================199
    水平抖动图
    >>> ax = TidySeabornFlexible(tips, "jitter", xvarname="total_bill", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================200
    分组抖动图
    >>> ax = TidySeabornFlexible(tips, "jitter", xvarname="total_bill", yvarname="day", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================201
    垂直抖动图
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================202
    二分组抖动图
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================203
    二分组并排排列抖动图
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================204
    不抖动
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1, "jitter": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================205
    散点颜色和大小
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", jitterparamsdict={"isdodge": 1, "color": "green", "size": 10}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================206
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================207
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================208
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/抖动图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================209
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================210
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "jitter", yvarname="total_bill", xvarname="day", groupby="sex", jitterparamsdict={"isdodge": 1}, xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================211
    测试小提琴图
    ===============================================================================212
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================213
    分组小提琴图
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================214
    二分组小提琴图
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", groupby="alive", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================215
    不填充颜色
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"isfill": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================216
    指定内部数据呈现方式
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"inner": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"inner": "quart"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"inner": "point"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"inner": "stick"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"inner": None}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================217
    指定单个图形的颜色
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", violinparamsdict={"color": "green", "saturation": 0.3}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================218
    一分为二
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"issplit": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================219
    控制间距
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", groupby="alive", violinparamsdict={"issplit": 1, "gap": 0.1, "inner": "quart"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================220
    绘制一半的箱线图
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="class", yvarname="age", violinparamsdict={"issplit": 1, "inner": "quart"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================221
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="deck", violinparamsdict={"inner": "point"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================222
    归一化密度
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="deck", violinparamsdict={"inner": "point", "density_norm": "count"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================223
    控制带宽
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="deck", violinparamsdict={"inner": "point", "bw_adjust": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================224
    测试一般绘图的标签参数
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================225
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================226
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/小提琴图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================227
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================228
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(titanic, "violin", xvarname="age", yvarname="class", xlabel="X轴", ylabel="Y轴", title="散点图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================229
    测试matrix矩阵图参数
    ===============================================================================230
    对角线上没有设置
    >>> ax = TidySeabornFlexible(penguins, "matrix", block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================231
    设置对角线为直方图
    >>> ax = TidySeabornFlexible(penguins, "matrix", matrixparamsdict={"subwhichplot": "hist"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================232
    设置上三角和下三角为不同的图
    >>> ax = TidySeabornFlexible(penguins, "matrix", matrixparamsdict={"subwhichplot": "kde", "upperwhichplot": "scatter", "lowerwhichplot": "kde", "issharediagy": 0}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================233
    下三角矩阵图
    >>> ax = TidySeabornFlexible(penguins, "matrix", matrixparamsdict={"subwhichplot": "kde", "lowerwhichplot": "scatter", "issharediagy": 0, "iscorner": 1}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================234
    分组矩阵散点图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================235
    设置对角线为箱线图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "box"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================236
    设置对角线为核密度估计图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================237
    设置对角线为小提琴图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "violin"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================238
    设置对角线为抖动图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "jitter"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================239
    设置对角线为经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "ecdf"}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================240
    添加图例
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, block=False)
    >>> plt.pause(4)
    >>> plt.close()
    ===============================================================================241
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, savefilename="./image/矩阵散点图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================242
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================243
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "matrix", groupby="species", matrixparamsdict={"subwhichplot": "kde", "islegend": 1}, matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================244
    测试联合图
    ===============================================================================245
    边际直方图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================246
    边际箱线图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================247
    边际小提琴图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================248
    边际核密度估计图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "kde"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================249
    边际抖动图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================250
    边际经验分布函数图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_plottype": "ecdf"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================251
    设置X和Y不同边际图
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "ecdf", "margin_y_plottype": "kde"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "kde", "margin_y_plottype": "box"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "kde", "margin_y_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "kde", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "box", "margin_y_plottype": "violin"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "box", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================252
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, savefilename="./image/联合分布图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================253
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================254
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(penguins, "joint", xvarname="bill_length_mm", yvarname="bill_depth_mm", groupby="species", jointparamsdict={"margin_x_plottype": "violin", "margin_y_plottype": "jitter"}, matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================255
    测试残差图
    ===============================================================================256
    线性回归的残差
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="weight", yvarname="displacement", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================257
    二次回归的残差
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="weight", yvarname="displacement", residparamsdict={"order": 2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", residparamsdict={"order": 2}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================258
    局部多项式回归的残差
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="weight", yvarname="displacement", residparamsdict={"islowess": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", residparamsdict={"islowess": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================259
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================260
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/残差图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================261
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================262
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(mpg, "resid", xvarname="horsepower", yvarname="mpg", xlabel="X轴", ylabel="Y轴", title="残差图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================263
    测试热图
    ===============================================================================264
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================265
    显示数据标签
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================266
    设置数据标签的格式
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================267
    设置分隔线宽度
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================268
    自定义数据标签
    >>> glue = glue.pivot(index="Model", columns="Task", values="Score")
    >>> ax = TidySeabornFlexible(glue, "heat", heatparamsdict={"annot": glue.rank(axis="columns"), "linewidths": 0.5}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================269
    换一个颜色
    >>> glue = glue.pivot(index="Model", columns="Task", values="Score")
    >>> ax = TidySeabornFlexible(glue, "heat", heatparamsdict={"annot": glue.rank(axis="columns"), "linewidths": 0.5}, colormap="viridis", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================270
    测试一般绘图的字体参数
    >>> glue = GetSeabornData("glue")
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================271
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", savefilename="./image/热图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================272
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="dark", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================273
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(glue.pivot(index="Model", columns="Task", values="Score"), "heat", heatparamsdict={"isannot": 1, "fmt": ".2f", "linewidths": 0.5}, xlabel="X轴", ylabel="Y轴", title="热图", xlabelsize=10, ylabelsize=16, titlesize=14, xticklabelsize=9, yticklabelsize=15, xticklabelrotation=30, yticklabelrotation=45, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================274
    测试Facet参数
    ===============================================================================275
    分面散点图
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", facetparamsdict={"whichplot": "scatter", "col": "time", "row": "sex"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================276
    分面直方图
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", facetparamsdict={"whichplot": "hist", "col": "time", "row": "sex"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================277
    分组分面散点图
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "time"}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================278
    分组分面散点图，添加图例
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "time", "islegend": 1}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================279
    一个列变量，分两行显示
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", facetparamsdict={"whichplot": "hist", "col": "size", "col_wrap": 3}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================280
    不共享xy轴坐标
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", facetparamsdict={"whichplot": "hist", "col": "size", "col_wrap": 3, "issharex": 0, "issharey": 0}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================281
    每一个子图的参数控制
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", facetparamsdict={"col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}}, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================282
    测试一般绘图的字体参数
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================283
    测试一般绘图的文件保存参数
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", savefilename="./image/分面图.pdf", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================284
    测试一般绘图参数的绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", snsstyle="darkgrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", snsstyle="whitegrid", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", snsstyle="white", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=0, contextstyle="talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", snsstyle="ticks", removeleftspine=0, removerightspine=1, removetopspine=1, removebottomspine=0, offset=None, trim=1, contextstyle="notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================285
    测试一般绘图参数的matplotlib绘图风格参数
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="Solarize_Light2", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="_classic_test_patch", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="_mpl-gallery", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="_mpl-gallery-nogrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="bmh", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="classic", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="dark_background", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="fast", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="fivethirtyeight", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="ggplot", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="grayscale", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-bright", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-colorblind", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-dark-palette", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-darkgrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-deep", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-muted", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-notebook", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-paper", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-pastel", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-poster", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-talk", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-ticks", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-white", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="seaborn-v0_8-whitegrid", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = TidySeabornFlexible(tips, "facet", xvarname="total_bill", yvarname="tip", groupby="sex", facetparamsdict={"whichplot": "scatter", "col": "size", "col_wrap": 3, "subplot_kws": {"xlabel_4": "X轴1", "ylabel_1": "Y轴"}, "islegend": 1}, fontfamily="幼圆", matplotlibstyle="tableau-colorblind10", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================286
    """
    # 字体对应
    fontfamily_dic = {
        "方正舒体": "FZSTK.TTF",
        "方正姚体": "FZYTK.TTF",
        "仿宋": "simfang.ttf",
        "黑体": "simhei.ttf",
        "华文彩云": "STCAIYUN.TTF",
        "华文仿宋": "STFANGSO.TTF",
        "华文琥珀": "STHUPO.TTF",
        "华文楷体": "STKAITI.TTF",
        "华文隶书": "STLITI.TTF",
        "华文宋体": "STSONG.TTF",
        "华文细黑": "STXIHEI.TTF",
        "华文新魏": "STXINWEI.TTF",
        "华文行楷": "STXINGKA.TTF",
        "华文中宋": "STZHONGS.TTF",
        "楷体": "simkai.ttf",
        "隶书": "SIMLI.TTF",
        "宋体": "simsun.ttc",
        "微软雅黑": "msyhl.ttc",
        "新宋体": "simsun.ttc",
        "幼圆": "SIMYOU.TTF",
        "TimesNewRoman": "times.ttf",
        "Arial": "arial.ttf"
    }
    # 设置字体路径
    fontpath = Path(
        current_PACKAGE_PATH, "fonts/{}".format(fontfamily_dic[fontfamily]))
    fontobj = font_manager.FontProperties(fname=fontpath)
    if plottype == "hist":
        # 默认的字典
        histparamsdictdefault = {
            "bins": "auto",
            "iskde": 0,
            "iscumulative": 0,
            "element": "bars",
            "color": None,
            "multiple": "layer",
            "isfill": 1,
            "stat": "count",
            "binwidth": None,
            "bw_adjust": 1,
            "shrink": 1,
            "islog": 0,
            "islegend": 1,
            "iscommon_norm": 0}
        # 更新字典
        histparamsdictdefault.update(histparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.histplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    color=histparamsdictdefault["color"],
                    bins=histparamsdictdefault["bins"],
                    binwidth=histparamsdictdefault["binwidth"],
                    stat=histparamsdictdefault["stat"],
                    fill=bool(
                        histparamsdictdefault["isfill"]),
                    element=histparamsdictdefault["element"],
                    multiple=histparamsdictdefault["multiple"],
                    kde=bool(
                        histparamsdictdefault["iskde"]),
                    cumulative=bool(
                        histparamsdictdefault["iscumulative"]),
                    kde_kws=None if histparamsdictdefault["bw_adjust"] == 1 else {
                        "bw_adjust": histparamsdictdefault["bw_adjust"]},
                    shrink=histparamsdictdefault["shrink"],
                    log_scale=bool(
                        histparamsdictdefault["islog"]) if histparamsdictdefault["islog"] == 0 or histparamsdictdefault["islog"] == 1 else histparamsdictdefault["islog"],
                    common_norm=bool(
                            histparamsdictdefault["iscommon_norm"]),
                    legend=bool(
                        histparamsdictdefault["islegend"]))
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.histplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    color=histparamsdictdefault["color"],
                    bins=histparamsdictdefault["bins"],
                    binwidth=histparamsdictdefault["binwidth"],
                    stat=histparamsdictdefault["stat"],
                    fill=bool(
                        histparamsdictdefault["isfill"]),
                    element=histparamsdictdefault["element"],
                    multiple=histparamsdictdefault["multiple"],
                    kde=bool(
                        histparamsdictdefault["iskde"]),
                    cumulative=bool(
                        histparamsdictdefault["iscumulative"]),
                    kde_kws=None if histparamsdictdefault["bw_adjust"] == 1 else {
                        "bw_adjust": histparamsdictdefault["bw_adjust"]},
                    shrink=histparamsdictdefault["shrink"],
                    log_scale=bool(
                        histparamsdictdefault["islog"]) if histparamsdictdefault["islog"] == 0 or histparamsdictdefault["islog"] == 1 else histparamsdictdefault["islog"],
                    common_norm=bool(
                            histparamsdictdefault["iscommon_norm"]),
                    legend=bool(
                        histparamsdictdefault["islegend"]))
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "bar":
        # 默认的字典
        barparamsdictdefault = {
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "n_boot": 1000,
            "seed": None,
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "width": 0.8,
            "dodge": "auto",
            "gap": 0,
            "islog": 0,
            "legend": "auto",
            "capsize": 0,
            "isshowdatalabel": 0,
            "datalabelsize": 10,
            "datalabelformat": "%g",
            "datalabelcolor": "black",
            "errorbar_linewidth": 1,
            "errorbar_linecolor": "black",
            "errorbar_linestyle": "-"}
        # 更新字典
        barparamsdictdefault.update(barparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                ax = sns.barplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                                 hue_order=hue_order, order=order, estimator=barparamsdictdefault[
                                     "estimator"],
                                 errorbar=barparamsdictdefault["errorbar"], n_boot=barparamsdictdefault["n_boot"],
                                 seed=barparamsdictdefault["seed"], orient=barparamsdictdefault["orient"],
                                 color=barparamsdictdefault["color"], saturation=barparamsdictdefault["saturation"],
                                 fill=bool(barparamsdictdefault["isfill"]), width=barparamsdictdefault["width"],
                                 dodge=barparamsdictdefault["dodge"], gap=barparamsdictdefault["gap"],
                                 log_scale=bool(barparamsdictdefault["islog"]) if barparamsdictdefault[
                                     "islog"] == 0 or barparamsdictdefault["islog"] == 1 else barparamsdictdefault["islog"],
                                 legend=barparamsdictdefault["legend"], capsize=barparamsdictdefault["capsize"],
                                 err_kws={"linestyle": barparamsdictdefault["errorbar_linestyle"], "color": barparamsdictdefault[
                                     "errorbar_linecolor"], "linewidth": barparamsdictdefault["errorbar_linewidth"]}
                                 )
                if bool(barparamsdictdefault["isshowdatalabel"]):
                    ax.bar_label(
                        ax.containers[0],
                        fontsize=barparamsdictdefault["datalabelsize"],
                        fmt=barparamsdictdefault["datalabelformat"],
                        color=barparamsdictdefault["datalabelcolor"])
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                ax = sns.barplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                                 hue_order=hue_order, order=order, estimator=barparamsdictdefault[
                                     "estimator"],
                                 errorbar=barparamsdictdefault["errorbar"], n_boot=barparamsdictdefault["n_boot"],
                                 seed=barparamsdictdefault["seed"], orient=barparamsdictdefault["orient"],
                                 color=barparamsdictdefault["color"], saturation=barparamsdictdefault["saturation"],
                                 fill=bool(barparamsdictdefault["isfill"]), width=barparamsdictdefault["width"],
                                 dodge=barparamsdictdefault["dodge"], gap=barparamsdictdefault["gap"],
                                 log_scale=bool(barparamsdictdefault["islog"]) if barparamsdictdefault[
                                     "islog"] == 0 or barparamsdictdefault["islog"] == 1 else barparamsdictdefault["islog"],
                                 legend=barparamsdictdefault["legend"], capsize=barparamsdictdefault["capsize"],
                                 err_kws={"linestyle": barparamsdictdefault["errorbar_linestyle"], "color": barparamsdictdefault[
                                     "errorbar_linecolor"], "linewidth": barparamsdictdefault["errorbar_linewidth"]}
                                 )
                if bool(barparamsdictdefault["isshowdatalabel"]):
                    ax.bar_label(
                        ax.containers[0],
                        fontsize=barparamsdictdefault["datalabelsize"],
                        fmt=barparamsdictdefault["datalabelformat"],
                        color=barparamsdictdefault["datalabelcolor"])
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "box":
        # 默认的字典
        boxparamsdictdefault = {
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "dodge": "auto",
            "width": 0.8,
            "gap": 0,
            "whis": 1.5,
            "linecolor": "auto",
            "linewidth": None,
            "fliersize": None,
            "islog": 0,
            "legend": "auto",
            "isnotch": 0,
            "isshowmean": 0,
            "isshowfliers": 1,
            "meanlinecolor": "red",
            "meanlinewidth": 1}
        # 更新字典
        boxparamsdictdefault.update(boxparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.boxplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    order=order,
                    orient=boxparamsdictdefault["orient"],
                    color=boxparamsdictdefault["color"],
                    saturation=boxparamsdictdefault["saturation"],
                    fill=bool(
                        boxparamsdictdefault["isfill"]),
                    dodge=boxparamsdictdefault["dodge"] if boxparamsdictdefault["dodge"] == "auto" else bool(
                        boxparamsdictdefault["dodge"]),
                    width=boxparamsdictdefault["width"],
                    gap=boxparamsdictdefault["gap"],
                    whis=boxparamsdictdefault["whis"],
                    linecolor=boxparamsdictdefault["linecolor"],
                    linewidth=boxparamsdictdefault["linewidth"],
                    fliersize=boxparamsdictdefault["fliersize"],
                    log_scale=bool(
                        boxparamsdictdefault["islog"]) if boxparamsdictdefault["islog"] == 1 or boxparamsdictdefault["islog"] == 0 else boxparamsdictdefault["islog"],
                    legend=boxparamsdictdefault["legend"],
                    notch=bool(
                        boxparamsdictdefault["isnotch"]),
                    showmeans=bool(
                        boxparamsdictdefault["isshowmean"]),
                    meanline=bool(
                        boxparamsdictdefault["isshowmean"]),
                    showfliers=bool(
                        boxparamsdictdefault["isshowfliers"]),
                    meanprops={
                        "color": boxparamsdictdefault["meanlinecolor"],
                        "linewidth": boxparamsdictdefault["meanlinewidth"]})
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.boxplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    order=order,
                    orient=boxparamsdictdefault["orient"],
                    color=boxparamsdictdefault["color"],
                    saturation=boxparamsdictdefault["saturation"],
                    fill=bool(
                        boxparamsdictdefault["isfill"]),
                    dodge=boxparamsdictdefault["dodge"] if boxparamsdictdefault["dodge"] == "auto" else bool(
                        boxparamsdictdefault["dodge"]),
                    width=boxparamsdictdefault["width"],
                    gap=boxparamsdictdefault["gap"],
                    whis=boxparamsdictdefault["whis"],
                    linecolor=boxparamsdictdefault["linecolor"],
                    linewidth=boxparamsdictdefault["linewidth"],
                    fliersize=boxparamsdictdefault["fliersize"],
                    log_scale=bool(
                        boxparamsdictdefault["islog"]) if boxparamsdictdefault["islog"] == 1 or boxparamsdictdefault["islog"] == 0 else boxparamsdictdefault["islog"],
                    legend=boxparamsdictdefault["legend"],
                    notch=bool(
                        boxparamsdictdefault["isnotch"]),
                    showmeans=bool(
                        boxparamsdictdefault["isshowmean"]),
                    meanline=bool(
                        boxparamsdictdefault["isshowmean"]),
                    showfliers=bool(
                        boxparamsdictdefault["isshowfliers"]),
                    meanprops={
                        "color": boxparamsdictdefault["meanlinecolor"],
                        "linewidth": boxparamsdictdefault["meanlinewidth"]})
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "kde":
        # 默认的字典
        kdeparamsdictdefault = {
            "color": None,
            "isfill": 0,
            "multiple": "layer",
            "iscumulative": 0,
            "bw_adjust": 1,
            "islog": 0,
            "level": 10,
            "thresh": 0.5,
            "islegend": 1,
            "iscommon_norm": 0}
        # 更新字典
        kdeparamsdictdefault.update(kdeparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.kdeplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                            hue_order=hue_order, color=kdeparamsdictdefault["color"],
                            fill=bool(kdeparamsdictdefault["isfill"]), multiple=kdeparamsdictdefault["multiple"],
                            cumulative=bool(kdeparamsdictdefault["iscumulative"]), bw_adjust=kdeparamsdictdefault["bw_adjust"],
                            log_scale=bool(kdeparamsdictdefault["islog"]) if kdeparamsdictdefault[
                                "islog"] == 0 or kdeparamsdictdefault["islog"] == 1 else kdeparamsdictdefault["islog"],
                            levels=kdeparamsdictdefault["level"], thresh=kdeparamsdictdefault["thresh"],
                            legend=bool(kdeparamsdictdefault["islegend"]), common_norm=bool(kdeparamsdictdefault["iscommon_norm"])
                            )
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.kdeplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                            hue_order=hue_order, color=kdeparamsdictdefault["color"],
                            fill=bool(kdeparamsdictdefault["isfill"]), multiple=kdeparamsdictdefault["multiple"],
                            cumulative=bool(kdeparamsdictdefault["iscumulative"]), bw_adjust=kdeparamsdictdefault["bw_adjust"],
                            log_scale=bool(kdeparamsdictdefault["islog"]) if kdeparamsdictdefault[
                                "islog"] == 0 or kdeparamsdictdefault["islog"] == 1 else kdeparamsdictdefault["islog"],
                            levels=kdeparamsdictdefault["level"], thresh=kdeparamsdictdefault["thresh"],
                            legend=bool(kdeparamsdictdefault["islegend"]), common_norm=bool(kdeparamsdictdefault["iscommon_norm"])
                            )
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "count":
        # 默认的字典
        countparamsdictdefault = {
            "orient": None,
            "color": None,
            "isfill": 1,
            "saturation": 0.75,
            "stat": "count",
            "width": 0.8,
            "dodge": "auto",
            "gap": 0,
            "islog": 0,
            "legend": "auto"}
        # 更新字典
        countparamsdictdefault.update(countparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.countplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                              hue_order=hue_order, order=order, orient=countparamsdictdefault[
                                  "orient"],
                              color=countparamsdictdefault["color"], fill=bool(
                                  countparamsdictdefault["isfill"]),
                              saturation=countparamsdictdefault["saturation"],
                              stat=countparamsdictdefault["stat"],
                              width=countparamsdictdefault["width"],
                              dodge=countparamsdictdefault["dodge"] if countparamsdictdefault["dodge"] == "auto" else bool(
                                  countparamsdictdefault["dodge"]),
                              gap=countparamsdictdefault["gap"],
                              log_scale=bool(countparamsdictdefault["islog"]) if countparamsdictdefault[
                                  "islog"] == 0 or countparamsdictdefault["islog"] == 1 else countparamsdictdefault["islog"],
                              legend=countparamsdictdefault["legend"]
                              )
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.countplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                              hue_order=hue_order, order=order, orient=countparamsdictdefault[
                                  "orient"],
                              color=countparamsdictdefault["color"], fill=bool(
                                  countparamsdictdefault["isfill"]),
                              saturation=countparamsdictdefault["saturation"],
                              stat=countparamsdictdefault["stat"],
                              width=countparamsdictdefault["width"],
                              dodge=countparamsdictdefault["dodge"] if countparamsdictdefault["dodge"] == "auto" else bool(
                                  countparamsdictdefault["dodge"]),
                              gap=countparamsdictdefault["gap"],
                              log_scale=bool(countparamsdictdefault["islog"]) if countparamsdictdefault[
                                  "islog"] == 0 or countparamsdictdefault["islog"] == 1 else countparamsdictdefault["islog"],
                              legend=countparamsdictdefault["legend"]
                              )
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "ecdf":
        # 默认的字典
        ecdfparamsdictdefault = {
            "stat": "proportion",
            "iscomplementary": 0,
            "islog": None,
            "islegend": 1}
        # 更新字典
        ecdfparamsdictdefault.update(ecdfparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.ecdfplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    stat=ecdfparamsdictdefault["stat"],
                    complementary=bool(
                        ecdfparamsdictdefault["iscomplementary"]),
                    log_scale=ecdfparamsdictdefault["islog"] if ecdfparamsdictdefault["islog"] is None else bool(
                        ecdfparamsdictdefault["islog"]),
                    legend=bool(
                        ecdfparamsdictdefault["islegend"]))
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.ecdfplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    stat=ecdfparamsdictdefault["stat"],
                    complementary=bool(
                        ecdfparamsdictdefault["iscomplementary"]),
                    log_scale=ecdfparamsdictdefault["islog"] if ecdfparamsdictdefault["islog"] is None else bool(
                        ecdfparamsdictdefault["islog"]),
                    legend=bool(
                        ecdfparamsdictdefault["islegend"]))
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "fit":
        # 默认的字典
        fitparamsdictdefault = {
            "col": None,
            "row": None,
            "marker": 'o',
            "col_order": None,
            "row_order": None,
            "islegend": 1,
            "isscatter": 1,
            "isreg": 1,
            "ci": 95,
            "order": 1,
            "islogistic": 0,
            "islowess": 0,
            "isrobust": 0,
            "issharex": 1,
            "issharey": 1,
            "islegendout": 1,
            "subplot_kws": None,
            "title": None}
        # 更新字典
        fitparamsdictdefault.update(fitparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 核心变量参数，颜色参数，图形参数
                facet = sns.lmplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 5 else 5,
                    aspect=fig_length / fig_width if fig_length / fig_width == 1 else 1,
                    col=fitparamsdictdefault["col"],
                    row=fitparamsdictdefault["row"],
                    col_order=fitparamsdictdefault["col_order"],
                    row_order=fitparamsdictdefault["row_order"],
                    markers=fitparamsdictdefault["marker"],
                    legend=bool(
                        fitparamsdictdefault["islegend"]),
                    scatter=bool(
                        fitparamsdictdefault["isscatter"]),
                    fit_reg=bool(
                        fitparamsdictdefault["isreg"]),
                    ci=fitparamsdictdefault["ci"],
                    order=fitparamsdictdefault["order"],
                    logistic=bool(
                        fitparamsdictdefault["islogistic"]),
                    lowess=bool(
                        fitparamsdictdefault["islowess"]),
                    robust=bool(
                        fitparamsdictdefault["isrobust"]),
                    facet_kws={
                        "sharex": bool(
                            fitparamsdictdefault["issharex"]),
                        "sharey": bool(
                            fitparamsdictdefault["issharey"]),
                        "legend_out": bool(
                            fitparamsdictdefault["islegendout"])})
        else:
            with plt.style.context(matplotlibstyle):
                # 核心变量参数，颜色参数，图形参数
                facet = sns.lmplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 5 else 5,
                    aspect=fig_length / fig_width if fig_length / fig_width == 1 else 1,
                    col=fitparamsdictdefault["col"],
                    row=fitparamsdictdefault["row"],
                    col_order=fitparamsdictdefault["col_order"],
                    row_order=fitparamsdictdefault["row_order"],
                    markers=fitparamsdictdefault["marker"],
                    legend=bool(
                        fitparamsdictdefault["islegend"]),
                    scatter=bool(
                        fitparamsdictdefault["isscatter"]),
                    fit_reg=bool(
                        fitparamsdictdefault["isreg"]),
                    ci=fitparamsdictdefault["ci"],
                    order=fitparamsdictdefault["order"],
                    logistic=bool(
                        fitparamsdictdefault["islogistic"]),
                    lowess=bool(
                        fitparamsdictdefault["islowess"]),
                    robust=bool(
                        fitparamsdictdefault["isrobust"]),
                    facet_kws={
                        "sharex": bool(
                            fitparamsdictdefault["issharex"]),
                        "sharey": bool(
                            fitparamsdictdefault["issharey"]),
                        "legend_out": bool(
                            fitparamsdictdefault["islegendout"])})
        fig = facet.fig
        axes = facet.axes
        axes = axes.flatten()
        subplotkws = fitparamsdictdefault["subplot_kws"]
        if subplotkws is not None:
            for ax, i in zip(axes, range(1, len(axes) + 1)):
                # 标题参数
                if subplotkws.get("xlabel_{}".format(i), None) is not None:
                    ax.set_xlabel(subplotkws["xlabel_{}".format(i)], fontproperties=fontobj,
                                  fontsize=subplotkws.get("xlabelsize_{}".format(i), 12))
                if subplotkws.get("ylabel_{}".format(i), None) is not None:
                    ax.set_ylabel(subplotkws["ylabel_{}".format(i)], fontproperties=fontobj,
                                  fontsize=subplotkws.get("ylabelsize_{}".format(i), 12))
                if subplotkws.get("title_{}".format(i), None) is not None:
                    ax.set_title(subplotkws["title_{}".format(
                        i)], fontproperties=fontobj, fontsize=subplotkws.get("titlesize", 12))
                # 刻度参数，刻度标签参数
                ax.tick_params(
                    'x', labelsize=subplotkws.get(
                        "xticklabelsize_{}".format(i), 12), rotation=subplotkws.get(
                        "xticklabelrotation_{}".format(i), 0))
                ax.tick_params(
                    'y', labelsize=subplotkws.get(
                        "yticklabelsize_{}".format(i), 12), rotation=subplotkws.get(
                        "yticklabelrotation_{}".format(i), 0))
                ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                              fontproperties=fontobj)
                ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                              fontproperties=fontobj)
        else:
            pass
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if fitparamsdictdefault["title"] is not None:
            plt.suptitle(fitparamsdictdefault["title"], fontproperties=fontobj)
        else:
            pass
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return axes
    elif plottype == "line":
        # 默认的字典
        lineparamsdictdefault = {
            "sizegroup": None,
            "stylegroup": None,
            "size_order": None,
            "style_order": None,
            "orient": "x",
            "issort": 1,
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "markers": None,
            "dashes": 1,
            "err_style": "band"}
        # 更新字典
        lineparamsdictdefault.update(lineparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.lineplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                             hue_order=hue_order, size=lineparamsdictdefault["sizegroup"],
                             style=lineparamsdictdefault["stylegroup"],
                             size_order=lineparamsdictdefault["size_order"],
                             style_order=lineparamsdictdefault["style_order"],
                             orient=lineparamsdictdefault["orient"],
                             sort=bool(lineparamsdictdefault["issort"]),
                             estimator=lineparamsdictdefault["estimator"],
                             errorbar=lineparamsdictdefault["errorbar"],
                             markers=bool(lineparamsdictdefault["markers"]) if lineparamsdictdefault[
                                 "markers"] == 0 or lineparamsdictdefault["markers"] == 1 else lineparamsdictdefault["markers"],
                             dashes=bool(lineparamsdictdefault["dashes"]) if lineparamsdictdefault[
                                 "dashes"] == 0 or lineparamsdictdefault["dashes"] == 1 else lineparamsdictdefault["dashes"],
                             err_style=lineparamsdictdefault["err_style"]
                             )
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.lineplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                             hue_order=hue_order, size=lineparamsdictdefault["sizegroup"],
                             style=lineparamsdictdefault["stylegroup"],
                             size_order=lineparamsdictdefault["size_order"],
                             style_order=lineparamsdictdefault["style_order"],
                             orient=lineparamsdictdefault["orient"],
                             sort=bool(lineparamsdictdefault["issort"]),
                             estimator=lineparamsdictdefault["estimator"],
                             errorbar=lineparamsdictdefault["errorbar"],
                             markers=bool(lineparamsdictdefault["markers"]) if lineparamsdictdefault[
                                 "markers"] == 0 or lineparamsdictdefault["markers"] == 1 else lineparamsdictdefault["markers"],
                             dashes=bool(lineparamsdictdefault["dashes"]) if lineparamsdictdefault[
                                 "dashes"] == 0 or lineparamsdictdefault["dashes"] == 1 else lineparamsdictdefault["dashes"],
                             err_style=lineparamsdictdefault["err_style"]
                             )
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "point":
        # 默认的字典
        pointparamsdictdefault = {
            "estimator": "mean",
            "errorbar": (
                "ci",
                95),
            "n_boot": 1000,
            "orient": "v",
            "color": None,
            "markers": "o",
            "linestyles": "-",
            "dodge": 0,
            "islog": 0,
            "legend": "auto",
            "capsize": 0,
            "errorbar_linewidth": 2,
            "errorbar_linestyle": "-",
            "errorbar_linecolor": "black",
            "markersize": 9}
        # 更新字典
        pointparamsdictdefault.update(pointparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.pointplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                              hue_order=hue_order, order=order, orient=pointparamsdictdefault[
                                  "orient"],
                              estimator=pointparamsdictdefault["estimator"],
                              errorbar=pointparamsdictdefault["errorbar"],
                              markers=pointparamsdictdefault["markers"],
                              linestyles=pointparamsdictdefault["linestyles"],
                              n_boot=pointparamsdictdefault["n_boot"],
                              color=pointparamsdictdefault["color"],
                              dodge=bool(pointparamsdictdefault["dodge"]) if pointparamsdictdefault[
                                  "dodge"] == 0 or pointparamsdictdefault["dodge"] == 1 else pointparamsdictdefault["dodge"],
                              log_scale=bool(pointparamsdictdefault["islog"]) if pointparamsdictdefault[
                                  "islog"] == 0 or pointparamsdictdefault["islog"] == 1 else pointparamsdictdefault["islog"],
                              legend=pointparamsdictdefault["legend"], capsize=pointparamsdictdefault["capsize"],
                              err_kws={"linewidth": pointparamsdictdefault["errorbar_linewidth"], "linestyle": pointparamsdictdefault[
                                  "errorbar_linestyle"], "color": pointparamsdictdefault["errorbar_linecolor"]},
                              markersize=pointparamsdictdefault["markersize"]
                              )
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.pointplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                              hue_order=hue_order, orient=pointparamsdictdefault["orient"],
                              estimator=pointparamsdictdefault["estimator"],
                              errorbar=pointparamsdictdefault["errorbar"],
                              markers=pointparamsdictdefault["markers"],
                              linestyles=pointparamsdictdefault["linestyles"],
                              n_boot=pointparamsdictdefault["n_boot"],
                              color=pointparamsdictdefault["color"],
                              dodge=bool(pointparamsdictdefault["dodge"]) if pointparamsdictdefault[
                                  "dodge"] == 0 or pointparamsdictdefault["dodge"] == 1 else pointparamsdictdefault["dodge"],
                              log_scale=bool(pointparamsdictdefault["islog"]) if pointparamsdictdefault[
                                  "islog"] == 0 or pointparamsdictdefault["islog"] == 1 else pointparamsdictdefault["islog"],
                              legend=pointparamsdictdefault["legend"], capsize=pointparamsdictdefault["capsize"],
                              err_kws={"linewidth": pointparamsdictdefault["errorbar_linewidth"], "linestyle": pointparamsdictdefault[
                                  "errorbar_linestyle"], "color": pointparamsdictdefault["errorbar_linecolor"]},
                              markersize=pointparamsdictdefault["markersize"]
                              )
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "scatter":
        # 默认的字典
        scatterparamsdictdefault = {
            "sizegroup": None,
            "stylegroup": None,
            "size_order": None,
            "style_order": None,
            "markers": True,
            "legend": "auto",
            "sizes": None}
        # 更新字典
        scatterparamsdictdefault.update(scatterparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.scatterplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    size=scatterparamsdictdefault["sizegroup"],
                    style=scatterparamsdictdefault["stylegroup"],
                    size_order=scatterparamsdictdefault["size_order"],
                    style_order=scatterparamsdictdefault["style_order"],
                    markers=scatterparamsdictdefault["markers"],
                    legend=scatterparamsdictdefault["legend"],
                    sizes=scatterparamsdictdefault["sizes"])
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.scatterplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    size=scatterparamsdictdefault["sizegroup"],
                    style=scatterparamsdictdefault["stylegroup"],
                    size_order=scatterparamsdictdefault["size_order"],
                    style_order=scatterparamsdictdefault["style_order"],
                    markers=scatterparamsdictdefault["markers"],
                    legend=scatterparamsdictdefault["legend"],
                    sizes=scatterparamsdictdefault["sizes"])
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "jitter":
        # 默认的字典
        jitterparamsdictdefault = {
            "jitter": 1,
            "isdodge": 0,
            "orient": None,
            "color": None,
            "size": 5,
            "legend": "auto"}
        # 更新字典
        jitterparamsdictdefault.update(jitterparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.stripplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                              hue_order=hue_order, order=order,
                              jitter=bool(jitterparamsdictdefault["jitter"]) if jitterparamsdictdefault[
                                  "jitter"] == 1 or jitterparamsdictdefault["jitter"] == 0 else jitterparamsdictdefault["jitter"],
                              dodge=bool(jitterparamsdictdefault["isdodge"]),
                              orient=jitterparamsdictdefault["orient"],
                              color=jitterparamsdictdefault["color"],
                              size=jitterparamsdictdefault["size"],
                              legend=jitterparamsdictdefault["legend"]
                              )
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.stripplot(data=df, x=xvarname, y=yvarname, hue=groupby, ax=ax, palette=colormap,
                              hue_order=hue_order, order=order,
                              jitter=bool(jitterparamsdictdefault["jitter"]) if jitterparamsdictdefault[
                                  "jitter"] == 1 or jitterparamsdictdefault["jitter"] == 0 else jitterparamsdictdefault["jitter"],
                              dodge=bool(jitterparamsdictdefault["isdodge"]),
                              orient=jitterparamsdictdefault["orient"],
                              color=jitterparamsdictdefault["color"],
                              size=jitterparamsdictdefault["size"],
                              legend=jitterparamsdictdefault["legend"]
                              )
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "violin":
        # 默认的字典
        violinparamsdictdefault = {
            "orient": None,
            "color": None,
            "saturation": 0.75,
            "isfill": 1,
            "dodge": "auto",
            "width": 0.8,
            "gap": 0,
            "linecolor": "auto",
            "linewidth": None,
            "islog": 0,
            "legend": "auto",
            "bw_adjust": 1,
            "density_norm": "area",
            "inner": "box",
            "issplit": 0}
        # 更新字典
        violinparamsdictdefault.update(violinparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.violinplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    order=order,
                    orient=violinparamsdictdefault["orient"],
                    color=violinparamsdictdefault["color"],
                    saturation=violinparamsdictdefault["saturation"],
                    fill=bool(
                        violinparamsdictdefault["isfill"]),
                    dodge=violinparamsdictdefault["dodge"] if violinparamsdictdefault["dodge"] == "auto" else bool(
                        violinparamsdictdefault["dodge"]),
                    width=violinparamsdictdefault["width"],
                    gap=violinparamsdictdefault["gap"],
                    linecolor=violinparamsdictdefault["linecolor"],
                    linewidth=violinparamsdictdefault["linewidth"],
                    log_scale=bool(
                        violinparamsdictdefault["islog"]) if violinparamsdictdefault["islog"] == 1 or violinparamsdictdefault["islog"] == 0 else violinparamsdictdefault["islog"],
                    legend=violinparamsdictdefault["legend"],
                    bw_adjust=violinparamsdictdefault["bw_adjust"],
                    density_norm=violinparamsdictdefault["density_norm"],
                    inner=violinparamsdictdefault["inner"],
                    split=bool(
                        violinparamsdictdefault["issplit"]))
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.violinplot(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    ax=ax,
                    palette=colormap,
                    hue_order=hue_order,
                    order=order,
                    orient=violinparamsdictdefault["orient"],
                    color=violinparamsdictdefault["color"],
                    saturation=violinparamsdictdefault["saturation"],
                    fill=bool(
                        violinparamsdictdefault["isfill"]),
                    dodge=violinparamsdictdefault["dodge"] if violinparamsdictdefault["dodge"] == "auto" else bool(
                        violinparamsdictdefault["dodge"]),
                    width=violinparamsdictdefault["width"],
                    gap=violinparamsdictdefault["gap"],
                    linecolor=violinparamsdictdefault["linecolor"],
                    linewidth=violinparamsdictdefault["linewidth"],
                    log_scale=bool(
                        violinparamsdictdefault["islog"]) if violinparamsdictdefault["islog"] == 1 or violinparamsdictdefault["islog"] == 0 else violinparamsdictdefault["islog"],
                    legend=violinparamsdictdefault["legend"],
                    bw_adjust=violinparamsdictdefault["bw_adjust"],
                    density_norm=violinparamsdictdefault["density_norm"],
                    inner=violinparamsdictdefault["inner"],
                    split=bool(
                        violinparamsdictdefault["issplit"]))
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "matrix":
        # 默认的字典
        matrixparamsdictdefault = {
            "vars": None,
            "x_vars": None,
            "y_vars": None,
            "iscorner": 0,
            "mainwhichplot": None,
            "subwhichplot": None,
            "upperwhichplot": None,
            "lowerwhichplot": None,
            "islegend": 0,
            "title": None,
            "issharediagy": 1}
        # 更新字典
        matrixparamsdictdefault.update(matrixparamsdict)
        subwhichplotdict = {
            "hist": sns.histplot,
            "kde": sns.kdeplot,
            "box": sns.boxplot,
            "violin": sns.violinplot,
            "jitter": sns.stripplot,
            "ecdf": sns.ecdfplot
        }
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 核心变量参数，颜色参数，图形参数
                facet = sns.PairGrid(
                    data=df,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 2.5 else 2.5,
                    aspect=fig_length /
                    fig_width if fig_length /
                    fig_width == 1 else 1,
                    vars=matrixparamsdictdefault["vars"],
                    x_vars=matrixparamsdictdefault["x_vars"],
                    y_vars=matrixparamsdictdefault["y_vars"],
                    corner=bool(
                        matrixparamsdictdefault["iscorner"]),
                    diag_sharey=bool(
                        matrixparamsdictdefault["issharediagy"]))
                if matrixparamsdictdefault["subwhichplot"] is not None:
                    facet.map_diag(
                        subwhichplotdict[matrixparamsdictdefault["subwhichplot"]])
                    if matrixparamsdictdefault["mainwhichplot"] is None:
                        if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                            facet.map_upper(
                                sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                            facet.map_lower(
                                sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                        else:
                            facet.map_offdiag(sns.scatterplot)
                    else:
                        facet.map_offdiag(
                            sns.scatterplot if matrixparamsdictdefault[
                                "mainwhichplot"] == "scatter" else sns.kdeplot
                        )
                else:
                    if matrixparamsdictdefault["mainwhichplot"] is None:
                        if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                            facet.map_upper(
                                sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                            facet.map_lower(
                                sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                        else:
                            facet.map(sns.scatterplot)
                    else:
                        facet.map_offdiag(
                            sns.scatterplot if matrixparamsdictdefault[
                                "mainwhichplot"] == "scatter" else sns.kdeplot
                        )
                if bool(matrixparamsdictdefault["islegend"]):
                    facet.add_legend()
                else:
                    pass
        else:
            with plt.style.context(matplotlibstyle):
                # 核心变量参数，颜色参数，图形参数
                facet = sns.PairGrid(
                    data=df,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 2.5 else 2.5,
                    aspect=fig_length /
                    fig_width if fig_length /
                    fig_width == 1 else 1,
                    vars=matrixparamsdictdefault["vars"],
                    x_vars=matrixparamsdictdefault["x_vars"],
                    y_vars=matrixparamsdictdefault["y_vars"],
                    corner=bool(
                        matrixparamsdictdefault["iscorner"]),
                    diag_sharey=bool(
                        matrixparamsdictdefault["issharediagy"]))
                if matrixparamsdictdefault["subwhichplot"] is not None:
                    facet.map_diag(
                        subwhichplotdict[matrixparamsdictdefault["subwhichplot"]])
                    if matrixparamsdictdefault["mainwhichplot"] is None:
                        if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                            facet.map_upper(
                                sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                            facet.map_lower(
                                sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                        else:
                            facet.map_offdiag(sns.scatterplot)
                    else:
                        facet.map_offdiag(
                            sns.scatterplot if matrixparamsdictdefault[
                                "mainwhichplot"] == "scatter" else sns.kdeplot
                        )
                else:
                    if matrixparamsdictdefault["mainwhichplot"] is None:
                        if matrixparamsdictdefault["upperwhichplot"] is not None and matrixparamsdictdefault["lowerwhichplot"] is not None:
                            facet.map_upper(
                                sns.scatterplot if matrixparamsdictdefault["upperwhichplot"] == "scatter" else sns.kdeplot)
                            facet.map_lower(
                                sns.scatterplot if matrixparamsdictdefault["lowerwhichplot"] == "scatter" else sns.kdeplot)
                        else:
                            facet.map(sns.scatterplot)
                    else:
                        facet.map_offdiag(
                            sns.scatterplot if matrixparamsdictdefault[
                                "mainwhichplot"] == "scatter" else sns.kdeplot
                        )
                if bool(matrixparamsdictdefault["islegend"]):
                    facet.add_legend()
                else:
                    pass
        fig = facet.fig
        axes = facet.axes
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if matrixparamsdictdefault["title"] is not None:
            plt.suptitle(
                matrixparamsdictdefault["title"], fontproperties=fontobj)
        else:
            pass
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return axes
    elif plottype == "joint":
        # 默认的字典
        jointparamsdictdefault = {
            "margin_plottype": "hist",
            "margin_x_plottype": None,
            "margin_y_plottype": None,
            "space": 0.2,
            "isdropna": 0,
            "xlim": None,
            "ylim": None,
            "isshowmargin_ticks": 0,
            "title": None}
        # 更新字典
        jointparamsdictdefault.update(jointparamsdict)
        marginplotdict = {
            "hist": sns.histplot,
            "kde": sns.kdeplot,
            "box": sns.boxplot,
            "violin": sns.violinplot,
            "jitter": sns.stripplot,
            "ecdf": sns.ecdfplot
        }
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 核心变量参数，颜色参数，图形参数
                facet = sns.JointGrid(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 6 else 6,
                    ratio=5,
                    xlim=jointparamsdictdefault["xlim"],
                    ylim=jointparamsdictdefault["ylim"],
                    dropna=bool(
                        jointparamsdictdefault["isdropna"]),
                    marginal_ticks=bool(
                        jointparamsdictdefault["isshowmargin_ticks"]))
                if jointparamsdictdefault["margin_x_plottype"] is not None and jointparamsdictdefault["margin_y_plottype"] is not None:
                    ax_x = facet.ax_marg_x
                    ax_y = facet.ax_marg_y
                    sns.scatterplot(data=df, x=xvarname,
                                    y=yvarname, ax=facet.ax_joint)
                    marginplotdict[jointparamsdictdefault["margin_x_plottype"]](
                        data=df, x=xvarname, ax=ax_x)
                    marginplotdict[jointparamsdictdefault["margin_y_plottype"]](
                        data=df, y=yvarname, ax=ax_y)
                else:
                    facet.plot(
                        sns.scatterplot, marginplotdict[jointparamsdictdefault["margin_plottype"]])

        else:
            with plt.style.context(matplotlibstyle):
                # 核心变量参数，颜色参数，图形参数
                facet = sns.JointGrid(
                    data=df,
                    x=xvarname,
                    y=yvarname,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 6 else 6,
                    ratio=5,
                    xlim=jointparamsdictdefault["xlim"],
                    ylim=jointparamsdictdefault["ylim"],
                    dropna=bool(
                        jointparamsdictdefault["isdropna"]),
                    marginal_ticks=bool(
                        jointparamsdictdefault["isshowmargin_ticks"]))
                if jointparamsdictdefault["margin_x_plottype"] is not None and jointparamsdictdefault["margin_y_plottype"] is not None:
                    ax_x = facet.ax_marg_x
                    ax_y = facet.ax_marg_y
                    sns.scatterplot(data=df, x=xvarname,
                                    y=yvarname, ax=facet.ax_joint)
                    marginplotdict[jointparamsdictdefault["margin_x_plottype"]](
                        data=df, x=xvarname, ax=ax_x)
                    marginplotdict[jointparamsdictdefault["margin_y_plottype"]](
                        data=df, y=yvarname, ax=ax_y)
                else:
                    facet.plot(
                        sns.scatterplot, marginplotdict[jointparamsdictdefault["margin_plottype"]])
        fig = facet.figure
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if jointparamsdictdefault["title"] is not None:
            plt.suptitle(
                jointparamsdictdefault["title"], fontproperties=fontobj)
        else:
            pass
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return fig
    elif plottype == "resid":
        # 默认的字典
        residparamsdictdefault = {
            "islowess": 0,
            "isrobust": 0,
            "order": 1,
            "label": None,
            "color": None}
        # 更新字典
        residparamsdictdefault.update(residparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.residplot(data=df, x=xvarname, y=yvarname, ax=ax,
                              lowess=bool(residparamsdictdefault["islowess"]),
                              robust=bool(residparamsdictdefault["isrobust"]),
                              order=residparamsdictdefault["order"],
                              label=residparamsdictdefault["label"],
                              color=residparamsdictdefault["color"]
                              )
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                sns.residplot(data=df, x=xvarname, y=yvarname, ax=ax,
                              lowess=bool(residparamsdictdefault["islowess"]),
                              robust=bool(residparamsdictdefault["isrobust"]),
                              order=residparamsdictdefault["order"],
                              label=residparamsdictdefault["label"],
                              color=residparamsdictdefault["color"]
                              )
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "heat":
        # 默认的字典
        heatparamsdictdefault = {
            "vmin": None,
            "vmax": None,
            "isannot": None,
            "annot": None,
            "fmt": ".2g",
            "annot_size": None,
            "linewidths": 0,
            "linecolor": "white",
            "iscolorbar": 1,
            "issquare": 0,
            "xticklabels": "auto",
            "yticklabels": "auto"}
        # 更新字典
        heatparamsdictdefault.update(heatparamsdict)
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                if heatparamsdictdefault["annot"] is None:
                    sns.heatmap(data=df, ax=ax,
                                vmin=heatparamsdictdefault["vmin"],
                                vmax=heatparamsdictdefault["vmax"],
                                cmap=colormap,
                                annot=bool(heatparamsdictdefault["isannot"]) if heatparamsdictdefault[
                                    "isannot"] == 0 or heatparamsdictdefault["isannot"] == 1 else heatparamsdictdefault["isannot"],
                                fmt=heatparamsdictdefault["fmt"],
                                annot_kws={
                                    "fontsize": heatparamsdictdefault["annot_size"], "fontproperties": fontobj},
                                linewidths=heatparamsdictdefault["linewidths"],
                                linecolor=heatparamsdictdefault["linecolor"],
                                cbar=bool(heatparamsdictdefault["iscolorbar"]),
                                square=bool(heatparamsdictdefault["issquare"]),
                                xticklabels=heatparamsdictdefault["xticklabels"],
                                yticklabels=heatparamsdictdefault["yticklabels"]
                                )
                else:
                    sns.heatmap(
                        data=df,
                        ax=ax,
                        vmin=heatparamsdictdefault["vmin"],
                        vmax=heatparamsdictdefault["vmax"],
                        cmap=colormap,
                        annot=heatparamsdictdefault["annot"],
                        fmt=heatparamsdictdefault["fmt"],
                        annot_kws={
                            "fontsize": heatparamsdictdefault["annot_size"],
                            "fontproperties": fontobj},
                        linewidths=heatparamsdictdefault["linewidths"],
                        linecolor=heatparamsdictdefault["linecolor"],
                        cbar=bool(
                            heatparamsdictdefault["iscolorbar"]),
                        square=bool(
                            heatparamsdictdefault["issquare"]),
                        xticklabels=heatparamsdictdefault["xticklabels"],
                        yticklabels=heatparamsdictdefault["yticklabels"])
        else:
            with plt.style.context(matplotlibstyle):
                # 开始绘图，画布参数
                fig, ax = plt.subplots(
                    figsize=(fig_length, fig_width), layout=layout)
                # 核心变量参数，颜色参数，图形参数
                if heatparamsdictdefault["annot"] is None:
                    sns.heatmap(data=df, ax=ax,
                                vmin=heatparamsdictdefault["vmin"],
                                vmax=heatparamsdictdefault["vmax"],
                                cmap=colormap,
                                annot=bool(heatparamsdictdefault["isannot"]) if heatparamsdictdefault[
                                    "isannot"] == 0 or heatparamsdictdefault["isannot"] == 1 else heatparamsdictdefault["isannot"],
                                fmt=heatparamsdictdefault["fmt"],
                                annot_kws={
                                    "fontsize": heatparamsdictdefault["annot_size"], "fontproperties": fontobj},
                                linewidths=heatparamsdictdefault["linewidths"],
                                linecolor=heatparamsdictdefault["linecolor"],
                                cbar=bool(heatparamsdictdefault["iscolorbar"]),
                                square=bool(heatparamsdictdefault["issquare"]),
                                xticklabels=heatparamsdictdefault["xticklabels"],
                                yticklabels=heatparamsdictdefault["yticklabels"]
                                )
                else:
                    sns.heatmap(
                        data=df,
                        ax=ax,
                        vmin=heatparamsdictdefault["vmin"],
                        vmax=heatparamsdictdefault["vmax"],
                        cmap=colormap,
                        annot=heatparamsdictdefault["annot"],
                        fmt=heatparamsdictdefault["fmt"],
                        annot_kws={
                            "fontsize": heatparamsdictdefault["annot_size"],
                            "fontproperties": fontobj},
                        linewidths=heatparamsdictdefault["linewidths"],
                        linecolor=heatparamsdictdefault["linecolor"],
                        cbar=bool(
                            heatparamsdictdefault["iscolorbar"]),
                        square=bool(
                            heatparamsdictdefault["issquare"]),
                        xticklabels=heatparamsdictdefault["xticklabels"],
                        yticklabels=heatparamsdictdefault["yticklabels"])
        # 标题参数
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontproperties=fontobj,
                          fontsize=xlabelsize)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontproperties=fontobj,
                          fontsize=ylabelsize)
        if title is not None:
            ax.set_title(title, fontproperties=fontobj, fontsize=titlesize)
        # 刻度参数，刻度标签参数
        ax.tick_params('x', labelsize=xticklabelsize,
                       rotation=xticklabelrotation)
        ax.tick_params('y', labelsize=yticklabelsize,
                       rotation=yticklabelrotation)
        ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                      fontproperties=fontobj)
        ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                      fontproperties=fontobj)
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return ax
    elif plottype == "facet":
        # 默认的字典
        facetparamsdictdefault = {
            "col": None,
            "row": None,
            "col_order": None,
            "row_order": None,
            "issharex": 1,
            "issharey": 1,
            "islegend_out": 1,
            "xlim": None,
            "ylim": None,
            "isshowmargin_titles": 0,
            "islegend": 0,
            "whichplot": "hist",
            "subplot_kws": None,
            "title": None,
            "col_wrap": None}
        # 更新字典
        facetparamsdictdefault.update(facetparamsdict)
        facetplotdict = {
            "hist": sns.histplot,
            "bar": sns.barplot,
            "box": sns.boxplot,
            "kde": sns.kdeplot,
            "count": sns.countplot,
            "ecdf": sns.ecdfplot,
            "fit": sns.regplot,
            "line": sns.lineplot,
            "point": sns.pointplot,
            "scatter": sns.scatterplot,
            "jitter": sns.stripplot,
            "violin": sns.violinplot,
            "resid": sns.residplot,
            "heat": sns.heatmap
        }
        if matplotlibstyle is None:
            with sns.axes_style(snsstyle):
                sns.set_context(contextstyle)
                # 核心变量参数，颜色参数，图形参数
                facet = sns.FacetGrid(
                    data=df,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 3 else 3,
                    aspect=fig_length /
                    fig_width if fig_length /
                    fig_width == 1 else 1,
                    col=facetparamsdictdefault["col"],
                    row=facetparamsdictdefault["row"],
                    col_order=facetparamsdictdefault["col_order"],
                    row_order=facetparamsdictdefault["row_order"],
                    legend_out=bool(
                        facetparamsdictdefault["islegend_out"]),
                    margin_titles=bool(
                        facetparamsdictdefault["isshowmargin_titles"]),
                    sharex=bool(facetparamsdictdefault["issharex"]),
                    sharey=bool(facetparamsdictdefault["issharey"]),
                    xlim=facetparamsdictdefault["xlim"],
                    ylim=facetparamsdictdefault["ylim"],
                    col_wrap=facetparamsdictdefault["col_wrap"])
                if facetparamsdictdefault["whichplot"] != "heat":
                    facet.map_dataframe(
                        facetplotdict[facetparamsdictdefault["whichplot"]], x=xvarname, y=yvarname)
                else:
                    facet.map_dataframe(
                        facetplotdict[facetparamsdictdefault["whichplot"]], data=df[[xvarname, yvarname]])
                if bool(facetparamsdictdefault["islegend"]):
                    facet.add_legend()
                else:
                    pass
        else:
            with plt.style.context(matplotlibstyle):
                # 核心变量参数，颜色参数，图形参数
                facet = sns.FacetGrid(
                    data=df,
                    hue=groupby,
                    palette=colormap,
                    hue_order=hue_order,
                    height=fig_width if fig_width == 3 else 3,
                    aspect=fig_length /
                    fig_width if fig_length /
                    fig_width == 1 else 1,
                    col=facetparamsdictdefault["col"],
                    row=facetparamsdictdefault["row"],
                    col_order=facetparamsdictdefault["col_order"],
                    row_order=facetparamsdictdefault["row_order"],
                    legend_out=bool(
                        facetparamsdictdefault["islegend_out"]),
                    margin_titles=bool(
                        facetparamsdictdefault["isshowmargin_titles"]),
                    sharex=bool(facetparamsdictdefault["issharex"]),
                    sharey=bool(facetparamsdictdefault["issharey"]),
                    xlim=facetparamsdictdefault["xlim"],
                    ylim=facetparamsdictdefault["ylim"],
                    col_wrap=facetparamsdictdefault["col_wrap"])
                if facetparamsdictdefault["whichplot"] != "heat":
                    facet.map_dataframe(
                        facetplotdict[facetparamsdictdefault["whichplot"]], x=xvarname, y=yvarname)
                else:
                    facet.map_dataframe(
                        facetplotdict[facetparamsdictdefault["whichplot"]], data=df[[xvarname, yvarname]])
                if bool(facetparamsdictdefault["islegend"]):
                    facet.add_legend()
                else:
                    pass
        fig = facet.fig
        axes = facet.axes
        axes = axes.flatten()
        subplotkws = facetparamsdictdefault["subplot_kws"]
        if subplotkws is not None:
            for ax, i in zip(axes, range(1, len(axes) + 1)):
                # 标题参数
                if subplotkws.get("xlabel_{}".format(i), None) is not None:
                    ax.set_xlabel(subplotkws["xlabel_{}".format(i)], fontproperties=fontobj,
                                  fontsize=subplotkws.get("xlabelsize_{}".format(i), 12))
                if subplotkws.get("ylabel_{}".format(i), None) is not None:
                    ax.set_ylabel(subplotkws["ylabel_{}".format(i)], fontproperties=fontobj,
                                  fontsize=subplotkws.get("ylabelsize_{}".format(i), 12))
                if subplotkws.get("title_{}".format(i), None) is not None:
                    ax.set_title(subplotkws["title_{}".format(
                        i)], fontproperties=fontobj, fontsize=subplotkws.get("titlesize", 12))
                # 刻度参数，刻度标签参数
                ax.tick_params(
                    'x', labelsize=subplotkws.get(
                        "xticklabelsize_{}".format(i), 12), rotation=subplotkws.get(
                        "xticklabelrotation_{}".format(i), 0))
                ax.tick_params(
                    'y', labelsize=subplotkws.get(
                        "yticklabelsize_{}".format(i), 12), rotation=subplotkws.get(
                        "yticklabelrotation_{}".format(i), 0))
                ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                              fontproperties=fontobj)
                ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                              fontproperties=fontobj)
        else:
            pass
        # 移除spines
        sns.despine(
            left=removeleftspine,
            right=removerightspine,
            top=removetopspine,
            bottom=removebottomspine,
            offset=offset,
            trim=trim)
        if facetparamsdictdefault["title"] is not None:
            plt.suptitle(
                facetparamsdictdefault["title"], fontproperties=fontobj)
        else:
            pass
        if savefilename is not None:
            fig.savefig(savefilename)
        else:
            pass
        if bool(isshowplot):
            plt.show(**kwargs)
        else:
            pass
        return axes
    else:
        pass
