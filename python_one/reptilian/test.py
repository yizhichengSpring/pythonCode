import requestsdemo


def get_one_page(url):
    response = requestsdemo.get(url)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url = "http://maoyan.com/board/4"
    html = get_one_page(url)
    print(html)



main()