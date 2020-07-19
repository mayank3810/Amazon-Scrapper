from selenium import webdriver
from time import sleep

ref_link ="""&tag=festivalkart2-21"""
####### Change Website Seeded Here #####

website = "https://www.amazon.in/GCT-Goddess-Sherawali-Dashboard-Showpiece/dp/B07DBR7V8Q/ref=sr_1_2?crid=2PMA6A1EWQQJE&dchild=1&keywords=durga+maa+murti&qid=1595094477&s=kitchen&sprefix=durg%2Ckitchen%2C422&sr=1-2"


#***************************************

# VARIABLES
image_url0 = []
image_url1 = []
image_url2 = []
image_url3 = []
image_url4 = []
image_url5 = []
image_url6 = []
image_url7 = []
image_url8 = []
image_url_all = []
driver = webdriver.Chrome(executable_path='./Drivers/chromedriver')
driver.get(website)
sleep(2)

# PROUDUCT URL

product_url = website + ref_link

#  PRODUCT NAME
product_tag = driver.find_element_by_id("productTitle")
product_name = product_tag.get_attribute('innerHTML').strip()

# AMAZON FULFILLED
try:
    driver.find_element_by_xpath('//*[@id="price-shipping-message"]/i')
    amazon_fulfilled = 'Yes'
except Exception:
    amazon_fulfilled = 'No'
# PRODUCT MRP
product_mrp_tag = driver.find_element_by_class_name('priceBlockStrikePriceString')
tail = product_mrp_tag.get_attribute('innerHTML').strip()
head, sep, product_mrp = tail.partition('₹&nbsp;')
# PRODUCT PRICE
try:
    product_price_tag = driver.find_element_by_id('priceblock_ourprice')
except Exception:
    product_price_tag = driver.find_element_by_id('priceblock_saleprice')
tail1 = product_price_tag.get_attribute('innerHTML').strip()
head1, sep1, product_price = tail1.partition('₹&nbsp;')
product_price.replace('₹&nbsp;','')

# EMI OPTION
try:
    driver.find_element_by_class_name('inemi-options-activate-popover')
    emi_option = 'EMI Option Avaliable'
except Exception:
    emi_option = 'EMI Option Not Avaliable'

# RATING STAR
head4 = driver.find_element_by_class_name('a-icon-alt').get_attribute('innerHTML')
product_rating, sep4, tail4 = head4.partition(' out')

# NUMBER OF REVIEWS
head5 = driver.find_element_by_id('acrCustomerReviewText').get_attribute('innerHTML') 
number_of_reviews, sep5, tail5 = head5.partition(' ratings')
number_of_reviews = number_of_reviews + 'Reviews'

# PRODUCT DESCRIPTION
product_description_final = []
product_descriptionl = driver.find_elements_by_xpath('//*[@id="feature-bullets"]/ul/li')
for i in range(0 , len(product_descriptionl)):
    product_descriptiont = product_descriptionl[i].find_element_by_class_name('a-list-item')
    product_description = product_descriptiont.get_attribute('innerHTML').strip()
    product_description_final.append(product_description)

# PRODUCT IMAGE
next_image = driver.find_elements_by_class_name('imageThumbnail')
for i in range(0,len(next_image)):
    next_image[i].click()
    sleep(0.2)
    print('Loop Executed')
for i in range(0,len(next_image)):
    if (i==0):
        image_url_list = driver.find_element_by_class_name("itemNo0")
        image_url_t1 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url0 = image_url_t1
    elif (i==1):
        image_url_list = driver.find_element_by_class_name("itemNo1")
        image_url_t2 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url1 = image_url_t2
    elif (i==2):
        image_url_list = driver.find_element_by_class_name("itemNo2")
        image_url_t2 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url2 = image_url_t2
    elif (i==3):
        image_url_list = driver.find_element_by_class_name("itemNo3")
        image_url_t3 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url3 = image_url_t3
    elif (i==4):
        image_url_list = driver.find_element_by_class_name("itemNo4")
        image_url_t4 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url4 = image_url_t4
    elif (i==5):
        image_url_list = driver.find_element_by_class_name("itemNo5")
        image_url_t5 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url5 = image_url_t5
    elif (i==6):
        image_url_list = driver.find_element_by_class_name("itemNo6")
        image_url_t6 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url6 = image_url_t6
    elif (i==7):
        image_url_list = driver.find_element_by_class_name("itemNo7")
        image_url_t7 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url7 = image_url_t7 
    elif (i==8):
        image_url_list = driver.find_element_by_class_name("itemNo8")
        image_url_t8 = image_url_list.find_element_by_tag_name('img').get_attribute('src')
        image_url8 = image_url_t8
image_url_all.append(image_url0)
image_url_all.append(image_url1)
image_url_all.append(image_url2)
image_url_all.append(image_url3)
image_url_all.append(image_url4)
image_url_all.append(image_url5)
image_url_all.append(image_url6)
image_url_all.append(image_url7)
image_url_all.append(image_url8)




# PRINTING TO CONSOLE
print(product_description_final)
print(image_url_all)
print(number_of_reviews)
print(product_rating)
print(emi_option)
print(product_url)
print(product_name)
print(amazon_fulfilled)
print(product_mrp)
print(product_price)



