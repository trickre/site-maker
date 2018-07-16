#coding:utf-8
import sys
"""
Usage   :>python main_module.py [target file] [option...]
Output  :"target file.html"
"""
def main():
    print("--- MarkDown Convert to HTML ---")
    #option flags
    is_verbose = False#Trueの時パース経過を出力する
    #option parse
    file = sys.argv[1]
    if len(sys.argv)>1:
        args = sys.argv[2:]
        for op in args:
            if op == "-verbose" or op == "-v":
                is_verbose = True
    
    print("target file is "+file+"\nHTML output\n")

    #get input MD file
    f = open(file,"r",encoding="utf-8")
    lines = f.readlines()
    f.close()
    lines.append("EOF_EOF")

    kw      = []#keywords
    dt      = []#date
    ds      = []#description
    cat     =   ""#category
    mode_MDparse = 0    #0:MD->HTML rewrite, 1:get META info
    html_article    =[] #本文部分

    state = ""
    for cnt in range(len(lines)):
        if cnt == 0:
            if not (lines[cnt][0] =='#'):
                print("! this is not mark down format.First Line Must be #Title1.")
                print("file processing is canceled.")
                print(lines[cnt])
                exit()
        if not(lines[cnt][0:4]=="<!--"):#comment out
            if not (state =="META"):
                #MD->HTML　書き換え
                html,state = md2html(lines[cnt],state)
                html_article.append(html)
        if(state == "META"):
            #メタ情報取得
            if (lines[cnt][0:5]=="# key"):
                mode_MDparse =1
                while(not(lines[cnt+1][0:2]=="EOF_EOF") and lines[cnt+1][0:2]=="- "):
                    cnt += 1
                    kw.append(lines[cnt][2:])
            if (lines[cnt][0:5]=="# dat"):
                mode_MDparse =1
                while(not(lines[cnt+1][0:2]=="EOF_EOF") and lines[cnt+1][0:2]=="- "):
                    cnt += 1
                    dt.append(lines[cnt][2:])
            if (lines[cnt][0:5]=="# des"):
                mode_MDparse =1
                while(not(lines[cnt+1][0:2]=="EOF_EOF") and lines[cnt+1][0:2]=="- "):
                    cnt += 1
                    ds.append(lines[cnt][2:])
            if (lines[cnt][0:5]=="# cat"):
                mode_MDparse =1
                while(not(lines[cnt+1][0:2]=="EOF_EOF") and lines[cnt+1][0:2]=="- "):
                    cnt += 1
                    cat = lines[cnt][2:]
    if is_verbose:
        print(kw)
        print(dt)
        print(ds)
        print(cat)
    """
    #HTMLのコンソールへの出力
    for l in html_article:
        print(l.encode("utf-8").decode())
    """

    #html前半
    html_header ="\
<!DOCTYPE html>\n\
<html lang=\"ja\">\
<head>\n\
<meta charset=\"utf-8\"/>\n\
<link rel=\"stylesheet\" href=\"style.css\">"
    #-----ここに<head>の中身をを挿入する-----
    html_header2 = "\
</head>\n\
<body>\n\
<h1>タイトル</h1>\n\
<div id = \"content_l0\">\n\
"

    #html後半
    html_footer="\n\
</div>\n\
<footer>\
</footer>\n\
</body>\n\
</html>\
"

    print(html_article[len(html_article)-2])
    with open("output.html",mode="w") as f:
        f.write(html_header)
        for l in html_article:
            f.write(l)
        f.write(html_footer)

"""
md_line :mdファイルの1行を入力
state   :htmlの処理の状態
    normal  :初期状態,見出しor文頭を検索している状態
    _p      :<p>タグを出力し終え、</p>タグの挿入個所を探している状態
    META    :本文が終わりMETA情報を探している状態へ移行 returnのみ。
return  :
    html    :書き換えられたhtml
    n_state :次の状態
"""
def md2html(md_line,state="normal"):
    html =""
    #MDが見出し行の場合
    if md_line[0] == "#":
        if state == "_p":
            html = "</p>\n"
            state = "normal"

        if (md_line[0:5]=="# key" or md_line[0:5]=="# dat" or md_line[0:5]=="# des"):
            state ="META"
        elif md_line[0:2] =="# ":#title0
            html += md_line.replace("# ","<h2>",1)
            html = html.replace("\n","")+"</h2>\n"
        elif md_line[0:3] =="## ":#title1
            html += md_line.replace("## ","<h3>",1)
            html =html.replace("\n","")+"</h3>\n"
        elif md_line[0:4] =="### ":#title2
            html += md_line.replace("### ","<h4>",1)
            html =html.replace("\n","")+"</h4>\n"
        elif md_line[0:5] =="#### ":#title3
            html += md_line.replace("#### ","<h5>",1)
            html =html.replace("\n","")+"</h5>\n"
        elif md_line[0:6] =="##### ":#title4
            html += md_line.replace("##### ","<h6>",1)
            html =html.replace("\n","")+"</h6>\n"
        elif md_line[0:7] =="###### ":#title5
            html += md_line.replace("###### ","<h7>",1)
            html =html.replace("\n","")+"</h7>\n"
        elif md_line[0:8] =="####### ":#title6
            html += md_line.replace("####### ","<h8>",1)
            html =html.replace("\n","")+"</h8>\n"
        
    elif md_line == "\n":#スペースだけの場合
        if state == "_p":
            html = "</p>\n"
            state = "normal"

    elif not (state == "_p"):
        html = "<p>" + md_line.replace("\n","<br />\n")
        state ="_p"
    else:
        html = md_line.replace("\n","<br />\n")

    return html,state

if (__name__ =="__main__"):
    main()

#defines
cat={\
    "dialy"     :"徒然",\
    "tech"      :"技術",\
    "child"     :"こども",\
    "work"      :"仕事",\
    }
"""
return :"カテゴリ名"
return False    :カテゴリ名が不正な場合
"""
def get_category(cat_symbol):
    global cat
    try:
        cat_name = cat[cat_symbol]
    except KeyError:
        print("Category name Error.Please check category symbol name.")
        return False
    return cat_name

"""
指定ディレクトリ内にあるhtmlファイルからカテゴリを読み取ってカテゴリ別のリンクリストを返す
input   dir:ディレクトリ
output  :
            cat1                cat2    ...
    list[   [[link_info],...],  [[]],   ...]

[link_info] = ["リンク先の見出し","html file name"]
"""
def make_index(dir):
    global cat
    cat_symbol = cat.keys()

    #linkすべき一覧を取得
    link_list = []
    for f in files:
        link = f
        cat = get_cat_from_html(f)
        date = get_data_from_html(f)
        link_list.append([link,cat,date])
    
    #link_listを並べ替え

    for c in cat_symbol:
        for l in linklist:
            if l[1]==c:
                pass
    
