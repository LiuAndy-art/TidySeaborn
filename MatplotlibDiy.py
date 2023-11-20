import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import warnings
# 禁用警告
warnings.filterwarnings("ignore")

# 获取包所在的路径
current_PACKAGE_PATH = Path(__file__).resolve().parent


def MatplotlibDiy(
        fig=None,
        fig_length=6.4,
        fig_width=4.8,
        facecolor="white",
        edgecolor="white",
        layout="tight",
        xlabel=None,
        ylabel=None,
        title=None,
        xlabelsize=12,
        ylabelsize=12,
        titlesize=12,
        xlabelcolor="black",
        ylabelcolor="black",
        titlecolor="black",
        xlabelha="center",
        ylabelha="center",
        xlabelva="center",
        ylabelva="center",
        titlelabelha="center",
        titlelabelva="center",
        xlabelpad=4,
        ylabelpad=4,
        titlelabelpad=6,
        xlabelrotation=0,
        ylabelrotation=90,
        titlelabelrotation=0,
        isxlabellatex=0,
        isylabellatex=0,
        istitlelatex=0,
        xtick=None,
        ytick=None,
        xticksize=4,
        yticksize=4,
        xtickwidth=1,
        ytickwidth=1,
        xtickdirection="out",
        ytickdirection="out",
        xtickcolor="black",
        ytickcolor="black",
        xtickzc="major",
        ytickzc="major",
        xticklabel=None,
        yticklabel=None,
        xticklabelsize=12,
        yticklabelsize=12,
        xticklabelcolor="black",
        yticklabelcolor="black",
        xticklabelrotation=0,
        yticklabelrotation=0,
        xlim=None,
        ylim=None,
        leftaxiswidth=1,
        rightaxiswidth=1,
        topaxiswidth=1,
        bottomaxiswidth=1,
        isleftaxisdisplay=1,
        isrightaxisdisplay=1,
        istopaxisdisplay=1,
        isbottomaxisdisplay=1,
        leftaxisstyle="-",
        rightaxisstyle="-",
        topaxisstyle="-",
        bottomaxisstyle="-",
        leftaxiscolor="black",
        rightaxiscolor="black",
        topaxiscolor="black",
        bottomaxiscolor="black",
        savefilename=None,
        isshowplot=1,
        fontfamily="华文楷体",
        **kwargs):
    """
    这是一个自定义图形细节样式函数的文档字符串。

    参数:
    fig (matplotlib.figure.Figure): 画布对象。
    fig_length (numeric): 图形长度。
    fig_width (numeric): 图形宽度。
    facecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 画布颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    edgecolor: (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 边缘颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    layout (str ; None): 图形在画布上的布局机制{"constrained", "compressed", "tight", None}。
    xlabel (str): X轴标签。
    ylabel (str): Y轴标签。
    title (str): 图形标题。
    xlabelsize (numeric): X轴标签字体大小。
    ylabelsize (numeric): Y轴标签字体大小。
    titlesize (numeric): 图形标题字体大小。
    xlabelcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): X轴标签字体颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    ylabelcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): Y轴标签字体颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    titlecolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 图形标题字体颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    xlabelha (str): X轴标签水平对齐方式{"center", "left", "right"}。
    ylabelha (str): Y轴标签水平对齐方式{"center", "left", "right"}。
    xlabelva (str): X轴标签竖直对齐方式{"bottom", "baseline", "center", "center_baseline", "top"}。
    ylabelva (str): Y轴标签竖直对齐方式{"bottom", "baseline", "center", "center_baseline", "top"}。
    titlelabelha (str): 图形标题水平对齐方式{"center", "left", "right"}。
    titlelabelva (str): 图形标题竖直对齐方式{"bottom", "baseline", "center", "center_baseline", "top"}。
    xlabelpad (numeric): X轴标题距离轴线的距离。
    ylabelpad (numeric): Y轴标题距离轴线的距离。
    titlelabelpad (numeric): 图形标题距离轴线的距离。
    xlabelrotation (numeric): X轴标题旋转角度。
    ylabelrotation (numeric): Y轴标题旋转角度。
    titlelabelrotation (numeric): 图形标题旋转角度。
    isxlabellatex (binary): X轴标题是否使用latex语法{1,0}。
    isylabellatex (binary): Y轴标题是否使用latex语法{1,0}。
    istitlelatex (binary): 图形标题是否使用latex语法{1,0}。
    xtick (list or array-like): X轴刻度位置。
    ytick (list or array-like): Y轴刻度位置。
    xticksize (numeric): X轴刻度长度。
    yticksize (numeric): Y轴刻度长度。
    xtickwidth (numeric): X轴刻度宽度。
    ytickwidth (numeric): Y轴刻度宽度。
    xtickdirection (str): X轴刻度方向{"inout", "in", "out"}。
    ytickdirection (str): Y轴刻度方向{"inout", "in", "out"}。
    xtickcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): X轴刻度颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    ytickcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): Y轴刻度颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    xtickzc (str): X轴刻度主次{"major", "minor"}
    ytickzc (str): Y轴刻度主次{"major", "minor"}
    xticklabel (list or array-like): X轴刻度标签。
    yticklabel (list or array-like): Y轴刻度标签。
    xticklabelsize (numeric): X轴刻度标签字体大小。
    yticklabelsize (numeric): Y轴刻度标签字体大小。
    xticklabelcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): X轴刻度标签颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    yticklabelcolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): Y轴刻度标签颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    xticklabelrotation (numeric): X轴刻度标签旋转角度。
    yticklabelrotation (numeric): Y轴刻度标签旋转角度。
    xlim (list or array-like): X轴范围。
    ylim (list or array-like): Y轴范围。
    leftaxiswidth (numeric): 左轴线宽度。
    rightaxiswidth (numeric): 右轴线宽度。
    topaxiswidth (numeric): 上轴线宽度。
    bottomaxiswidth (numeric): 下轴线宽度。
    isleftaxisdisplay (binary): 左轴线是否显示{1,0}。
    isrightaxisdisplay (binary): 右轴线是否显示{1,0}。
    istopaxisdisplay (binary): 上轴线是否显示{1,0}。
    isbottomaxisdisplay (binary): 下轴线是否显示{1,0}。
    leftaxisstyle (str): 左轴线样式{'-', '--', '-.', ':'}。
    rightaxisstyle (str): 右轴线样式{'-', '--', '-.', ':'}。
    topaxisstyle (str): 上轴线样式{'-', '--', '-.', ':'}。
    bottomaxisstyle (str): 下轴线样式{'-', '--', '-.', ':'}。
    leftaxiscolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 左轴线颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    rightaxiscolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 右轴线颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    topaxiscolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 上轴线颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    bottomaxiscolor (colorname str ; tuple of RGB(A) with value range between 0 and 1 ; hex color str): 下轴线颜色。Matplotlib支持的颜色名称字符串；缩放到01范围内的RGB(A)三元组；十六进制颜色字符串。
    savefilename (str): 保存图形的文件名（带后缀）{"*.png", "*.jpg", "*.pdf"}。
    isshowplot (binary): 是否显示图像{1,0}。
    fontfamily (str): 支持的中英文字体名称{"方正舒体", "方正姚体", "仿宋", "黑体", "华文彩云", "华文仿宋", "华文琥珀", "华文楷体", "华文隶书", "华文宋体", "华文细黑", "华文新魏", "华文行楷", "华文中宋", "楷体", "隶书", "宋体", "微软雅黑", "新宋体", "幼圆", "TimesNewRoman", "Arial"}。

    返回:
    matplotlib.axes.Axes: 图形对象。

    示例:
    ===============================================================================0
    导入模块
    >>> from TidyStats import MatplotlibDiy
    >>> import matplotlib.pyplot as plt
    测试画布参数
    ===============================================================================1
    >>> fig, ax = plt.subplots(figsize=(2, 2))
    >>> ax = MatplotlibDiy(fig, block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================2
    >>> ax = MatplotlibDiy(fig_length=5, fig_width=4, facecolor="pink", edgecolor="green", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================3
    >>> ax = MatplotlibDiy(facecolor=(0.4,0.5,0.6), edgecolor=(0.2,0.4,0.9,0.3), block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================4
    >>> ax = MatplotlibDiy(layout="constrained", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================5
    >>> ax = MatplotlibDiy(layout="compressed", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================6
    >>> ax = MatplotlibDiy(layout="tight", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================7
    测试横轴标签，纵轴标签，标题
    >>> ax = MatplotlibDiy(xlabel="日期", ylabel="人数", title="人数关于日期的图形", xlabelsize=10, ylabelsize=15, titlesize=13, xlabelcolor="purple", ylabelcolor=(0.3, 0.9, 0.4, 0.4), titlecolor=(0,0,0), xlabelha="left", ylabelha="center", xlabelva="top", ylabelva="bottom", titlelabelha="center", titlelabelva="center_baseline", xlabelpad=8, ylabelpad=10, titlelabelpad=10, xlabelrotation=30, ylabelrotation=0, titlelabelrotation=10, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================8
    测试latex语法，不能含有中文
    >>> ax = MatplotlibDiy(xlabel="$x$", ylabel="$y$", title="$y=\\sin(x)$", isxlabellatex=1, isylabellatex=1, istitlelatex=1, block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================9
    测试刻度
    >>> ax = MatplotlibDiy(xtick=[0.3, 0.6, 0.9], ytick=[0.3, 0.6, 0.9], xticksize=2, yticksize=6, xtickwidth=1, ytickwidth=5, xtickdirection="in", ytickdirection="out", xtickcolor="red", ytickcolor="green", xtickzc="major", ytickzc="major", block=False)
    >>> plt.pause(3)
    >>> plt.close()
    ===============================================================================10
    测试刻度标签
    >>> ax = MatplotlibDiy(xtick=[0.3, 0.6, 0.9], ytick=[0.3, 0.6, 0.9], xticklabel=["a", "b", "c"], yticklabel=["A", "B", "C"], xticklabelsize=10, yticklabelsize=16, xticklabelcolor="purple", yticklabelcolor="pink", xticklabelrotation=20, yticklabelrotation=10, block=False)
    >>> plt.pause(3)
    >>> plt.close()
    ===============================================================================11
    测试XY轴范围
    >>> ax = MatplotlibDiy(xlim=[0, 10], ylim=[-10,10], block=False)
    >>> plt.pause(3)
    >>> plt.close()
    ===============================================================================12
    测试显示轴线
    >>> ax = MatplotlibDiy(leftaxiswidth=2, rightaxiswidth=3, topaxiswidth=4, bottomaxiswidth=5, isleftaxisdisplay=1, isrightaxisdisplay=1, istopaxisdisplay=1, isbottomaxisdisplay=1, leftaxisstyle="-", rightaxisstyle="--", topaxisstyle="-.", bottomaxisstyle=":", leftaxiscolor="black", rightaxiscolor="red", topaxiscolor="green", bottomaxiscolor="blue", block=False)
    >>> plt.pause(3)
    >>> plt.close()
    ===============================================================================13
    测试不显示轴线
    >>> ax = MatplotlibDiy(leftaxiswidth=2, bottomaxiswidth=5, isleftaxisdisplay=1, isrightaxisdisplay=0, istopaxisdisplay=0, isbottomaxisdisplay=1, leftaxisstyle="-", bottomaxisstyle=":", leftaxiscolor="black", bottomaxiscolor="blue", block=False)
    >>> plt.pause(3)
    >>> plt.close()
    ===============================================================================14
    测试保存文件
    >>> ax = MatplotlibDiy(savefilename="最后一张.pdf", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    >>> ax = MatplotlibDiy(savefilename="最后一张.png", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    >>> ax = MatplotlibDiy(savefilename="最后一张.jpg", block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================15
    测试不显示图形
    >>> ax = MatplotlibDiy(isshowplot=0, block=False)
    >>> plt.pause(1)
    >>> plt.close()
    ===============================================================================16
    测试字体显示
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="方正舒体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="方正姚体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="仿宋", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="黑体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文彩云", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文仿宋", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文琥珀", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文楷体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文隶书", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文宋体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文细黑", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文新魏", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文行楷", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="华文中宋", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="楷体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="隶书", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="宋体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="微软雅黑", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="新宋体", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="中文字体", ylabel="显示正确", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="幼圆", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="X-axis", ylabel="Y-axis", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="TimesNewRoman", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    >>> ax = MatplotlibDiy(xlabel="X-axis", ylabel="Y-axis", xlabelsize=15, ylabelsize=15, xlabelcolor="pink", ylabelcolor="purple", fontfamily="Arial", block=False)
    >>> plt.pause(2)
    >>> plt.close()
    ===============================================================================17
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
    if fig is not None:
        ax = fig.gca()
    else:
        # 开始绘图，画布参数
        fig, ax = plt.subplots(
            figsize=(
                fig_length, fig_width), layout=layout, facecolor=facecolor, edgecolor=edgecolor)
    # 标题参数
    if xlabel is not None:
        ax.set_xlabel(
            xlabel,
            fontproperties=fontobj,
            fontsize=xlabelsize,
            color=xlabelcolor,
            horizontalalignment=xlabelha,
            verticalalignment=xlabelva,
            labelpad=xlabelpad,
            rotation=xlabelrotation,
            usetex=bool(isxlabellatex))
    if ylabel is not None:
        ax.set_ylabel(
            ylabel,
            fontproperties=fontobj,
            fontsize=ylabelsize,
            color=ylabelcolor,
            horizontalalignment=ylabelha,
            verticalalignment=ylabelva,
            labelpad=ylabelpad,
            rotation=ylabelrotation,
            usetex=bool(isylabellatex))
    if title is not None:
        ax.set_title(
            title,
            fontproperties=fontobj,
            fontsize=titlesize,
            color=titlecolor,
            horizontalalignment=titlelabelha,
            verticalalignment=titlelabelva,
            pad=titlelabelpad,
            rotation=titlelabelrotation,
            usetex=bool(istitlelatex))
    # 刻度参数，刻度标签参数
    ax.tick_params(
        'x',
        labelsize=xticklabelsize,
        labelcolor=xticklabelcolor,
        length=xticksize,
        width=xtickwidth,
        direction=xtickdirection,
        which=xtickzc,
        color=xtickcolor,
        rotation=xticklabelrotation)
    ax.tick_params(
        'y',
        labelsize=yticklabelsize,
        labelcolor=yticklabelcolor,
        length=yticksize,
        width=ytickwidth,
        direction=ytickdirection,
        which=ytickzc,
        color=ytickcolor,
        rotation=yticklabelrotation)
    if xtick is not None:
        ax.set_xticks(xtick)
    if ytick is not None:
        ax.set_yticks(ytick)
    # 刻度标签参数
    if xticklabel is not None:
        ax.set_xticklabels(xticklabel)
    if yticklabel is not None:
        ax.set_yticklabels(yticklabel)
    if xlim is not None:
        ax.set_xlim(xlim)
    if ylim is not None:
        ax.set_ylim(ylim)
    # 默认的刻度标签，设置中文字体
    ax.set_xticks(ax.get_xticks(), ax.get_xticklabels(),
                  fontproperties=fontobj)
    ax.set_yticks(ax.get_yticks(), ax.get_yticklabels(),
                  fontproperties=fontobj)
    # 轴线参数
    ax.spines["left"].set_linewidth(leftaxiswidth)
    ax.spines["right"].set_linewidth(rightaxiswidth)
    ax.spines["top"].set_linewidth(topaxiswidth)
    ax.spines["bottom"].set_linewidth(bottomaxiswidth)
    ax.spines["left"].set_color(leftaxiscolor)
    ax.spines["right"].set_color(rightaxiscolor)
    ax.spines["top"].set_color(topaxiscolor)
    ax.spines["bottom"].set_color(bottomaxiscolor)
    ax.spines["left"].set_visible(bool(isleftaxisdisplay))
    ax.spines["right"].set_visible(bool(isrightaxisdisplay))
    ax.spines["top"].set_visible(bool(istopaxisdisplay))
    ax.spines["bottom"].set_visible(bool(isbottomaxisdisplay))
    ax.spines["left"].set_linestyle(leftaxisstyle)
    ax.spines["right"].set_linestyle(rightaxisstyle)
    ax.spines["top"].set_linestyle(topaxisstyle)
    ax.spines["bottom"].set_linestyle(bottomaxisstyle)
    if savefilename is not None:
        fig.savefig(savefilename)
    else:
        pass
    if bool(isshowplot):
        plt.show(**kwargs)
    else:
        pass
    return ax
