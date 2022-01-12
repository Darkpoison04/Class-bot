def console_disp(data):
    if len(data.get('items')) < 1:
        return print("No Meetings Today")
    print(
        f"Email id:-{data.get('summary')}\nTimeZone:- {data.get('timeZone')}\nEvent Name:- {data.get('items')[0].get('summary')}\nClick here to join the event:-{data.get('items')[0].get('hangoutLink')}"
    )
