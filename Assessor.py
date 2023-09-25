import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
login = driver.get("http://market.theshortlistd.com/")
time.sleep(4)
a = driver.maximize_window()
time.sleep(2)
candidate_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nav[1]/div[1]/div[1]/div[2]/div[1]/label[1]").click()
time.sleep(2)
enter_mno = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("9110244192")
time.sleep(2)
get_otp = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
time.sleep(2)

otps = ['1', '2', '3', '4', '5', '6']
otp_paths = ['/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]', '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/input[1]', '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/input[1]', '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/input[1]', '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/div[1]/input[1]',
             '/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[6]/div[1]/input[1]']


# Loop through the OTP input fields and enter OTPs
try:
    for i in range(len(otps)):
        otp_field = driver.find_element(By.XPATH, value=otp_paths[i])
        otp_field.send_keys(otps[i])
        time.sleep(1)

except Exception as e:
    print(f"An error occurred: {str(e)}")

time.sleep(2)

verify_otp = driver.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/button[1]").click()
time.sleep(10)
login_success_popup = driver.find_element(By.XPATH,"/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/button[1]").click()
time.sleep(2)

verify_date_and_time = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[2]/b[1]")

try:
    find_names = driver.find_element(*verify_date_and_time)
    verify_date_and_time = find_names.text.strip()
    if verify_date_and_time:
        print(f"1.The '{verify_date_and_time}' pop up is displayed")
        if verify_date_and_time == '25-Sep-2023 10:00':
            print('1.Date and time is same as scheduled by assesor ')
        else:
            print('1.Date and time is not same as scheduled by the assesor')
    else:
        print(f"1.The'{verify_date_and_time}'pop up is not displayed")
except Exception as e:
    print(f"An error occurred: {str(e)}")