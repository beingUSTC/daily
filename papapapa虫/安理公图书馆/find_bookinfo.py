from bs4 import BeautifulSoup
import requests
import os


# context = requests.get("http://210.45.147.188:8080/opac/openlink.php?location=ALL&title=java&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=20&showmode=table&orderby=DESC&sort=CATA_DATE&onlylendable=no&count=274&with_ebook=on&page=2")
# soup = BeautifulSoup(context.text,'html.parser')
# s = soup.find_all("td",{"class":"whitetext"})
# print(s)

def main():
    target = "https://www.biqubao.com/book/17570/"
    save_path = 'E:/' \
                ''
    index_path = 'https://www.biqubao.com'
    req = requests.get(url=target)
    req.encoding = 'gbk'
    # gbk是网站编码方式
    soup = BeautifulSoup(req.text,"html.parser")
    list_tag = soup.div(id="list")
    print(type(list_tag))
    #find title
    title = list_tag[0].dl.dt.string
    path = save_path + '/' + title
    if not os.path.exists(path):
        os.path.join(save_path,title)
        os.mkdir(path)
    print(1)

    for tag in list_tag[0].dl.find_all('dd'):
        chapter_name = tag.string
        print(2)
        chapter_url = index_path+tag.a.get("href")
        chapter_req = requests.get(url = chapter_url)
        chapter_req.encoding = "gbk"
        chapter_soup = BeautifulSoup(chapter_req.text,"html.parser")
        text = chapter_soup.div.find(id="content")
        print(type(text))
        content_text = str(text.text.replace('\xa0', '\n'))
        with open(path+'/'+chapter_name+'.txt', 'w') as f:
            f.write('本文网址:'+chapter_url)
            f.write(content_text)
if __name__ == '__main__':
    main()