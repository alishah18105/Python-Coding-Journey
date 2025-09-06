import pyautogui
import pyperclip
import time
from pynput import mouse

# Step 1: Click browser icon (always same place)
pyautogui.click(508, 751)  # your browser icon coordinates
time.sleep(2)

print("👉 Browser opened. Now drag to select text in the browser.")
print("   When you release the mouse button, the text will be copied & saved.\n")

def on_click(x, y, button, pressed):
    if not pressed:  
        # Step 2: Copy selected text
        pyautogui.hotkey("ctrl", "c")
        time.sleep(1)

        # Step 3: Retrieve text
        text = pyperclip.paste()
        print("\n✅ Copied text:\n")
        print(text)

        # Step 4: Save to file
        with open("output.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

        return False  # stop listener after one copy

# Listen for mouse release
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
