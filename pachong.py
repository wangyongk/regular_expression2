import re
pat = "bai"
string = "https://www.baidu.com/"
str1 = re.search(pat, string)
print(str1)

pat2 = "\n"
string2 = '''adfghh
qrfrrty'''
str2 = re.search(pat2, string2)
print(str2)

pat3 = "\w\dpython\w"
string3 = "asdfg7python3"
str3 = re.search(pat3, string3)
print(str3)

pat4 = ".python..."
string4 = "asdfg7python389"
str4 = re.search(pat4, string4)
print(str4)

pat4 = "python|Php"
string4 = "aphpwerthpythonview"
str4 = re.search(pat4, string4, re.I) # 模式修正符I
print(str4)




