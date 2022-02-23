from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
from handlers.display import consoledisplay

def event_fetcher(creds):
    try:
        service = build("calendar", "v3", credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + "Z"
        events_result = (
            service.events().list(calendarId="primary",timeMin=now,maxResults=10,singleEvents=True,orderBy="startTime",).execute()
        )
        consoledisplay.console_disp(events_result)

    except HttpError as error:
        print("An error occurred: %s" % error)
