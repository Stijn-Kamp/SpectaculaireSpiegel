from os import path
import pickle
from datetime import datetime
from io import open
from pickle import UnpicklingError

from google.auth.exceptions import TransportError
from httplib2 import ServerNotFoundError

from basicfuctions import get_package_root

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from oauth2client import clientsecrets

class GoogleClass:
    """This class is used to manage the connections to the Google cloud."""
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    CREDENTIALS = path.join(get_package_root(), 'credentials')

    def __init__(self, version, buildType):
        """
        :param version: version of the api
        :param buildType: build of the api
        """
        self.version = version
        self.buildType = buildType

        self.__service = None

    def get_service(self):
        if not self.__service:
            try:
                self.__service = self.checkCredentials()
            except (clientsecrets.InvalidClientSecretsError, FileNotFoundError):
                self.__service = None
        return self.__service

    def checkCredentials(self):
        credentials = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        # TODO fix this mess
        token = path.join(self.CREDENTIALS, 'token.pickle')
        if path.exists(token):
            with open(token, 'rb') as tk:
                try:
                    credentials = pickle.load(tk)
                except UnpicklingError:
                    credentials = None
        # If there are no (valid) credentials available, let the user log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                try:
                    credentials.refresh(Request())
                except Exception:
                    print("Token not refreshed, google services will not be available.")
                    return None
            else:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(path.join(self.CREDENTIALS, 'credentials.json'), self.SCOPES)
                    credentials = flow.run_local_server(port=0)
                except:
                    print("Credentials not found, google services will not be available.")
                    return None
            # Save the credentials for the next run
            with open(token, 'wb') as tk:
                pickle.dump(credentials, tk)
        try:
            return build(self.buildType, self.version, credentials=credentials)
        except ServerNotFoundError:
            return None


class GoogleCalendar(GoogleClass):
    """
    This class is used to manage connections to the Google calendar API.
    """

    def __init__(self):
        GoogleClass.__init__(self, version='v3', buildType='calendar')

    def getCalendars(self):
        service = self.get_service()
        if service is None:
            return None  # Couldn't load calendars
        result = service.calendarList().list().execute()
        calendars = result.get('items', [])
        return calendars

    def getEvents(self, dateMin, dateMax, maxResults=100, calendarId='primary'):
        """
        This function is used to get the upcoming events from the Google calendar.
        @param dateMin: The minimum date of the events.
        @param dateMax: The maximum date of the events.
        @param maxResults: Maximum number of results
        @param calendarId: Id of the calendar
        @return: List of events.
        """
        dateMin = self.TimeToGoogleTime(dateMin)
        dateMax = self.TimeToGoogleTime(dateMax)
        service = self.get_service()
        if service is None:
            return None  # Couldn't load events
        results = service.events().list(calendarId=calendarId, timeMin=dateMin, timeMax=dateMax,
                                        maxResults=maxResults, singleEvents='false',
                                        orderBy='startTime').execute()
        events = results.get('items', [])
        return events

    @staticmethod
    def TimeToGoogleTime(timeStamp):
        """
        This function turns a timestamp into a time format that is understood by the google api.
        @param timeStamp: Timestamp retrieved with the time.time() method.
        :return: Formatted time.
        """
        return datetime.utcfromtimestamp(int(timeStamp)).isoformat() + 'Z'

GoogleCalendar().checkCredentials()

if __name__ == '__main__':
    calendars = GoogleCalendar().getCalendars()

    c = []
    for calendar in calendars:
        c.append({
            'id': calendar.get('id'),
            'name': calendar.get('summary'),
        })
    print(c)
