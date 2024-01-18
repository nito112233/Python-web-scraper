from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import matplotlib.pyplot as plt
import re

# Extract the month string
def extract_month(date_str):
    # Regex to find month
    match = re.search(r"gada \d+\. (\w+)", date_str)
    if match:
        return match.group(1)
    return None

# Check if user input is correct
def check_input():
    print("Lūdzu, ievadiet semestri, kuru vēlaties apskatīties- 1 vai 2 vai 3")
    print("1 -Rudens semestris 2023/2024, 2 -Pavasara semestris 2023/2024, 3 -Rudens semestris 2023/2024")
    user_input = input()
    if user_input in ["1", "2", "3"]:
        return user_input
    else:
        print("Kļūdaina ievade")
        return check_input()

# Extracts data and creates graph
def extract_lecture_data(driver, month):
    days_data = {}
    total_minutes_all_days = 0

    # Find all events (dates) containing lecture times
    event_containers = driver.find_elements(By.CLASS_NAME, "fc-daygrid-day-frame")

    for container in event_containers:
        # Extract date information
        try:
            date_element = container.find_element(By.XPATH, ".//div[contains(@class, 'fc-daygrid-day-top')]/a[contains(@class, 'fc-daygrid-day-number')]")
        except NoSuchElementException:
            # Skip the day if date element is not found
            continue

        date_str = date_element.get_attribute("aria-label")

        # Extract the month name
        month_str = extract_month(date_str)

        # Check if its correct month
        if month_str != month.lower():
            continue

        date = date_element.text.strip()

        # Extract lecture times for the day
        day_lectures = container.find_elements(By.XPATH, ".//div[contains(@class, 'fc-event-time') and contains(., ':')]")
        lecture_times = set()

        for event_time in day_lectures:
            time_str = event_time.text
            start_time_str, end_time_str = map(str.strip, time_str.split('-'))
            lecture_times.add((start_time_str, end_time_str))

        days_data[date] = lecture_times

    total_minutes_per_day = []
    print(f"{month}, papildus informācija:")

    # Calculate total minutes for each day
    for date, lecture_times in days_data.items():
        total_minutes = 0

        for start_time, end_time in lecture_times:
            start_minutes = int(start_time.split(':')[0]) * 60 + int(start_time.split(':')[1])
            end_minutes = int(end_time.split(':')[0]) * 60 + int(end_time.split(':')[1])
            total_minutes += end_minutes - start_minutes

        # Add to total monutes
        total_minutes_all_days += total_minutes
        print(f"Minūtes {date} datumā: {total_minutes} minūtes")
        total_minutes_per_day.append(total_minutes)

    # Calculate total minutes for all days
    print(f"Minūtes pa visām dienām: {total_minutes_all_days} minūtes")
    total_minutes = total_minutes_all_days
    hours = total_minutes // 60
    minutes = total_minutes % 60
    # Check if hours ends with 1 for correct spelling
    if hours % 10 == 1 and hours % 100 != 11:
        hours_suffix = "a"
    else:
        hours_suffix = "as"

    # Check if minutes ends with 1 for correct spelling
    if minutes % 10 == 1 and minutes % 100 != 11:
        minutes_suffix = "e"
    else:
        minutes_suffix = "es"
    # Graph
    dates = list(days_data.keys())
    plt.bar(dates, total_minutes_per_day)
    plt.xlabel('Datums')
    plt.ylabel('Minūtes')
    plt.title(f"{month}, kopā: {hours} stund{hours_suffix}, {minutes} minūt{minutes_suffix}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Clicks next month button
def click_next_month(driver):
    next_month_button = driver.find_element(By.CSS_SELECTOR, "button.fc-prev-button")
    next_month_button.click()

# Check if input is ok
user_input = check_input()

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://nodarbibas.rtu.lv/"
driver.get(url)
time.sleep(1)

# User input options
if user_input == "1":
    months = ["Decembris", "Novembris", "Oktobris", "Septembris"]
    first_month = "Janvāris"
    semester_id = "20"
elif user_input == "2":
    months = ["Maijs", "Aprīlis", "Marts", "Februāris", "Janvāris"]
    first_month = "Jūnijs"
    semester_id = "18"
elif user_input == "3":
    months = ["Decembris", "Novembris", "Oktobris", "Septembris"]
    first_month = "Janvāris"
    semester_id = "17"

# Pick semester
select_element = driver.find_element(By.ID, "semester-id")
select = Select(select_element)
select.select_by_value(semester_id)
time.sleep(1)

# Click to open study programn dropdown
dropdown_button = driver.find_element(By.XPATH, "//button[@data-id='program-id']")
dropdown_button.click()

# Wait for course number to show up
dropdown_options = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//a[@class='dropdown-item opt' and .//span[text()='Informācijas tehnoloģija (RDBI0)']]"))
)
# Pick study programn
dropdown_option = driver.find_element(By.XPATH, "//a[@class='dropdown-item opt' and .//span[text()='Informācijas tehnoloģija (RDBI0)']]")
dropdown_option.click()
time.sleep(1)

# Pick course number
select_element_course = driver.find_element(By.ID, "course-id")
select_course = Select(select_element_course)
select_course.select_by_value("1")
time.sleep(1)

# Pick group
select_element_group = driver.find_element(By.ID, "group-id")
select_group = Select(select_element_group)
select_group.select_by_visible_text("1")
time.sleep(3)
extract_lecture_data(driver, first_month)

# Ittarate over months
for month in months:
    click_next_month(driver)
    time.sleep(3)
    extract_lecture_data(driver, month)


time.sleep(1)

driver.quit()
