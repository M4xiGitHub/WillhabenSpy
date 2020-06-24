"""
Bleier Maximilian
24.06.2020
"""

import urllib.request
from lxml import html as lh
import json
from datetime import date
import codecs
import time


#Reads the File
def readFile(file):
    f = open(file,"r")
    return f.readlines() 


#Gets Price from Product from Willhaben
def getPrice(html):
    element = '//*[@id="skip-to-content"]/article/section[3]/div/div[3]/div/div[1]/div[1]/div/span[1]'   #Price        
    xml = lh.fromstring(html)
    return xml.xpath(element)[0].text_content().replace("€","").replace(".","")

#Gets Name from Product from Willhaben
def getName(html):
    element = '//*[@id="skip-to-content"]/article/section[3]/div/div[1]/div/div[1]/h1'   #Name        
    xml = lh.fromstring(html)
    return xml.xpath(element)[0].text_content()

#Saves the array to data.json to load in js
def export(out):
    with codecs.open('data.json', 'w+', encoding="utf-8") as outfile:
        json.dump(out, outfile, ensure_ascii=False)
    return  

#Loads the array in to update it
def load():
    with open('data.json',encoding='utf-8') as json_file:
        return(json.load(json_file))




def main():
    while True:
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
        jsonArray[str(date.today())] = items
        export(jsonArray)
    time.sleep(3600)





if __name__ == "__main__":
    main()