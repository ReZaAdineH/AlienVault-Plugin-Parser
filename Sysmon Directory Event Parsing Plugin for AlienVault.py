import csv
from collections import defaultdict

def parse_sysmon_log(file_path):
    logs = defaultdict(list)

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        for row in reader:
            log = {}
            for header in headers:
                log[header] = row[header]
            logs[row['EventID']].append(log)

    return dict(logs)

if __name__ == '__main__':
    sysmon_logs = parse_sysmon_log('sysmon.csv')
    for event_id, log_entries in sysmon_logs.items():
        print(f'Event ID: {event_id}')
        for log in log_entries:
            print(log)
