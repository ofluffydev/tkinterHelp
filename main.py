import tkinter

from geometry_helper import generate_geometry
from image_helper import swap_image


def update_image():
    global is_on
    is_on = swap_image(is_on, label, path_to_on, path_to_off)


background_color = 'purple'
window_width = 400
window_height = 400
window_title = "Purple space :3"

root = tkinter.Tk()
root.title(window_title)

root.geometry(generate_geometry(window_width, window_height))
root.configure(bg=background_color)

button = tkinter.Button(root, text="Click me!", bg='white')
button.pack(side='bottom')

is_on = True
path_to_on = 'images/on.png'
path_to_off = 'images/off.png'
image = tkinter.PhotoImage(file=path_to_on)
label = tkinter.Label(root, image=image, bg=background_color)
label.pack()

button['command'] = update_image

root.mainloop()
