#-*- encoding:'utf-8' -*-

from bs4 import BeautifulSoup
import requests

def file_process(soup,page):
   blog = open('./Snow_Star_blog'+page+'.html','w',encoding='utf-8')
   blog.write("<!DOCTYPE HTML>\n<html>\n<head>\n<link rel=\'stylesheet' href=\'snowstar.css\' type=\'text/css\'>\n</head>\n<body>\n<input type=\"text\" id=\"search_text\">\n<input  name=Search type=\"submit\" Value=\"Search\"  id=\"search\" >\n")
   blog.write(repr(soup.find_all('article')))
   if page=='1':
      blog.write('<span aria-current=\"page\" class=\"page-numbers current\">1</span>\n<a class=\"page-numbers\" href=\"./Snow_Star_blog2.html\">2</a>\n<a class=\"next page-numbers\" href=\"./Snow_Star_blog2.html\">下一页 →</a>')
   if page=='2':
      blog.write('<a class=\"page-numbers\" href=\"./Snow_Star_blog1.html\">1</a>\n<span aria-current=\"page\" class=\"page-numbers current\">2</span>\n<a class=\"next page-numbers\" href=\"./Snow_Star_blog1.html\">上一页 →</a>')
   blog.write("</body>\n</html>")

def page_crawer(name_url,page_number):
   headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36;'}
   res = requests.get(name_url,headers=headers).content
   soup = BeautifulSoup(res,'lxml',from_encoding='utf-8')
   file_process(soup,page_number)

def thecrawer():
   page_crawer('https://snowstar.org/','1')
   page_crawer('https://snowstar.org/page/2/','2')

thecrawer()