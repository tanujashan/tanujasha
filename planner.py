import calendar
yy = int(input("enter the year:"))
mm = int(input("enter the month:"))
print(calendar.month(yy, mm))
'''from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()'''
from datetime import date
from workalendar.asia import India
cal = India()
cal.holidays(2019)
[(datetime.date(2019, 1, 1), 'New year'),
 (datetime.date(2019, 4, 9), 'Easter Monday'),
 (datetime.date(2019, 5, 1), 'Labour Day'),
 (datetime.date(2019, 5, 8), 'Victory in Europe Day'),
 (datetime.date(2019, 5, 17), 'Ascension Day'),
 (datetime.date(2019, 5, 28), 'Whit Monday'),
 (datetime.date(2019, 7, 14), 'Bastille Day'),
 (datetime.date(2019, 8, 15), 'Assumption of Mary to Heaven'),
 (datetime.date(2019, 11, 1), "All Saints' Day"),
 (datetime.date(2019, 11, 11), 'Armistice Day'),
 (datetime.date(2019, 12, 25), 'Christmas')]
cal.is_working_day(date(2019, 12, 25))
False
cal.is_working_day(date(2019, 12, 30))
False
cal.is_working_day(date(2019, 12, 26))
True
cal.add_working_days(date(2019, 12, 23), 5)
datetime.date(2019, 12, 31)