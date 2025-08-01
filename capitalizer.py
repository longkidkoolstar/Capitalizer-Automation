import pyperclip
import time

def capitalize_clipboard():
    last_copied_text = ""
    print("Clipboard Capitalizer is running...")
    print("Press Ctrl+C to stop.")

    while True:
        try:
            current_clipboard_text = pyperclip.paste()

            if current_clipboard_text and current_clipboard_text != last_copied_text:
                if current_clipboard_text != current_clipboard_text.upper():
                    capitalized_text = current_clipboard_text.upper()
                    pyperclip.copy(capitalized_text)
                    last_copied_text = capitalized_text
                    print(f"Capitalized: '{current_clipboard_text}' -> '{capitalized_text}'")
                else:
                    last_copied_text = current_clipboard_text # Update last_copied_text even if already capitalized
            
            time.sleep(0.1) # Check every 100 milliseconds

        except pyperclip.PyperclipException as e:
            print(f"Error accessing clipboard: {e}. Please ensure a copy/paste mechanism is available.")
            time.sleep(1) # Wait longer on error
        except KeyboardInterrupt:
            print("Clipboard Capitalizer stopped.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(1) # Wait longer on error

if __name__ == "__main__":
    capitalize_clipboard()