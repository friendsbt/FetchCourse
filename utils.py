import re


def clean_course_name(name):
    """
    去除课程名中的多余部分，abc（def）gh1-> abcgh
    """
    name = re.sub(r'[〔（\(\[].*$', '', name)
    return re.sub(r'(?<=[\u4e00-\u9fff])(Ⅰ|Ⅱ|Ⅲ|Ⅳ|Ⅴ|I|II|III|IV|V|[a-zA-Z]|[0-9\/\-]*)$', r'', name)


if __name__ == '__main__':
    print(clean_course_name("毕业论文（二〕"))
    print(clean_course_name("毕业论文（资产定价）2"))
    print(clean_course_name("Matlab在信号与系统课程中的应用3-"))
    print(clean_course_name("工程CAD"))
    print(clean_course_name("大学英语3-"))
