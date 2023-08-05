#  Copyright 2022 Exactpro (Exactpro Systems Limited)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass

from th2_data_services.interfaces.struct import IEventStruct, IMessageStruct



@dataclass
class HTTPEventStruct(IEventStruct):
    """Interface for Event of data-provider v5."""

    EVENT_ID: str
    PARENT_EVENT_ID: str
    STATUS: str
    NAME: str
    TYPE: str
    BATCH_ID: str
    IS_BATCHED: str
    EVENT_TYPE: str
    END_TIMESTAMP: str
    START_TIMESTAMP: str
    ATTACHED_MESSAGES_IDS: str
    BODY: str


http_event_struct = HTTPEventStruct(
    EVENT_ID="eventId",
    PARENT_EVENT_ID="parentEventId",
    STATUS="successful",
    NAME="eventName",
    TYPE="type",
    BATCH_ID="batchId",
    IS_BATCHED="isBatched",
    EVENT_TYPE="eventType",
    END_TIMESTAMP="endTimestamp",
    START_TIMESTAMP="startTimestamp",
    ATTACHED_MESSAGES_IDS="attachedMessageIds",
    BODY="body",
)


@dataclass
class HTTPMessageStruct(IMessageStruct):
    """Interface for Message of data-provider v5."""

    DIRECTION: str
    SESSION_ID: str
    MESSAGE_TYPE: str
    CONNECTION_ID: str
    SESSION_ALIAS: str
    SUBSEQUENCE: str
    SEQUENCE: str
    TIMESTAMP: str
    BODY: str
    BODY_BASE64: str
    TYPE: str
    MESSAGE_ID: str
    ATTACHED_EVENT_IDS: str


http_message_struct = HTTPMessageStruct(
    DIRECTION="direction",
    SESSION_ID="sessionId",
    MESSAGE_TYPE="messageType",
    CONNECTION_ID="connectionId",
    SESSION_ALIAS="sessionAlias",
    SUBSEQUENCE="subsequence",
    SEQUENCE="sequence",
    TIMESTAMP="timestamp",
    BODY="body",
    BODY_BASE64="bodyBase64",
    TYPE="type",
    MESSAGE_ID="messageId",
    ATTACHED_EVENT_IDS="attachedEventIds",
)


@dataclass
class GRPCEventStruct(IEventStruct):
    """Interface for Event of data-provider v6."""

    EVENT_ID: str
    PARENT_EVENT_ID: str
    STATUS: str
    NAME: str
    TYPE: str
    BATCH_ID: str
    IS_BATCHED: str
    EVENT_TYPE: str
    END_TIMESTAMP: str
    START_TIMESTAMP: str
    ATTACHED_MESSAGES_IDS: str
    BODY: str


grpc_event_struct = GRPCEventStruct(
    EVENT_ID="eventId",
    PARENT_EVENT_ID="parentEventId",
    STATUS="successful",
    NAME="eventName",
    TYPE="type",
    BATCH_ID="batchId",
    IS_BATCHED="isBatched",
    EVENT_TYPE="eventType",
    END_TIMESTAMP="endTimestamp",
    START_TIMESTAMP="startTimestamp",
    ATTACHED_MESSAGES_IDS="attachedMessageIds",
    BODY="body",
)


@dataclass
class GRPCMessageStruct(IMessageStruct):
    """Interface for Message of data-provider v6."""

    DIRECTION: str
    SESSION_ID: str
    MESSAGE_TYPE: str
    CONNECTION_ID: str
    SESSION_ALIAS: str
    SUBSEQUENCE: str
    SEQUENCE: str
    TIMESTAMP: str
    BODY: str
    BODY_BASE64: str
    TYPE: str
    MESSAGE_ID: str
    ATTACHED_EVENT_IDS: str


grpc_message_struct = GRPCMessageStruct(
    DIRECTION="direction",
    SESSION_ID="sessionId",
    MESSAGE_TYPE="messageType",
    CONNECTION_ID="connectionId",
    SESSION_ALIAS="sessionAlias",
    SUBSEQUENCE="subsequence",
    SEQUENCE="sequence",
    TIMESTAMP="timestamp",
    BODY="body",
    BODY_BASE64="bodyBase64",
    TYPE="type",
    MESSAGE_ID="messageId",
    ATTACHED_EVENT_IDS="attachedEventIds",
)
