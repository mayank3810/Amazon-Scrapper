from selenium import webdriver
from time import sleep
import xlsxwriter


##### Change Database Name Here Here ###

workbook = xlsxwriter.Workbook('Product_Database_Durgapuja.csv')


#***************************************
worksheet = workbook.add_worksheet('Product_database')
worksheet.write('A1', 'Product Url')
worksheet.write('B1', 'Product Name')
worksheet.write('C1', 'Image Url')
worksheet.write('D1', 'Categorie')


####### Change Website Seeded Here #####

website = "https://www.amazon.in/s?k=durga+puja+decoration+items&crid=2L3AYDUA16SS2&sprefix=Durga+Puja+De%2Caps%2C364&ref=nb_sb_ss_ts-a-p_1_13"


#***************************************
ref_link ="""&tag=festivalkart2-21"""
driver = webdriver.Chrome(executable_path='./Drivers/chromedriver')
driver.get(website)
sleep(3)
def fetch_data(number):
    counter = 0
    data = []
    firstResult = driver.find_elements_by_css_selector('div[data-component-type="s-search-result"]')
    sleep(2)
    for j in range(1, len(firstResult)):
        if firstResult[j].find_element_by_class_name('a-link-normal'):
            url_tag = firstResult[j].find_element_by_class_name('a-link-normal')
            name_tag = firstResult[j].find_element_by_class_name('a-text-normal')
            image_tag = firstResult[j-1].find_element_by_class_name('s-image-square-aspect')
            image_final = image_tag.find_element_by_xpath('./following::img')
            data = url_tag.get_attribute('href')
            final_name = name_tag.get_attribute('text').strip()
            image = image_final.get_attribute('srcset')
            head, sep, tail = image.partition('2.5x, ')
            final_image, sep2, tail2 = tail.partition('3x')
            final_product = data + ref_link


            ####### Change Categorie Here ##########

            worksheet.write(number,3,'Durga Puja')
            
            #***************************************
            worksheet.write(number,2,final_image)
            worksheet.write(number,1,final_name)
            worksheet.write(number,0,final_product)
            number = number + 1
            counter = counter + 1
        else:
            print('Out of Object')
    print('Product Fetched',counter)
    return counter
print('First Page')
count1 = fetch_data(1)
sleep(2)
driver.find_element_by_class_name('a-last').click()
sleep(5)



####### Add Pages Here #######

print('Second Page')
count2 = fetch_data(count1)
count3 = count1 + count2
print('Third Page')
count4 = fetch_data(count3)
count5 = count3 + count4
print('Fourth Page')
count6 = fetch_data(count5)
count7 = count5 + count6
print('Fifth Page')
count8 = fetch_data(count7)
count9 = count7 + count8
print('Total Product Fetched ',count9)

#****************************************
workbook.close()