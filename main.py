import os, sys, subprocess
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

label1 = Label(window, text="Look At the last message at Status_Log.txt to view the differences", fg="Blue",
               font="Times 22",
               width=50)
label1.grid()
label1.grid_forget()
flag = True

date_hour1_var = StringVar()
date_hour1_var.set("")
date_hour1 = Entry(window, text=date_hour1_var)
date_hour1.grid(column=0, row=2)
date_hour2_var = StringVar()
date_hour2_var.set("")
date_hour2 = Entry(window, text=date_hour2_var)
date_hour2.grid(column=0, row=3)

sleep_Val=100

def click_me2():
    t = threading.Thread(target=worker2)
    if not t.is_alive():
        t.start()

button1 = Button(window, text="Enter", command=click_me2)
button1.grid(column=0, row=6)
date_hour1.grid_remove()
date_hour2.grid_remove()
button1.grid_remove()
label = Label(window,
              text="Enter the first date&hour and then second date&hour to take a sampling in format '0000.00.00 00:00:00'-The earliest in the upper text box. You Must Choose a date with exactly the same day from the dates exists in the service list!")
label.grid(column=0, row=12)
label.grid_remove()


def clickMe():
    global sleep_Val
    sleep_Val = int(name.get())
    if not t1.is_alive():
        t1.start()
    else:
        global flag
        flag = True


label_x = Label(window, text="Enter a few seconds for which each time the machine performs a service sampling")
label_x.grid(column=0, row=2)
x_sec = Entry(window, width=30, textvariable=name)
x_sec.grid(column=0, row=4)
button = Button(window, text="Click", command=clickMe)
button.grid(column=0, row=5)
label_x.grid_remove()
x_sec.grid_remove()
button.grid_remove()


def worker():
    global sleep_Val
    sleep_Val = int(name.get())
    f_s = File_sampling(sleep_Val)
    while flag:
        f_s.set_sleep_val(sleep_Val)
        f_s.set_file_service()
        f_s.set_file_log()


t1 = threading.Thread(target=worker)


def monitor_mode():
    label.grid_remove()
    button1.grid_remove()
    date_hour1.grid_remove()
    date_hour2.grid_remove()
    if 'label1' in globals():
        label1.grid_remove()
    x_sec.grid()
    button.grid()
    label_x.grid()


# 2021.6.2 7:39:27
# 2021.6.2 7:39:39
def worker2():
    date_hour_of_first_stamp = str(date_hour1_var.get())
    date_hour_of_second_stamp = str(date_hour2_var.get())
    firstparam = date_hour_of_first_stamp
    secondparam = date_hour_of_second_stamp
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


def enter_date_and_hour():
    label.grid()


def manual_mode():
    global flag
    flag = False
    date_hour1.grid()
    date_hour2.grid()
    button1.grid()
    enter_date_and_hour()
    x_sec.grid_remove()
    label_x.grid_remove()
    button.grid_remove()


def show_service_list():
    if sys.platform == "win32":
        os.startfile(f"serviceList.txt")
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, "serviceList.txt"])


def show_Status_log():
    if sys.platform == "win32":
        os.startfile(f"Status_Log.txt")
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, "Status_Log.txt"])


def gui():
    # set window size
    window.geometry("1100x600")
    title = Label(window, text="welcome to our Monitoring software", bg="red", fg="white", font="Times 32",
                  width=40)
    title.grid(column=0, row=17)
    label1 = Label(window, text="Please select the monitor mode you want to turn on:", fg="black", font="Times 22",
                   width=50)
    label1.grid(column=0, row=20)

    # Creating a Button
    btn1 = Button(window, text='Monitor Mode', command=monitor_mode)

    # Creating a Button
    btn2 = Button(window, text='Manual Mode', command=manual_mode)

    # Set the position of button on the top of window.
    btn1.place(x=400, y=300)
    btn1.config(font=30)
    btn2.place(x=600, y=300)
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
