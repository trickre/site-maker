#python:python3
#coding:utf-8
import markdown
import sys

#>python main.py file.txt
def main():
    print("--- MarkDown Convert to HTML ---")

    args = sys.argv
    file = args[1]

    print("target file is "+file+"\nHTML output\n")

    #get input MD file
    f = open(file,"r",encoding="utf-8")
    text = f.read()
    f.close()

    #markdown to html
    md = markdown.Markdown()
    html = md.convert(text)

    #print(html)

    
    idx = file.rfind("/")+1
    if(idx ==-1):idx = 0
    file_output = file[idx:-3]
    file_output += ".html"
    fw = open(file_output,"w",encoding="utf-8")
    fw.write(html)

    print(file_output)
if (__name__ =="__main__"):
    main()