import pandas as pd
import re


def findSchool(str):
    s = re.match('(.*?)大学', str)
    if s:
        return 1
    else:
        return 0


df = pd.read_excel('1.xlsx')
school = []
for i in df.就业单位:#df.就业单位这样的一列是str类型
    if findSchool(i):
        school.append(i)
print(school)
print(len(school))
count = {}
for data in school:
    if data not in count.keys():#查找值是否在字典键值中
        count[data] = school.count(data)#字典增加值

print(count)



