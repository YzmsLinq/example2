# example2
# webrobot
一、启动服务器前准备<br>
　１、导入库。本程序应用到的Python导入库有：<br>
　　　　flask<br>
　　　　flask_script<br>
　　　　flask_bootstrap<br>
　　　　flask_moment<br>
　　　　flask_wtf<br>
　　　　aiml<br>
　　I、其中库：flaskflask、flask_script、flask_bootstrap、flask_moment及flask_wtf可以使用如下命令安装：<br>
  　　　pip install <库名>　（如：pip install flask）<br>
　　　如安装过程中出现下载错误可以进入packages目录，实施本地安装。<br>
　　II、安装AIML库。只要将aiml文件夹复制(或移动)至python的安装目录的Lib\site-packages路径中即可（如：D:\python\Lib\site-packages）。如原来已安装了AIML库请覆盖。<br>
　２、数据库准备。本程序的数据库为程序目录下的db\tlkDB.db，可以直接使用。如需新建请先删除tlkDB.db，然后运行命令：<br>
　　　　python createdb.py runserver <br> 
二、启动服务器。请输入以下命令：<br>
　python webrobot.py runserver <br>
三、启动对话。请在浏览器中输入http://127.0.0.1<br>
四、关于目录结构说明：<br>
　　\webrobot<br>
  　　｜\aiml　　AIML库目录<br>
  　　｜\chinese　　中文语料库目录<br>
  　　｜\english　　英文语料库目录<br>
  　　｜\packages　　所需库目录<br>
  　　｜\static　　静态图标目录<br>
  　　｜\templates　　网页模板文件目录<br>
