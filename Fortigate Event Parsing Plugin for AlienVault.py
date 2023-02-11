import logging
import re

logging.basicConfig(filename='parsing.log', level=logging.INFO)

def parse_event(event):
    try:
        # Regex pattern to extract relevant information from Fortigate log events
        pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) " \
                  r"(?P<hostname>\S+) (?P<message>.+)"
        match = re.match(pattern, event)
        extracted_data = {
            "timestamp": match.group("timestamp"),
            "hostname": match.group("hostname"),
            "message": match.group("message")
        }
        return extracted_data
    except Exception as e:
        logging.error("Error parsing event: " + str(e))

def handler(event, context):
    try:
        extracted_data = parse_event(event)
        if extracted_data:
            return extracted_data
        else:
            raise ValueError("Unable to extract relevant information from event")
    except Exception as e:
        logging.error("Error in handler: " + str(e))
