from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def scrap_cas(email, password):
    sleep(5)
    driver = webdriver.Remote(
        command_executor="http://selenium:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME
    )

    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get('https://camsonline.com')
    # driver.fullscreen_window()

    driver.implicitly_wait(10)
    # submit_button = driver.find_element(By.ID, 'mat-radio-2-input')

    # select submit button
    submit_button = driver.find_element(By.ID, 'mat-radio-2')
    submit_button.click()

    # select proceed button
    proceed_button = driver.find_element(By.CSS_SELECTOR, 'input.check-now-btn.mr-right')
    proceed_button.click()

    driver.implicitly_wait(10)

    # select transaction container
    select_transaction = driver.find_element(By.XPATH,
                                             '/html/body/app-root/div/app-homeinv/div[3]/div[2]/div[2]/div/div/a/span')

    select_transaction.click()

    # select cas container
    driver.implicitly_wait(10)
    select_cas = driver.find_element(By.XPATH, '/html/body/app-root/div/app-investtransact/div[2]/div/div[1]/div')
    select_cas.click()

    # select detailed radio button
    driver.implicitly_wait(10)
    select_detailed = driver.find_element(By.XPATH, '//*[@id="mat-radio-6"]/label/div[1]')
    select_detailed.click()

    # select specific period
    driver.implicitly_wait(10)
    select_specific_period = driver.find_element(By.XPATH, '//*[@id="mat-radio-14"]/label/div[1]')
    select_specific_period.click()

    # select the date picker
    driver.implicitly_wait(10)
    select_date = driver.find_element(By.CSS_SELECTOR, 'span.mat-button-wrapper')
    select_date.click()

    # select year and month option
    driver.implicitly_wait(10)
    select_year_and_month_picker = driver.find_element(By.XPATH,
                                                       '//*[@id="mat-datepicker-1"]'
                                                       '/mat-calendar-header/div/div/button[1]/span')
    select_year_and_month_picker.click()
    # select_year_and_month.send_keys('01-JAN-1990')

    driver.implicitly_wait(10)
    select_year_and_month = driver.find_element(By.XPATH,
                                                '//*[@id="mat-datepicker-1"]/'
                                                'div/mat-multi-year-view/table/tbody/tr[6]/td[3]/div')
    select_year_and_month.click()

    while 1:
        # select the fist value in the year list
        driver.implicitly_wait(10)
        select_text = driver.find_element(By.XPATH, '//*[@id="mat-datepicker-1"]/div/'
                                                    'mat-multi-year-view/table/tbody/tr[1]/td[1]/div')
        # if year > 1990 click prev arrow and continue
        if select_text.text and int(select_text.text) > 1990:
            select_next = driver.find_element(By.XPATH,
                                              '//*[ @id="mat-datepicker-1"]/mat-calendar-header/div/div/button[2]')
            select_next.click()


        else:
            driver.implicitly_wait(10)
            # if year < 1990 select the year 1990
            select_year = driver.find_element(By.XPATH,
                                              '//*[@id="mat-datepicker-1"]/'
                                              'div/mat-multi-year-view/table/tbody/tr[6]/td[3]/div')
            select_year.click()

            # select the jan month
            driver.implicitly_wait(10)
            select_month = driver.find_element(By.XPATH,
                                               '//*[@id="mat-datepicker-1"]/'
                                               'div/mat-year-view/table/tbody/tr[2]/td[1]/div')
            select_month.click()

            # select date as 1
            driver.implicitly_wait(10)
            select_date = driver.find_element(By.XPATH,
                                              '//*[@id="mat-datepicker-1"]/div'
                                              '/mat-month-view/table/tbody/tr[2]/td[2]/div')
            select_date.click()
            break

    # select the folio radio button
    driver.implicitly_wait(10)
    select_folio = driver.find_element(By.XPATH, '//*[@id="mat-radio-8"]/label/div[1]')
    select_folio.click()
    select_folio.click()

    # select email field and enter the email id
    driver.implicitly_wait(10)
    insert_email = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
    insert_email.send_keys(email)

    # select the password field and enter the password
    driver.implicitly_wait(10)
    insert_password = driver.find_element(By.XPATH, '//*[@id="mat-input-2"]')
    insert_password.send_keys(password)

    # select the password field and enter the password
    driver.implicitly_wait(10)
    insert_conform_password = driver.find_element(By.XPATH, '//*[@id="mat-input-3"]')
    insert_conform_password.send_keys(password)

    driver.implicitly_wait(10)
    submit = driver.find_element(By.CLASS_NAME, 'check-now-btn')
    submit.click()

    driver.implicitly_wait(10)
    result = driver.find_element(By.XPATH,
                                 "/html/body/app-root/div/app-investtransact/div[2]/div/div[1]/div[2]/div/app-statements/div/div/div/h1").text
    return result


if __name__ == "__main__":
    scrap_cas('anil.kumar@ankhyainfinity.com', "15041989")
