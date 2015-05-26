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
    def fetch_courses(cls, school_url):
        form_data = cls.form_data.copy()
        print(up.urlparse(school_url).query)
        form_data['xs'] = up.parse_qs(up.urlparse(school_url).query)['xs']
        form_data['xq'] = '1'
        r1 = requests.post(cls.url, data=form_data)
        form_data['xq'] = '2'
        r2 = requests.post(cls.url, data=form_data)
        r1.encoding = r2.encoding = cls.PAGE_ENCODING

        courses = html.fromstring(r1.text).cssselect("table tr td:nth-child(2) a")
        print([c.text for c in courses])
        courses = html.fromstring(r2.text).cssselect("table tr td:nth-child(2) a")
        print([c.text for c in courses])
        """
        with open('1.html', 'w', encoding=cls.FILE_ENCODING) as f1, \
             open('2.html', 'w', encoding=cls.FILE_ENCODING) as f2:
            f1.write(r1.text)
            f2.write(r2.text)
        """
