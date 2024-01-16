from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

# Open the webpage
url = "https://nodarbibas.rtu.lv/"  # replace with the actual URL
driver.get(url)
time.sleep(2)

# Find and print the text inside the <span> element with class "navbar-brand"
try:
    element = driver.find_element(By.CSS_SELECTOR, ".navbar-brand span")
    print("Text found:", element.text)
except Exception as e:
    print("Error:", e)

driver.quit()

# name = []
# program read information from people.csv file and put all data in name list.
# with open("people.csv", "r") as file:
#     next(file)
#     for line in file:
#         row = line.rstrip().split(",")
#         fullname = row[2] + " " + row[3]
#         name.append(fullname)

# Open the CRC32
# namecoded = []
# url = "https://emn178.github.io/online-tools/crc32.html"
# driver.get(url)
# time.sleep(2)

# for row in name:
#     find = driver.find_element(By.ID, "input")
#     find.send_keys(row)
#     time.sleep(0.05)  # Add a delay
#     code = driver.find_element(By.ID, "output").get_attribute("value")
#     namecoded.append(code)
#     find.clear()

# driver.quit()

# Read data from salary.xlsx
# personsalary = {}
# wb = load_workbook("salary.xlsx")
# ws = wb.active

# for i in range(2, ws.max_row + 1):
#     codedname = ws['A' + str(i)].value
#     salary = ws['B' + str(i)].value
#     if salary is not None:  # Check if salary is not None
#         personsalary[codedname] = personsalary.get(codedname, 0) + int(salary)

# # Display total salary
# for i, (fullname, codedname) in enumerate(zip(name, namecoded), start=1):
#     total_salary = personsalary.get(codedname, 0)
#     print(f"{i}. {fullname}: {total_salary}")