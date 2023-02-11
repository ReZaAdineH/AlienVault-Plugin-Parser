import sys
import json
import logging

from alienvault import json_dumps

# Define the plugin class
class WinSecurityEventPlugin:

    def __init__(self):
        self.data = {}
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
    
    def parse_event(self, event):
        try:
            event_data = json.loads(event)
            self.data['timestamp'] = event_data['System']['TimeCreated']['@SystemTime']
            self.data['event_id'] = int(event_data['System']['EventID']['#text'])
            self.data['computer_name'] = event_data['System']['Computer']
            self.data['message'] = event_data['EventData']['Message']
        except (KeyError, ValueError) as e:
            self.data['error'] = f'Error parsing event: {e}'
            self.logger.error(f'Error parsing event: {e}', exc_info=True)

    def __str__(self):
        return json_dumps(self.data)

# Main function
def main(event):
    plugin = WinSecurityEventPlugin()
    plugin.parse_event(event)
    print(str(plugin))
    return 0

# Call the main function
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: No event data provided')
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
