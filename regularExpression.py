# _*_ coding:utf-8 _*_
fh = open(r"D:\Python\hoilday_codes\fradulent_emails.txt", "r", encoding='UTF-8').read()
"""
gbk' codec can't decode byte 0x80 in position 118396: illegal multibyte sequence
txt文件编码方式改成uft-8则不会出现此类问题

"""
'''
fh = open(r"D:\Python\hoilday_codes\fradulent_emails.txt", "r", encoding='UTF-8').read()

for line in fh.split("\n"):
    if "From:" in line:
        print(line)
    '''
"""
'.'匹配除了换行符以外的任何字符。如果设置re.DOTALL,它将匹配包括换行在内的任何字符。
'*' : 指定前一个字符匹配零次或者多次。

例如:ca*t将匹配 ct(0 个 a)，cat（1 个字符 a），caaat（3 个字符 a）.....

另一个实现重复的元字符是 +，用于指定前一个字符匹配一次或者多次。

要特别注意 * 和 + 的区别：
* 匹配的是零次或者多次，所以被重复的内容可能压根儿不会出现；

+ 至少需要出现一次。例如 ca+t 会匹配 cat 和 caaat，但不会匹配 ct 

另一个实现重复的元字符是 +，用于指定前一个字符匹配一次或者多次。
? 问号: 字符匹配零次或者一次。

\w 匹配字母数字字符，即 a-z、A-Z 和 0-9，也会匹配下划线 _ 和连接号 –
\d 匹配数字，即 0-9
\s 匹配空白字符，包括制表符、换行符、回车符和空格符
\S 匹配非空白字符
re.search()
re.split()
re.sub()
因为 re.search() 返回的是一个 re 匹配对象，
所以我们不能直接通过 print 展示其中的名称和电子邮箱地址。
我们必须首先为其应用 group() 函数。
我们已经在上面的代码中将它们输出显示了出来。
如我们所见，group() 函数的作用是将匹配对象转换成字符串。
而 print(match.group()) 只会显示字符串。

"""
import re
match = re.findall("From:.*", fh)
for line in match:
    print(re.findall("\w\S*@.*\w", line))