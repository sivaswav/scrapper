import requests;
import sys;
from bs4 import BeautifulSoup;
from bs4 import element;
import json;
import datetime;
import os;
import re;


class download_xtract:
    def __init__(self, url):
        print("Download & Extraction Started......");
        self.url = url;
        self.page = "";
        self.sp = "";
        self.words = [];
        self.dicts = {};
        self.jsson = "";
        self.json_data = "";

    def downloader(self):
        try:
            print("download started......");
            self.page = requests.get(self.url);
            if (self.page.status_code == 200):
                print("download ended......");
                return self.page.text;
            else:
                return "URL download NOT POSSIBLE" + str(self.page);
        except:
            print("Exception Occurred" + str(sys.exc_info()));

    def parser(self, page):
        try:
            print("parsing started......");
            self.sp = BeautifulSoup(page, 'html.parser');
            '''with open("source.html","w") as f:
                f.write(self.sp.prettify());'''
            print("parsing ended......");
        except:
            print("Exception Occurred" + str(sys.exc_info()));

    def extractor_dataset_count(self):
        try:
            print("dataset count extraction started......");
            '''for k in self.sp.findAll('div',{'class':'row my-4'}) :
                for i in k.findAll('div',{'class':'card'}) :
                        self.words.append(i.text.replace('\n','').replace('$','-$'));
            '''
            for k in self.sp.findAll('div', {'class': 'new-results'}):
                self.words.append(k.text.replace('\n', ''));

            print("dataset count  extraction ended......");

        except:
            print("Exception Occurred" + str(sys.exc_info()));

    def extractor_latest_dataset(self):
        try:
            print("latest dataset  extraction started......");
            for k in self.sp.findAll('li', {'class': 'dataset-item has-organization'}, limit=1):
                for i in k.findAll('a', limit=1):
                    self.words.append(i.text);

            print("latest dataset  extraction ended......");

        except:
            print("Exception Occurred" + str(sys.exc_info()));

    def json_converter(self):
        try:
            print("json conversion started......");
            self.dicts[datetime.datetime.today().strftime('%d-%m-%Y')] = self.words;
            self.json_data = json.dumps(self.dicts);
            with open("source.html", "a+") as f:
                f.write(self.json_data);
            print("json conversion ended......");
        except:
            print("Exception Occurred" + str(sys.exc_info()));

    def __del__(self):
        print("Download & Extraction Done......");


