import server_pb2 as _server_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExactSumReqeust(_message.Message):
    __slots__ = ["target_number"]
    TARGET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    target_number: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, target_number: _Optional[_Iterable[int]] = ...) -> None: ...

class ExactSumResponse(_message.Message):
    __slots__ = ["error", "statistic", "sum_number"]
    class StatisticEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STATISTIC_FIELD_NUMBER: _ClassVar[int]
    SUM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    error: GeneralError
    statistic: _containers.ScalarMap[int, int]
    sum_number: int
    def __init__(self, sum_number: _Optional[int] = ..., statistic: _Optional[_Mapping[int, int]] = ..., error: _Optional[_Union[GeneralError, _Mapping]] = ...) -> None: ...

class GeneralError(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class OneOfResepone(_message.Message):
    __slots__ = ["error", "name", "number"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    error: GeneralError
    name: str
    number: int
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ..., error: _Optional[_Union[GeneralError, _Mapping]] = ...) -> None: ...

class SumRequest(_message.Message):
    __slots__ = ["target_number"]
    TARGET_NUMBER_FIELD_NUMBER: _ClassVar[int]
    target_number: int
    def __init__(self, target_number: _Optional[int] = ...) -> None: ...

class SumResponse(_message.Message):
    __slots__ = ["error", "sum_number"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUM_NUMBER_FIELD_NUMBER: _ClassVar[int]
    error: GeneralError
    sum_number: int
    def __init__(self, sum_number: _Optional[int] = ..., error: _Optional[_Union[GeneralError, _Mapping]] = ...) -> None: ...
