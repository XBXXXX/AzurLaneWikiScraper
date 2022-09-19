# -*- coding: utf-8 -*-
import requests
import re
import csv
import os
from urllib import parse

# 获取图片名保存在csv中
def get_picture_links(source_code, re_source, re_, data_path=''):
        # re_current = re.compile(r'<div class="center"><div class="floatnone"><a href=".*?" class="image"><img alt="(?P<name>.*?)" src="(?P<link>)" decoding="async" width="2560" height="1440" data-file-width="(?P<width>.*?)" data-file-height="(?P<height>.*?)" /></a></div></div>')
        iter = re_source.finditer(source_code)
        with open(data_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'width', 'height'])
            writer.writeheader()
            for match in iter:
                writer.writerow(dict(zip(['name', 'width', 'height'], match.group('name','width','height'))))
        f.close()

# 从链接获取源代码
def get_source_code_from_link(url, headers={}):
        rsp = requests.get(url, headers=headers)
        source_code = rsp.text
        rsp.close()
        return source_code

# 从链接保存图片
def save_picture_from_link(download_link, save_path):
        with open(save_path,'wb')as img:
            pic_bytes = requests.get(download_link).content
            img.write(pic_bytes)
   
# 获取下载链接      
def get_download_link(pic_name, re_):
    url = 'https://wiki.biligame.com/blhx/%E6%96%87%E4%BB%B6:' + pic_name
    rsp = requests.get(url)
    link = re_.findall(rsp.text)
    rsp.close()
    return link
    
    
###################################################################################################################
class Scraper():
    # 用于匹配源代码中图片地址的re
    re_source = re.compile(r'<li class="gallerybox" style="width: .*?"><div style="width: .*?">.*?<div class="thumb" style="width: .*?;"><div style="margin:.*? auto;"><a href="/blhx/%E6%96%87%E4%BB%B6:(?P<name>.*?)" class="image"><img alt=".*?" src=".*?" decoding=".*?" width=".*?" height=".*?" srcset=".*?" data-file-width="(?P<width>.*?)" data-file-height="(?P<height>.*?)" /></a></div></div>', re.S)
    # 用于匹配子页面中BG图片下载地址的re
    re_ = re.compile(r'<span class="mw-filepage-other-resolutions">其他分辨率：.*<a href="(?P<download_link>.*?)" class="mw-thumbnail-link">.*?</a>。</span>', re.S) 
    # 碧蓝航线WIKI的文件页面
    source_bg = 'https://wiki.biligame.com/blhx/%E5%BD%B1%E7%94%BB%E7%9B%B8%E5%85%B3'
    source_other = 'https://wiki.biligame.com/blhx/%E7%94%BB%E5%B8%88%E8%B4%BA%E5%9B%BE%E3%80%81%E5%90%8C%E4%BA%BA%E5%9B%BE%E5%90%88%E9%9B%86'
    # 数据库位置
    local_path = os.path.abspath('.')
    data_path = local_path + '/data'
    data_path_bg = data_path + '/bg.csv'
    data_path_other = data_path + '/other.csv'
    # 停止标志
    stop_flag = False
    
    def __init__(self, tag) -> None:
        self.save_path_bg = self.local_path + '/donwload/bg'
        self.save_path_other = self.local_path + '/download/other'
        self.tag = tag
        
        if not os.path.exists(self.data_path):
            os.makedirs(self.data_path)
        
        
    def set_save_path(self, path):
        self.save_path_bg = path.replace('\\','/') +'/bg'
        self.save_path_other = path.replace('\\','/') +'/other'

    def update(self):
        if self.tag=='bg':
            source_link = self.source_bg
            data_path = self.data_path_bg
        elif self.tag=='other':
            source_link = self.source_other
            data_path = self.data_path_other
        else:
            pass
        print('-> processing in ' + data_path)
        self.source_code = get_source_code_from_link(url = source_link)
        get_picture_links(source_code=self.source_code, re_source=self.re_source, re_=self.re_, data_path=data_path)
        print('-> ' + self.tag + ' Update Successfully')
        
    def scraper_run(self):
        self.stop_flag = False
        if self.tag=='bg':
            save_path = self.save_path_bg
            data_path = self.data_path_bg 
        elif self.tag=='other':
            save_path = self.save_path_other
            data_path = self.data_path_other
        else:
            pass
        print('-> Processing in path: '+ save_path)
        
        if not os.path.exists(data_path):
                self.update(self.tag)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(data_path, 'r', encoding='utf-8') as database:
            local_set = set(os.listdir(save_path))
            reader = csv.DictReader(database)
            for line in reader:
                if self.stop_flag:
                    print('-> Stopped by user')
                    break
                name = parse.unquote(line['name'], encoding='utf-8')
                if name not in local_set:
                    download_link = get_download_link(line['name'], self.re_)
                    if download_link:
                        save_picture_from_link(download_link[0], save_path+'/'+name)
                        print('-> Saving:  '+ name+' Done.')
                    else:
                        pass
                        # print('-> No download link in this page. Ignore.')
                else:
                    pass
                    # print('-> File: '+ name+' Already exists.')  

    def scraper_stop(self):
        self.stop_flag = True
        