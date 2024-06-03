import requests
from bs4 import BeautifulSoup
import sys
import re
sys.stdout.reconfigure(encoding='utf-8')
def getThaiWord(word):
    url = f'https://dict.longdo.com/search/{word}'

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        rows = soup.find_all('tr', class_=['lang-rows', 'lang-EN', 'lang-TH'])
        checkPronouce=False
        checkTranslate=False
        for row in rows:
            cells = row.find_all('td')  
            for cell in cells:
                # print(cell.text.strip())
                if(cell.text.strip()=="English-Thai: HOPE Dictionary [with local updates]"):
                    checkPronouce=True
                    continue
                if(checkPronouce):
                    # print(cell.text.strip())
                    text=cell.text.strip()
                    matches = re.findall(r'\(.*?\)', text) 
                    print(matches[0][1:-1].replace("'",""))
                    checkPronouce=False
                    continue
                if(cell.text.strip()=="English-Thai: NECTEC's Lexitron-2 Dictionary [with local updates]"):
                    checkTranslate=True
                    continue
                if(checkTranslate):
                    text=cell.text.strip().split(word)
                    print(text[1][4:])
                    checkTranslate=False
                    continue
getThaiWord("train")