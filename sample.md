# [H2]SiteMaker
SiteMakerをつくろう思います。

## コンセプト
- 自前の技術サイトを安くホスティングしたい

### MarkDownで記事を書きたい・保管したい
- DBを扱うとなると手軽にバックアップできない、テキストの安心感が欲しい
- 普段記事をMDで書きたい

### 静的HTMLを生成する
- 各記事からHTMLのサイトを構築する

### 静的HTMLだけどコメントなどのインタフェースはある
- Lambdaなどを使用してS3でのホスティングながらコメント・カウンタ備える



<!-- コメントをMDには入れれるが、HTMLには書き込まれない -->

<!-- HTML>HEAD>keyword -->
<!-- 同時に「タグ」にもなり、ユーザーに見える -->
# key
- keyword1
- keyword2

<!-- フォーマットは "yyyy-mm-dd" -->
# date
- [first date]
[- up date1]
[- up date2]

# desc
- 説明文

<!-- カテゴリ -->
# cat
- category