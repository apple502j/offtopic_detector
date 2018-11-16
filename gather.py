import requests
from bs4 import BeautifulSoup

def get_urls(tag, page=1):
    root_url = "https://qiita.com/tags/{}/items?page={}".format(str(tag),str(page))
    r = requests.get(root_url)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup.find_all("a",{"class":"tsf-ArticleBody_title"})


def main(tags, limit_page=5):
    out = []
    for tag in tags:
        for page in range(limit_page):
            out += ["https://qiita.com/"+x['href'] for x in get_urls(tag, page+1)]
    return out    

if __name__ == "__main__":
    tags = ["初心者", "ポエム"]
    with open("bad_articles.txt", "w") as f:
        f.write('\n'.join(main(tags)))
