from customtkinter import CTk, set_default_color_theme
from tkdevin.tkin import DTk


class CDTk(CTk, DTk):
    pass


if __name__ == '__main__':
    root = CDTk()
    if not root.wm_is_mark_id("devin"):
        root.wm_mark_id("devin", {})
    root.wm_mark_size("devin")
    root.mainloop()