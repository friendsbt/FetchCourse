import os

DATAPATH = 'fetched_data/pku'

courses = set()

with open('course/pku_course.txt', 'w', encoding='utf-8') as w:
    for school in os.listdir(DATAPATH):
        with open(os.path.join(DATAPATH, school), 'r', encoding='utf-8') as r:
            for line in r.readlines():
                courses.add(line)

    w.writelines(courses)