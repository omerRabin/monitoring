import string
import datetime


class Manual:

    def __init__(self, timestamp_a, timestamp_b):
        self.timestamp_a = timestamp_a
        self.timestamp_b = timestamp_b
        self.year = datetime.date.today().year
        # self.month = datetime.date.today().month
        txt = open("serviceList.txt", 'r')
        self.file_split = str(txt.read()).split("========================================")
        print(self.file_split)
        self.file_stamp = []
        index = 0
        num = 0
        for i in self.file_split:
            if ":" in i or str(self.year) in i:
                self.file_stamp.append(i)

    # print(self.file_stamp)

    def devide_to_samplings(self):
        print(self.file_split)
        dict = {}
        for i in self.file_split:
            index1 = i.find("\ndate:")
            index2 = i.find("\nHour:")
            if index1 < 0 or index2 < 0:
                continue
            key1 = i[index1 + 7:index2]
            k = i.find("\n\n")  # the first occurrence of \n\n
            key2 = i[index2 + 6:k]
            date_and_hour = key1 + key2
            dict[date_and_hour] = i
        return dict

    def closet_sampling_by_hour(self, l: list, hour: str):
        hours = l
        now = datetime.datetime.strptime(hour, "%H:%M:%S")
        return min(hours, key=lambda t: abs(now - datetime.datetime.strptime(t, "%H:%M:%S")))

    def closet_sampling_by_date(self, date_and_hour: str):  # the format is 'date hour'
        date = (date_and_hour.split(" "))[0]
        hour = (date_and_hour.split(" "))[1]
        d = self.devide_to_samplings()
        l = []
        for k1 in d.keys():
            date_hour = k1.split(" ")
            if date_hour[0] == date:  # date is good
                l.append(date_hour[1])  # add the hours that their dates are good

        if len(l) == 0:
            return None
        close_hour = self.closet_sampling_by_hour(l, hour)
        the_key = date + " " + close_hour
        return d.get(the_key)


def main():
    # add the case if none from the date to do on another date
    date1 = "2021.5.24 18:32:40"
    date2 = "2021.5.24 18:38:43"
    file_stamp = Manual(date1, date2)
    # file_stamp.file_by_stamp()
    d = file_stamp.devide_to_samplings()
    print(d)
    s = file_stamp.closet_sampling_by_date(date1)
    print(s)


if __name__ == "__main__":
    main()
