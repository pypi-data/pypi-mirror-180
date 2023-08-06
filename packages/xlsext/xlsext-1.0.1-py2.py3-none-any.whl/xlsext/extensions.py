# -*- coding:utf-8 -*-

import xlwt


class XlsExtTools(object):
    def hyperlink(self, link_location: str, friendly_name: str = None) -> str:
        if not friendly_name:
            return xlwt.Formula('HYPERLINK("{0}"\r)'.format(link_location))
        return xlwt.Formula('HYPERLINK("{0}", "{1}"\r)'.format(link_location, friendly_name))


xlsext = XlsExtTools()
