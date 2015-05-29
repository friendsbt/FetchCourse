import os
from utils import clean_course_name

DATAPATH = 'fetched_data/pku'

courses = set()

with open('course/pku_course.txt', 'w', encoding='utf-8') as w:
    for school in os.listdir(DATAPATH):
        with open(os.path.join(DATAPATH, school), 'r', encoding='utf-8') as r:
            for line in r.readlines():
                courses.add(clean_course_name(line))

    w.writelines(courses)