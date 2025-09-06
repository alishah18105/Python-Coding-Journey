from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:  # when mouse button is pressed
        print(f"Mouse clicked at ({x}, {y})")

# Start listening for mouse events
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
