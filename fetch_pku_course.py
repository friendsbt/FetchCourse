# coding: utf-8

from concurrent.futures import ThreadPoolExecutor
from lxml import html
import requests

from pku_school_course import PKUSchoolCourse

START_PAGE = 'http://dean.pku.edu.cn/pkudean/course/kcb.php?ll=1'

r = requests.get(START_PAGE)
r.encoding = 'gb2312'
htmltree = html.fromstring(r.text)
school_urls = [a for a in htmltree.cssselect("table>tr>td>a")]


p = PKUSchoolCourse()
for school_url in school_urls:
    p.fetch_courses(school_url.attrib['href'], school_url.text)
