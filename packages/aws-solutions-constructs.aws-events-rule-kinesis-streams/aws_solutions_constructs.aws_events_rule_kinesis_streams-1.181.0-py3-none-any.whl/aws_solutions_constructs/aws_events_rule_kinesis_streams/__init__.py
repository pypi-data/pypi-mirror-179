'''
# aws-events-rule-kinesisstreams module

<!--BEGIN STABILITY BANNER-->---


![Stability: Deprecated](https://img.shields.io/badge/STABILITY-DEPRECATED-red?style=for-the-badge)

> Some of our early constructs don’t meet the naming standards that evolved for the library. We are releasing completely feature compatible versions with corrected names. The underlying implementation code is the same regardless of whether you deploy the construct using the old or new name. We will support both names for all 1.x releases, but in 2.x we will only publish the correctly named constructs. This construct is being replaced by the functionally identical aws-eventbridge-kinesisstreams.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_events_rule_kinesisstreams`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-events-rule-kinesisstreams`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.eventsrulekinesisstreams`|

## Overview

This AWS Solutions Construct implements an Amazon CloudWatch Events rule to send data to an Amazon Kinesis data stream.

Here is a minimal deployable pattern definition:

Typescript

```python
// aws-events-rule-kinesisstreams has been deprecated for CDK V2 in favor of aws-eventbridge-kinesisstreams.
// This sample uses the CDK V1 syntax
import * as cdk from '@aws-cdk/core';
import * as events from '@aws-cdk/aws-events';
import { EventsRuleToKinesisStreams, EventsRuleToKinesisStreamsProps } from "@aws-solutions-constructs/aws-events-rule-kinesisstreams";

const constructProps: EventsRuleToKinesisStreamsProps = {
  eventRuleProps: {
    schedule: events.Schedule.rate(cdk.Duration.minutes(5)),
  }
};

new EventsRuleToKinesisStreams(this, 'test-events-rule-kinesis-streams', constructProps);
```

Python

```python
# aws-events-rule-kinesisstreams has been deprecated for CDK V2 in favor of aws-eventbridge-kinesisstreams.
# This sample uses the CDK V1 syntax
from aws_solutions_constructs.aws_events_rule_kinesis_streams import EventsRuleToKinesisStreams, EventsRuleToKinesisStreamsProps
from aws_cdk import (
    aws_events as events,
    core
)

EventsRuleToKinesisStreams(self, 'test_events_rule_kinesis_streams',
                        event_rule_props=events.RuleProps(
                            schedule=events.Schedule.rate(
                                core.Duration.minutes(5)),
                        ))
```

Java

```java
// aws-events-rule-kinesisstreams has been deprecated for CDK V2 in favor of aws-eventbridge-kinesisstreams.
// This sample uses the CDK V1 syntax
import software.constructs.Construct;

import software.amazon.awscdk.core.*;
import software.amazon.awscdk.services.events.*;
import software.amazon.awsconstructs.services.eventsrulekinesisstreams.*;

new EventsRuleToKinesisStreams(this, "test-events-rule-kinesis-streams",
        new EventsRuleToKinesisStreamsProps.Builder()
                .eventRuleProps(new RuleProps.Builder()
                        .schedule(Schedule.rate(Duration.minutes(5)))
                        .build())
                .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|existingEventBusInterface?|[`events.IEventBus`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-events.IEventBus.html)| Optional user-provided custom EventBus for construct to use. Providing both this and `eventBusProps` results an error.|
|eventBusProps?|[`events.EventBusProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-events.EventBusProps.html)|Optional user-provided properties to override the default properties when creating a custom EventBus. Setting this value to `{}` will create a custom EventBus using all default properties. If neither this nor `existingEventBusInterface` is provided the construct will use the `default` EventBus. Providing both this and `existingEventBusInterface` results an error.|
|eventRuleProps|[`events.RuleProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-events.RuleProps.html)|User provided eventRuleProps to override the defaults. |
|existingStreamObj?|[`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-kinesis.Stream.html)|Existing instance of Kinesis Stream, providing both this and `kinesisStreamProps` will cause an error.|
|kinesisStreamProps?|[`kinesis.StreamProps`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-kinesis.StreamProps.html)|Optional user-provided props to override the default props for the Kinesis stream. |
|createCloudWatchAlarms|`boolean`|Whether to create recommended CloudWatch alarms. |

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|eventBus?|[`events.IEventBus`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-events.IEventBus.html)|Returns the instance of events.IEventBus used by the construct|
|eventsRule|[`events.Rule`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-events.Rule.html)|Returns an instance of events.Rule created by the construct.|
|kinesisStream|[`kinesis.Stream`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-kinesis.Stream.html)|Returns an instance of the Kinesis stream created by the pattern.|
|eventsRole?|[`iam.Role`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-iam.Role.html)|Returns an instance of the iam.Role created by the construct for events rule.|
|cloudwatchAlarms?|[`cloudwatch.Alarm[]`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-cloudwatch.Alarm.html)|Returns an instance of the cloudwatch.Alarm[] created by the construct.|

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon CloudWatch Events Rule

* Configure least privilege access IAM role for Events Rule to publish to the Kinesis Data Stream.

### Amazon Kinesis Stream

* Enable server-side encryption for Kinesis Data Stream using AWS Managed KMS Key.

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_cloudwatch
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_kinesis
import aws_cdk.core


class EventsRuleToKinesisStreams(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-events-rule-kinesisstreams.EventsRuleToKinesisStreams",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        event_rule_props: typing.Union[aws_cdk.aws_events.RuleProps, typing.Dict[str, typing.Any]],
        create_cloud_watch_alarms: typing.Optional[builtins.bool] = None,
        event_bus_props: typing.Optional[typing.Union[aws_cdk.aws_events.EventBusProps, typing.Dict[str, typing.Any]]] = None,
        existing_event_bus_interface: typing.Optional[aws_cdk.aws_events.IEventBus] = None,
        existing_stream_obj: typing.Optional[aws_cdk.aws_kinesis.Stream] = None,
        kinesis_stream_props: typing.Any = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param event_rule_props: User provided eventRuleProps to override the defaults. Default: - None
        :param create_cloud_watch_alarms: Whether to create recommended CloudWatch alarms. Default: - Alarms are created
        :param event_bus_props: A new custom EventBus is created with provided props. Default: - None
        :param existing_event_bus_interface: Existing instance of a custom EventBus. Default: - None
        :param existing_stream_obj: Existing instance of Kinesis Stream object, providing both this and KinesisStreamProps will cause an error. Default: - Default props are used
        :param kinesis_stream_props: User provided props to override the default props for the Kinesis Stream. Default: - Default props are used

        :access: public
        :summary: Constructs a new instance of the EventsRuleToKinesisStreams class.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                event_rule_props: typing.Union[aws_cdk.aws_events.RuleProps, typing.Dict[str, typing.Any]],
                create_cloud_watch_alarms: typing.Optional[builtins.bool] = None,
                event_bus_props: typing.Optional[typing.Union[aws_cdk.aws_events.EventBusProps, typing.Dict[str, typing.Any]]] = None,
                existing_event_bus_interface: typing.Optional[aws_cdk.aws_events.IEventBus] = None,
                existing_stream_obj: typing.Optional[aws_cdk.aws_kinesis.Stream] = None,
                kinesis_stream_props: typing.Any = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EventsRuleToKinesisStreamsProps(
            event_rule_props=event_rule_props,
            create_cloud_watch_alarms=create_cloud_watch_alarms,
            event_bus_props=event_bus_props,
            existing_event_bus_interface=existing_event_bus_interface,
            existing_stream_obj=existing_stream_obj,
            kinesis_stream_props=kinesis_stream_props,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="eventsRole")
    def events_role(self) -> aws_cdk.aws_iam.Role:
        return typing.cast(aws_cdk.aws_iam.Role, jsii.get(self, "eventsRole"))

    @builtins.property
    @jsii.member(jsii_name="eventsRule")
    def events_rule(self) -> aws_cdk.aws_events.Rule:
        return typing.cast(aws_cdk.aws_events.Rule, jsii.get(self, "eventsRule"))

    @builtins.property
    @jsii.member(jsii_name="kinesisStream")
    def kinesis_stream(self) -> aws_cdk.aws_kinesis.Stream:
        return typing.cast(aws_cdk.aws_kinesis.Stream, jsii.get(self, "kinesisStream"))

    @builtins.property
    @jsii.member(jsii_name="cloudwatchAlarms")
    def cloudwatch_alarms(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_cloudwatch.Alarm]]:
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_cloudwatch.Alarm]], jsii.get(self, "cloudwatchAlarms"))

    @builtins.property
    @jsii.member(jsii_name="eventBus")
    def event_bus(self) -> typing.Optional[aws_cdk.aws_events.IEventBus]:
        return typing.cast(typing.Optional[aws_cdk.aws_events.IEventBus], jsii.get(self, "eventBus"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-events-rule-kinesisstreams.EventsRuleToKinesisStreamsProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_rule_props": "eventRuleProps",
        "create_cloud_watch_alarms": "createCloudWatchAlarms",
        "event_bus_props": "eventBusProps",
        "existing_event_bus_interface": "existingEventBusInterface",
        "existing_stream_obj": "existingStreamObj",
        "kinesis_stream_props": "kinesisStreamProps",
    },
)
class EventsRuleToKinesisStreamsProps:
    def __init__(
        self,
        *,
        event_rule_props: typing.Union[aws_cdk.aws_events.RuleProps, typing.Dict[str, typing.Any]],
        create_cloud_watch_alarms: typing.Optional[builtins.bool] = None,
        event_bus_props: typing.Optional[typing.Union[aws_cdk.aws_events.EventBusProps, typing.Dict[str, typing.Any]]] = None,
        existing_event_bus_interface: typing.Optional[aws_cdk.aws_events.IEventBus] = None,
        existing_stream_obj: typing.Optional[aws_cdk.aws_kinesis.Stream] = None,
        kinesis_stream_props: typing.Any = None,
    ) -> None:
        '''
        :param event_rule_props: User provided eventRuleProps to override the defaults. Default: - None
        :param create_cloud_watch_alarms: Whether to create recommended CloudWatch alarms. Default: - Alarms are created
        :param event_bus_props: A new custom EventBus is created with provided props. Default: - None
        :param existing_event_bus_interface: Existing instance of a custom EventBus. Default: - None
        :param existing_stream_obj: Existing instance of Kinesis Stream object, providing both this and KinesisStreamProps will cause an error. Default: - Default props are used
        :param kinesis_stream_props: User provided props to override the default props for the Kinesis Stream. Default: - Default props are used

        :summary: The properties for the EventsRuleToKinesisStreams Construct
        '''
        if isinstance(event_rule_props, dict):
            event_rule_props = aws_cdk.aws_events.RuleProps(**event_rule_props)
        if isinstance(event_bus_props, dict):
            event_bus_props = aws_cdk.aws_events.EventBusProps(**event_bus_props)
        if __debug__:
            def stub(
                *,
                event_rule_props: typing.Union[aws_cdk.aws_events.RuleProps, typing.Dict[str, typing.Any]],
                create_cloud_watch_alarms: typing.Optional[builtins.bool] = None,
                event_bus_props: typing.Optional[typing.Union[aws_cdk.aws_events.EventBusProps, typing.Dict[str, typing.Any]]] = None,
                existing_event_bus_interface: typing.Optional[aws_cdk.aws_events.IEventBus] = None,
                existing_stream_obj: typing.Optional[aws_cdk.aws_kinesis.Stream] = None,
                kinesis_stream_props: typing.Any = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument event_rule_props", value=event_rule_props, expected_type=type_hints["event_rule_props"])
            check_type(argname="argument create_cloud_watch_alarms", value=create_cloud_watch_alarms, expected_type=type_hints["create_cloud_watch_alarms"])
            check_type(argname="argument event_bus_props", value=event_bus_props, expected_type=type_hints["event_bus_props"])
            check_type(argname="argument existing_event_bus_interface", value=existing_event_bus_interface, expected_type=type_hints["existing_event_bus_interface"])
            check_type(argname="argument existing_stream_obj", value=existing_stream_obj, expected_type=type_hints["existing_stream_obj"])
            check_type(argname="argument kinesis_stream_props", value=kinesis_stream_props, expected_type=type_hints["kinesis_stream_props"])
        self._values: typing.Dict[str, typing.Any] = {
            "event_rule_props": event_rule_props,
        }
        if create_cloud_watch_alarms is not None:
            self._values["create_cloud_watch_alarms"] = create_cloud_watch_alarms
        if event_bus_props is not None:
            self._values["event_bus_props"] = event_bus_props
        if existing_event_bus_interface is not None:
            self._values["existing_event_bus_interface"] = existing_event_bus_interface
        if existing_stream_obj is not None:
            self._values["existing_stream_obj"] = existing_stream_obj
        if kinesis_stream_props is not None:
            self._values["kinesis_stream_props"] = kinesis_stream_props

    @builtins.property
    def event_rule_props(self) -> aws_cdk.aws_events.RuleProps:
        '''User provided eventRuleProps to override the defaults.

        :default: - None
        '''
        result = self._values.get("event_rule_props")
        assert result is not None, "Required property 'event_rule_props' is missing"
        return typing.cast(aws_cdk.aws_events.RuleProps, result)

    @builtins.property
    def create_cloud_watch_alarms(self) -> typing.Optional[builtins.bool]:
        '''Whether to create recommended CloudWatch alarms.

        :default: - Alarms are created
        '''
        result = self._values.get("create_cloud_watch_alarms")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def event_bus_props(self) -> typing.Optional[aws_cdk.aws_events.EventBusProps]:
        '''A new custom EventBus is created with provided props.

        :default: - None
        '''
        result = self._values.get("event_bus_props")
        return typing.cast(typing.Optional[aws_cdk.aws_events.EventBusProps], result)

    @builtins.property
    def existing_event_bus_interface(
        self,
    ) -> typing.Optional[aws_cdk.aws_events.IEventBus]:
        '''Existing instance of a custom EventBus.

        :default: - None
        '''
        result = self._values.get("existing_event_bus_interface")
        return typing.cast(typing.Optional[aws_cdk.aws_events.IEventBus], result)

    @builtins.property
    def existing_stream_obj(self) -> typing.Optional[aws_cdk.aws_kinesis.Stream]:
        '''Existing instance of Kinesis Stream object, providing both this and KinesisStreamProps will cause an error.

        :default: - Default props are used
        '''
        result = self._values.get("existing_stream_obj")
        return typing.cast(typing.Optional[aws_cdk.aws_kinesis.Stream], result)

    @builtins.property
    def kinesis_stream_props(self) -> typing.Any:
        '''User provided props to override the default props for the Kinesis Stream.

        :default: - Default props are used
        '''
        result = self._values.get("kinesis_stream_props")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventsRuleToKinesisStreamsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EventsRuleToKinesisStreams",
    "EventsRuleToKinesisStreamsProps",
]

publication.publish()
