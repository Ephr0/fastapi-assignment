import json
import typing
from .models import Event


class EventFileManager():
    FILE_PATH = "event.json"
        
    def read_events_from_file(self):
        try:
            with open(self.FILE_PATH, 'r') as file:
                a = json.load(file)
            return a
        except:
            return []
        
    def write_events_to_file(self, a:dict):
        try:
            with open(self.FILE_PATH, 'w') as file:
                json.dump(a, file, indent=4)
        except Exception as e:
            print(f"ERROR: {e}")
            

# a = EventFileManager()

# # test = {'id': 2, 'name': 'Test event 1', 'date': '2024-03-06', 'organizer': {'name': 'fdev', 'email': 'fdev@example.com'}, 'status': 'active', 'type': 'event', 'joiners': [{'name': 'Test User', 'email': 'test@test.com', 'country': 'Hungary'}], 'location': 'Budapest, Hungary', 'max_attendees': 100}
# a.write_events_to_file(test)

           
            