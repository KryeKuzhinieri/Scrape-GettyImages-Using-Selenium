from selenium import webdriver
import urllib.request
import time
import os


def download_image(person_name, src, seq, dir):
    try:
        filename = person_name + str(seq) + '.png' # i.e: "JohnTravolta0.png"
        image_path = os.path.abspath(os.path.join(os.getcwd(), dir, filename)) # /home/user/Desktop/dirname
        urllib.request.urlretrieve(src, image_path) # download image
    
    except Exception:
        pass


def browse_page(person_name, pages, dir):
    seq = 0 #initialize the file number. 
    for i in range(pages): # Loop for the number of pages you want to scrape.
        try:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # Scroll to the end of page.
            time.sleep(2) # Wait for all the images to load correctly.
            images = driver.find_elements_by_xpath("//img[contains(@class, 'gallery-asset__thumb gallery-mosaic-asset__thumb')]") # Find all images.
        except:
            continue

        for image in images: # For each image in one page:
              try:
                src = image.get_attribute('src') # Get the link
                download_image(person_name, src, seq, dir) # And download it to directory
              except:
                pass
              seq += 1
        try:
          nextpage = driver.find_element_by_css_selector('.search-pagination__button-icon--next').click() # Move to next page
        except:
          pass
        time.sleep(2)
  
if __name__ == '__main__':
    person_name = input("Please Provide The Person's Name: \n") 
    url = input('Please Provide The Page URL: \n')
    dir = input('Please Provide The Directory Where The Data Will be Saved: \n')
    pages = int(input('Please Provide How Many Pages You Want To Be Scrapped: \n'))
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url)
    if not os.path.isdir(dir): # If the folder does not exist in working directory, create a new one.
        os.makedirs(dir)
    browse_page(person_name, pages, dir)

			