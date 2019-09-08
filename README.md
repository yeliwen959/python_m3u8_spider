# python_vidio_spider

# url_lists.txt
视频链接的存放文件

# main.py
主运行文件，通过调用get_m3u8_url.py 和download_merge_change.py执行主要步骤

# get_m3u8_url.py
类：Get_m3u8
方法：
parse_url（） 		根据url和头信息拿到html内容

get_findAll_urls（）	正则表达筛选出从html内容中找到m3u8文件链接

run（）				将m3u8链接追加写入到2.txt中

# download_merge_change

需要根据自己电脑自定义文件存放路径
        self.download_path = "E:/FFOutput/"
        self.mp4_path = "E:/FFOutput/mp4/"
        self.wav_path = "E:/FFOutput/wav/"

类：Dmc就是个缩写
遍历2.txt里获取到的m3u8地址做一下循环

方法：
w_m3u8()     		获取m3u8内容，写入m3u8.txt文本中
get_ts_urls() 		过滤一个m3u8.txt文本的有效内容，放在列表里
download() 			下载列表里所有的ts文件到指定的位置
merge_file() 		合成所有ts文件为mp4然后清空ts

change_mp4towav() 	将mp4用ffmpeg转码成wav放置到指定位置

### 下一个版本要改进的地方
1- 写多线程同步处理
2- 添加停止后自动跳过已处理的url，从上一次停止的地方开始
3- 将变量方法写得更加简洁
4- 修改you-get程序应用在获取普通视频上