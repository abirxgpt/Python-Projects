from tkinter import *
from requests import *

def get_quote():
    kanye_says = get("https://api.kanye.rest")
    kanye_says.raise_for_status()
    kanye_data = kanye_says.json()
    quote = kanye_data["quote"]
    if len(quote) > 50:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 20, "bold"))
    else:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 30, "bold"))



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
