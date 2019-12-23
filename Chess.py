from threading import Thread
import os
import smtplib
from email.message import EmailMessage
import json
import requests
import urllib.request
from bs4 import BeautifulSoup

class EventNotifier:
    def __init__ (self, emails):
        self.emails = emails
        self.participants = {}
        self.tournaments = {}
        self.last_updated = ""
        self.domain = "http://chess-results.com/"
        self.data = []
        self.app_run = True
        self.appending = True
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

    def run (self):
        self.appending = False
        while self.app_run:
            #self.get_update()
            for url in self.participants:
                self.get_patricipant_update(url)
            for url in self.tournaments:
                self.tournament_update(url)

    def append_participant (self, url):
        player = {"name": "Unknown", "rating": "0", "points": "0", "rank": "0", "rd": "1"}

        r = requests.get(url)
        html_content = r.text

        soup = BeautifulSoup(html_content, "html.parser")

        data = soup.find("td", text="Name")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
                player["name"] = data[1].text

        data = soup.find("td", text="Rating")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
                player["rating"] = data[1].text

        data = soup.find("td", text="Points")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
                player["points"] = data[1].text

        data = soup.find("td", text="Rank")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
               player["rank"] = data[1].text

        data = soup.find_all("table", {"class": "CRs1"})
        if len(data) > 2:
            data = data[1]
            participant_tr = data.find_all("tr")
            if len(participant_tr) > 0:
                participant_tr = participant_tr[-1]
                participant = participant_tr.find_all("td")
                if len(participant) > 0:
                    player["rd"] = participant[0].text

        self.participants[url] = player

    def append_tournament (self, url):
        r = requests.get(url)
        html_content = r.text
        soup = BeautifulSoup(html_content, "html.parser")
        title = soup.find_all("div", {"id": "_ctl0_F7"})[0].find("h2")
        if title == None:
            title = "Unknown"
        else:
            title = title.text
        self.tournament_update(url, title)


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

    def get_patricipant_update (self, url):        
        r = requests.get(url)
        html_content = r.text

        soup = BeautifulSoup(html_content, "html.parser")

        data = soup.find("td", text="Rating")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
                if self.participants[url]["rating"] != data[1].text:
                    self.send_email("Rating ("+self.participants[url]["name"]+") was updated. New rating: "+data[1].text)
                    self.participants[url]["rating"] = data[1].text

        data = soup.find("td", text="Points")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
                if self.participants[url]["points"] != data[1].text:
                    self.send_email("Points ("+self.participants[url]["name"]+") was updated. New points: "+data[1].text)
                    self.participants[url]["points"] = data[1].text

        data = soup.find("td", text="Rank")
        if (data != None):
            data = data.find_parent("tr").find("td")
            if len(data) > 1:
               if self.participants[url]["rank"] != data[1].text:
                    self.send_email("Rank ("+self.participants[url]["name"]+") was updated. New rank: "+data[1].text)
                    self.participants[url]["rank"] = data[1].text

        data = soup.find_all("table", {"class": "CRs1"})
        if len(data) > 2:
            data = data[1]
            participant_tr = data.find_all("tr")
            if len(participant_tr) > 0:
                participant_tr = participant_tr[-1]
                participant = participant_tr.find_all("td")
                if len(participant) > 0:
                    if self.participants[url]["rd"] != participant[0].text:
                        self.send_email("Rd. ("+self.participants[url]["name"]+") was updated. New rd.: "+data[1].text)
                        self.participants[url]["rd"] = participant[0].text

    def check_tournament (self, link, title, data):
        for item in self.data:
            if item["link"] == link:
                update = False
                if item["data"][0][1] != data[0][1]:
                    if self.appending == False:
                        self.send_email("Tournament \""+title+"\" was updated. New tour started: "+data[0][1])
                    item["data"][0][1] = data[0][1]
                    item["data"][0][0] = data[0][0]
                    update = True
                if item["data"][1][0] != data[1][0]:
                    if self.appending == False:    
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
        for email in self.emails:
            msg['To'] = email
            s = smtplib.SMTP('localhost', 1025)
            s.send_message(msg)
        s.quit()
    
    def tournament_update (self, link, title):
        r = requests.get(link+"&zeilen=99999")
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