# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_reflection/v1alpha/reflection.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(grpc_reflection/v1alpha/reflection.proto\x12\x17grpc.reflection.v1alpha\"\x8a\x02\n\x17ServerReflectionRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x1a\n\x10\x66ile_by_filename\x18\x03 \x01(\tH\x00\x12 \n\x16\x66ile_containing_symbol\x18\x04 \x01(\tH\x00\x12N\n\x19\x66ile_containing_extension\x18\x05 \x01(\x0b\x32).grpc.reflection.v1alpha.ExtensionRequestH\x00\x12\'\n\x1d\x61ll_extension_numbers_of_type\x18\x06 \x01(\tH\x00\x12\x17\n\rlist_services\x18\x07 \x01(\tH\x00\x42\x11\n\x0fmessage_request\"E\n\x10\x45xtensionRequest\x12\x17\n\x0f\x63ontaining_type\x18\x01 \x01(\t\x12\x18\n\x10\x65xtension_number\x18\x02 \x01(\x05\"\xd1\x03\n\x18ServerReflectionResponse\x12\x12\n\nvalid_host\x18\x01 \x01(\t\x12J\n\x10original_request\x18\x02 \x01(\x0b\x32\x30.grpc.reflection.v1alpha.ServerReflectionRequest\x12S\n\x18\x66ile_descriptor_response\x18\x04 \x01(\x0b\x32/.grpc.reflection.v1alpha.FileDescriptorResponseH\x00\x12Z\n\x1e\x61ll_extension_numbers_response\x18\x05 \x01(\x0b\x32\x30.grpc.reflection.v1alpha.ExtensionNumberResponseH\x00\x12N\n\x16list_services_response\x18\x06 \x01(\x0b\x32,.grpc.reflection.v1alpha.ListServiceResponseH\x00\x12@\n\x0e\x65rror_response\x18\x07 \x01(\x0b\x32&.grpc.reflection.v1alpha.ErrorResponseH\x00\x42\x12\n\x10message_response\"7\n\x16\x46ileDescriptorResponse\x12\x1d\n\x15\x66ile_descriptor_proto\x18\x01 \x03(\x0c\"K\n\x17\x45xtensionNumberResponse\x12\x16\n\x0e\x62\x61se_type_name\x18\x01 \x01(\t\x12\x18\n\x10\x65xtension_number\x18\x02 \x03(\x05\"P\n\x13ListServiceResponse\x12\x39\n\x07service\x18\x01 \x03(\x0b\x32(.grpc.reflection.v1alpha.ServiceResponse\"\x1f\n\x0fServiceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\rErrorResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t2\x93\x01\n\x10ServerReflection\x12\x7f\n\x14ServerReflectionInfo\x12\x30.grpc.reflection.v1alpha.ServerReflectionRequest\x1a\x31.grpc.reflection.v1alpha.ServerReflectionResponse(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_reflection.v1alpha.reflection_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SERVERREFLECTIONREQUEST._serialized_start=70
  _SERVERREFLECTIONREQUEST._serialized_end=336
  _EXTENSIONREQUEST._serialized_start=338
  _EXTENSIONREQUEST._serialized_end=407
  _SERVERREFLECTIONRESPONSE._serialized_start=410
  _SERVERREFLECTIONRESPONSE._serialized_end=875
  _FILEDESCRIPTORRESPONSE._serialized_start=877
  _FILEDESCRIPTORRESPONSE._serialized_end=932
  _EXTENSIONNUMBERRESPONSE._serialized_start=934
  _EXTENSIONNUMBERRESPONSE._serialized_end=1009
  _LISTSERVICERESPONSE._serialized_start=1011
  _LISTSERVICERESPONSE._serialized_end=1091
  _SERVICERESPONSE._serialized_start=1093
  _SERVICERESPONSE._serialized_end=1124
  _ERRORRESPONSE._serialized_start=1126
  _ERRORRESPONSE._serialized_end=1184
  _SERVERREFLECTION._serialized_start=1187
  _SERVERREFLECTION._serialized_end=1334
# @@protoc_insertion_point(module_scope)
