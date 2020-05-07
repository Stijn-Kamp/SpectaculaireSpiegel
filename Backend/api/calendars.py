from api.googlefunctions import GoogleCalendar
from time import time

from basicfuctions import get_system_time_offset


class Calendar:
    """Baseclass to communicate with a calendar"""

    def __init__(self):
        raise NotImplementedError("abstract class not implemented")

    def get_events(self):
        raise NotImplementedError

    class Event:
        def __init__(self, summary, startTime):
            self.summary = summary
            self.startTime = startTime


class CalendarApi(Calendar):
    """Class used to communicate with the google calendar api"""

    def __init__(self):
        self.eventDuration = 604800  # look for events during coming week
        self.googleCalendar = GoogleCalendar()

    def get_events(self):
        """
        :return: A list of events retrieved by the google calendar class
        """
        now = time()
        events = self.googleCalendar.getEvents(now, now + self.eventDuration)
        if events is None:
            return None
        return self.parse_events(events)

    @classmethod
    def parse_events(cls, googleEvents):
        events = []
        for event in googleEvents:
            summary = event.get('summary')
            start = event.get('start')
            if 'dateTime' in start:
                start = start.get('dateTime')
            else:
                start = start.get('date') + ("T00:00:01%s" % get_system_time_offset())  # Convert date to localDateTime
            events.append(cls.Event(summary=summary, startTime=start))
        return events

    @classmethod
    def create_event(cls, googleEvent):
        """
        Used to parse an event
        :param googleEvent: event retrieved by google calendar api
        :return: Event class
        """
        summary = googleEvent.get('summary')
        startTime = googleEvent.get('startTime').get('dateTime')
        return cls.Event(summary=summary, startTime=startTime)


if __name__ == "__main__":
    ev = CalendarApi().get_events()
    print(ev[0])
