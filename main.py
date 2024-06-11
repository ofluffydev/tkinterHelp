import tkinter

from geometry_helper import generate_geometry
from image_helper import swap_image


# Function to update the image displayed on the label
def update_image():
    """
    This function is used to update the image displayed on the label.
    It calls the swap_image function from the image_helper module and updates the global variable is_on.
    """
    global is_on
    is_on = swap_image(is_on, label, path_to_on, path_to_off)


# Set the background color of the window
background_color = 'purple'
# Set the width of the window
window_width = 400
# Set the height of the window
window_height = 400
# Set the title of the window
window_title = "Purple space :3"

# Create a tkinter window
root = tkinter.Tk()
# Set the title of the window
root.title(window_title)

# Set the geometry of the window using the generate_geometry function from the geometry_helper module
root.geometry(generate_geometry(window_width, window_height))
# Set the background color of the window
root.configure(bg=background_color)

# Create a button with the text "Click me!" and a white background
button = tkinter.Button(root, text="Click me!", bg='white')
# Pack the button to the bottom of the window
button.pack(side='bottom')

# Initialize the is_on variable to True
is_on = True
# Set the path to the 'on' image
path_to_on = 'images/on.png'
# Set the path to the 'off' image
path_to_off = 'images/off.png'
# Create a PhotoImage object with the 'on' image
image = tkinter.PhotoImage(file=path_to_on)
# Create a label with the 'on' image and a background color matching the window's background color
label = tkinter.Label(root, image=image, bg=background_color)
# Pack the label to the window
label.pack()

# Set the command of the button to the update_image function
button['command'] = update_image

# Start the tkinter event loop
root.mainloop()
