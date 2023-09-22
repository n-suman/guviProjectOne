from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import msedgedriver
import time

msedgedriver.install()

# Initialize the Edge Webdriver
driver = webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")


# Get the value entered in the password field
act_pwd = driver.find_element(By.NAME, "password").get_attribute("value")
exp_pwd="admin123"

if act_pwd == exp_pwd:
    print("Login Successfully")
else:
    print("Invalid user ")

driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

# Navigate to PIM module
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span").click()

# Fill in employee details
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input").send_keys("Disha")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("110022")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[1]/button/i").click()


# Wait for a moment to see the result
time.sleep(3)

# Search for the newly added employee
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button/i").click()
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div").send_keys("Disha Sharma")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()

# Wait for search results
time.sleep(2)

# Verify if the employee exists in the search results
search_results = driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr")
if len(search_results) > 0:
    print("Employee added successfully!")
else:
    print("Employee not found in the search results.")

    time.sleep(2)

# Click the checkbox of the employee to be deleted
driver.find_element(By.XPATH, "input[id*='chkSelectRecord']").click()

# Click the "Delete" button
driver.find_element(By.ID, "btnDelete").click()

# Confirm the deletion in the popup
driver.switch_to.alert.accept()

# Wait for a moment to see the result
time.sleep(2)

# Verify successful deletion message
success_message = driver.find_element(By.ID, "deleteConfModal").text
if "Successfully Deleted" in success_message:
    print("Employee deleted successfully!")
else:
    print("Employee deletion failed.")

# Close the browser
driver.close()