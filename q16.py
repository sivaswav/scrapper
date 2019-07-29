import requests;
import sys;
from bs4 import BeautifulSoup;
from bs4 import element;

class q16:
    def __init__(self):
        print("Exraction is start");
        self.page_text="";
        self.spobj="";

    def urlget(self,url):
        try:
            self.page_text=requests.get(url);
            if self.page_text.status_code==200:
                return True;
            else:
                return False;
        except:
            print("Exception Ocurred "+str(sys.exc_info()));

    def toBsobj(self):
        try:
            self.spobj=BeautifulSoup(self.page_text.text,"html.parser");
            with open("source.html","w") as f:
                f.write(self.spobj.prettify());
        except:
            print("Exception Ocurred " + str(sys.exc_info()));

    def toExtract(self):
        try:
            res=self.spobj.findAll('td',{'class':'company-col'},limit=1);
            print(res);
           # for i in res.findAll('tb):
            #    print(i);
        except:
            print("Exception Ocurred " + str(sys.exc_info()));


    def __del__(self):
        print("Exraction is over");

if __name__=="__main__":
    xobj=q16();
    retval=xobj.urlget("https://projects.propublica.org/nonprofits/search?c_code%5Bid%5D=&ntee%5Bid%5D=&order=revenue&q=&sort_order=desc&state%5Bid%5D=&utf8=%E2%9C%93");
    if retval==True:
        xobj.toBsobj();
        xobj.toExtract();
