import pyperclip
import time
import keyboard

class ClipboardCapitalizer:
    def __init__(self):
        self.last_copied_text = ""
        self.enabled = True
        
    def toggle(self):
        self.enabled = not self.enabled
        status = "ENABLED" if self.enabled else "DISABLED"
        print(f"Clipboard processing {status}")
        
    def process_clipboard(self):
        try:
            current_text = pyperclip.paste()
            if current_text and current_text != self.last_copied_text and \
               (not current_text.isupper() or '\n' in current_text or '\r' in current_text):
                if self.enabled:
                    processed_text = current_text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ').strip().upper()
                    pyperclip.copy(processed_text)
                    self.last_copied_text = processed_text
                    print(f"Processed text: {current_text} -> {processed_text}")
                else:
                    self.last_copied_text = current_text
        except Exception as e:
            print(f"Error processing clipboard: {e}")

    def start(self):
        print("Clipboard capitalizer started. Press HOME to toggle processing.")
        print("Press CTRL+C to exit.")
        
        # Register global hotkey for Home key
        keyboard.add_hotkey('home', self.toggle)

        try:
            while True:
                self.process_clipboard()
                time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nScript stopped.")
        finally:
            keyboard.unhook_all()

if __name__ == "__main__":
    capitalizer = ClipboardCapitalizer()
    capitalizer.start()