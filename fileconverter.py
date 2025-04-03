#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess

class ConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Media Converter")
        self.geometry("500x350")
        self.create_widgets()
    
    def create_widgets(self):
        # Input file selection
        self.input_label = tk.Label(self, text="Input File:")
        self.input_label.pack(pady=(20, 5))
        self.input_entry = tk.Entry(self, width=60)
        self.input_entry.pack(pady=5)
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        # Output format selection
        self.format_label = tk.Label(self, text="Output Format:")
        self.format_label.pack(pady=5)
        # List of common video and audio formats
        self.format_options = ["mp4", "mp3", "avi", "mkv", "mov", "webm", "wav", "flac", "aac", "ogg"]
        self.format_var = tk.StringVar()
        self.format_combobox = ttk.Combobox(self, textvariable=self.format_var, values=self.format_options, state="readonly")
        self.format_combobox.current(0)  # default to mp4
        self.format_combobox.pack(pady=5)

        # Output file selection
        self.output_label = tk.Label(self, text="Output File:")
        self.output_label.pack(pady=5)
        self.output_entry = tk.Entry(self, width=60)
        self.output_entry.pack(pady=5)
        self.output_button = tk.Button(self, text="Browse", command=self.browse_output_file)
        self.output_button.pack(pady=5)

        # Convert button
        self.convert_button = tk.Button(self, text="Convert", command=self.convert)
        self.convert_button.pack(pady=20)
    
    def browse_file(self):
        filename = filedialog.askopenfilename(title="Select Input File")
        if filename:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, filename)
            # Auto-fill output filename if empty
            if not self.output_entry.get():
                base, _ = os.path.splitext(filename)
                self.output_entry.insert(0, base + "." + self.format_var.get())

    def browse_output_file(self):
        # Get desired extension from dropdown
        ext = self.format_var.get()
        filetypes = [(f"{ext.upper()} Files", f"*.{ext}"), ("All Files", "*.*")]
        filename = filedialog.asksaveasfilename(title="Select Output File", filetypes=filetypes, defaultextension="." + ext)
        if filename:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, filename)

    def convert(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()
        if not input_file or not os.path.isfile(input_file):
            messagebox.showerror("Error", "Invalid input file.")
            return
        if not output_file:
            messagebox.showerror("Error", "Please specify an output file.")
            return
        
        # Determine if input is audio and output is video so we can add a dummy video track if needed.
        audio_exts = [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"]
        video_exts = [".mp4", ".avi", ".mkv", ".mov", ".webm"]
        input_ext = os.path.splitext(input_file)[1].lower()
        output_ext = os.path.splitext(output_file)[1].lower()

        if input_ext in audio_exts and output_ext in video_exts:
            # For converting audio (e.g., mp3) to a video format (e.g., mp4), add a dummy black background.
            command = [
                "ffmpeg", "-y",
                "-f", "lavfi", "-i", "color=c=black:s=640x480:r=25",
                "-i", input_file,
                "-shortest",
                "-c:v", "libx264",
                "-c:a", "aac",
                output_file
            ]
        else:
            # Standard conversion for video-to-video or audio-to-audio conversions
            command = ["ffmpeg", "-y", "-i", input_file, output_file]
        
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                messagebox.showinfo("Success", "Conversion completed successfully.")
            else:
                error_message = stderr.decode("utf-8")
                messagebox.showerror("Error", f"Conversion failed.\n{error_message}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = ConverterGUI()
    app.mainloop()
