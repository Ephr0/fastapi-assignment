from .models import Event
class EventAnalyzer():
    def get_joiners_multiple_meetings_method(self, events:list[dict]):
        lst = []
        for i in range(len(events)):
            temp = events[i]["joiners"] #list of dics
            for j in range(i+1, len(events)):
                if temp == []:
                    break
                for val in temp:
                    if val in events[j]["joiners"]:
                        if val not in lst:
                            lst.append(val)
                        temp.remove(val)
        return lst
            