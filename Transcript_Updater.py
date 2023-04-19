import re
import tkinter as tk
from tkinter import filedialog

def process_transcript(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        processed_line = re.sub(r'^\d+\n|(\d{2}:\d{2}:\d{2}\.\d+ --> \d{2}:\d{2}:\d{2}\.\d+\n)', '', line)
        if processed_line:
            processed_lines.append(processed_line.strip())

    return processed_lines

def write_output_file(output_file_path, lines):
    with open(output_file_path, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def browse_file():
    file_path = filedialog.askopenfilename()
    return file_path

def save_file(lines):
    output_file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    write_output_file(output_file_path, lines)

def main():
    root = tk.Tk()
    root.title('Transcript Cleaner')

    input_label = tk.Label(root, text='1. Select the input file:')
    input_label.pack()

    browse_button = tk.Button(root, text='Browse', command=lambda: select_file.set(browse_file()))
    browse_button.pack()

    select_file = tk.StringVar()
    input_file_path_label = tk.Label(root, textvariable=select_file)
    input_file_path_label.pack()

    process_button = tk.Button(root, text='2. Process & Export', command=lambda: save_file(process_transcript(select_file.get())))
    process_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()