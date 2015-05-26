# coding: utf-8

from concurrent.futures import ThreadPoolExecutor
from lxml import html
import requests

from pku_school_course import PKUSchoolCourse

START_PAGE = 'http://dean.pku.edu.cn/pkudean/course/kcb.php?ll=1'

htmltree = html.fromstring(requests.get(START_PAGE).text)
school_urls = [a.attrib['href'] for a in htmltree.cssselect("table>tr>td>a")]

PKUSchoolCourse().fetch_courses(school_urls[0])

"""
for school_url in school_urls:
    p = PKUSchoolCourse()
"""