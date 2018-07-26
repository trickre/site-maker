#coding:utf-8
import sys
"""
Usage   :>python main_module.py [target file] [option...]
Output  :"target file.html"
"""
class HTML_Object(object):
    def __init__(self):
        self.content = []
        self.tag_start  = ""
        self.tag_end    = ""
    def print_tag_start(self):
        print (self.tag_start)
    def print_tag_end(self):
        print (self.tag_end)
    def print_content(self):
        self.print_tag_start()
        for c in self.content:
            if issubclass(type(c),HTML_Object):
                print("print innner")
                c.print_content()
            else:
                print(c)
        self.print_tag_end()
    
    def add_content(self,c):
        self.content.append(c)
class p(HTML_Object):
    def __init__(self):
        super().__init__()
        self.tag_start = "<p>"
        self.tag_end = "</p>"

class Html(HTML_Object):
    def __init__(self):
        super().__init__()
        self.tag_start = "<html>"
        self.tag_end = "</html>"


class Article():
    title = ""
    def __init__(self,title_txt):
        title = title_txt

if __name__ =="__main__":
    print("TEST html classes")
    tp = p()
    html = Html()
    tp.add_content("this is p content")
    html.add_content(tp)
    html.print_content()    