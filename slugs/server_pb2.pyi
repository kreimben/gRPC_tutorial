from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GeoRequest(_message.Message):
    __slots__ = ["latitude", "longitude"]
    LATITUDE_FIELD_NUMBER: _ClassVar[int]
    LONGITUDE_FIELD_NUMBER: _ClassVar[int]
    latitude: float
    longitude: float
    def __init__(self, longitude: _Optional[float] = ..., latitude: _Optional[float] = ...) -> None: ...

class GeoResponse(_message.Message):
    __slots__ = ["country_name"]
    COUNTRY_NAME_FIELD_NUMBER: _ClassVar[int]
    country_name: str
    def __init__(self, country_name: _Optional[str] = ...) -> None: ...

class HelloRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class HelloResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class TimeRequest(_message.Message):
    __slots__ = ["timezone"]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    timezone: str
    def __init__(self, timezone: _Optional[str] = ...) -> None: ...

class TimeResponse(_message.Message):
    __slots__ = ["current_time", "tz"]
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    TZ_FIELD_NUMBER: _ClassVar[int]
    current_time: str
    tz: str
    def __init__(self, current_time: _Optional[str] = ..., tz: _Optional[str] = ...) -> None: ...
