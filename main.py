from bs4 import BeautifulSoup
import requests


def main(url):
    File = open("amazon.csv", "a")
      # available on the internet
    HEADERS = ({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 'en-US, en;q=0.5'})
    webpage = requests.get(url, headers=HEADERS)


    soup = BeautifulSoup(webpage.content, "lxml")

    try:
        title = soup.find("span", 
                          attrs={"id": 'productTitle'})
        title_value = title.string
        title_string = title_value.strip().replace(',', '')
    except AttributeError:

        title_string = "NA"

        print("product Title = ", title_string)

    File.write(f"{title_string},")
   

# closing the file
    File.close()

if __name__ == '__main__':
  # opening our url file to access URLs
    # file = open("url.txt", "r")

    # iterating over the urls
    # for links in file.readlines():
    main("https://www.amazon.com/Amazon-vibrant-helpful-routines-Charcoal/dp/B09B8V1LZ3/ref=asc_df_B09B8V1LZ3?mcid=1ad576cb6b5c3199aa9b82f2f916e42a&hvocijid=5258534744136503602-B09B8V1LZ3-&hvexpln=73&tag=hyprod-20&linkCode=df0&hvadid=730434204848&hvpos=&hvnetw=g&hvrand=5258534744136503602&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9010619&hvtargid=pla-2281435179778&psc=1")