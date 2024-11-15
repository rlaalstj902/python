from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def hollys_store(result):
    for page in range(1, 50):
        # 문자열 포맷팅을 위해 % 대신 f-string을 사용합니다.
        Hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store='
        print(Hollys_url)
        html = urllib.request.urlopen(Hollys_url)
        soupHollys = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupHollys.find('tbody')
        for store in tag_tbody.find_all('tr'):
            store_td = store.find_all('td')
            if len(store_td) < 6:  # 컬럼이 부족할 경우 무시
                continue
            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            result.append([store_name, store_sido, store_address, store_phone])

def main():
    result = []  # 리스트 초기화
    print('Hollys store crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    hollys_store(result)  # hollys_store 함수 호출
    hollys_tbl = pd.DataFrame(result, columns=('store', 'sido-gu', 'address', 'phone'))
    hollys_tbl.to_csv('./hollys.csv', encoding='cp949', mode='w', index=True)
    del result[:]

if __name__ == '__main__':
    main()
