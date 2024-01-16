from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import matplotlib.pyplot as plt

def extract_lecture_data(driver, month):
    days_data = {}
    total_minutes_all_days = 0
    first_day_found = 0

    # Find all events (dates) containing lecture times
    event_containers = driver.find_elements(By.CLASS_NAME, "fc-daygrid-day-frame")

    for container in event_containers:
        # Extract date information
        try:
            date_element = container.find_element(By.XPATH, ".//div[contains(@class, 'fc-daygrid-day-top')]/a[contains(@class, 'fc-daygrid-day-number')]")
        except NoSuchElementException:
            # Skip the day if date element is not found
            continue
        # Check if first day
        if first_day_found == 0 and date_element.text.strip() != "1":
            continue
        # Check if first day is already found
        if first_day_found == 1 and date_element.text.strip() == "1":
            break
        if date_element.text.strip() == "1":
            first_day_found = 1
        
        date = date_element.text.strip()
        # print(f"Date ", date)

        # Extract lecture times for the day
        day_lectures = container.find_elements(By.XPATH, ".//div[contains(@class, 'fc-event-time') and contains(., ':')]")
        lecture_times = set()

        for event_time in day_lectures:
            time_str = event_time.text
            start_time_str, end_time_str = map(str.strip, time_str.split('-'))
            lecture_times.add((start_time_str, end_time_str))

        days_data[date] = lecture_times

    total_minutes_per_day = []
    # Calculate total minutes for each day
    print(f"{month}, papildus informācija:")
    for date, lecture_times in days_data.items():
        total_minutes = 0
        for start_time, end_time in lecture_times:
            start_minutes = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
            end_minutes = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])
            total_minutes += end_minutes - start_minutes
            total_minutes_all_days += total_minutes
        print(f"Minūtes {date} datumā: {total_minutes} minūtes")
        total_minutes_per_day.append(total_minutes)

    # Calculate total minutes for all days
    print(f"Minūtes pa visām dienām: {total_minutes_all_days} minūtes")
    # Graph
    dates = list(days_data.keys())
    plt.bar(dates, total_minutes_per_day)
    plt.xlabel('Datums')
    plt.ylabel('Minūtes')
    plt.title(month)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def click_next_month(driver):
    next_month_button = driver.find_element(By.CSS_SELECTOR, "button.fc-prev-button")
    next_month_button.click()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Example for multiple months
months = ["Maijs", "Aprīlis", "Marts", "Februāris", "Janvāris"]  # Should be passed to func to display month name in graph
first_month = "Jūnijs"
semester_id = "18"

semester_id = input("Enter the semester ID you'd like to view: ")
print(semester_id)


url = "https://nodarbibas.rtu.lv/"
driver.get(url)
time.sleep(1)

select_element = driver.find_element(By.ID, "semester-id")
select = Select(select_element)
select.select_by_value(semester_id)
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
time.sleep(2)
extract_lecture_data(driver, first_month)

for month in months:
    click_next_month(driver)
    time.sleep(2)
    extract_lecture_data(driver, month)


time.sleep(5)

driver.quit()
