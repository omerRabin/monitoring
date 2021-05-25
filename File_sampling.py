import copy
from time import sleep
from Samp import Samp


class File_sampling:
    def __init__(self, sleep_val: int):
        self.serviceList = open('serviceList.txt', 'a')
        self.Status_Log = open('Status_Log.txt', 'a')
        self.serviceList.close()
        self.Status_Log.close()
        self.sleep_val = sleep_val
        self.previous = None
        self.new = None

    def set_file_service(self):
        self.serviceList = open('serviceList.txt', 'a')
        if self.previous is None:
            self.new = Samp()
        if self.previous is not None:
            if self.new.seconds != self.previous.seconds:
                self.serviceList.write(self.new.sample)
        else:
            self.serviceList.write(self.new.sample)
        self.serviceList.close()

    def set_file_log(self):
        self.Status_Log = open('Status_Log.txt', 'a')
        if self.previous is None:
            self.previous = copy.copy(self.new)
            return
        self.previous = copy.copy(self.new)
        sleep(self.sleep_val)
        self.new = Samp()
        difer = "The differences between that sample: \n"
        difer += self.new.s_date + "\n"
        difer += self.new.s_hour + "\n"
        difer += "to that sample: \n"
        difer += self.previous.s_date + "\n"
        difer += self.previous.s_hour + "\n"
        exist = False
        for i in self.new.e_set:
            if i not in self.previous.e_set:
                difer += i + "new process as been created\n"
                exist = True
        for i in self.previous.e_set:
            if i not in self.new.e_set:
                difer += i + " process as been stop\n"
                exist = True
        if exist is False:
            difer += "They are the same\n"
        difer += "\n"
        self.Status_Log.write(difer)
        self.Status_Log.close()
        return

    def compare_two_stamps(self, first_stamp: str, second_stamp: str) -> str:
        list_stamp1 = first_stamp.split("\n")
        list_stamp2 = second_stamp.split("\n")
        list_stamp1_1 = []
        list_stamp2_1 = []
        for x in list_stamp1:
            if x != "" and x.find("date") < 0 and x.find("Hour") < 0:
                list_stamp1_1.append(x)
        for y in list_stamp2:
            if y != "" and y.find("date") < 0 and y.find("Hour") < 0:
                list_stamp2_1.append(y)
        difer = "The differences between the samples are: \n"
        exist = False
        for i in list_stamp2_1:
            if i not in list_stamp1_1:
                difer += i + "new process as been created\n"
                exist = True
        for i in list_stamp1_1:
            if i not in list_stamp2_1:
                difer += i + " process as been stop\n"
                exist = True
        if exist is False:
            difer += "They are the same\n"
        difer += "\n"
        print(difer)
        return difer
