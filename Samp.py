import datetime
import psutil


class Samp:
    def __init__(self):
        self.e_set = {"e_set"}
        self.year = datetime.date.today().year
        self.month = datetime.date.today().month
        self.date = datetime.date.today().day
        self.hour = datetime.datetime.now().hour
        self.minute = datetime.datetime.now().minute
        self.seconds = datetime.datetime.now().second
        self.s_date = "date: " + str(self.year) + "." + str(self.month) + "." + str(self.date) #set_s_date(self)
        self.s_hour = "Hour: " + str(self.hour) + ":" + str(self.minute) + ":" + str(self.seconds)
        for proc in psutil.process_iter():
            try:
                process_name = proc.name()
                self.e_set.add(process_name)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        samp = "\n========================================\n"
        samp += self.s_date +"\n" + self.s_hour + "\n"
        for i in self.e_set:
            samp += i + "\n"
        self.sample = samp
