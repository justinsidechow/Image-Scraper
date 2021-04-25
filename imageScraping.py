import selenium
from selenium import webdriver
import time
import requests
import io
import os
from PIL import Image
import hashlib

def fetch_image_urls(query:str, max_links_to_fetch:int, wd:webdriver, sleep_between_interactions:int=1):
    def scroll_to_end(wd):
<<<<<<< HEAD
        scroll_pause_time = 3 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = wd.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 1
        
        time.sleep(scroll_pause_time)
        
        while True:
            # scroll one screen height each time
            wd.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
            i += 1
            time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = wd.execute_script("return document.body.scrollHeight;")  
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break
=======
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(sleep_between_interactions)    
>>>>>>> f91bc3b832797b976262e2a7af2dfdb4ed0827ee
        
    # build the google query
    search_url = "https://opensea.io/assets/{q}"
    # load the page
    wd.get(search_url.format(q=query))
<<<<<<< HEAD
    wd.maximize_window()
=======

>>>>>>> f91bc3b832797b976262e2a7af2dfdb4ed0827ee
    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
        scroll_to_end(wd)

        # get all image thumbnail results
        thumbnail_results = wd.find_elements_by_class_name("Image--image")
        number_results = len(thumbnail_results)
        
        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
<<<<<<< HEAD
=======
        
>>>>>>> f91bc3b832797b976262e2a7af2dfdb4ed0827ee
        for img in thumbnail_results[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
            #    img.click()
                time.sleep(sleep_between_interactions)
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_class_name("Image--image")
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
        else:
            print("Found:", len(image_urls), "image links, looking for more ...")
            time.sleep(30)
            return
            pipload_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(thumbnail_results)
<<<<<<< HEAD

=======
        
        
>>>>>>> f91bc3b832797b976262e2a7af2dfdb4ed0827ee
    return image_urls


def persist_image(folder_path:str,url:str):
    try:
        image_content = requests.get(url).content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")

<<<<<<< HEAD
def search_and_download(search_term:str,driver_path:str,target_path='C:/Users/justi/OneDrive/Desktop/secret sauce/programming/Image-Scrapper-Base/images/',number_images=1):
=======
def search_and_download(search_term:str,driver_path:str,target_path='/Users/halfamotorcycle/Desktop/imageScrapped/images/',number_images=5):
>>>>>>> f91bc3b832797b976262e2a7af2dfdb4ed0827ee
    target_folder = os.path.join(target_path,'_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images, wd=wd, sleep_between_interactions=0.5)
        
    for elem in res:
        persist_image(target_folder,elem)

# This is the path I use
# DRIVER_PATH = '.../Desktop/Scraping/chromedriver 2'
# Put the path for your ChromeDriver here
<<<<<<< HEAD
DRIVER_PATH = 'C:/Users/justi/OneDrive/Desktop/secret sauce/programming/Image-Scrapper-Base/chromedriver'
wd = webdriver.Chrome(executable_path=DRIVER_PATH)

search_term = 'cryptopunks'
=======
DRIVER_PATH = '/Users/halfamotorcycle/Desktop/imageScrapped/chromedriver'
wd = webdriver.Chrome(executable_path=DRIVER_PATH)

search_term = 'pixel-cats'
>>>>>>> f91bc3b832797b976262e2a7af2dfdb4ed0827ee
search_and_download(search_term, DRIVER_PATH)
