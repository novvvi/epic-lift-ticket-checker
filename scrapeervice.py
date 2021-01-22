import requests as req
from selenium import webdriver
from selenium.webdriver.support.ui import Select 
from selenium.common.exceptions import NoSuchElementException
import time

class ScrapeService:
    driver = webdriver.Chrome()

    def scraperEpicLiftTicket(self):
        url = "https://www.wilmotmountain.com/api/LiftAccessApi/GetLiftTicketControlReservationInventory?startDate=01-23-2021&endDate=01-24-2021&_=1611326261550"

        headers = {
            "__requestverificationtoken": "IcnlfTKqKCyZHJdOL3F5Jor4jXoyHmRN0avX3t7YBrxNqUetizpb7hpQ9XKbsOplFnkqJ_VF-mzmBh5RTDjJLPwvGHc1:UUa6S5S7XVlo3KFHOCUHK1oGioQthk4uodWAys9QrW2soUBUACLYVcsItWQyOSHxnZFXs08uux-fAW2hYLeZW7uDTzb4T-h6s4RVokslEBL37zQK0",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6",
            "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-queueit-ajaxpageurl": "https%3A%2F%2Fwww.wilmotmountain.com%2Fplan-your-trip%2Flift-access%2Ftickets.aspx%3FstartDate%3D01%252F25%252F2021%26numberOfDays%3D1%26ageGroup%3DAdult",
            "x-requested-with": "XMLHttpRequest"
        }   
        response = req.get(url, headers)
        data = response.headers
        return data

    def seleniumScraperEpicLiftTicket(self):
        try:
            self.driver.get('https://www.wilmotmountain.com/plan-your-trip/lift-access/tickets.aspx?startDate=01%2F23%2F2021&numberOfDays=1&ageGroup=Adult')
            time.sleep(2)
            value = self.driver.find_element_by_id('ticket0').get_attribute("aria-hidden")
            if value == 'true': return True
        except NoSuchElementException:
            return False
        

if __name__ == "__main__":
    service = ScrapeService()
    print(service.seleniumScraperEpicLiftTicket())