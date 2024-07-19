from tkinter import *

window = Tk()
window.title("Dollars($) to Rupees(₹) Converter")
window.config(padx=20,pady=20)

# Labels
label_dollar = Label(text="Dollars")
label_dollar.grid(column=2,row=0)

label_rupee = Label(text="Rupees")
label_rupee.grid(column=2,row=1)

label_value = Label(text="0")
label_value.grid(column=1,row=1)

label_equals_to = Label(text="is equals to")
label_equals_to.grid(column=0,row=1)


# Buttons
def currency_dollars():
    values = float(inputs.get())
    converted = round(values * 83.74, 2)
    label_value.config(text=converted)



new_button = Button(text="Calculate", command=currency_dollars)
new_button.grid(column=1,row=2)


# Entry
inputs = Entry(width=10)
inputs.grid(column=1,row=0)




window.mainloop()
