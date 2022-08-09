from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
import time
import random
from fake_useragent import UserAgent


user_agents = ["Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit / ",
               "605.1.15 (KHTML, как Gecko) Версия / 13.1 Safari / 605.1.15",
               "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit / 537.36 "
               "(KHTML, как Gecko) Chrome / 80.0.3987.163 Safari / 537.36",
               "Mozilla / 5.0 (Macintosh; Intel Mac OS X 10.14; rv: 75.0) Gecko / 20100101 Firefox / 75.0"]


class UseSelenium:
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def save_page(self):
        persona = self.__get_headers_proxy()

        options = webdriver.ChromeOptions()
        user = random.choice(user_agents)
        options.add_argument(f"user-agent={user}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--headless")

        # options_proxy = {
        #     'proxy': {
        #         'https': persona['http_proxy'],
        #         'no_proxy': 'localhost,127.0.0.1:8080'
        #     }
        # }

        s = Service(executable_path='chromedriver')

        driver = webdriver.Chrome(options=options, service=s)

        try:
            driver.get(self.url)
            time.sleep(3)
            driver.execute_script("window.scrollTo(5,4000);")
            time.sleep(5)
            html = driver.page_source
            with open('pages/' + self.filename, 'w', encoding='utf-8') as f:
                f.write(html)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()




    def __get_headers_proxy(self) -> dict:
        users = [{
                'http_proxy':'http://VLk5nq:pEJKY7@91.188.240.228:9432',
                'user-agent': random.choice(user_agents)
            },
            {
                'http_proxy':'http://VLk5nq:pEJKY7@91.188.243.244:9715',
                'user-agent': random.choice(user_agents)
            },
            {
                'http_proxy': 'http://VLk5nq:pEJKY7@91.188.241.80:9406',
                'user-agent': random.choice(user_agents)
            },
            {
                'http_proxy': 'http://VLk5nq:pEJKY7@91.188.240.117:9314',
                'user-agent': random.choice(user_agents)
            },
        ]

        try:
            persona = random.choice(users)
        except ImportError:
            persona = None
        return persona

