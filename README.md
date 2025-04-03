Media Converter GUI

A simple, user-friendly media converter built with Python's tkinter library. This application leverages the power of ffmpeg to convert audio and video files between various formats.

Features
Graphical Interface: Intuitive GUI built with tkinter.
Input & Output Selection: Easily browse for input files and specify output file paths.
Format Options: Choose from a list of common video and audio formats:
Video: mp4, avi, mkv, mov, webm
Audio: mp3, wav, flac, aac, ogg

Automatic Filename Suggestion: Automatically fills the output filename based on the input filename and selected format.
Smart Conversion: If converting an audio file to a video format, a dummy video track with a black background is added to ensure compatibility.
Error Handling: Provides clear error messages if issues arise during file selection or conversion.

Prerequisites
Python 3: Ensure Python 3 is installed on your system.
tkinter: Typically bundled with Python. If not, install it via your package manager.
ffmpeg: Must be installed and accessible from your system's PATH. Download it from ffmpeg.org.

Installation
Clone the Repository or Download the Script:

git clone https://github.com/yourusername/media-converter-gui.git
Or simply download the media_converter.py file to your preferred directory.

Navigate to the Project Directory:
cd media-converter-gui

Verify ffmpeg Installation:
Run the following command in your terminal to ensure ffmpeg is installed:

ffmpeg -version

Usage
Make the Script Executable (Optional):

If you're on a Unix-like system, you can make the script executable:
chmod +x media_converter.py

Run the Application:
You can start the application by running:
./media_converter.py

Or with Python explicitly:
python3 media_converter.py

Using the GUI:
Input File: Click the Browse button next to the "Input File" field to select your media file.
Output Format: Use the dropdown to choose your desired output format.
Output File: Click the Browse button next to the "Output File" field to select where to save the converted file.
Convert: Click the Convert button to start the conversion process. A message will display upon successful conversion, or an error message if the process fails.

How It Works
tkinter GUI: The application creates a simple graphical user interface using Python's tkinter module.
File Browsing: Users can browse for files using the standard file dialog.
ffmpeg Conversion: Based on user input, the script constructs and executes an ffmpeg command:

Standard Conversion: For most conversions, it simply passes the input and output paths to ffmpeg.
Audio-to-Video Conversion: If the input is an audio file and the output format is video, the script adds a dummy video track (a black background) to ensure the output is a valid video file.
Subprocess Handling: The conversion process is handled using Python’s subprocess module, capturing both standard output and error messages to inform the user of the process status.

Error Handling
Invalid Input File: Displays an error if the selected input file does not exist.
Missing Output File: Prompts the user to specify an output file if none is provided.
Conversion Errors: Any issues during the conversion process will trigger an error message with details from ffmpeg.

Contributing
Contributions are welcome! If you have suggestions, bug fixes, or new features, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Built with Python and the tkinter library.
Media conversion powered by ffmpeg.
