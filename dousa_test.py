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
        

if __name__ =="__main__":
    main()