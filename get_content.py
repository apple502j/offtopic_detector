# coding: utf-8
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def get_content(url):
    r = requests.get(url).content
    soup = BeautifulSoup(r, "html.parser")
    return soup.find("section", {"class":"it-MdContent"}).getText()


def main(bad_file, good_file):
    import pandas as pd
    out = []
    with open(bad_file) as f:
        for line in tqdm(f):
            line = line.strip()
            try:
                out.append({"url":line, "content":get_content(line), "label":False})
            except:
                print("error")
                break
    
    with open(good_file) as f:
        for line in tqdm(f):
            line = line.strip()
            try:
                out.append({"url":line, "content":get_content(line), "label":True})
            except:
                print("error")
                break
    
    pd.DataFrame(out).to_csv("content.csv", index=False)

if __name__ == "__main__":
    main("bad_articles.txt", "good_articles.txt")
