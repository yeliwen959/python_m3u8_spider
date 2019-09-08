#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-07 15:57:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import requests
import re

class Get_m3u8:
	def __init__(self):
		#默认伪装请求头部信息如下
		self.headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}

	def main(self, urls_list_file):
		get_m3u8 = Get_m3u8()
		file = open(urls_list_file)
		for line in file:
			#去除换行符
			line = line.strip('\n')
			get_m3u8.run(line)
		file.close()

        #正则表达式找到m3u8链接
	def get_findAll_urls(self, text):
		urls = re.findall(
        r"(^http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)|([a-zA-Z]+.\w+\.+[a-zA-Z0-9\/_]+)"+'.m3u8', text)
		urls = list(sum(urls, ()))
		urls = [x for x in urls if x != '']
		return urls

		#requests.get()获取html内容
	def parse_url(self, url):
		r = requests.get(url, headers=self.headers)
		return r.content.decode()


	def run(self, line):
		#拿到url地址
		url = line
        #根据url和头信息拿到html内容
		html_str = self.parse_url(url)
        #根据html内容获取m3u8地址，如果没有获取就跳过
		m3u8_url = self.get_findAll_urls(str(html_str))
		if m3u8_url:
			m3u8_url = "http://"+m3u8_url[0]+".m3u8?"+"\n"
			with open("2.txt", "a+", encoding="utf-8") as f:
				f.write(m3u8_url)