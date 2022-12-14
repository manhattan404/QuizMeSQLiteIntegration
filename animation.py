import tkinter as tk

# Create the root window
root = tk.Tk()

# Create a canvas to draw on
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()

# Set up some initial values
rect_x = 0
rect_y = 0

# This function will be called repeatedly to update the position of the rectangle


def update_rectangle():
    global rect_x, rect_y

    # Clear the canvas
    canvas.delete("all")

    # Update the position of the rectangle
    rect_x += 1
    rect_y += 1

    # Draw the rectangle at its new position
    canvas.create_rectangle(rect_x, rect_y, rect_x + 50, rect_y + 50)

    # Schedule this function to be called again after 10 milliseconds
    root.after(10, update_rectangle)


# Schedule the first call to the update_rectangle() function
root.after(10, update_rectangle)

# Start the main event loop
root.mainloop()
