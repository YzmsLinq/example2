# example2
webrobot

一、启动服务器前准备
　１、导入库。本程序应用到的Python导入库有：
　　　　flask
　　　　flask_script
　　　　flask_bootstrap
　　　　flask_moment
　　　　flask_wtf
　　　　flask_sqlalchemy
　　　　aiml
　　I、其中库：flaskflask、flask_script、flask_bootstrap、flask_moment、flask_wtf及flask_sqlalchemy可以使用如下命令安装：
 　　　pip install <库名>　（如：pip install flask）
　　　如安装过程中出现下载错误可以进入packages目录，实施本地安装。
　　II、安装AIML库。只要将aiml文件夹复制(或移动)至python的安装目录的Lib\site-packages路径中即可（如：D:\python\Lib\site-packages）。如原来已安装了AIML库请覆盖。
　２、数据库准备。本程序的数据库为程序目录下的db\tlkDB.db，可以直接使用。如需新建请先删除tlkDB.db，然后运行命令：
　　　　python createdb.py runserver 
二、启动服务器。请输入以下命令：
　python webrobot.py runserver 
三、启动对话。请在浏览器中输入http://127.0.0.1
四、关于目录结构说明：
　　\webrobot
 　　｜\aiml　　AIML库目录
 　　｜\another　　其它各类程序目录
 　　｜\chinese　　中文语料库目录
 　　｜\db　　数据库目录
 　　｜\english　　英文语料库目录
 　　｜\packages　　所需库目录
 　　｜\standard　　标准语料库目录
 　　｜\static　　静态图标目录
 　　｜\templates　　网页模板文件目录
