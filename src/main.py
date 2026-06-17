import win32evtlog

def read_event_logs():
    log_handle = win32evtlog.OpenEventLog("localhost","Security")

    event_read = win32evtlog.ReadEventLog(
        log_handle,
        win32evtlog.EVENTLOG_FORWARDS_READ |
        win32evtlog.EVENTLOG_SEQUENTIAL_READ,
        0
    )
    

    for event in event_read:

        event_data = {
            "event_id": event.EventID,
            "recordNumber": event.RecordNumber,
            "time": str(event.TimeGenerated),
            "Source": event.SourceName

        }
        
        print(event_data)


read_event_logs()
