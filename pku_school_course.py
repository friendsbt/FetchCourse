# coding: utf-8

from pprint import pprint as print
import urllib.parse as up
from lxml import html
import requests


class PKUSchoolCourse:
    """
    fetch courses of each school
    """
    form_data = {
        'zy': '%',
        'xn': '14-15',
        'xq': ['1', '2'],
        'xs': None,
        'nj': '%',
        'B1': '%CC%E1%BD%BB%28Submit%29'  # don't know what this is
    }
    url = 'http://dean.pku.edu.cn/pkudean/course/kcbxs.php'
    PAGE_ENCODING = 'gb2312'
    FILE_ENCODING = 'utf-8'

    @classmethod
    def fetch_courses(cls, school_url, school_name):
        form_data = cls.form_data.copy()
        print(up.urlparse(school_url).query)
        form_data['xs'] = up.parse_qs(up.urlparse(school_url).query)['xs']
        form_data['xq'] = '1'
        r1 = requests.post(cls.url, data=form_data)
        form_data['xq'] = '2'
        r2 = requests.post(cls.url, data=form_data)
        r1.encoding = r2.encoding = cls.PAGE_ENCODING

        courses = html.fromstring(r1.text)\
            .cssselect("table tr td:nth-child(2) a")
        courses += html.fromstring(r2.text)\
            .cssselect("table tr td:nth-child(2) a")

        # remove dups
        courses = set([c.text.split()[0] for c in courses])

        # write to file
        with open('fetched_data/pku/' + school_name, 'w',
                  encoding=cls.FILE_ENCODING) as f:
            for c in courses:
                f.writelines(c + '\n')

