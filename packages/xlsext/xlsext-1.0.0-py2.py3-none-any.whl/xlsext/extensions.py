# -*- coding:utf-8 -*-

import xlwt


class XlsExtTools(object):
    def hyperlink(self, link_location: str, friendly_name: str = None) -> str:
        return xlwt.Formula('HYPERLINK("{0}", "{1}")'.format(link_location, friendly_name))


xlsext = XlsExtTools()
