import requests
from xml.etree import ElementTree
from environment import CB_ADDRES

def dollar_currency():
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
    print(dollar_currency())

