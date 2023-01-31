import requests
from bs4 import BeautifulSoup, SoupStrainer
from pathlib import Path
import os

image_page_base = 'https://geekquestioner.com'

destination = Path(r'C:\Users\benhartd\PycharmProjects\Fun\geekscapes')
existing_files = os.listdir(destination)
images_checked = 0


def get_images(hrefs, images_checked):
    for page_link in hrefs:
        title = '-'.join(page_link.split('-')[1:]) + '.png'
        images_checked += 1
        print(images_checked)
        if title in existing_files:
            pass
        else:
            # try:
            image_info_page = requests.get(image_page_base + page_link)
            image_page_soup = BeautifulSoup(image_info_page.content, 'html.parser')
            page_images = image_page_soup.find_all('img')
            for img in page_images:
                if img.has_attr('class'):
                    img_class = img.get('class')
                    if 'thumb-image' in img_class:
                        image = requests.get(img.attrs['data-image'])
                        file = open(destination.joinpath(title), 'wb')
                        file.write(image.content)
                        file.close()
            # except:
            #     pass

    return images_checked


next_page = '/content?category=Geekscapes&tag=gsotd2018'

while True:

    url = image_page_base + next_page
    r = requests.get(url)
    # r = requests.get(image_page_base)

    soup = BeautifulSoup(r.content, 'html.parser')

    # hrefs = soup.find_all('a', {'class': 'read-more'})
    hrefs = soup.find_all('a', href=True)

    page_links = []
    for link in hrefs:
        href = link.get('href')
        if link.has_attr('class'):
            if link.get('class')[0] == 'read-more':
                page_links.append(href)

        if r'/content?offset=' in href:
            next_page = href

    images_checked = get_images(page_links, images_checked)
