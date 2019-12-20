from threading import Thread
import os
import smtplib
from email.message import EmailMessage
import json
import requests
import urllib.request
from bs4 import BeautifulSoup

class EventNotifier:
    def __init__ (self):
        self.last_updated = ""
        self.domain = "http://chess-results.com/"
        self.data = []
        self.app_run = True
        self.data_update = False
        if os.path.isfile("data.dv"):
            with open('data.dv') as saved_data:
                self.data = json.load(saved_data)

        self.saveing_thread = Thread(target = self.saveing)
        self.saveing_thread.start()

    def saveing (self):
        while self.app_run:
            if self.data_update:
                self.save_data()

    def save_data (self):
        self.data_update = False
        with open('data.dv', 'w') as saved_data:
            json.dump(self.data, saved_data)
        print("Tournament updated - "+self.data[len(self.data)-1]["link"])

    def run (self):
        while self.app_run:
            self.get_update()

    def get_update (self):        
        r = requests.get(self.domain)
        html_content = r.text

        soup = BeautifulSoup(html_content, "html.parser")
        data = soup.find_all("table", {"class": "CRs2"})[0]
        trs = data.find_all("tr")
        updated = trs[1].find_all("td")[1]
        if self.last_updated != updated.text:
            self.last_updated = updated.text
            self.tournament_update(updated.find_all("a")[0]['href'], self.last_updated)

    def check_tournament (self, link, title, data):
        for item in self.data:
            if item["link"] == link:
                update = False
                if item["data"][0][1] != data[0][1]:
                    self.send_email("Tournament \""+title+"\" was updated. New tour started: "+data[0][1])
                    item["data"][0][1] = data[0][1]
                    item["data"][0][0] = data[0][0]
                    update = True
                if item["data"][1][0] != data[1][0]:
                    self.send_email("Tournament \""+title+"\" was updated. New participant added: "+data[1][1])
                    item["data"][1][0] = data[1][0]
                    item["data"][1][1] = data[1][1]
                    update = True
                if update:
                    self.data_update = True
                return
        self.data.append({"link": link, "title": title, "data": data})
        self.data_update = True

    def send_email (self, message):
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = f'Chess updates'
        msg['From'] = "danylyk@python.com"
        msg['To'] = "webdvitaly@gmail.com"
        s = smtplib.SMTP('localhost', 1025)
        s.send_message(msg)
        s.quit()
    
    def tournament_update (self, link, title):
        r = requests.get(self.domain+link+"&zeilen=99999")
        html_content = r.text

        soup = BeautifulSoup(html_content, "html.parser")
        data = soup.find("td", text="Board Pairings")
        tours = [None,None]
        if (data != None):
            data = data.find_parent("tr").find("td", {"class": "CR"}).find_all("a")
            rd = data[len(data)-2].text.split("/")[0]
            rd = rd[3:]
            tours = [data[len(data)-2]["href"], rd]
        team = [None,None]
        participant_tr = soup.find("table", {"class": "CRs1"})
        if participant_tr != None:
            participant_tr = participant_tr.find_all("tr")
            if len(participant_tr) > 0:
                participant_tr = participant_tr[-1]
                participant = participant_tr.find_all("td")
                if len(participant) > 0:
                    team[0] = participant[0].text
                name = participant_tr.find("a", {"class", "CRdb"})
                if name != None:
                    team[1] = name.text
                elif len(participant) > 2:
                    team[1] = participant[2].text
        self.check_tournament(link, title, [tours, team])

if __name__ == "__main__":
    notifier = EventNotifier()
    notifier.run()