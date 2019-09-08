#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-08 02:41:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import datetime,requests,os,sys,re
from get_m3u8_url import Get_m3u8
from download_merge_change import Dmc

get_m3u8 = Get_m3u8()
get_m3u8.main("url_lists.txt")
dmc = Dmc()
dmc.main()
