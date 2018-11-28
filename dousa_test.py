#encoding:utf8
import parser_md #be tested class
def main():
    psr = parser_md.MDParser()
    #TEST1  :h2 test
    input1 ="# This is H2 class" 
    get1 = psr.parse_line(input1)
    ans1 ="<h2>This is H2 class</h2>"
    if(get1==ans1):
        print("OK 1")
        print("input",end="  :");print(input1)
        print("output",end=" :");print(ans1)
    else:
        print("NG 1")
        print("input",end=" :");print(input1)
        print("output",end=":");print(ans1)

def parse_sample_file():
    print("parse file test")
    html = "test"
    psr = parser_md.MDParser()
    html = psr.parse_file("sample.md")
    print(html)
    with open("sample.html",mode="w",encoding="utf-8") as f:
       f.write(html)
    
if __name__ =="__main__":
    main()
    parse_sample_file()