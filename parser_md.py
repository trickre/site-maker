#coding:utf-8
import sys
import class_html as chtml
"""
Usage   :>python main_module.py [target file] [option...]
Output  :"target file.html"
"""
class MDParser(object):
    def __init__(self):
        pass
    def parse_file(self,file_name):
        pass
    def parse_line(self,line):
        if(line[:2]=="# "):#H2
            html = chtml.h(2)
            html.add_content(line[2:])
            return(html.print_html())
    