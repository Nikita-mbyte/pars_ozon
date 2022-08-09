from bs4 import BeautifulSoup
import glob

def get_pages() -> list:
    return glob.glob('pages/*.html')

def get_html(page: str):
    with open(page, 'r', encoding='utf-8') as f:
        return f.read()

def parse_data(html: str) -> str:

    soup = BeautifulSoup(html, 'html.parser')
    links = []
    # for link in soup.find_all('a', href=True):
    #    links.append(link)
    # #
    # Links = []

    products = soup.find("div", class_="wj9")

    # soup.find_all("a", class_="sister")
    if products is not None:
        products = products.find_all('a')
        for product in products:
            links.append(product.get('href').split('?')[0])
        print(products)
        return set(links)
    else:
        return ('')
    # for product in products:
    #     links.append(product.get('href').split('?')[0])



    # for link in links:
    #     Links.append(link.get('href').split('?')[0])



def main():
    pages = get_pages()

    all_links = []

    for page in pages:
        html = get_html(page)
        links = parse_data(html)
        all_links = all_links + list(links)

    # print(all_links)
    # print(len(all_links))

    with open('product_links.txt', 'w', encoding='utf-8') as f:
        for link in all_links:
            if link != None:
                f.write(link+'\n')



if __name__ == '__main__':
    main()