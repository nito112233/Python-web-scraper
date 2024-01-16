from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://nodarbibas.rtu.lv/"
driver.get(url)
time.sleep(1)

select_element = driver.find_element(By.ID, "semester-id")
select = Select(select_element)
select.select_by_value("18")

time.sleep(0.5)

dropdown_button = driver.find_element(By.XPATH, "//button[@data-id='program-id']")
dropdown_button.click()

dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[@class='dropdown-item opt' and .//span[text()='Informācijas tehnoloģija (RDBI0)']]"))
)

dropdown_option = driver.find_element(By.XPATH, "//a[@class='dropdown-item opt' and .//span[text()='Informācijas tehnoloģija (RDBI0)']]")
dropdown_option.click()

time.sleep(0.5)

select_element_course = driver.find_element(By.ID, "course-id")
select_course = Select(select_element_course)
select_course.select_by_value("1")

time.sleep(0.5)

select_element_group = driver.find_element(By.ID, "group-id")
select_group = Select(select_element_group)
select_group.select_by_visible_text("1")

time.sleep(1)

event_times = driver.find_elements(By.XPATH, "//div[@class='fc-event-time' and contains(., ':')]")
lecture_times = set()  # To store unique lecture times
previous_time = None

for event_time in event_times:
    time_str = event_time.text
    start_time_str, end_time_str = map(str.strip, time_str.split('-'))
    print(f"T: {start_time_str}-{end_time_str}")

    current_time = (start_time_str, end_time_str)

    if current_time != previous_time:  # Check for duplicates
        start_time = time.strptime(start_time_str, '%H:%M')
        end_time = time.strptime(end_time_str, '%H:%M')
        lecture_times.add((start_time, end_time))

    previous_time = current_time

total_minutes = 0

for start_time, end_time in lecture_times:
    # print(f"S: {start_time.tm_hour}:{start_time.tm_min}")
    # print(f"E: {end_time.tm_hour}:{end_time.tm_min}")
    
    start_minutes = start_time.tm_hour * 60 + start_time.tm_min
    end_minutes = end_time.tm_hour * 60 + end_time.tm_min
    print(f"Total minutes: {total_minutes}")
    total_minutes += end_minutes - start_minutes

print(f"Total minutes for lectures: {total_minutes} minutesssss")

time.sleep(2)

driver.quit()



driver.quit()
