# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/internal.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.api import user_pb2 as chirpstack__api_dot_api_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!chirpstack-api/api/internal.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1d\x63hirpstack-api/api/user.proto\"G\n\x06\x41piKey\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12\x11\n\ttenant_id\x18\x04 \x01(\t\"3\n\x13\x43reateApiKeyRequest\x12\x1c\n\x07\x61pi_key\x18\x01 \x01(\x0b\x32\x0b.api.ApiKey\"1\n\x14\x43reateApiKeyResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05token\x18\x02 \x01(\t\"!\n\x13\x44\x65leteApiKeyRequest\x12\n\n\x02id\x18\x01 \x01(\t\"X\n\x12ListApiKeysRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x10\n\x08is_admin\x18\x03 \x01(\x08\x12\x11\n\ttenant_id\x18\x04 \x01(\t\"G\n\x13ListApiKeysResponse\x12\x13\n\x0btotal_count\x18\x01 \x01(\r\x12\x1b\n\x06result\x18\x02 \x03(\x0b\x32\x0b.api.ApiKey\"\xc8\x01\n\x0eUserTenantLink\x12.\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x11\n\ttenant_id\x18\x03 \x01(\t\x12\x10\n\x08is_admin\x18\x04 \x01(\x08\x12\x17\n\x0fis_device_admin\x18\x05 \x01(\x08\x12\x18\n\x10is_gateway_admin\x18\x06 \x01(\x08\"/\n\x0cLoginRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1c\n\rLoginResponse\x12\x0b\n\x03jwt\x18\x01 \x01(\t\"P\n\x0fProfileResponse\x12\x17\n\x04user\x18\x01 \x01(\x0b\x32\t.api.User\x12$\n\x07tenants\x18\x03 \x03(\x0b\x32\x13.api.UserTenantLink\"D\n\x13GlobalSearchRequest\x12\x0e\n\x06search\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03\"?\n\x14GlobalSearchResponse\x12\'\n\x06result\x18\x01 \x03(\x0b\x32\x17.api.GlobalSearchResult\"\xe2\x01\n\x12GlobalSearchResult\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x02\x12\x11\n\ttenant_id\x18\x03 \x01(\t\x12\x13\n\x0btenant_name\x18\x04 \x01(\t\x12\x16\n\x0e\x61pplication_id\x18\x05 \x01(\t\x12\x18\n\x10\x61pplication_name\x18\x06 \x01(\t\x12\x16\n\x0e\x64\x65vice_dev_eui\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65vice_name\x18\x08 \x01(\t\x12\x12\n\ngateway_id\x18\t \x01(\t\x12\x14\n\x0cgateway_name\x18\n \x01(\t\">\n\x10SettingsResponse\x12*\n\x0eopenid_connect\x18\x01 \x01(\x0b\x32\x12.api.OpenIdConnect\"q\n\rOpenIdConnect\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x1b\n\tlogin_url\x18\x02 \x01(\tR\x08loginURL\x12\x13\n\x0blogin_label\x18\x03 \x01(\t\x12\x1d\n\nlogout_url\x18\x04 \x01(\tR\tlogoutURL\"8\n\x19OpenIdConnectLoginRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\"+\n\x1aOpenIdConnectLoginResponse\x12\r\n\x05token\x18\x01 \x01(\t\"-\n\x18GetDevicesSummaryRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\t\"\xd2\x01\n\x19GetDevicesSummaryResponse\x12\x14\n\x0c\x61\x63tive_count\x18\x01 \x01(\r\x12\x16\n\x0einactive_count\x18\x02 \x01(\r\x12=\n\x08\x64r_count\x18\x03 \x03(\x0b\x32+.api.GetDevicesSummaryResponse.DrCountEntry\x12\x18\n\x10never_seen_count\x18\x04 \x01(\r\x1a.\n\x0c\x44rCountEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\".\n\x19GetGatewaysSummaryRequest\x12\x11\n\ttenant_id\x18\x01 \x01(\t\"d\n\x1aGetGatewaysSummaryResponse\x12\x14\n\x0c\x61\x63tive_count\x18\x01 \x01(\r\x12\x16\n\x0einactive_count\x18\x02 \x01(\r\x12\x18\n\x10never_seen_count\x18\x03 \x01(\r\"\xc7\x01\n\x07LogItem\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x62ody\x18\x04 \x01(\t\x12\x30\n\nproperties\x18\x05 \x03(\x0b\x32\x1c.api.LogItem.PropertiesEntry\x1a\x31\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"0\n\x1aStreamGatewayFramesRequest\x12\x12\n\ngateway_id\x18\x01 \x01(\t\",\n\x19StreamDeviceFramesRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\",\n\x19StreamDeviceEventsRequest\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\";\n\x13ListRegionsResponse\x12$\n\x07regions\x18\x01 \x03(\x0b\x32\x13.api.RegionListItem\">\n\x0eRegionListItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x06region\x18\x02 \x01(\x0e\x32\x0e.common.Region\" \n\x10GetRegionRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x95\x02\n\x11GetRegionResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x06region\x18\x02 \x01(\x0e\x32\x0e.common.Region\x12\x11\n\tuser_info\x18\x03 \x01(\t\x12+\n\x0fuplink_channels\x18\x04 \x03(\x0b\x32\x12.api.RegionChannel\x12\x11\n\trx1_delay\x18\x05 \x01(\r\x12\x15\n\rrx1_dr_offset\x18\x06 \x01(\r\x12\x0e\n\x06rx2_dr\x18\x07 \x01(\r\x12\x15\n\rrx2_frequency\x18\x08 \x01(\r\x12\x1c\n\x14\x63lass_b_ping_slot_dr\x18\t \x01(\r\x12#\n\x1b\x63lass_b_ping_slot_frequency\x18\n \x01(\r\"B\n\rRegionChannel\x12\x11\n\tfrequency\x18\x01 \x01(\r\x12\x0e\n\x06\x64r_min\x18\x02 \x01(\r\x12\x0e\n\x06\x64r_max\x18\x03 \x01(\r2\xb4\x08\n\x0fInternalService\x12\x30\n\x05Login\x12\x11.api.LoginRequest\x1a\x12.api.LoginResponse\"\x00\x12\x39\n\x07Profile\x12\x16.google.protobuf.Empty\x1a\x14.api.ProfileResponse\"\x00\x12\x45\n\x0cGlobalSearch\x12\x18.api.GlobalSearchRequest\x1a\x19.api.GlobalSearchResponse\"\x00\x12\x45\n\x0c\x43reateApiKey\x12\x18.api.CreateApiKeyRequest\x1a\x19.api.CreateApiKeyResponse\"\x00\x12\x42\n\x0c\x44\x65leteApiKey\x12\x18.api.DeleteApiKeyRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x42\n\x0bListApiKeys\x12\x17.api.ListApiKeysRequest\x1a\x18.api.ListApiKeysResponse\"\x00\x12;\n\x08Settings\x12\x16.google.protobuf.Empty\x1a\x15.api.SettingsResponse\"\x00\x12W\n\x12OpenIdConnectLogin\x12\x1e.api.OpenIdConnectLoginRequest\x1a\x1f.api.OpenIdConnectLoginResponse\"\x00\x12T\n\x11GetDevicesSummary\x12\x1d.api.GetDevicesSummaryRequest\x1a\x1e.api.GetDevicesSummaryResponse\"\x00\x12W\n\x12GetGatewaysSummary\x12\x1e.api.GetGatewaysSummaryRequest\x1a\x1f.api.GetGatewaysSummaryResponse\"\x00\x12H\n\x13StreamGatewayFrames\x12\x1f.api.StreamGatewayFramesRequest\x1a\x0c.api.LogItem\"\x00\x30\x01\x12\x46\n\x12StreamDeviceFrames\x12\x1e.api.StreamDeviceFramesRequest\x1a\x0c.api.LogItem\"\x00\x30\x01\x12\x46\n\x12StreamDeviceEvents\x12\x1e.api.StreamDeviceEventsRequest\x1a\x0c.api.LogItem\"\x00\x30\x01\x12\x41\n\x0bListRegions\x12\x16.google.protobuf.Empty\x1a\x18.api.ListRegionsResponse\"\x00\x12<\n\tGetRegion\x12\x15.api.GetRegionRequest\x1a\x16.api.GetRegionResponse\"\x00\x42T\n\x11io.chirpstack.apiB\rInternalProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.internal_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.chirpstack.apiB\rInternalProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api'
  _GETDEVICESSUMMARYRESPONSE_DRCOUNTENTRY._options = None
  _GETDEVICESSUMMARYRESPONSE_DRCOUNTENTRY._serialized_options = b'8\001'
  _LOGITEM_PROPERTIESENTRY._options = None
  _LOGITEM_PROPERTIESENTRY._serialized_options = b'8\001'
  _APIKEY._serialized_start=171
  _APIKEY._serialized_end=242
  _CREATEAPIKEYREQUEST._serialized_start=244
  _CREATEAPIKEYREQUEST._serialized_end=295
  _CREATEAPIKEYRESPONSE._serialized_start=297
  _CREATEAPIKEYRESPONSE._serialized_end=346
  _DELETEAPIKEYREQUEST._serialized_start=348
  _DELETEAPIKEYREQUEST._serialized_end=381
  _LISTAPIKEYSREQUEST._serialized_start=383
  _LISTAPIKEYSREQUEST._serialized_end=471
  _LISTAPIKEYSRESPONSE._serialized_start=473
  _LISTAPIKEYSRESPONSE._serialized_end=544
  _USERTENANTLINK._serialized_start=547
  _USERTENANTLINK._serialized_end=747
  _LOGINREQUEST._serialized_start=749
  _LOGINREQUEST._serialized_end=796
  _LOGINRESPONSE._serialized_start=798
  _LOGINRESPONSE._serialized_end=826
  _PROFILERESPONSE._serialized_start=828
  _PROFILERESPONSE._serialized_end=908
  _GLOBALSEARCHREQUEST._serialized_start=910
  _GLOBALSEARCHREQUEST._serialized_end=978
  _GLOBALSEARCHRESPONSE._serialized_start=980
  _GLOBALSEARCHRESPONSE._serialized_end=1043
  _GLOBALSEARCHRESULT._serialized_start=1046
  _GLOBALSEARCHRESULT._serialized_end=1272
  _SETTINGSRESPONSE._serialized_start=1274
  _SETTINGSRESPONSE._serialized_end=1336
  _OPENIDCONNECT._serialized_start=1338
  _OPENIDCONNECT._serialized_end=1451
  _OPENIDCONNECTLOGINREQUEST._serialized_start=1453
  _OPENIDCONNECTLOGINREQUEST._serialized_end=1509
  _OPENIDCONNECTLOGINRESPONSE._serialized_start=1511
  _OPENIDCONNECTLOGINRESPONSE._serialized_end=1554
  _GETDEVICESSUMMARYREQUEST._serialized_start=1556
  _GETDEVICESSUMMARYREQUEST._serialized_end=1601
  _GETDEVICESSUMMARYRESPONSE._serialized_start=1604
  _GETDEVICESSUMMARYRESPONSE._serialized_end=1814
  _GETDEVICESSUMMARYRESPONSE_DRCOUNTENTRY._serialized_start=1768
  _GETDEVICESSUMMARYRESPONSE_DRCOUNTENTRY._serialized_end=1814
  _GETGATEWAYSSUMMARYREQUEST._serialized_start=1816
  _GETGATEWAYSSUMMARYREQUEST._serialized_end=1862
  _GETGATEWAYSSUMMARYRESPONSE._serialized_start=1864
  _GETGATEWAYSSUMMARYRESPONSE._serialized_end=1964
  _LOGITEM._serialized_start=1967
  _LOGITEM._serialized_end=2166
  _LOGITEM_PROPERTIESENTRY._serialized_start=2117
  _LOGITEM_PROPERTIESENTRY._serialized_end=2166
  _STREAMGATEWAYFRAMESREQUEST._serialized_start=2168
  _STREAMGATEWAYFRAMESREQUEST._serialized_end=2216
  _STREAMDEVICEFRAMESREQUEST._serialized_start=2218
  _STREAMDEVICEFRAMESREQUEST._serialized_end=2262
  _STREAMDEVICEEVENTSREQUEST._serialized_start=2264
  _STREAMDEVICEEVENTSREQUEST._serialized_end=2308
  _LISTREGIONSRESPONSE._serialized_start=2310
  _LISTREGIONSRESPONSE._serialized_end=2369
  _REGIONLISTITEM._serialized_start=2371
  _REGIONLISTITEM._serialized_end=2433
  _GETREGIONREQUEST._serialized_start=2435
  _GETREGIONREQUEST._serialized_end=2467
  _GETREGIONRESPONSE._serialized_start=2470
  _GETREGIONRESPONSE._serialized_end=2747
  _REGIONCHANNEL._serialized_start=2749
  _REGIONCHANNEL._serialized_end=2815
  _INTERNALSERVICE._serialized_start=2818
  _INTERNALSERVICE._serialized_end=3894
# @@protoc_insertion_point(module_scope)
