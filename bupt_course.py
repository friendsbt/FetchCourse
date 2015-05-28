# coding: utf-8

import xlrd
import xlwt
from utils import *

bupt_xls = xlrd.open_workbook('北邮课表.xls')
courses = set()
sheet = bupt_xls.sheets()[0]

for row in range(1, sheet.nrows):
    courses.add(clean_course_name(sheet.cell(row, 4).value.strip()))

courses.remove('')

with open('course/bupt_course.txt', 'w', encoding='utf-8') as w:
    for course in courses:
        w.write(course + '\n')