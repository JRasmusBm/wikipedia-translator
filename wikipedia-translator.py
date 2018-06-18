from bs4 import BeautifulSoup
from os.path import join
from urllib.parse import parse_qsl
import requests

def translate(word, target_language="en"):

    google_base_url = "https://www.google.com/search?q="
    google_url = join(google_base_url, word + " wikipedia")

    google_response = requests.get(google_url, timeout=5)
    google_content = BeautifulSoup(google_response.content, "html.parser")
    wikipedia_link = ""
    for a in google_content.find_all("a", href=True):
        if "wikipedia.org" in a["href"]:
            wikipedia_link = parse_qsl(a["href"])[0][1]
            break
    if wikipedia_link == "" :
        raise Exception("No translation found!")
    wikipedia_response = requests.get(wikipedia_link)
    wikipedia_content = BeautifulSoup(wikipedia_response.content, "html.parser")

    lang_node = wikipedia_content.find(id="p-lang").find("a", lang=target_language)

    if lang_node != None :
        wikipedia_link = lang_node["href"]
        wikipedia_response = requests.get(wikipedia_link)
        wikipedia_content = BeautifulSoup(wikipedia_response.content, "html.parser")

    return(wikipedia_content.find(id="firstHeading").text)

try:
    print(translate("Mjukglass", "en"))
except Exception as e:
    print(e)

