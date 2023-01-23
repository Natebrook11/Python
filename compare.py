import tkinter as tk
from tkinter import filedialog
import requests
import time

def compare_files(reference_file, file_list):
  # Read in reference file
  if reference_file.startswith('https://github.com'):
    reference_data = requests.get(reference_file).text
  else:
    with open(reference_file, 'r') as f:
      reference_data = f.read()

  # Compare each file to reference file
  for file in file_list:
    # Read in file
    start_time = time.perf_counter()
    if file.startswith('https://github.com'):
      file_data = requests.get(file).text
    else:
      with open(file, 'r') as f:
        file_data = f.read()
    end_time = time.perf_counter()

    # Compare file data to reference data
    num_same = sum(1 for c1, c2 in zip(file_data, reference_data) if c1 == c2)
    num_total = len(reference_data)
    percentage = 100.0 * num_same / num_total
    if file_data == reference_data:
      result_label.config(text=f"{file} is identical to {reference_file} ({percentage:.1f}% match). (Completed in {end_time - start_time:.2f} seconds)", fg='green')
    else:
      result_label.config(text=f"{file} is NOT identical to {reference_file} ({percentage:.1f}% match). (Completed in {end_time - start_time:.2f} seconds)", fg='red')

# Create main window
window = tk.Tk()
window.title("File Comparison Tool")

# Create widgets
reference_file_label = tk.Label(text="Reference file:")
reference_file_entry = tk.Entry()
reference_file_button = tk.Button(text="Browse", command=lambda: reference_file_entry.insert(0, filedialog.askopenfilename()))
file_list_label = tk.Label(text="Files to compare:")
file_list_entry = tk.Entry()
file_list_button = tk.Button(text="Browse", command=lambda: file_list_entry.insert(0, filedialog.askopenfilenames()))
compare_button = tk.Button(text="Compare", command=lambda: compare_files(reference_file_entry.get(), file_list_entry.get().split(' ')))
result_label = tk.Label()

# Add widgets to window
reference_file_label.pack()
reference_file_entry.pack()
reference_file_button.pack()
file_list_label.pack()
file_list_entry.pack()
file_list_button.pack()
compare_button.pack()
result_label.pack()

# Run main loop
window.mainloop()