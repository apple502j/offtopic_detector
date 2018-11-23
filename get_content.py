# coding: utf-8
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import os
import json
import time

def get_content(url):
    try:
        r = requests.get(url).content
        soup = BeautifulSoup(r, "html.parser")
        #return soup.find("section", {"class":"it-MdContent"}).getText()
        pid=url.replace("https://scratch.mit.edu/discuss/post/","").replace("/","")
        return soup.select(f"div#p{pid} div.box div.box-content div.postright")[0].getText()
    except:
        raise Exception(f"Does {url} really exist?")


def main(bad_file, good_file):
    import pandas as pd
    try:
        raise Exception
        out = pd.read_csv("content.csv")
    except:
        out=[]
    os.rename("content.csv",f"content.csv.{time.time()}")
    with open(bad_file) as f:
        for line in tqdm(f):
            line = line.strip()
            #try:
            fp=open("got.json","r")
            try:
                js0n={}
            except SystemExit:
                print("ERROR!")
                js0n={}
            if line in js0n.get("bad",[]):
                fp.close()
                continue
            else:
                try:
                    js0n["bad"].append(line)
                except:
                    js0n["bad"]=[line]
            fp.close()
            fp=open("got.json","w")
            json.dump(js0n, fp)
            fp.close()
            if True:
                out.append({"url":line, "content":get_content(line), "label":False})
            if False:
            #except:
                print("error")
                break

    with open(good_file) as f:
        for line in tqdm(f):
            line = line.strip()
            fp=open("got.json","r+")
            try:
                js0n={}
            except:
                print("ERROR!")
                js0n={}
            if line in js0n.get("good",[]):
                fp.close()
                continue
            else:
                try:
                    js0n["good"].append(line)
                except:
                    js0n["good"]=[line]
            fp.close()
            fp=open("got.json","w")
            json.dump(js0n, fp)
            fp.close()

            try:
                out.append({"url":line, "content":get_content(line), "label":True})
            except:
                print("error")
                break

    pd.DataFrame(out).to_csv("content.csv", index=False)


if __name__ == "__main__":
    main("bad_articles.txt", "good_articles.txt")
