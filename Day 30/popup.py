import tkinter as tk


class Popup:
    def __init__(self, title:str="Popup", message:str="", master=None):
        if master is None:
            # If the caller didn't give us a master, use the default one instead
            master = tk._get_default_root()

        # Create a toplevel widget
        self.root = tk.Toplevel(master)
        # A min size so the window doesn't start to look too bad
        self.root.minsize(200, 40)
        # Stop the user from resizing the window
        self.root.resizable(False, False)
        # If the user presses the `X` in the titlebar of the window call
        # self.destroy()
        self.root.protocol("WM_DELETE_WINDOW", self.destroy)
        # Set the title of the popup window
        self.root.title(title)

        # Calculate the needed width/height
        width = max(map(len, message.split("\n")))
        height = message.count("\n") + 1
        # Create the text widget
        self.text = tk.Text(self.root, bg="#f0f0ed", height=height,
                            width=width, highlightthickness=0, bd=0,
                            selectbackground="orange")
        # Add the text to the widget
        self.text.insert("end", message)
        # Make sure the user can't edit the message
        self.text.config(state="disabled")
        self.text.pack()

        # Create the "Ok" button
        self.button = tk.Button(self.root, text="Ok", command=self.destroy)
        self.button.pack()

        # Please note that you can add an icon/image here. I don't want to
        # download an image right now.
        ...

        # Make sure the user isn't able to spawn new popups while this is
        # still alive
        self.root.grab_set()
        # Stop code execution in the function that called us
        self.root.mainloop()

    def destroy(self) -> None:
        # Stop the `.mainloop()` that's inside this class
        self.root.quit()
        # Destroy the window
        self.root.destroy()
