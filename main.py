# importing libraries
from bs4 import BeautifulSoup
import requests

def main(URL):
    # opening our output file in append mode
    File = open("out.csv", "a")

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")


    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id": 'productTitle'})
        price =soup.find("span", attrs={"class": "a-price-whole"}).get_text().replace('.','')


        # Inner NavigableString Object:
        # if title:
        title_value = title.string
        title_string = title_value.strip().replace(',', '')
        # else:
            # title_string="N/A"

        # Title as a string value
        
        File.write(f"{title_string},")
        # saving
        File.write(f"{price}"+"\n")

    except AttributeError:
        title_string = "NA"
        File.write(f"{title_string},")

        price = "NA"
        File.write(f"{price}"+"\n")
    

    # closing the file
    File.close()


if __name__ == '__main__':
  # opening our url file to access URLs
    file = open("url.txt", "r")

    # iterating over the urls
    for links in file.readlines():
        main(links)
