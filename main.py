import requests_html
import requests


def img_downloader(n, **kwargs):
    if kwargs.get("start_page") != None:
        first = kwargs.get("start_page")
    else:
        first = 1
    for i in range(first, n+1):
        url = f"https://www.skidrowreloaded.com/page/{i}/"
        session = requests_html.HTMLSession()
        r = session.get(url)
        r.html.render(sleep=2, scrolldown=10)
        items = r.html.find("div#main-content", first=True)
        img_srcs = items.find("img.lazy-loaded")
        i = 1
        for img_src in img_srcs:
            temp_src = img_src.attrs["src"]
            if temp_src[:1] == "/":
                src = "https://www.skidrowreloaded.com" + temp_src
            else:
                src = temp_src
            img = requests.get(src)
            temp_title = img_src.attrs["alt"]
            if len(temp_title) == 0:
                title = "unnamed" + str(i)
                i += 1
            else:
                title = temp_title
            with open(title + ".jpg", "wb") as imagefile:
                imagefile.write(img.content)


# if you want a certain single page content, provide its number as follows:
img_downloader(2, start_page=2)

# if you want to scrape from the start page to a certain page, provide only the number of the last page,
# as follows:
img_downloader(5)

# if you want to scrape from a certain page up to another certain page, provide both pages numbers,
# as follows:
img_downloader(5, start_page=2)


