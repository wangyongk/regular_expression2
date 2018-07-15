import urllib.request
import re


pat = '<div class="name">(.*?)</div>'
data = urllib.request.urlopen("https://read.douban.com/provider/all").read().decode("utf-8")
str1 = re.compile(pat).findall(str(data))
'''
r是保持字符串原始值的意思，就是说不对其中的符号进行转义
。因为windows下的目录字符串中通常有斜杠"\"，
而斜杠在Python的字符串中有转义的作用。
例如：\n表示换行如果路径中有\new就会被转义。加上r就是为了避免这种情况。
'''
file = open(r"D:\Python\hoilday_codes\1.txt", "w", encoding="utf-8")
for i in str1:
    file.write(i)
    file.write("\n")
