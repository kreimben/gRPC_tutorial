# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sum.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import server_pb2 as server__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tsum.proto\x1a\x0cserver.proto\"\x1f\n\x0cGeneralError\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\nSumRequest\x12\x15\n\rtarget_number\x18\x01 \x01(\x05\"(\n\x0f\x45xactSumReqeust\x12\x15\n\rtarget_number\x18\x01 \x03(\x05\"`\n\rOneOfResepone\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x10\n\x06number\x18\x02 \x01(\x05H\x00\x12\x1e\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.GeneralErrorH\x00\x42\r\n\x0btest_one_of\"\xba\x01\n\x10\x45xactSumResponse\x12\x12\n\nsum_number\x18\x01 \x01(\x05\x12\x33\n\tstatistic\x18\x02 \x03(\x0b\x32 .ExactSumResponse.StatisticEntry\x12!\n\x05\x65rror\x18\x03 \x01(\x0b\x32\r.GeneralErrorH\x00\x88\x01\x01\x1a\x30\n\x0eStatisticEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\x42\x08\n\x06_error\"N\n\x0bSumResponse\x12\x12\n\nsum_number\x18\x01 \x01(\x05\x12!\n\x05\x65rror\x18\x02 \x01(\x0b\x32\r.GeneralErrorH\x00\x88\x01\x01\x42\x08\n\x06_error2\x96\x01\n\x07ManySum\x12*\n\x0bsumToTarget\x12\x0b.SumRequest\x1a\x0c.SumResponse0\x01\x12/\n\x08\x65xactSum\x12\x10.ExactSumReqeust\x1a\x11.ExactSumResponse\x12.\n\ttestOneOf\x12\r.HelloRequest\x1a\x0e.OneOfResepone(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sum_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXACTSUMRESPONSE_STATISTICENTRY._options = None
  _EXACTSUMRESPONSE_STATISTICENTRY._serialized_options = b'8\001'
  _GENERALERROR._serialized_start=27
  _GENERALERROR._serialized_end=58
  _SUMREQUEST._serialized_start=60
  _SUMREQUEST._serialized_end=95
  _EXACTSUMREQEUST._serialized_start=97
  _EXACTSUMREQEUST._serialized_end=137
  _ONEOFRESEPONE._serialized_start=139
  _ONEOFRESEPONE._serialized_end=235
  _EXACTSUMRESPONSE._serialized_start=238
  _EXACTSUMRESPONSE._serialized_end=424
  _EXACTSUMRESPONSE_STATISTICENTRY._serialized_start=366
  _EXACTSUMRESPONSE_STATISTICENTRY._serialized_end=414
  _SUMRESPONSE._serialized_start=426
  _SUMRESPONSE._serialized_end=504
  _MANYSUM._serialized_start=507
  _MANYSUM._serialized_end=657
# @@protoc_insertion_point(module_scope)