
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

FORM_URL="https://forms.gle/nA58FfYgg35ty8hG8"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver=webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/Zillow-Clone/")

all_properties_links=driver.find_elements(By.CSS_SELECTOR, value=".StyledPropertyCardDataWrapper a")
# print(len(all_properties_links))
link_properties=[link.get_attribute("href") for link in all_properties_links]
# print(link_properties)
all_properties_prices=driver.find_elements(By.CLASS_NAME,value="PropertyCardWrapper__StyledPriceLine")

prices_properties=[]
for price in all_properties_prices:
    if "+" in price.text:
        final_price=price.text.split("+")[0]
        prices_properties.append(final_price)
    else:    
        final_price=price.text.split("/")[0]
        prices_properties.append(final_price)
# print(prices_properties)    
all_properties_addresses=driver.find_elements(By.CSS_SELECTOR, value=".StyledPropertyCardDataWrapper address")
addresses_properties=[address.text.replace("|","").strip() for address in all_properties_addresses]
print("Direcciones:", addresses_properties)
print("Precios:", prices_properties)
print("Links:", link_properties)

base_window=driver.window_handles[0]


for n in range(len(link_properties)):
    driver.execute_script("window.open('');")
    form_window=driver.window_handles[1]
    driver.switch_to.window(form_window)
    driver.get(FORM_URL)
    
    
    input_field_address=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_field_address.send_keys(addresses_properties[n])
    input_field_price=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_field_price.send_keys(prices_properties[n])
    input_field_link=driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_field_link.send_keys(link_properties[n])
    
    button_send=driver.find_element(By.CSS_SELECTOR,value=".lRwqcd div")
    button_send.click()
    driver.close()
    driver.switch_to.window(base_window)
    



driver.quit()