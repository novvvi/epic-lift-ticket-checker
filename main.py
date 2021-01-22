from scrapeervice import ScrapeService
from msg import MSG as msg
import time

class Main:

    def __init__(self, cellnumber):
        self.service = ScrapeService()
        self.cellNumber = cellnumber
    
    def run(self):
        check = 1
        msg().text(self.cellNumber, "GOOGLE", "lift ticket 23 & 24 checker - do not rely")
        while True:
            res = self.service.scraperEpicLiftTicket()
            print(res)
            if res:
                if res[0]['Capacity'] > 0:
                    msg().text(self.cellNumber, "GOOGLE", "capacity: {}, www.wilmotmountain.com/plan-your-trip/lift-access/tickets.aspx?startDate=01%2F23%2F2021&numberOfDays=1&ageGroup=Adult".format(res[0]['Capacity']))
                if res[1]['Capacity'] > 0:
                    msg().text(self.cellNumber, "GOOGLE", "capacity: {}, www.wilmotmountain.com/plan-your-trip/lift-access/tickets.aspx?startDate=01%2F24%2F2021&numberOfDays=1&ageGroup=Adult".format(res[0]['Capacity']))
                if check % 6 == 0:
                    msg().text(self.cellNumber, "GOOGLE", "still running checking avaiability...")
            time.sleep(30)
            check += 1

    def seleniumRun(self):
        check = 1
        msg().text(self.cellNumber, "GOOGLE", "lift ticket 23 & 24 checker now LIVE - do not rely")
        while True:
            res = self.service.seleniumScraperEpicLiftTicket()
            if res:
                msg().text(self.cellNumber, "GOOGLE", "now availiable on 23")
                msg().text(self.cellNumber, "GOOGLE", "www.wilmotmountain.com/plan-your-trip/lift-access/tickets.aspx?startDate=01%2F23%2F2021&numberOfDays=1&ageGroup=Adult")
            if check % 20 == 0: # check if the script is running correctly
                msg().text(self.cellNumber, "GOOGLE", "still checking avaiability... 10 mins pass")
            time.sleep(30) # check every 30 sec
            check += 1

            
if __name__ == "__main__":
    Main("8001234567").seleniumRun()