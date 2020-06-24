import urllib.request
from lxml import html as lh
import json
from datetime import date
import codecs
import time



def readFile(file):
    f = open(file,"r")
    return f.readlines() 



def getPrice(html):
    element = '//*[@id="skip-to-content"]/article/section[3]/div/div[3]/div/div[1]/div[1]/div/span[1]'   #Price        
    xml = lh.fromstring(html)
    return xml.xpath(element)[0].text_content().replace("€","").replace(".","")

def getName(html):
    element = '//*[@id="skip-to-content"]/article/section[3]/div/div[1]/div/div[1]/h1'   #Name        
    xml = lh.fromstring(html)
    return xml.xpath(element)[0].text_content()

def export(out):
    with codecs.open('data.json', 'w+', encoding="utf-8") as outfile:
        json.dump(out, outfile, ensure_ascii=False)
    return  


def load():
    with open('data.json',encoding='utf-8') as json_file:
        return(json.load(json_file))




def main():
    while 1:
        items = []
        jsonArray = load()
        for url in readFile("./search.txt"): 
            fp = urllib.request.urlopen(url)
            html = fp.read().decode("utf8")
            fp.close()
            tmp = getName(html)
            if(tmp not in jsonArray["Products"]):
                jsonArray["Products"].append(getName(html))
            items.append(getPrice(html))
        jsonArray[str(date.today())+"a"] = items
        export(jsonArray)
    time.sleep(3600)





if __name__ == "__main__":
    main()