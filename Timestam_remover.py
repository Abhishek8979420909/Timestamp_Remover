import tkinter as tk
from tkinter import scrolledtext
import re

def remove_timestamps(script):
    # Regex pattern to match common timestamp formats (e.g., [00:00], 00:00:00, etc.)
    timestamp_pattern = r'\[?\b\d{1,2}:\d{2}(?::\d{2})?\b\]?'
    
    # Substitute the timestamps with an empty string
    cleaned_script = re.sub(timestamp_pattern, '', script)
    
    return cleaned_script.strip()

def process_text():
    # Get user input from the text area
    user_input = text_input.get("1.0", tk.END)  # Get all text from the text area
    cleaned_script = remove_timestamps(user_input)
    # Display the cleaned script in the output area
    text_output.delete("1.0", tk.END)  # Clear the previous output
    text_output.insert(tk.END, cleaned_script)

# Create the main window
window = tk.Tk()
window.title("Timestamp Remover")

# Create a text area for user input
text_input = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=15)
text_input.pack(padx=10, pady=10)

# Create a button to process the text
process_button = tk.Button(window, text="Remove Timestamps", command=process_text)
process_button.pack(pady=5)

# Create a text area to display the output
text_output = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=15)
text_output.pack(padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
