import json
import logging
import rsyslog

logging.basicConfig(filename='parsing.log', level=logging.INFO)

def parse_event(event):
    try:
        syslog_event = rsyslog.SyslogEvent(event)
        extracted_data = {
            "timestamp": str(syslog_event.timestamp),
            "facility": syslog_event.facility,
            "severity": syslog_event.severity,
            "hostname": syslog_event.hostname,
            "message": syslog_event.message
        }
        return extracted_data
    except Exception as e:
        logging.error("Error parsing event: " + str(e))

def handler(event, context):
    try:
        return json.dumps(parse_event(event))
    except Exception as e:
        logging.error("Error in handler: " + str(e))
