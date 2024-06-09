import tkinter


def swap_image(is_on: bool, label: tkinter.Label, path_to_on: str, path_to_off: str) -> bool:
    if is_on:
        is_on = False
        label.image = tkinter.PhotoImage(file=path_to_off)
        label.configure(image=label.image)
        label.pack()
    else:
        is_on = True
        label.image = tkinter.PhotoImage(file=path_to_on)
        label.configure(image=label.image)
        label.pack()
    return is_on
