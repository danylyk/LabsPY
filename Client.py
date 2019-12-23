from Chess import EventNotifier

if __name__ == "__main__":
    emails = ["webdvitaly@gmail.com", "web.vitaly@rambler.ru"]
    notifier = EventNotifier(emails)
    notifier.append_participant("http://chess-results.com/tnr83447.aspx?lan=1&art=9&snr=23")
    notifier.append_participant("http://chess-results.com/tnr149322.aspx?lan=1&art=9&snr=118")
    notifier.append_tournament("http://chess-results.com/tnr219320.aspx?lan=1")
    notifier.run()