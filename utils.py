import re


def clean_course_name(name):
    """
    去除课程名中的多余部分，abc（def）gh1-> abcgh
    """
    name = re.sub(r'\（.*\）|\(.*\)', '', name)
    return re.sub(r'(Ⅰ|Ⅱ|Ⅲ|Ⅳ|Ⅴ|I|II|III|IV|V|[0-9])$', r'', name)
