from typing import List, Optional

from pydantic import BaseModel


class Gateway(BaseModel):
    id: str
    internalipaddress: str
    internalport: str
    macaddress: str
    name: str


class Action(BaseModel):
    alert: str
    bri: int
    colormode: str
    ct: str
    effect: str
    hue: str
    on: str
    sat: str


class State(BaseModel):
    all_on: bool = False
    any_on: bool = False


class Group(BaseModel):
    action: Action = None
    devicemembership: Optional[List[object]] = None
    etag: str = ''
    hidden: bool = False
    id: str = ''
    lights: Optional[List[object]]
    lightsequence: Optional[List[object]]
    multideviceids: Optional[List[object]]
    name: str = ''
    scene: Optional[List[object]]
    type: str = ''
    state: State = None
    selected: bool = False
