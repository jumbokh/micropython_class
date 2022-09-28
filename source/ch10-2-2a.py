import urequests, ujson
import xtools

ip = xtools.connect_wifi_led()
print(ip)

url = "https://www.googleapis.com/books/v1/volumes?maxResults=3&q=Python&projection=lite"
r = urequests.get(url)
if r.status_code == 200:
    print(" 下載: ", len(r.text), "字元")
    info = ujson.loads(r.text)
    print("--------------------------")
    for item in info["items"]:
        book = item["volumeInfo"]        
        print("圖書名: " , book["title"])
        if "publisher" in book.keys():
            print("出版商: ", book["publisher"])
        print("出版日: ", book["publishedDate"])
        print("--------------------------")       
else:
    print("沒有圖書資料")