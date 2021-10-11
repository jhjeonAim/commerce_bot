from app.spiders.category import Category
import time

# 카테고리 수집 실행


def category_run():
    cat = Category()

    # 데이터를 수집할 url
    cat.proc("https://www.naver.com")
    # 1초 휴식
    time.sleep(1)
