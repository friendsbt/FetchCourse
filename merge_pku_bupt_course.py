import json


json_data = {
    "meta": {
        "max": 0
    },
    "course": {

    }
}

school_course_file = [
    'course/pku_course.txt',
    'course/bupt_course.txt'
]

courses = set()

for file in school_course_file:
    with open(file, encoding='utf-8') as f:
        for line in f:
            courses.add(line.strip())

index = 0
for course in sorted(courses):
    index += 1
    json_data["course"][index] = course

json_data["meta"]["max"] = index

with open('course/course.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent='\t', ensure_ascii=False)