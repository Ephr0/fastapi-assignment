from fastapi import APIRouter, HTTPException
from typing import List
from .models import Event
from .file_storage import EventFileManager
from .event_analyzer import EventAnalyzer
import json


router = APIRouter()
eventManager = EventFileManager()
analyzer = EventAnalyzer()


@router.get("/events", response_model=List[Event])
async def get_all_events():
    return eventManager.read_events_from_file()

@router.get("/events/filter", response_model=List[Event])
async def get_events_by_filter(date: str = None, organizer: str = None, status: str = None, event_type: str = None):
    events = eventManager.read_events_from_file()
    filtered = []
    for event in events:
        if (event["date"] == date or date == None) and (event["organizer"] == organizer or organizer == None) and (event["status"] == status or status == None) and (event["type"] == event_type or event_type == None):
            filtered.append(event)
    return filtered


@router.get("/events/{event_id}", response_model=Event)
async def get_event_by_id(event_id: int):
    events = eventManager.read_events_from_file()
    for event in events:
        if event['id'] == event_id:
            return event
    return "Event not found"


@router.post("/events", response_model=Event)
async def create_event(event: Event):
    R_events = eventManager.read_events_from_file()
    eventNew = event.model_dump()
    for R_event in R_events:
        if R_event["id"] == eventNew["id"]:
            return "Event id already exists"
    R_events.append(eventNew)
    eventManager.write_events_to_file(R_events)
    return event
    

@router.put("/events/{event_id}", response_model=Event)
async def update_event(event_id: int, event: Event):
    R_events = eventManager.read_events_from_file()
    for ind, R_event in enumerate(R_events):
        if R_event["id"] == event_id:
            R_events[ind].update(event.model_dump())
            eventManager.write_events_to_file(R_events)
            return R_events[ind]
    return "Event Not found"
    


@router.delete("/events/{event_id}")
async def delete_event(event_id: int):
    R_events = eventManager.read_events_from_file()
    a = False
    lst = []
    for event in R_events:
        if event["id"] == event_id:
            a = True
            continue
        else:
            lst.append(event)
    if not a:
        return "Event not found"
    eventManager.write_events_to_file(lst)
    return "Event deleted successfully"
        
    
@router.get("/events/joiners/multiple-meetings")
async def get_joiners_multiple_meetings():
    R_events = eventManager.read_events_from_file()
    a = analyzer.get_joiners_multiple_meetings_method(R_events)
    if a == []:
        return "No joiners attending at least 2 meetings"
    return a


