from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from GUI.weather import Ui_weather_info_selenium
import pandas as pd


class WeatherSearch:
    def __init__(self):
        self.city = str(input("Enter city name for which you want weather info:"))
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(f"https://www.accuweather.com/ro/search-locations?query={self.city}")
        self.my_weather_list = []

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Consent')]")))

            self.driver.find_element(By.XPATH, "//p[contains(text(),'Consent')]").click()
        except ValueError:
            print("Something went wrong here ...")
        try:
            WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "DAILY")))

            self.driver.find_element(By.LINK_TEXT, "DAILY").click()

        except ValueError:
            print("Something went wrong here ...")

        try:

            results = self.driver.find_elements(By.CLASS_NAME, "daily-forecast-card ")
            for result in results:
                day = result.find_element(By.XPATH, ".//span[@class='module-header dow date']").text
                date = result.find_element(By.XPATH, ".//span[@class='module-header sub date']").text
                high_temp = result.find_element(By.XPATH, ".//span[@class='high']").text
                low_temp = result.find_element(By.XPATH, ".//span[@class='low']").text
                print(day, date, high_temp, low_temp)
                results_dict = {"City": self.city,
                                "Day ": day,
                                "Date": date,
                                "Temp.Max": high_temp,
                                "Low.Temp": low_temp}
                self.my_weather_list.append(results_dict)
        finally:
            df = pd.DataFrame(self.my_weather_list)
            self.driver.quit()

    def get_data(self):
        df = pd.DataFrame(self.my_weather_list)
        return df

if __name__=="__main__":
    ws=WeatherSearch()