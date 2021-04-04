from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import csv_code as csv 
import download_XLS as xls 
import grafhmata_code as gr 

pressed5 = False
pressed6 = False
#set buttons actions call functions from script grafhmata_code
def buttonClick1():
    try:
        gr.grafhma_1()
    except:
        messagebox.showerror("Error", "Download XLS and creat CSVs first!")

def buttonClick2(cmb):
    try:
        if cmb.get() == "2011":
            gr.grafhma_2(2011)
        elif cmb.get() == "2012":
            gr.grafhma_2(2012)
        elif cmb.get() == "2013":
            gr.grafhma_2(2013)
        elif cmb.get() == "2014":
            gr.grafhma_2(2014)
        elif cmb.get() == "2015":
            gr.grafhma_2(2015)
        else:
            #show plot for all years
            gr.grafhma_2(-1)
    except:
        messagebox.showerror("Error", "Download XLS and creat CSVs first!")

def buttonClick3():
    try:
        gr.grafhma_3()
    except:
        messagebox.showerror("Error", "Download XLS and creat CSVs first!")

def buttonClick4():
    try:
        gr.grafhma_4()
    except:
        messagebox.showerror("Error", "Download XLS and creat CSVs first!")

def buttonClick5():
    global pressed5
    if not pressed5:
        xls.download_xls()
        messagebox.showinfo("Info", "Download successful")
        pressed5 = True
    else:
        messagebox.showerror("Error", "Already downloaded XLS")
    

def buttonClick6():
    global pressed6
    if not pressed6:
        csv.create_csv()
        messagebox.showinfo("Info", "Creation successful")
        pressed6 = True
    else:
        messagebox.showerror("Error", "Already created CSVs")
   




window = Tk()
window.geometry('600x450')
window.resizable(False, False)
window.title("GREEK TOURISM STATISTICS")

#titles for all buttons
# title1 = "ΣΥΝΟΛΙΚΕΣ ΑΦΙΞΕΙΣ ΣΤΗΝ ΕΛΛΛΑΔΑ\n ΓΙΑ ΤΗΝ ΠΕΝΤΑΕΤΙΑ 2011-2015"
# title2 = "10 ΠΡΩΤΕΣ ΧΩΡΕΣ ΚΑΤΑΓΩΓΗΣ \nΜΕ ΤΟ ΜΕΓΑΛΥΤΕΡΟ ΜΕΡΙΔΙΟ ΣΤΙΣ ΑΦΙΞΕΙΣ\n(ΕΠΙΛΟΓΗ ΕΤΟΥΣ)"
# title3 = "ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΣΤΗΝ ΕΛΛΑΔΑ \nΑΝΑ ΜΕΣΟ ΜΕΤΑΦΟΡΑΣ ΓΙΑ ΤΗΝ ΠΕΝΤΑΕΤΙΑ \n2011-2015"
# title4 = "ΑΦΙΞΕΙΣ ΤΟΥΡΙΣΤΩΝ ΣΤΗΝ ΕΛΛΑΔΑ \nΑΝΑ ΤΡΙΜΗΝΟ ΓΙΑ ΤΗΝ ΠΕΝΤΑΕΤΙΑ \n2011-2015"
# title5 = "ΛΗΨΗ ΤΩΝ ΑΠΑΙΤΟΥΜΕΝΩΝ XLS"
# title6 = "ΔΗΜΙΟΥΡΓΙΑ ΑΠΑΡΑΙΤΗΤΩΝ CSVs"
title1 = "TOTAL ARRIVALS IN GREECE\n FROM 2011 TO 2015"
title2 = "10 FIRST COUNTRIES \n WITH THE BIGGEST NUMBER OF ARRIVALS \n(CHOOSE YEAR)"
title3 = "ARRIVALS OF TOURISTS IN GREECE \n BY MEANS OF TRANSPORT 2011-2015"
title4 = "ARRIVALS OF TOURISTS IN GREECE \n PER QUARTER 2011-2015"
title5 = "DOWNLOAD NEEDED XLS"
title6 = "CREATE NEEDED CSVs"


#button placement 
btn1 = Button(window, text=title1, bg="black", fg="cyan", width=200, height=200, font=("Arial",10,"bold"), command=buttonClick1)
btn1.place(x = 0, y = 0, width = 300, height = 150)

#set button 2 and combo box for year choice
combo = ttk.Combobox(window, state="readonly", values=(2011, 2012, 2013, 2014, 2015, "ALL YEARS"))
combo.current(5) #set the selected item
combo.place(x = 300, y = 130, width = 300, height = 20)
btn2 = Button(window, text=title2, bg="black", fg="cyan", font=("Arial",10,"bold"), command=lambda : buttonClick2(combo))
btn2.place(x = 300, y = 0, width = 300, height = 130)


btn3 = Button(window, text=title3, bg="black", fg="cyan", font=("Arial",10,"bold"), command=buttonClick3)
btn3.place(x = 0, y = 150, width = 300, height = 150)

btn4 = Button(window, text=title4, bg="black", fg="cyan", font=("Arial",10,"bold"), command=buttonClick4)
btn4.place(x = 300, y = 150, width = 300, height = 150)

btn5 = Button(window, text=title5, bg="green", fg="black", font=("Arial",10,"bold"), command=buttonClick5)
btn5.place(x = 0, y = 300, width = 300, height = 150)

btn6 = Button(window, text=title6, bg="green", fg="black", font=("Arial",10,"bold"), command=buttonClick6)
btn6.place(x = 300, y = 300, width = 300, height = 150)


window.mainloop()