# AlienVault-Plugin-Parser
Python code for a plugin that parses Windows security events:
Windows Security Event Parsing Plugin

A Python script for parsing Windows security events and extracting relevant information.

Features

Parses Windows security events in JSON format
Extracts relevant information such as timestamp, event ID, computer name, and message
Provides error handling and logging for debugging purposes
Requirements

Python 3.x
json and logging Python modules
alienvault module for custom json_dumps method (included in repository)
Usage

To use this script, simply run the following command and provide the JSON formatted Windows security event as an argument:

php
Copy code
python win_sec_event_parser.py <event_data>
The script will parse the event and print the extracted information in JSON format.

Contribution

This project is open for contributions and improvements. If you have any suggestions or bug fixes, feel free to submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
