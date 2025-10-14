import tkinter

window = tkinter.Tk()
window.title("Miles to KM Convertor")
window.minsize(width=200, height=200)
window.config(padx=50,pady=50 )

#label
label1 = tkinter.Label(text="Miles")
label1.grid(row=0,column=2)

label2 = tkinter.Label(text="is equal to")
label2.grid(row=1,column=0)

label3 = tkinter.Label(text="Km")
label3.grid(row=1,column=2)

#Entry
entry = tkinter.Entry(width=7)
entry.grid(row=0,column=1)

#Button

def convertor():
    KM_value = float(entry.get()) * 1.60934
    label4 = tkinter.Label(text=f"{KM_value}")
    label4.grid(row=1,column=1)

button = tkinter.Button(text="Calculate", command =convertor)
button.grid(row=2,column=1)




window.mainloop()