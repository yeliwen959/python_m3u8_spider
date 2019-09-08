#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-08 00:45:43
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import datetime
import requests
import os
import sys
import shutil


class Dmc():

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
        #下载，mp4、wav文件存放路径
        self.download_path = "E:/FFOutput/"
        self.mp4_path = "E:/FFOutput/mp4/"
        self.wav_path = "E:/FFOutput/wav/"


    def main(self):
        #文件按顺序命名
        n = 1
        file = open("2.txt")
        #主循环
        for line in file:
            
            #去除换行符
            line = line.strip('\n')
            self.w_m3u8(line)
            urls = self.get_ts_urls("m3u8.txt")
            self.download(urls,self.download_path)
            self.merge_file(str(n), self.download_path, self.mp4_path)
            self.change_mp4towav(str(n),self.mp4_path,self.wav_path)
            n += 1
        file.close()
        # 
        # print(str(res))

    # 获取m3u8内容，写入文本中
    def w_m3u8(self,m3u8_url):
        res = requests.get(m3u8_url, headers=self.headers)
        res = res.content.decode()
        with open("m3u8.txt", "w", encoding="utf-8") as f:
            f.write(str(res))


    # 过滤一个m3u8文本的有效内容，返回列表
    def get_ts_urls(self,m3u8_path):

        urls = []

        with open(m3u8_path, "r") as file:

            lines = file.readlines()

            for line in lines:

                if line[0] == "h":
                    urls.append(line.strip("\n"))

        return urls

    # 根据列表里的有效URL下载ts文件至下载目录
    def download(self,ts_urls, download_path):
    
        for i in range(len(ts_urls)):
    
            ts_url = ts_urls[i]
    
            file_name = ts_url.split("/")[-1]
    
            print("开始下载 %s" % file_name)
    
            start = datetime.datetime.now().replace(microsecond=0)
    
            try:
    
                response = requests.get(ts_url, stream=True, verify=False)
    
            except Exception as e:
    
                print("异常请求：%s" % e.args)
    
                return
    
            ts_path = download_path+"/{0}.ts".format(i)
    
            with open(ts_path, "wb+") as file:
    
                for chunk in response.iter_content(chunk_size=1024):
    
                    if chunk:
    
                           file.write(chunk)

            end = datetime.datetime.now().replace(microsecond=0)

            print("耗时：%s" % (end-start))

    # 合成文件夹里所有的ts文件并转成mp4格式再移动到目标文件夹
    def merge_file(self, file_name, ts_path, mp4_path):
        mp4_file_name = file_name
        os.chdir(ts_path)
        cmd = "copy /b * " + mp4_file_name+".tmp"
        os.system(cmd)
        os.system('del /Q *.ts')
        os.rename(mp4_file_name+".tmp", mp4_file_name+".mp4")
        shutil.move(mp4_file_name+".mp4", mp4_path)
        os.system('del /Q *.tmp')
        os.system('del /Q *.mp4')

    # 将mp4文件用ffmpeg转码成16K wav音频文件至目标文件夹
    def change_mp4towav(self,file_name,mp4_path,wav_path):
        wav_file_name = file_name + ".wav"
        mp4_file_name = file_name + ".mp4"
        os.chdir(mp4_path)
        cmd = "ffmpeg -i "+ mp4_file_name + " -f wav -ar 16000 " + wav_file_name
        os.system(cmd)
        shutil.move(wav_file_name, wav_path)

