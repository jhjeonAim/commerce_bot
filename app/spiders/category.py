from bs4 import BeautifulSoup
from app.spiders.spider import get_html


headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
}


class Category:
    # 카테고리 데이터 추출
    def extract(self, page):
        return None

    # 카테고리 페이지 다운
    def proc(self, url):
        html = get_html(url, headers)
        document = BeautifulSoup(html, 'html.parser')

        data = {
            'category': self.extract(document)
        }

        return data
