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
    #input  :MDfile
    #output :HTMLfile
    def parse_file(self,file_name):
        html = chtml.Html()
        with open(file_name,mode= "r",encoding="utf-8") as f:
            lines = f.readlines()
            for l in lines:
                parsed = self.parse_line(l)
                html.add_content(parsed)
        return(html.print_html())

    #input  :line of MDfile
    #output :tag and content of HTML
    def parse_line(self,line,prev_line=None):
        #[TODO] 複数行にまたがるp要素　複数行にまたがる可能性があるのはpだけか？
        #html = chtml.p()
        if(prev_line!=None): #prev_lineがある場合は複数行にまたがる要素の可能性があるのでそれらを確認
            pass

        if(line[:2]=="# "):#H2
            html = chtml.h(2)
            html.add_content(line[2:])
            return(html.print_html())
        elif(line[:3]=="## "):#H3
            html = chtml.h(3)
            html.add_content(line[3:])
            return(html.print_html())
        elif(line[:4]=="### "):#H3
            html = chtml.h(4)
            html.add_content(line[4:])
            return(html.print_html())
        elif(line[:2]=="- "):
            html = chtml.li()
            html.add_content(line[2:])
            return(html.print_html())
        elif(line[:2]=="<!"):
            return("")
            pass #because comment out
        else: #maybe p object
            html = chtml.p()
            html.add_content(line)
            return(html.print_html())