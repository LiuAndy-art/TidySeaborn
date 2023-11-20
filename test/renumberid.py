import sys

try:
    filename = sys.argv[1]
except BaseException:
    filename = "testMatplotlibDiy.txt"
with open(filename, "rt", encoding="utf-8") as fp:
    res = fp.readlines()
count = 0
for line in res:
    if line.__contains__("=" * 79):
        # 先添加换行符
        res.insert(res.index(line) + 1, "\n")
        # 再将上一个元素替换
        res[res.index(line)] = "=" * 79 + "{}".format(count)
        count += 1
with open(filename, "wt", encoding="utf-8") as fp:
    fp.writelines(res)
