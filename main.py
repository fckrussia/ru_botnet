# MUST INSTALL requests MODULE
#    pip install freeze

import requests

def make_req() :
    print("FAZENDO REQUEST")

    targets = [
            'https://www.gazprom.ru/',
            'https://lukoil.ru',
            'https://magnit.ru/',
            'https://www.nornickel.com/',
            'https://www.surgutneftegas.ru/',
            'https://www.tatneft.ru/',
            'https://www.evraz.com/ru/',
            'https://nlmk.com/',
            'https://www.sibur.ru/',
            'https://www.severstal.com/',
            'https://www.metalloinvest.com/',
            'https://nangs.org/',
            'https://rmk-group.ru/ru/',
            'https://www.tmk-group.ru/',
            'https://www.polymetalinternational.com/ru/',
            'https://www.uralkali.com/ru/',
            'https://www.eurosib.ru/',
            'https://omk.ru/'
            ]

    while True:
        for target in targets :
            response = requests.get(target.strip())
    
            print("SITE: {} - RESPOSTA: {}".format(target, response))

def main() :
    make_req()

if __name__ == "__main__" :
    main()
