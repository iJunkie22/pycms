import re
import xml.etree.ElementTree as ET

__author__ = 'Ethan Randall'


class MDLine(object):
    h_pat = re.compile('^(?P<before>\s*)(?P<hcount>#{1,6})\s(?P<after>.*)$')
    im_pat = re.compile('')

    @classmethod
    def parse_headers(cls, line_str):
        m = cls.h_pat.match(line_str, re.MULTILINE)

        if not m:
            return '', line_str, ''

        b, hc, a = m.groups()
        h_el = 'h' + str(len(hc))
        return b + '<' + h_el + '>', a, '</' + h_el + '>'

    @classmethod
    def parse_images(cls, line_str):
        pass


