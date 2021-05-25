from os import startfile
from tkinter import *
import threading
from Manual import Manual
from tkinter.filedialog import askopenfilename

import Samp
from Samp import Samp
from File_sampling import File_sampling

window = Tk()
name = StringVar()
window.title("The Monitor Of Omer And Itamar")

label1 = Label(window, text="Look At the last message at serviceList to view the differences", fg="black",
               font="Times 22",
               width=50)
label1.grid()
label1.grid_forget()
flag = True


def worker():
    sleep_Val = int(name.get())
    f_s = File_sampling(sleep_Val)
    while flag:
        f_s.set_file_service()
        f_s.set_file_log()


t1 = threading.Thread(target=worker)


def clickMe():
    t1.start()


def monitor_mode():
    if 'label1' in globals():
        label1.grid_remove()
    label = Label(window, text="Enter a few seconds for which each time the machine performs a service sampling")
    label.grid(column=0, row=2)
    x_sec = Entry(window, width=30, textvariable=name)
    x_sec.grid(column=0, row=4)
    button = Button(window, text="Click", command=clickMe)
    button.grid(column=0, row=5)


def worker2():
    date_hour_of_2_stamps = str(name.get())
    l = date_hour_of_2_stamps.split(",")
    firstparam = l[0]
    secondparam = l[1]
    m_m = Manual(firstparam, secondparam)
    stamp1 = m_m.closet_sampling_by_date(firstparam)
    stamp2 = m_m.closet_sampling_by_date(secondparam)
    f_s = File_sampling(0)
    # this function will return a string represent the difference file

    differ = f_s.compare_two_stamps(stamp1, stamp2)  # the output of this mode - convert to button open a txt file
    f = open("Status_Log.txt", "a")
    f.write(differ)
    f.close()
    if 'label1' in globals():
        label1.grid()


def click_me2():
    t = threading.Thread(target=worker2)
    if not t.is_alive():
        t.start()


def enter_date_and_hour():
    label = Label(window, text="Enter the first date&hour then ',' and then second date&hour to take a sampling ")
    label.grid(column=0, row=2)
    date_hour = Entry(window, width=30, textvariable=name)
    date_hour.grid(column=0, row=4)
    button = Button(window, text="Enter", command=click_me2)
    button.grid(column=0, row=5)


def manual_mode():
    global flag
    flag = False
    enter_date_and_hour()


def show_service_list():
    startfile(f"serviceList.txt")


def show_Status_log():
    startfile(f"Status_Log.txt")


def gui():
    # set window size
    window.geometry("1100x600")
    title = Label(window, text="welcome to our Monitoring software", bg="red", fg="white", font="Times 32",
                  width=40)
    title.grid()
    label1 = Label(window, text="Please select the monitor mode you want to turn on:", fg="black", font="Times 22",
                   width=50)
    label1.grid()

    # Creating a Button
    btn1 = Button(window, text='Monitor Mode', command=monitor_mode)

    # Creating a Button
    btn2 = Button(window, text='Manual Mode', command=manual_mode)

    # Set the position of button on the top of window.
    btn1.place(x=400, y=200)
    btn1.config(font=30)
    btn2.place(x=600, y=200)
    btn2.config(font=30)
    os_button = Button(window, text="Open service list", command=show_service_list)
    os_button.place(x=400, y=500)
    os_button.config(font=30)
    os_button2 = Button(window, text="Open Status Log", command=show_Status_log)
    os_button2.place(x=600, y=500)
    os_button2.config(font=30)
    window.mainloop()


def main():
    gui()


if __name__ == "__main__":
    main()
