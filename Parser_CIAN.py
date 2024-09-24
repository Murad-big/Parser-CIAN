import csv
import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

cookies = {
    '_CIAN_GK': 'a70f2533-64b3-4d8f-bbcc-d05e7b9a6a85',
    '_gcl_au': '1.1.618295093.1717577550',
    'tmr_lvid': '05799f858f2202d77b831afae9380b23',
    'tmr_lvidTS': '1717577550596',
    'uxfb_usertype': 'searcher',
    'sopr_utm': '%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
    '_ym_uid': '1717577828457315184',
    '_ym_d': '1717577828',
    '_gid': 'GA1.2.1896544277.1717577828',
    'uxs_uid': '96d01ab0-2319-11ef-9f60-2db628b3bcd0',
    '_ym_isad': '2',
    'adrdel': '1717577829037',
    'adrcid': 'AMuz3i-Rh4Da-teWconVbtg',
    'afUserId': '84c35d2f-aba6-4625-abdb-0c2f8e2f1ca0-p',
    'AF_SYNC': '1717577829374',
    'forever_region_id': '4593',
    'forever_region_name': '%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C',
    'domain_sid': '_Vgl7lRd-qLqYCOmSqB_t%3A1717577883018',
    'adrcid': 'AMuz3i-Rh4Da-teWconVbtg',
    'session_region_id': '4857',
    'login_mro_popup': '1',
    'sopr_session': '9e93996ec6764a12',
    '_ym_visorc': 'b',
    'cookie_agreement_accepted': '1',
    'pview': '1',
    '__cf_bm': 'a7XYtJBI84RNDlUxXl4ZViPYjLXKiXgoAYkm9a8j5E0-1717598570-1.0.1.1-nYq7hPolutRH6a75_dQxpliRoYaA8lEMzIMoGh_GVeQqsM5ld3xGbmpBCFhwwIuJiEnxDkQKF4EFMjFwUS0IdA',
    '_ga_3369S417EL': 'GS1.1.1717596354.4.1.1717598738.58.0.0',
    '_ga': 'GA1.2.165647225.1717577657',
    '_dc_gtm_UA-30374201-1': '1',
    'tmr_detect': '0%7C1717598739907',
}

headers = {
    'authority': 'www.cian.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': '_CIAN_GK=a70f2533-64b3-4d8f-bbcc-d05e7b9a6a85; _gcl_au=1.1.618295093.1717577550; tmr_lvid=05799f858f2202d77b831afae9380b23; tmr_lvidTS=1717577550596; uxfb_usertype=searcher; sopr_utm=%7B%22utm_source%22%3A+%22yandex%22%2C+%22utm_medium%22%3A+%22organic%22%7D; _ym_uid=1717577828457315184; _ym_d=1717577828; _gid=GA1.2.1896544277.1717577828; uxs_uid=96d01ab0-2319-11ef-9f60-2db628b3bcd0; _ym_isad=2; adrdel=1717577829037; adrcid=AMuz3i-Rh4Da-teWconVbtg; afUserId=84c35d2f-aba6-4625-abdb-0c2f8e2f1ca0-p; AF_SYNC=1717577829374; forever_region_id=4593; forever_region_name=%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C; domain_sid=_Vgl7lRd-qLqYCOmSqB_t%3A1717577883018; adrcid=AMuz3i-Rh4Da-teWconVbtg; session_region_id=4857; login_mro_popup=1; sopr_session=9e93996ec6764a12; _ym_visorc=b; cookie_agreement_accepted=1; pview=1; __cf_bm=a7XYtJBI84RNDlUxXl4ZViPYjLXKiXgoAYkm9a8j5E0-1717598570-1.0.1.1-nYq7hPolutRH6a75_dQxpliRoYaA8lEMzIMoGh_GVeQqsM5ld3xGbmpBCFhwwIuJiEnxDkQKF4EFMjFwUS0IdA; _ga_3369S417EL=GS1.1.1717596354.4.1.1717598738.58.0.0; _ga=GA1.2.165647225.1717577657; _dc_gtm_UA-30374201-1=1; tmr_detect=0%7C1717598739907',
    'referer': 'https://www.cian.ru/realtors/?regionId=4593&page=2',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "YaBrowser";v="24.4", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36',
}
def realtores(url):
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
    )
    response_text = response.text
    try:
        data = json.loads(response_text)
        realtors = data['items']
        ids = []
        for realtor in realtors:
            ids.append(realtor["cianUserId"])
        return ids
    except:
        ids = []
        return ids

def realtor(id):
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36")
    name = "-"
    email = "-"
    tg = "-"
    number = "-"
    with open('realtores.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')

    try:
        with webdriver.Chrome(options=options) as browser:

            browser.get(f"https://www.cian.ru/agents/{id}/")
            time.sleep(0.2)
            show = browser.find_element(By.CSS_SELECTOR,"div._3ea6fa5da8--hidden-phone--rwAmU")
            show.click()
            number = show.text.split("\n")[0]
            Name = browser.find_element(By.CSS_SELECTOR,"span._3ea6fa5da8--name--JPPsh").text
            name = Name
            try:
                info = browser.find_element(By.CSS_SELECTOR, "div._3ea6fa5da8--info--xfvTI").text.split("\n")
                for i in info:
                    if "@" in i:
                        email = i
                    elif "t.me" in i:
                        tg = i
            except:
                print()
    except:
        print(f"{id} содержит ошибку")
    print(name)
    return [name,number,email,tg]



def main():
    regionIds = ["1","4593"]
    k = 0
    person = []
    for regionId in regionIds:
        for page in range(2500,3000):
            k += 1
            t = 0
            url = f"https://api.cian.ru/agent-catalog-search/v1/get-realtors/?regionId={regionId}&page={page}"
            response = requests.get(url)
            if response.status_code != 400:
                if realtores(url):
                    print(page)
                    ids = realtores(url=url)
                    for id in ids:
                        person.append(realtor(id))

            else:
                t += 1
                if t == 4:
                    break

            if k % 4 == 0:
                with open('realtores.csv', 'a', encoding='utf-8-sig', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    for member in person:
                        writer.writerow(member)
                person = []
                print("файл был создан")
    with open('realtores.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for member in person:
            writer.writerow(member)
if __name__ == '__main__':
    main()

