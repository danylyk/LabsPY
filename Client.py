from Chess import EventNotifier

if __name__ == "__main__":
    emails = ["webdvitaly@gmail.com", "web.vitaly@rambler.ru"]
    notifier = EventNotifier(emails)
    notifier.run()