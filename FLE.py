from tkinter import *
windows = Tk()
app_width = 760
app_height = 400
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()
mainxaxis = (screen_width / 2) - (app_width / 2)
mainyaxis = (screen_height / 2) - (app_height / 2)
windows.geometry(f"{app_width}x{app_height}+{int(mainxaxis)}+{int(mainyaxis)}")
windows.mainloop()
