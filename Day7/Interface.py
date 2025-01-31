from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod
    def send(self):
        pass

class Email(Mail):
    def send(self):
        print("Email sent")

class SMS(Mail):
    def send(self):
        print("SMS sent")

class WhatsApp(Mail):
    def send(self):
        print("WhatsApp message sent")

email = Email()
sms = SMS()
whatsapp = WhatsApp()

email.send()
sms.send()
whatsapp.send()