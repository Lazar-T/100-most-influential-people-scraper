import csv

from termcolor import colored
from selenium import webdriver

# Opening outupt.csv file for writing
writer = csv.writer(open('output.csv', 'wb'))

# Writing header row into a output.csv file
writer.writerow(['Person', 'About', 'Page url', 'Picture url'])

# Launching web driver instance
driver = webdriver.Firefox()

# Loading start url
driver.get('http://time.com/collection/2015-time-100/')

# Fetch people urls
urls = driver.find_elements_by_xpath('//h2/a')

list_urls = []
for url in urls:
    url = url.get_attribute('href')
    list_urls.append(url)

for number, url in enumerate(list_urls, start=1):
    driver.get(url)

    # person field
    person = driver.find_elements_by_xpath('//h2')[1].text
    person = person.encode('utf-8')

    # about field
    about_raw = driver.find_elements_by_xpath('//div/p')
    about = [line.text for line in about_raw]  # Iterate and grab text from each line
    about = ''.join(about)  # Transform list to unicode
    about = about.encode('utf-8')

    # page_url field
    page_url = driver.current_url
    page_url = page_url.encode('utf-8')

    # img_src field
    try:
        img_url = driver.find_element_by_xpath('//*[@class="article-hero_wrapper"]/img')
        img_src = img_url.get_attribute('src')
        img_src = img_src.encode('utf-8')
    except:
        img_src = 'None'

    print '-' * 120
    print colored('Person number: ', 'red'), colored(number, 'green')
    print colored('Name: ', 'red'), colored(person, 'green')
    print colored('About: ', 'red'), colored(about, 'green')
    print colored('Url of the page: ', 'red'), colored(page_url, 'green')
    print colored('Url of the image: ', 'red'), colored(img_src, 'green')
    print '-' * 120
    print '\n'

    # Write current row into a output.csv file
    writer.writerow([person, about, page_url, img_src])

# Close web driver instance
driver.close()
