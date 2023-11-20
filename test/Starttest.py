import sys
import os
# 删除临时文件
if os.path.exists("temptestscript.py"):
    os.remove("temptestscript.py")
try:
    filename = sys.argv[1]
except BaseException:
    filename = None
try:
    runfirst = int(sys.argv[2])
except BaseException:
    runfirst = 0
try:
    runend = int(sys.argv[3])
except BaseException:
    runend = 1
if filename is not None:
    # 读取测试文件
    with open(filename, "rt", encoding="UTF-8") as fp:
        res = fp.readlines()
# 将测试代码提取到列表中
commands_lst = []
zerocommand = "=" * 79 + "{}\n".format(0)
onecommand = "=" * 79 + "{}\n".format(1)
zero_index = res.index(zerocommand)
one_index = res.index(onecommand)
zeroone_res = res[zero_index:one_index]
startcommand = "=" * 79 + "{}\n".format(runfirst)
endcommand = "=" * 79 + "{}\n".format(runend)
start_index = res.index(startcommand)
end_index = res.index(endcommand)
startend_res = res[start_index:end_index]
for command in zeroone_res + startend_res:
    if command.__contains__(">>>"):
        commands_lst.append(command.strip(">>> "))
# 将测试代码字符串列表保存到临时文件中
with open("temptestscript.py", "a+", encoding="UTF-8") as fp:
    fp.writelines(commands_lst)

os.system("python temptestscript.py")
