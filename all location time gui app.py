import tkinter as tk
from datetime import datetime
import pytz  # This library is not included by default

# Function to get the current time in a specific timezone
def get_time(timezone_name):
  try:
    timezone = pytz.timezone(timezone_name)
    current_time = datetime.now(timezone)
    return current_time.strftime("%H:%M:%S %Z")  # Format the time string
  except pytz.UnknownTimeZoneError:
    return "Invalid Timezone"

# Function to update the time display
def update_time():
  # Get the selected timezone from the dropdown menu
  selected_timezone = timezone_var.get()
  current_time_str = get_time(selected_timezone)
  # Update the label text with the current time
  time_label.config(text=current_time_str)
  # Call this function again after 1 second to update the time
  root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("World Time")

# Create a label to display the current time
time_label = tk.Label(root, text="Time", font=("Arial", 20))
time_label.pack()

# Create a dropdown menu to select the timezone
timezone_var = tk.StringVar(root)
timezone_menu = tk.OptionMenu(root, timezone_var, *pytz.all_timezones)
timezone_menu.pack()

# Set the default timezone selection (optional)
timezone_var.set('US/Eastern')  # Replace with a valid timezone

# Create a button to start the time update
start_button = tk.Button(root, text="Start", command=update_time)
start_button.pack()

# Start the main event loop
root.mainloop()
