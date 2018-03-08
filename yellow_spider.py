import requests
import re
import time
import threading



def downloadvideo(num):
    url_embed = "https://www.pornhub.com/embed/"+num
    html = requests.get(url_embed)
    url_video = re.findall('"videoUrl":"(.*?)"',html.text,re.S)
    a = url_video[0].replace("\\",'')
    print("url is {}" .format(a))
    with open("{}.mp4" .format(num),"wb") as f:
        video = requests.get(a)
        f.write(video.content)

def main():
    searchkeyword = input("Please input keywords in English:")
    page_num = input("Please input page number:")
    url = "https://www.pornhub.com/video/search?search="+searchkeyword+"&page="+page_num
    proxies = {"http":"http://127.0.0.1:1080",
                "https":"http://127.0.0.1:1080"
            }
    html = requests.get(url,proxies = proxies)
    num_list = re.findall('<a href="/view_video.php.viewkey=(.*?)" title',html.text)
    num_list = list(set(num_list))
    print(num_list)
    threads = []
    for num in num_list:
        try:
            thread = threading.Thread(target=downloadvideo,args=(num,))
            threads.append(thread)
        except:
            continue
    for t in threads:
        try:    
            t.start()
        except:
            continue
    t.join()   

if __name__ == "__main__":
    main()

