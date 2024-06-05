# Import the tkinter module for creating GUIs (*in simple terms, think of it as the library for making windows and buttons*)
import tkinter as tk  # GUI stuff
# Import specific parts from tkinter, like filedialog and ttk (*which stands for themed tkinter, essentially more stylish widgets*)
from tkinter import filedialog, ttk  # File dialog and stylish widgets
# Regular expressions library (*for searching patterns in text*)
import re  # Searching patterns
# Module for finding pathnames matching a specified pattern (*imagine searching for files using wildcards*)
import glob  # Find matching file paths
# Module providing a higher-level interface for file operations (*copying, removing, etc.*)
import shutil  # File operations
# Module to fetch information about the operating system (*like whether it's Windows, Mac, or Linux*)
import platform  # OS information
# Module providing a portable way of using operating system dependent functionality (*like reading or writing to a file*)
import os  # OS dependent functionality
# Module to handle time-related tasks (*like measuring time, waiting for a specific duration, etc.*)
import time  # Time handling
# Module to spawn new processes, connect to their input/output/error pipes, and obtain their return codes (*in simple terms, you can run other programs from your Python program*)
import subprocess  # Running other programs
# Module providing support for threads (*allowing you to perform multiple tasks simultaneously*)
import threading  # Working with threads
# Message box for showing messages in tkinter (*like "Are you sure you want to delete this file?"*)
import tkinter.messagebox  # Popup messages
# Module for handling date and time (*for instance, getting the current date and time*)
from datetime import datetime  # Date and time handling
# Drag-and-drop functionality for tkinter (*enables dragging and dropping files into the application*)
from tkinterdnd2 import DND_FILES, TkinterDnD  # Drag-and-drop functionality
# Import the MKVFile class from the pymkv module (*a module for interacting with Matroska files*)
from pymkv import MKVFile  # Importing the MKVFile class from the pymkv module
# Define a class named SubtitleEditor, which is a type of window for editing VobSub index files quickly
class SubtitleEditor(TkinterDnD.Tk):  # TkinterDnD.Tk is a special type of window in tkinter that supports drag-and-drop functionality
    # Constructor method of the SubtitleEditor class
    def __init__(self):  # This method is automatically called when an object of the SubtitleEditor class is created
        super().__init__()  # Call the constructor of the superclass (TkinterDnD.Tk) to initialize the window
        self.title("VobSub Index File Fast Editor")  # Set the title of the window to "VobSub Index File Fast Editor"
        self.geometry("305x471")  # Set the size of the window to 305x471 pixels (*width x height*)
        
        # Create the main frame inside the window
        self.main_frame = ttk.Frame(self)  # ttk.Frame is a container widget that groups other widgets together
        self.main_frame.pack(expand=False, fill="both")  # Pack the main frame into the window
        
        # Boolean variable to keep track of whether language preference should be saved or not
        self.language_save = tk.BooleanVar()  # tk.BooleanVar is a special variable that holds a Boolean value (True or False)
        
        # Button widget for selecting a folder
        self.folder_button = ttk.Button(self.main_frame, text="Select Folder", command=self.open_folder)  # Create a button labeled "Select Folder" that calls the open_folder method when clicked
        self.folder_button.grid(row=0, column=0, pady=(10, 0), sticky="ew")  # Place the button in the main frame at row 0, column 0, with some padding and stretching horizontally
        
        # Button widget for browsing files
        self.browse_button = ttk.Button(self.main_frame, text="Browse", command=self.open_file)  # Create a button labeled "Browse" that calls the open_file method when clicked
        self.browse_button.grid(row=0, column=1, pady=(10, 0), padx=(5, 0), sticky="ew")  # Place the button in the main frame at row 0, column 1, with some padding and stretching horizontally

        # Label widget prompting the user to select a file
        self.file_label = ttk.Label(self.main_frame, text="Select File:")  # Create a label with the text "Select File:"
        self.file_label.grid(row=1, column=0, pady=(10, 0), sticky="w")  # Place the label in the main frame at row 1, column 0, with some padding and alignment to the left (*west*)

        # Variable to hold the file path entered by the user
        self.file_path = tk.StringVar()  # Create a special variable to hold text data
        # Entry widget for displaying and entering file path
        self.file_entry = ttk.Entry(self.main_frame, textvariable=self.file_path, width=40)  # Create a text entry box that displays the content of the file_path variable and has a width of 40 characters
        self.file_entry.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)  # Place the entry box in the main frame at row 2, spanning two columns, with some padding around it

        # Frame for resolution-related widgets
        self.resolution_frame = ttk.Frame(self.main_frame)  # Create a frame to hold resolution-related widgets
        self.resolution_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the frame in the main frame at row 3, spanning two columns, with some padding above and stretching horizontally

        # Label widget for indicating video resolution
        self.resolution_label = ttk.Label(self.resolution_frame, text="Video Resolution:")  # Create a label with the text "Video Resolution:"
        self.resolution_label.grid(row=0, column=0, pady=(0, 10), sticky="w")  # Place the label in the resolution frame at row 0, column 0, with some padding below and alignment to the left

        # Boolean variable to determine whether resolution should be saved
        self.resolution_save = tk.BooleanVar()  # Create a special variable to hold a boolean value
        # Checkbutton widget for toggling resolution save option
        self.resolution_check = ttk.Checkbutton(self.resolution_frame, text="Save", variable=self.resolution_save)  # Create a check button labeled "Save" that toggles the resolution_save variable
        self.resolution_check.grid(row=0, column=1, pady=(0, 10), sticky="w")  # Place the check button in the resolution frame at row 0, column 1, with some padding below and alignment to the left

        # Entry widget for entering resolution
        self.resolution_entry = ttk.Entry(self.resolution_frame, width=10)  # Create a text entry box with a width of 10 characters for entering resolution
        self.resolution_entry.grid(row=1, column=0, pady=(0, 10))  # Place the entry box in the resolution frame at row 1, column 0, with some padding below

        # Button for changing resolution
        self.resolution_button_pressed = False  # Variable to track whether resolution button is pressed or not
        self.resolution_button = ttk.Button(self.resolution_frame, text="Change Resolution", command=self.on_resolution_button_pressed)  # Create a button labeled "Change Resolution" that calls the on_resolution_button_pressed method when clicked
        self.resolution_button.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the button in the resolution frame at row 2, spanning two columns, with some padding above and stretching horizontally

        # Frame for time-related widgets
        self.time_frame = ttk.Frame(self.main_frame)  # Create a frame to hold time-related widgets
        self.time_frame.grid(row=4, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the frame in the main frame at row 4, spanning two columns, with some padding above and stretching horizontally

        # Label widget for indicating time change in milliseconds
        self.time_label = ttk.Label(self.time_frame, text="Change Time in ms:")  # Create a label with the text "Change Time in ms:"
        self.time_label.grid(row=0, column=0, pady=(0, 10), sticky="w")  # Place the label in the time frame at row 0, column 0, with some padding below and alignment to the left

        # Dictionary to hold subtitle entries
        self.subtitle_entries = {}  # Create an empty dictionary to store subtitle entries

        # Boolean variable to determine whether time should be saved
        self.time_save = tk.BooleanVar()  # Create a special variable to hold a boolean value
        # Checkbutton widget for toggling time save option
        self.time_check = ttk.Checkbutton(self.time_frame, text="Save", variable=self.time_save)  # Create a check button labeled "Save" that toggles the time_save variable
        self.time_check.grid(row=0, column=1, pady=(0, 10), sticky="w")  # Place the check button in the time frame at row 0, column 1, with some padding below and alignment to the left

        # Entry widget for entering time
        self.time_entry = ttk.Entry(self.time_frame, width=10)  # Create a text entry box with a width of 10 characters for entering time
        self.time_entry.grid(row=1, column=0, pady=(0, 10))  # Place the entry box in the time frame at row 1, column 0, with some padding below

        # Variable to hold the mode of time change (add or subtract)
        self.time_mode = tk.StringVar(value="Add")  # Create a special variable to hold text data with a default value of "Add"
        # Radiobutton widget for selecting time mode as "Add"
        self.time_radio_add = ttk.Radiobutton(self.time_frame, text="Add", variable=self.time_mode, value="Add")  # Create a radio button labeled "Add" that sets the time_mode variable to "Add" when selected
        self.time_radio_add.grid(row=1, column=1, pady=(0, 10), padx=(10, 0))  # Place the radio button in the time frame at row 1, column 1, with some padding below and padding on the left

        # Radiobutton widget for selecting time mode as "Subtract"
        self.time_radio_subtract = ttk.Radiobutton(self.time_frame, text="Subtract", variable=self.time_mode, value="Subtract")  # Create a radio button labeled "Subtract" that sets the time_mode variable to "Subtract" when selected
        self.time_radio_subtract.grid(row=1, column=2, pady=(0, 5))  # Place the radio button in the time frame at row 1, column 2, with some padding below

        # Button for changing time
        self.time_button = ttk.Button(self.time_frame, text="Change Time", command=self.change_time)  # Create a button labeled "Change Time" that calls the change_time method when clicked
        self.time_button.grid(row=2, column=0, columnspan=4, pady=(10, 0), sticky="ew")  # Place the button in the time frame at row 2, spanning four columns

        # Button for opening the backup folder
        self.backup_button = ttk.Button(self.main_frame, text="Open Backup Folder", command=self.open_backup_folder)  # Create a button labeled "Open Backup Folder" that calls the open_backup_folder method when clicked
        self.backup_button.grid(row=5, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the button in the main frame at row 5, spanning two columns, with some padding above and stretching horizontally

        # List to store subtitle track IDs
        self.subtitle_tracks = []  # List to store subtitle track IDs

        # Button for extracting subtitles from a video file
        self.extract_subtitles_button = ttk.Button(self.main_frame, text="Extract Subtitles", command=self.extract_subtitles_dialog)  # Create a button labeled "Extract Subtitles" that calls the extract_subtitles_dialog method when clicked
        self.extract_subtitles_button.grid(row=6, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the button in the main frame at row 6, spanning two columns, with some padding above and stretching horizontally

        # Label widget indicating the language
        self.language_label = ttk.Label(self.resolution_frame, text="Language:")  # Create a label with the text "Language:"
        self.language_label.grid(row=0, column=2, pady=(10, 0), columnspan=2, padx=(0, 0), sticky="w")  # Place the label in the resolution frame at row 0, column 2, spanning two columns, with some padding above and alignment to the left

        # Variable to hold language information
        self.language_info = tk.StringVar()  # Create a special variable to hold text data
        # Entry widget for displaying language information
        self.language_entry = ttk.Entry(self.resolution_frame, textvariable=self.language_info, width=8, state="readonly")  # Create a read-only text entry box that displays the content of the language_info variable and has a width of 8 characters
        self.language_entry.grid(row=1, column=2, pady=(0, 10), padx=(0, 0), sticky="ew")  # Place the entry box in the resolution frame at row 1, column 2, with some padding above and alignment to the left

        # Checkbutton widget for toggling language save option
        self.language_check = ttk.Checkbutton(self.resolution_frame, text="Save", variable=self.language_save)  # Create a check button labeled "Save" that toggles the language_save variable
        self.language_check.grid(row=2, column=2, pady=(0, 10), padx=(10, 0), sticky="w")  # Place the check button in the resolution frame at row 2, column 2, with some padding above and alignment to the left

        # Button for opening a text file
        self.open_text_file_button = ttk.Button(self.main_frame, text="Open Text File", command=self.open_text_file)  # Create a button labeled "Open Text File" that calls the open_text_file method when clicked
        self.open_text_file_button.grid(row=8, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the button in the main frame at row 8, spanning two columns, with some padding above and stretching horizontally

        # Thread for checking file existence
        self.check_file_thread = threading.Thread(target=self.check_file_existence)  # Create a thread that runs the check_file_existence method
        self.check_file_thread.daemon = True  # Set the thread as a daemon, meaning it will automatically terminate when the main program ends
        self.check_file_thread.start()  # Start the thread

        # Register drop target for browse button
        self.browse_button.drop_target_register(DND_FILES)  # Register the browse button as a drop target for files
        self.browse_button.dnd_bind('<<Drop>>', self.drop_file)  # Bind the drop event to the drop_file method

        # Register drop target for folder button
        self.folder_button.drop_target_register(DND_FILES)  # Register the folder button as a drop target for files
        self.folder_button.dnd_bind('<<Drop>>', self.drop_folder)  # Bind the drop event to the drop_folder method

        # Register drop target for extract subtitles button
        self.extract_subtitles_button.drop_target_register(DND_FILES)  # Register the extract subtitles button as a drop target for files
        self.extract_subtitles_button.dnd_bind('<<Drop>>', self.drop_extract_subtitles)  # Bind the drop event to the drop_extract_subtitles method

        # Dictionary to hold information about tracks
        self.tracks_info = {}  # Create an empty dictionary to store track information

        # Button for editing timestamps
        self.edit_timestamps_button = ttk.Button(self.main_frame, text="Edit Timestamps", command=self.edit_timestamps)  # Create a button labeled "Edit Timestamps" that calls the edit_timestamps method when clicked
        self.edit_timestamps_button.grid(row=7, column=0, columnspan=2, pady=(10, 0), sticky="ew")  # Place the button in the main frame at row 7, spanning two columns, with some padding above and stretching horizontally

    # Method for handling file drop events
    def drop_file(self, event):
        file_path = event.data.strip('{}')  # Extract the file path from the event data
        self.file_list = [file_path]  # Store the file path in the file list
        self.current_file_index = -1  # Reset the current file index
        self.process_next_file()  # Process the dropped file
        self.load_country()  # Load the country information if available

    # Method triggered when a folder is dropped into the application
    def drop_folder(self, event):  
        # Extract the folder path from the event data
        folder_path = event.data.strip('{}')  
        # Check if the extracted path points to a valid directory
        if os.path.isdir(folder_path):  
            print("Selected folder (drop_folder):", folder_path)  # Debug: Print selected folder path
            self.file_list = []  # Initialize an empty list to store file paths
            # Traverse through the directory structure to find .idx files
            for root, _, files in os.walk(folder_path):
                for file_name in files:
                    # Check if the file has .idx extension
                    if file_name.endswith(".idx"):  
                        file_path = os.path.join(root, file_name)  # Construct the full file path
                        self.file_list.append(file_path)  # Add the file path to the list
            # If .idx files are found in the folder
            if self.file_list:  
                self.current_file_index = -1  # Reset the current file index
                self.process_next_file()  # Process the next file in the list
                self.resolution_button_pressed = False  # Reset resolution button status
                print("Processing files in the folder (drop_folder)...")
                self.load_language()  # Load language information from the file
            else:
                print("No .idx files found in the selected folder (drop_folder).")  # Print a message if no .idx files are found

    def find_sub_files(self, directory, base_filename):
        try:
            # Construct the search pattern for .sub files
            search_pattern = os.path.join(directory, f"{base_filename}*.sub")  # Construct the search pattern
            print("Search path:", search_pattern)  # Debugging: Print the search path
            sub_files = glob.glob(search_pattern)  # Search for .sub files matching the pattern
            print("Found .sub files:", sub_files)  # Debugging: Print the found .sub files
            return sub_files
        except Exception as e:  # Handle any exceptions that may occur
            print("Error finding .sub files:", e)  # Notify user in case of an error
            return []

    def clear_fields(self, exclude_resolution=False, exclude_time=False):  # Define a method to clear certain input fields
        if not exclude_resolution:  # Check if the resolution field should not be excluded from clearing
            self.resolution_entry.delete(0, tk.END)  # Clear the content of the resolution entry field  # Remove all text from the resolution input field
        if not exclude_time:  # Check if the time field should not be excluded from clearing
            self.time_entry.delete(0, tk.END)  # Clear the content of the time entry field  # Remove all text from the time input field

    # Method for handling extract subtitles drop events
    def drop_extract_subtitles(self, event):
        mkv_file = event.data.strip('{}')  # Extract the MKV file path from the event data
        if mkv_file.endswith(".mkv"):  # Check if the file is an MKV video
            self.extract_subtitles(mkv_file)  # Extract subtitles from the MKV file

    # Method for continuously checking file existence
    def check_file_existence(self):
        while True:
            file_path = self.file_path.get()  # Get the current file path
            if file_path:
                if not os.path.exists(file_path):  # Check if the file does not exist
                    self.file_path.set("")  # Clear the file path
                    self.clear_fields()  # Clear other fields
                    self.language_info.set("")  # Clear language information
            time.sleep(3)  # Sleep for 3 seconds

    # Method to open a folder dialog and process the selected folder
    def open_folder(self):
        # Open a dialog to select a folder
        folder_path = filedialog.askdirectory()
        if folder_path:  # Check if a folder is selected
            print("Selected folder (open_folder):", folder_path)  # Debug: Print selected folder path
            self.file_list = []  # Initialize an empty list to store file paths
            # Walk through the directory tree and find .idx files
            for root, _, files in os.walk(folder_path):  # Traverse through folders and files
                for file_name in files:  # Iterate through files
                    if file_name.endswith(".idx"):  # Check if the file has .idx extension
                        file_path = os.path.join(root, file_name)  # Construct the full file path
                        self.file_list.append(file_path)  # Add the file path to the list
            if self.file_list:  # Check if any .idx files are found
                self.current_file_index = -1  # Reset the current file index
                self.process_next_file()  # Process the next file in the list
                self.resolution_button_pressed = False  # Reset the resolution button state
                print("Processing files in the folder (open_folder)...")  # Debug: Print status message
                self.load_language()  # Load language information from the file
            else:
                print("No .idx files found in the selected folder (open_folder).")  # Debug: Print status message

    # Method to process the next file in the file list
    def process_next_file(self):
        self.current_file_index += 1  # Increment the current file index
        if self.current_file_index < len(self.file_list):  # Check if there are more files to process
            file_path = self.file_list[self.current_file_index]  # Get the file path from the list
            self.original_file_path = file_path  # Store the original file path
            self.file_path.set(file_path)  # Set the file path in the entry widget
            self.clear_fields(exclude_resolution=self.resolution_save.get(), exclude_time=self.time_save.get())  # Clear fields excluding resolution and time
            self.load_resolution()  # Load resolution information from the file
            if self.language_save.get():  # Check if language save option is enabled
                print("Before loading language")  # Debug: Print status message
                language = self.load_language()  # Load language information from the file
                print("After loading language")  # Debug: Print status message
                if language:  # Check if language is successfully loaded
                    self.create_backup(file_path, language)  # Create a backup with language information
                else:
                    print("Language could not be loaded")  # Debug: Print error message
                    self.create_backup(file_path)  # Create a backup without language information
            else:
                self.create_backup(file_path)  # Create a backup without saving language information
            if hasattr(self, 'timestamps_window_open') and self.timestamps_window_open:  # Check if timestamps window is open
                self.edit_timestamps()  # Edit timestamps if window is open
            self.timestamps_window_open = False  # Reset the timestamps window state
        # Move the call to change_resolution outside the if block
        self.change_resolution()  # Change resolution of the video

    def extract_subtitles_dialog(self):
        # Prompt user to select a MKV file
        mkv_file = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv")])  # Ask the user to select a MKV file using a file dialog
        if mkv_file:  # If a file is selected
            self.extract_subtitles(mkv_file)  # Call the extract_subtitles method with the selected file path

    def extract_subtitles(self, mkv_file):
        try:
            print("Extracting subtitles from:", mkv_file)  # Print a message indicating that subtitles extraction is in progress
            subtitle_dir = os.path.dirname(mkv_file)  # Get the directory path of the MKV file
            ffmpeg_command = ['ffmpeg', '-i', mkv_file]  # Create a command to extract information from the MKV file using FFmpeg
            process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # Execute the FFmpeg command and capture the output
            output, error = process.communicate()  # Get the output and error streams from the process
            output = error.decode('utf-8')  # Decode the error stream as UTF-8
            subtitles_info = self.parse_subtitles_info(output)  # Parse the subtitles information from the output
            self.tracks_info = {}  # Initialize a dictionary to store subtitles track information
            if subtitles_info:  # If subtitles information is available
                self.show_subtitles_info(subtitles_info, mkv_file, subtitle_dir)  # Show the subtitles information
            else:  # If no subtitles information is available
                self.show_no_subtitles_message()  # Show a message indicating that no subtitles were found

        except Exception as e:  # Catch any exceptions that occur during the process
            print("Error extracting subtitles:", e)  # Print an error message if an exception occurs

    def parse_subtitles_info(self, output):
        # Dictionary to store subtitles information
        subtitles_info = {}
        lines = output.split('\n')  # Split the output into lines
        for i, line in enumerate(lines):  # Iterate through each line of the output
            if 'Subtitle' in line:  # Check if the line contains subtitle information
                try:
                    parts = line.split('Subtitle:')  # Split the line to extract subtitle parts
                    track_info = parts[0].strip()  # Get the track information
                    track_id = track_info.split('#0:')[1].split('(')[0].strip()  # Extract the track ID
                    language = track_info.split('(')[1].split(')')[0].strip()  # Extract the language
                    resolution = line.split('dvd_subtitle, ')[1].split(' (default)')[0]  # Extract the resolution
                    duration = None  # Initialize duration to None
                    for l in lines[i:]:  # Iterate through lines from the current line to the end
                        if 'DURATION' in l:  # Check if line contains duration information
                            duration = l.split('DURATION')[1].strip().split(': ')[1].strip()  # Extract the duration
                            duration = duration.rstrip('0').rstrip('.')  # Remove trailing zeros and dots from the duration
                            break  # Exit the loop once duration is found
                    subtitles_info[track_id] = {'resolution': resolution, 'duration': duration, 'language': language}  # Store subtitles information in the dictionary
                except (IndexError, ValueError) as e:  # Catch any parsing errors
                    print(f"Error parsing line: {line}")  # Print an error message indicating the line that caused the error
                    print(f"Error details: {e}")  # Print details of the error
        return subtitles_info  # Return the subtitles information dictionary

    # Function for displaying subtitle information
    def show_subtitles_info(self, subtitles_info, mkv_file, subtitle_dir):
        # Create a new window
        new_window = tk.Toplevel(self)
        new_window.title("Subtitle Information")  # Set the title of the new window to "Subtitle Information"
        
        # Position the new window adjacent to the parent window
        parent_x = self.winfo_x()
        parent_y = self.winfo_y()
        parent_width = self.winfo_width()
        new_window.geometry(f"+{parent_x + parent_width + 10}+{parent_y}")  # Adjust the '+10' to add some space between the windows if needed

        # Iterate over subtitle information
        for track_id, info in subtitles_info.items():
            # Extract information
            resolution = info.get('resolution', 'unknown')  # Get resolution information or set to 'unknown' if not available
            duration = info.get('duration', 'unknown')  # Get duration information or set to 'unknown' if not available
            language = info.get('language', 'unknown')  # Get language information or set to 'unknown' if not available
            # Create a label displaying subtitle track information
            label = ttk.Label(new_window, text=f"Track {track_id}: Resolution: {resolution}, Duration: {duration}, Language: {language}")  # Create a label with subtitle track information
            label.pack()  # Display the label in the new window
            # Label for entering custom data
            ttk.Label(new_window, text="Enter Data:").pack()  # Create a label with the text "Enter Data:" and display it in the new window
            # Default entry value for user input
            entry_default = f"{os.path.splitext(os.path.basename(mkv_file))[0]}_{track_id}_{language}"  # Default value for user input based on file name, track ID, and language
            # Entry widget for user input
            entry = ttk.Entry(new_window)  # Create a text entry box
            entry.insert(0, entry_default)  # Insert the default value into the entry box
            entry.pack()  # Display the entry box in the new window
            self.tracks_info[entry] = {'track_id': track_id, 'info': info}  # Store track information associated with the entry

        # Function for converting subtitles
        def convert_subtitles():
            for entry, track_info in self.tracks_info.items():
                track_id = track_info['track_id']  # Get track ID from stored information
                info = track_info['info']  # Get subtitle information from stored information
                user_data = entry.get()  # Get user input from the entry box
                output_file = f"{user_data}.sub"  # Generate output file name based on user input
                mkvextract_command = ['mkvextract', 'tracks', mkv_file, f"{track_id}:{os.path.join(subtitle_dir, output_file)}"]  # Command for extracting subtitles
                subprocess.run(mkvextract_command)  # Execute the command
            print("Subtitles extraction completed.")  # Print completion message
            print(f"Subtitle files saved in: {subtitle_dir}")  # Print the directory where subtitle files are saved
            new_window.destroy()  # Close the new window after completion

        # Button for initiating subtitle conversion
        convert_button = ttk.Button(new_window, text="Convert Subtitles", command=convert_subtitles)  # Create a button labeled "Convert Subtitles" that calls the convert_subtitles function when clicked
        convert_button.pack(pady=10)  # Display the button in the new window with some vertical padding

    # Function for displaying a message when no subtitles are found
    def show_no_subtitles_message(self):
        # Create a new window
        new_window = tk.Toplevel()
        new_window.title("No Subtitles Found")  # Set the title of the new window to "No Subtitles Found"
        # Label indicating no subtitles were found
        label = ttk.Label(new_window, text="No subtitles were found in the selected file.")  # Create a label with the message
        label.pack(pady=20)  # Display the label in the new window with some vertical padding
        # Button for closing the window
        ok_button = ttk.Button(new_window, text="OK", command=new_window.destroy)  # Create a button labeled "OK" that closes the window when clicked
        ok_button.pack(pady=10)  # Display the button in the new window with some vertical padding

    def open_file(self):
        # Open a file dialog to select a VobSub index file
        file_path = filedialog.askopenfilename(filetypes=[("VobSub index files", "*.idx")])
        if file_path:  # If a file is selected
            # Reset file list and index, process the next file, and load country information
            self.file_list = [file_path]  # Set the file list with the selected file
            self.current_file_index = -1  # Reset the current file index
            self.process_next_file()  # Process the next file
            self.load_country()  # Load country information
            self.resolution_button_pressed = False  # Reset the resolution button state

    def load_country(self):  # Define a method called 'load_country' within the class
        try:  # Start a try block to handle potential exceptions
            with open(self.file_path.get(), "r", encoding="utf-8") as file:  # Open the file specified in 'file_path' for reading with UTF-8 encoding
                content = file.read()  # Read the entire content of the file and store it in the variable 'content'
            country_match = re.search(r'id: (.+?), index', content)  # Search for the pattern 'id: (something), index' in the content
            if country_match:  # If the pattern is found (country_match is not None)
                country = country_match.group(1)  # Extract the first capturing group from the match, which is the country name
                self.language_info.set(country)  # Set the extracted country name into the 'language_info' variable
            else:  # If the pattern is not found (country_match is None)
                current_language = self.language_info.get()  # Get the current value of 'language_info'
                if not current_language:  # Check if 'current_language' is empty or not set
                    self.language_info.set("Not Found")  # Set 'language_info' to "Not Found" if it was previously empty
        except Exception as e:  # Catch any exceptions that occur during the try block
            print("Error loading country:", e)  # Print an error message to the console
            self.language_info.set("und")  # Set 'language_info' to "und", indicating undefined

    def load_resolution(self):  # Define a method called 'load_resolution' within the class
        try:  # Start a try block to handle potential exceptions
            with open(self.file_path.get(), "r", encoding="utf-8") as file:  # Open the file specified in 'file_path' for reading with UTF-8 encoding
                content = file.read()  # Read the entire content of the file and store it in the variable 'content'
                if 'size' not in content:  # Check if the string 'size' is not found in the content
                    tkinter.messagebox.showerror("Error", "Failed to find resolution in the file.")  # Show an error message box
                    self.file_path.set("")  # Clear the value in 'file_path'
                resolution_match = re.search(r'size: (\d+)x(\d+)', content)  # Search for the pattern 'size: widthxheight' in the content
                if resolution_match:  # If the pattern is found (resolution_match is not None)
                    width, height = resolution_match.groups()  # Extract the width and height from the match
                    if 'x' not in resolution_match.group(0):  # Check if the 'x' character is missing in the resolution string
                        tkinter.messagebox.showerror("Error", "Invalid size format in the file.")  # Show an error message box
                        self.file_path.set("Error. Invalid video resolution format.")  # Set an error message in 'file_path'
                    if not self.resolution_save.get():  # Check if 'resolution_save' is not set (i.e., the user doesn't want to save the resolution)
                        self.resolution_entry.insert(0, f"{width}x{height}")  # Insert the resolution string into the 'resolution_entry' widget
                else:  # If the pattern is not found (resolution_match is None)
                    tkinter.messagebox.showerror("Error", "Failed to find resolution in the file.")  # Show an error message box
                    self.file_path.set("")  # Clear the value in 'file_path'
                if not any("timestamp:" in content):  # Check if there are no occurrences of the string 'timestamp:' in the content
                    tkinter.messagebox.showerror("Error", "Failed to find timestamp in the file.")  # Show an error message box
                    self.file_path.set("")  # Clear the value in 'file_path'
        except Exception as e:  # Catch any exceptions that occur during the try block
            print("Error loading resolution or time:", e)  # Print an error message to the console

    def change_resolution(self):
        # Method to change the resolution of the video
        if not self.resolution_button_pressed:  # If the resolution button is not pressed, do nothing
            return
        try:
            # Load language and file information
            language = self.load_language()  # Load the language
            original_file = self.original_file_path  # Get the original file path
            original_dir = os.path.dirname(original_file)  # Get the directory of the original file
            original_base_filename, file_extension = os.path.splitext(os.path.basename(original_file))  # Get the base filename and extension of the original file
            if original_base_filename.startswith(":"):  # Remove special characters from the file name if present
                original_base_filename = original_base_filename[1:]
            new_resolution = self.resolution_entry.get()  # Get the new resolution from the entry
            # Construct the new file name based on the language and resolution
            if not original_base_filename.endswith(f"-{language}"):  # If the base filename does not end with the language
                if self.language_save.get():  # If language saving is enabled
                    new_file_name = f"{original_base_filename}-{language}{file_extension}" if language else f"{original_base_filename}{file_extension}"  # Append the language to the base filename
                else:
                    new_file_name = f"{original_base_filename}{file_extension}"  # Keep the original base filename
            else:
                new_file_name = original_base_filename + file_extension  # Keep the original base filename
            new_file_path = os.path.join(original_dir, new_file_name)  # Construct the new file path
            # Update file content with the new resolution
            with open(original_file, "r", encoding="utf-8") as file:
                content = file.read()  # Read the content of the original file
            os.remove(original_file)  # Remove the original file
            time.sleep(0.5)  # Wait for 1 second for the file to be removed
            # Write the modified content with the new resolution to the new file
            with open(new_file_path, "w", encoding="utf-8") as new_file:
                new_file.write(re.sub(r'size: \d+x\d+', f'size: {new_resolution}', content))  # Substitute the resolution in the content
            self.file_path.set(new_file_path)  # Set the file path to the new file
            self.original_file_path = new_file_path  # Update the original file path
            # Create a backup with language information if saving is enabled
            if self.language_save.get():
                self.create_backup(new_file_path, language)
            else:
                self.create_backup(new_file_path, None)
            # Find and rename associated .sub files
            self.change_sub_file_name(original_dir, original_base_filename, language, new_file_name)  # Call function to change subtitle file names using the original base filename
        except Exception as e:
            print("Error changing resolution:", e)  # Print any errors encountered while changing resolution
        finally:
            self.resolution_button_pressed = False  # Reset the resolution button state

    def change_sub_file_name(self, directory, base_filename, language, new_file_name):
        try:
            # Find subtitle files associated with the base filename
            sub_files = self.find_sub_files(directory, base_filename)  # Find associated subtitle files in the directory
            # Rename each subtitle file with the new file name
            for sub_file in sub_files:  # Iterate through each subtitle file
                sub_dir, sub_file_name = os.path.split(sub_file)  # Split the subtitle file path
                new_sub_file_name = new_file_name.replace(".idx", ".sub")  # Generate the new subtitle file name
                new_sub_file_path = os.path.join(sub_dir, new_sub_file_name)  # Generate the new subtitle file path
                os.rename(sub_file, new_sub_file_path)  # Rename the subtitle file
                print(f"Renamed {sub_file} to {new_sub_file_path}")  # Inform user about the renaming process
        except Exception as e:  # Handle any exceptions that may occur
            print("Error changing sub file name:", e)  # Notify user in case of an error

    # Method for loading language information from the current file
    def load_language(self):
        try:
            with open(self.file_path.get(), "r", encoding="utf-8") as file:
                content = file.read()  # Read the content of the file
            country_match = re.search(r'id: (.+?), index', content)  # Search for the country information pattern
            if country_match:  # If country information is found
                country = country_match.group(1)  # Extract the country information
                self.language_info.set(country)  # Set the language information in the entry widget
                return country  # Return the extracted country information
            else:  # If country information is not found
                current_language = self.language_info.get()  # Get the current language information
                if not current_language:  # If current language information is empty
                    self.language_info.set("Not Found")  # Set the language information to "Not Found"
                    return None  # Return None
        except Exception as e:  # Handle exceptions
            print("Error loading country:", e)  # Print error message
            self.language_info.set("und")  # Set language information to "und" (undefined)
            return None  # Return None

    def on_resolution_button_pressed(self):
        # Callback function when the resolution button is pressed
        self.resolution_button_pressed = True  # Set the resolution button state to pressed
        self.process_next_file()  # Call the process_next_file method to handle the next file

    def change_time(self):
        try:
            original_dir = os.path.dirname(self.original_file_path)  # Get the directory of the original file
            language = self.load_language()  # Load the language information from the subtitle file
            original_file = self.file_path.get()  # Get the path of the original subtitle file
            if self.language_save.get():  # Check if the language save option is enabled
                self.create_backup(original_file, language)  # Create a backup of the original file with language information
            else:  # If language save option is disabled
                self.create_backup(original_file, None)  # Create a backup of the original file without language information
            time_delta = int(self.time_entry.get())  # Get the time delta entered by the user
            mode = self.time_mode.get()  # Get the selected time mode (Add/Subtract)
            with open(original_file, "r+", encoding="utf-8") as file:  # Open the original file for reading and writing
                content = file.readlines()  # Read the content of the original file
                for i, line in enumerate(content):  # Iterate through each line in the file
                    if line.startswith("timestamp:"):  # Check if the line contains a timestamp
                        # Extract hours, minutes, seconds, and milliseconds from the timestamp
                        timestamp_match = re.search(r'(\d+):(\d+):(\d+):(\d+)', line)
                        if timestamp_match:  # If timestamp pattern is found in the line
                            hours, minutes, seconds, milliseconds = map(int, timestamp_match.groups())  # Extract timestamp components
                            if mode == "Add":  # If the mode is Add
                                milliseconds += time_delta  # Add the time delta to milliseconds
                            else:  # If the mode is Subtract
                                milliseconds -= time_delta  # Subtract the time delta from milliseconds
                            # Handle overflow and underflow for milliseconds, seconds, minutes, and hours
                            while milliseconds < 0:  # While milliseconds is negative
                                milliseconds += 1000  # Add 1000 milliseconds
                                seconds -= 1  # Subtract 1 second
                            while milliseconds >= 1000:  # While milliseconds is greater than or equal to 1000
                                milliseconds -= 1000  # Subtract 1000 milliseconds
                                seconds += 1  # Add 1 second
                            while seconds < 0:  # While seconds is negative
                                seconds += 60  # Add 60 seconds
                                minutes -= 1  # Subtract 1 minute
                            while seconds >= 60:  # While seconds is greater than or equal to 60
                                seconds -= 60  # Subtract 60 seconds
                                minutes += 1  # Add 1 minute
                            while minutes < 0:  # While minutes is negative
                                minutes += 60  # Add 60 minutes
                                hours -= 1  # Subtract 1 hour
                            while minutes >= 60:  # While minutes is greater than or equal to 60
                                minutes -= 60  # Subtract 60 minutes
                                hours += 1  # Add 1 hour
                            # Format the new timestamp
                            new_timestamp = f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}"
                            # Replace the old timestamp with the new one in the content list
                            content[i] = re.sub(r'timestamp: \d+:\d+:\d+:\d+', f'timestamp: {new_timestamp}', line)
                # Write the modified content back to the original file
                file.seek(0)  # Move the file pointer to the beginning of the file
                file.writelines(content)  # Write the modified content to the file
                file.truncate()  # Truncate the file to the current position
            file_name, _ = os.path.splitext(os.path.basename(original_file))  # Extract the base file name
            sub_files = self.find_sub_files(original_dir, file_name)  # Find associated subtitle files
            for sub_file in sub_files:  # Iterate through each subtitle file
                new_sub_file_name = f"{file_name}.sub"  # Generate the new subtitle file name
                new_sub_file_path = os.path.join(original_dir, new_sub_file_name)  # Generate the new subtitle file path
                os.rename(sub_file, new_sub_file_path)  # Rename the subtitle file
                print(f"Renamed {sub_file} to {new_sub_file_path}")  # Inform user about the renaming process

        except Exception as e:  # Handle any exceptions that may occur
            print("Error changing time:", e)  # Notify user in case of an error

    def create_backup(self, file_path, language=None):
        try:
            # Specify the folder for storing backups
            backup_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "subtitle_backups")  # Specify backup folder path
            # Create the backup folder if it doesn't exist
            if not os.path.exists(backup_folder):  # Check if backup folder exists
                os.makedirs(backup_folder)  # Create backup folder if not exists
            # Extract file name and extension
            file_name, file_extension = os.path.splitext(os.path.basename(file_path))  # Extract file name and extension
            # Generate a timestamp for the backup file
            timestamp = time.strftime("%H%M%S")  # Get current time as a string
            # Determine the backup file name based on language
            if language:  # If language information is provided
                backup_file_name = f"{file_name}-{language}-{timestamp}{file_extension}"  # Include language in backup file name
            else:  # If language information is not provided
                backup_file_name = f"{file_name}-{timestamp}{file_extension}"  # Use only timestamp in backup file name
            # Copy the original file to the backup folder with the generated backup file name
            shutil.copy(file_path, os.path.join(backup_folder, backup_file_name))  # Copy file to backup folder
            print(f"Backup created: {backup_file_name}")  # Notify user about backup creation
        except Exception as e:  # Handle any exceptions that may occur
            print("Error creating backup:", e)  # Notify user in case of an error

    def open_backup_folder(self):
        try:
            # Указываем папку, содержащую бэкапы
            backup_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "subtitle_backups")  

            # Открываем папку с бэкапами в зависимости от платформы
            if platform.system() == "Windows":  
                subprocess.Popen(["explorer", backup_folder])  # Открыть папку с помощью проводника Windows
            elif platform.system() == "Darwin":  
                subprocess.Popen(["open", backup_folder])  # Открыть папку с помощью Finder на MacOS
            else:  
                subprocess.Popen(["xdg-open", backup_folder])  # Открыть папку с помощью xdg-open на Linux
        except Exception as e:  
            print("Error opening backup folder:", e)  

    def open_text_file(self):
        try:
            file_path = self.file_path.get()  # Get the path of the selected file
            if file_path:  # If a file is selected
                with open(file_path, "r", encoding="utf-8") as file:  # Open the file for reading
                    file_content = file.read()  # Read the content of the file
                # Create a new window for displaying the text content
                text_editor_window = tk.Toplevel(self)  # Create a new top-level window
                text_editor_window.title("Text Editor")  # Set the title of the window
                # Create a text widget to display the file content
                text_editor = tk.Text(text_editor_window, wrap="word")  # Create a text widget
                text_editor.insert("1.0", file_content)  # Insert file content into the text widget
                text_editor.pack(expand=True, fill="both")  # Pack the text widget to fill the window
                # Create a button to save changes
                save_button = ttk.Button(text_editor_window, text="Save", command=lambda: self.save_text_file(file_path, text_editor.get("1.0", "end-1c")))  # Create a button
                save_button.pack()  # Pack the button into the window
            else:  # If no file is selected
                tkinter.messagebox.showinfo("Info", "Please select a file first.")  # Show an info message
        except Exception as e:  # Handle any exceptions that may occur
            print("Error opening file:", e)  # Notify user in case of an error

    def save_text_file(self, file_path, content):
        try:
            with open(file_path, "w", encoding="utf-8") as file:  # Open the file for writing
                file.write(content)  # Write the content to the file
            tkinter.messagebox.showinfo("Info", "File saved successfully.")  # Show a success message
        except Exception as e:  # Handle any exceptions that may occur
            print("Error saving file:", e)  # Notify user in case of an error

    def edit_timestamps(self):
        try:  # Attempt to execute the following code block
            timestamps_checkboxes = []  # Initialize a list to store checkbox variables for timestamps  # Store checkbox variables to track selection of timestamps
            with open(self.file_path.get(), "r", encoding="utf-8") as file:  # Open the subtitle file for reading  # Open the subtitle file to read its content
                content = file.readlines()  # Read the content of the subtitle file

            # Create a new window for editing timestamps
            timestamps_window = tk.Toplevel(self)  # Create a new top-level window as a child of the main window
            timestamps_window.title("Edit Timestamps")  # Set the window title to "Edit Timestamps"
            self.timestamps_window_open = True  # Mark the timestamps window as open  # Set a flag to indicate that the timestamps window is currently open
            main_frame = ttk.Frame(timestamps_window)  # Create a main frame to hold the widgets
            main_frame.pack(fill="both", expand=True)  # Expand the frame to fill the window
            canvas = tk.Canvas(main_frame)  # Create a canvas for scrolling  # Create a canvas widget to enable scrolling within the window
            scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)  # Create a vertical scrollbar to navigate through the content
            scrollable_frame = ttk.Frame(canvas)  # Create a frame inside the canvas for scrollable content  

            # Configure scrolling behavior  # Configure the canvas to allow scrolling
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")  # Update the scroll region to include all content
                )
            )

            # Create a window inside the canvas to hold the scrollable frame  # Create a window within the canvas for the scrollable frame
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")  # Attach the scrollable frame to the canvas
            canvas.configure(yscrollcommand=scrollbar.set)  # Connect the canvas scrolling to the scrollbar

            # Pack the scrollbar and canvas to enable scrolling  # Pack the scrollbar and canvas widgets to enable scrolling
            scrollbar.pack(side="right", fill="y")  # Pack the scrollbar widget on the right side, filling the vertical space
            canvas.pack(side="left", fill="both", expand=True)  # Pack the canvas widget on the left side, filling both directions

            # Find the index of the first timestamp in the content  # Find the index of the first occurrence of a timestamp in the subtitle file
            first_timestamp_index = None  # Initialize a variable to store the index of the first timestamp
            for i, line in enumerate(content):  # Iterate through the lines of the subtitle file
                if line.startswith("timestamp:"):  # Check if the line contains a timestamp
                    first_timestamp_index = i  # Store the index of the first timestamp
                    break  # Exit the loop once the first timestamp is found

            # If no timestamps are found, display a message and return
            if first_timestamp_index is None:  # Check if no timestamps were found
                tk.Label(scrollable_frame, text="No timestamps found").pack()  # Display a label indicating no timestamps were found
                return  # Exit the method

            # Extract timestamps and their corresponding line indices from the subtitle file
            timestamps_list = [(re.search(r'timestamp: (\d+):(\d+):(\d+):(\d+)', line).group(), i + first_timestamp_index) for i, line in enumerate(content[first_timestamp_index:]) if line.startswith("timestamp:")]

            # Determine the number of columns based on the number of timestamps
            num_timestamps = len(timestamps_list)  # Get the total number of timestamps
            if num_timestamps > 30:  # If there are more than 30 timestamps
                num_columns = 3  # Set the number of columns to 3
                timestamps_window.geometry("400x471")  # Set the window size accordingly
            elif num_timestamps > 15:  # If there are more than 15 timestamps
                num_columns = 2  # Set the number of columns to 2
                timestamps_window.geometry("270x471")  # Set the window size accordingly
            else:  # For fewer than 15 timestamps
                num_columns = 1  # Set the number of columns to 1
                timestamps_window.geometry("141x471")  # Set the window size accordingly

            for i, (timestamp, index) in enumerate(timestamps_list):  # Create entry fields and checkboxes for each timestamp
                row = i % (num_timestamps // num_columns + 1)  # Calculate the row position based on the number of columns and timestamps
                col = i // (num_timestamps // num_columns + 1)  # Calculate the column position based on the number of columns and timestamps
                entry = tk.Entry(scrollable_frame, width=15)  # Create an entry field for the timestamp
                entry.insert(tk.END, timestamp.split(": ")[1])  # Insert the timestamp value into the entry field
                entry.grid(row=row, column=col*2, sticky="w")  # Place the entry field in the appropriate row and column
                var = tk.BooleanVar(value=False)  # Create a Boolean variable for the checkbox, initially set to False
                chk = ttk.Checkbutton(scrollable_frame, variable=var)  # Create a checkbox associated with the Boolean variable
                chk.grid(row=row, column=col*2 + 1, sticky="e")  # Position the checkbox widget within the grid
                timestamps_checkboxes.append((var, index, entry))  # Add the checkbox variable, index, and entry field to the list for tracking

            # Create a button to delete selected timestamps  # Create a button widget to delete selected timestamps
            delete_button = ttk.Button(timestamps_window, text="Delete Selected", command=lambda: self.delete_selected_timestamps(timestamps_window, timestamps_checkboxes))  # Define a button to trigger deletion of selected timestamps
            delete_button.pack(side="top", anchor="ne")  # Position the delete button at the top right of the window  # Pack the delete button to the top right corner

            # Create a button to save changes made to timestamps  # Create a button widget to save changes made to timestamps
            save_button = ttk.Button(timestamps_window, text="Save Changes", command=lambda: self.save_timestamp_changes(timestamps_window, timestamps_checkboxes, content))  # Define a button to save changes to timestamps
            save_button.pack(side="top", anchor="ne")  # Position the save button at the top right of the window

        except Exception as e:  # Handle any exceptions that occur during timestamp editing
            print("Error editing timestamps:", e)  # Print an error message if an exception occurs

    def delete_selected_timestamps(self, timestamps_window, timestamps_checkboxes):
        try:
            with open(self.file_path.get(), "r", encoding="utf-8") as file:
                content = file.readlines()  # Read the content of the subtitle file
            new_content = []  # Initialize an empty list to store modified content
            for i, line in enumerate(content):  # Iterate through each line in the content
                if not any([i == index for (var, index, entry) in timestamps_checkboxes if var.get()]):  # Check if the line should be deleted
                    new_content.append(line)  # Append the line to the new content list if it should not be deleted

            with open(self.file_path.get(), "w", encoding="utf-8") as file:
                file.writelines(new_content)  # Write the modified content back to the subtitle file
            timestamps_window.destroy()  # Close the timestamps window
            self.edit_timestamps()  # Refresh the timestamps view

        except Exception as e:  # Handle any exceptions that may occur
            print("Error deleting timestamps:", e)  # Notify user in case of an error

    def save_timestamp_changes(self, timestamps_window, timestamps_checkboxes, content):
        try:
            for checkbox, index, entry in timestamps_checkboxes:  # Iterate through each checkbox, index, and entry tuple
                if checkbox.get():  # Check if the checkbox is selected
                    content[index] = ""  # Remove the timestamp line from the content
                else:
                    new_timestamp = entry.get()  # Get the new timestamp entered by the user
                    start_pos = content[index].find("timestamp: ") + len("timestamp: ")  # Find the start position of the timestamp
                    end_pos = content[index].find(",", start_pos)  # Find the end position of the timestamp
                    # Replace the old timestamp with the new one in the content
                    content[index] = content[index][:start_pos] + new_timestamp + content[index][end_pos:]
            with open(self.file_path.get(), "w", encoding="utf-8") as file:
                file.writelines(content)  # Write the modified content back to the subtitle file
            timestamps_window.destroy()  # Close the timestamps window
            self.edit_timestamps()  # Refresh the timestamps view

        except Exception as e:  # Handle any exceptions that may occur
            print("Error saving timestamp changes:", e)  # Notify user in case of an error

# Check if this script is being run directly
if __name__ == "__main__":
    # Create an instance of the SubtitleEditor class
    app = SubtitleEditor()  # This initializes the GUI application
    # Start the event loop to run the application
    app.mainloop()  # This keeps the application running and responsive to user actions until the window is closedy
