"""
这个文件是记录该程序学习过程中所遇到的问题以及解决方法

1.Python的虚拟环境(venv)它是一个虚拟出来的环境。通俗的来讲，这个虚拟的环境可以理解为一个“容器”，在这个容器中，
我们可以只安装我们需要的依赖包，而且各个容器之间互相隔离，互不影响。
Virtualenv是一个非常好的virtual python environment builder，他最大的好处是，可以让每一个python项目单独使用
一个环境，而不会影响python系统环境，也不会影响其他项目的环境。
比如在本地同时在不同项目中开发django1.3与django1.8，或者python2/3；

2.&#x5b59;&#x536b;&#x7434;&#x7f16;&#x8457;
常在一些网站源码中看到&#x开头的内容，这是转化成unicode编码后的汉字
形如——
&name;
&#dddd;
&#xhhhh;
——的一串字符是 HTML、XML 等 SGML 类语言的转义序列（escape sequence）。它们不是「编码」。

3.list_tag = soup.div(id="list")  <class 'bs4.element.ResultSet'>  text = chapter_soup.div.find(id="content")  <class 'bs4.element.Tag'>
有无find是不同的
"""