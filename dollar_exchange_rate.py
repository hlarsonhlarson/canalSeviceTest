import requests
from xml.etree import ElementTree

CB_ADDRES = 'https://www.cbr.ru/scripts/XML_daily.asp?ID=R01235'
def transform_dollars_rubles():
    response = requests.get(CB_ADDRES)

    tree = ElementTree.fromstring(response.content)
    for child in tree.findall('Valute'):
        for elem in child:
            if elem.tag == 'Value':
                ans = float(elem.text.replace(',', '.'))
            elif elem.tag == 'CharCode':
                if elem.text == 'USD':
                    return ans
    return None

if __name__ == '__main__':
    print(transform_dollars_rubles())

