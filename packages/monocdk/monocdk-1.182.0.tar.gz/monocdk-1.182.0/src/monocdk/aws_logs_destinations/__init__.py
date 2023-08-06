'''
# AWS CloudWatch Logs Subscription Destination Library

This library contains destinations for AWS CloudWatch Logs SubscriptionFilters. You
can send log data to Kinesis Streams or Lambda Functions.

See the documentation of the `logs` module for more information.
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

from .._jsii import *

from .. import Construct as _Construct_e78e779f
from ..aws_iam import IRole as _IRole_59af6f50
from ..aws_kinesis import IStream as _IStream_14c6ec7f
from ..aws_lambda import IFunction as _IFunction_6e14f09e
from ..aws_logs import (
    ILogGroup as _ILogGroup_846e17a0,
    ILogSubscriptionDestination as _ILogSubscriptionDestination_4c87195f,
    LogSubscriptionDestinationConfig as _LogSubscriptionDestinationConfig_29b34d24,
)


@jsii.implements(_ILogSubscriptionDestination_4c87195f)
class KinesisDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_logs_destinations.KinesisDestination",
):
    '''(experimental) Use a Kinesis stream as the destination for a log subscription.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_iam as iam
        from monocdk import aws_kinesis as kinesis
        from monocdk import aws_logs_destinations as logs_destinations
        
        # role: iam.Role
        # stream: kinesis.Stream
        
        kinesis_destination = logs_destinations.KinesisDestination(stream,
            role=role
        )
    '''

    def __init__(
        self,
        stream: _IStream_14c6ec7f,
        *,
        role: typing.Optional[_IRole_59af6f50] = None,
    ) -> None:
        '''
        :param stream: The Kinesis stream to use as destination.
        :param role: (experimental) The role to assume to write log events to the destination. Default: - A new Role is created

        :stability: experimental
        '''
        if __debug__:
            def stub(
                stream: _IStream_14c6ec7f,
                *,
                role: typing.Optional[_IRole_59af6f50] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisDestinationProps(role=role)

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _Construct_e78e779f,
        _source_log_group: _ILogGroup_846e17a0,
    ) -> _LogSubscriptionDestinationConfig_29b34d24:
        '''(experimental) Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param _source_log_group: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: _Construct_e78e779f,
                _source_log_group: _ILogGroup_846e17a0,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument _source_log_group", value=_source_log_group, expected_type=type_hints["_source_log_group"])
        return typing.cast(_LogSubscriptionDestinationConfig_29b34d24, jsii.invoke(self, "bind", [scope, _source_log_group]))


@jsii.data_type(
    jsii_type="monocdk.aws_logs_destinations.KinesisDestinationProps",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class KinesisDestinationProps:
    def __init__(self, *, role: typing.Optional[_IRole_59af6f50] = None) -> None:
        '''(experimental) Customize the Kinesis Logs Destination.

        :param role: (experimental) The role to assume to write log events to the destination. Default: - A new Role is created

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_iam as iam
            from monocdk import aws_logs_destinations as logs_destinations
            
            # role: iam.Role
            
            kinesis_destination_props = logs_destinations.KinesisDestinationProps(
                role=role
            )
        '''
        if __debug__:
            def stub(*, role: typing.Optional[_IRole_59af6f50] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def role(self) -> typing.Optional[_IRole_59af6f50]:
        '''(experimental) The role to assume to write log events to the destination.

        :default: - A new Role is created

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_59af6f50], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_ILogSubscriptionDestination_4c87195f)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_logs_destinations.LambdaDestination",
):
    '''(experimental) Use a Lambda Function as the destination for a log subscription.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import monocdk as destinations
        # fn: lambda.Function
        # log_group: logs.LogGroup
        
        
        logs.SubscriptionFilter(self, "Subscription",
            log_group=log_group,
            destination=destinations.LambdaDestination(fn),
            filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread")
        )
    '''

    def __init__(
        self,
        fn: _IFunction_6e14f09e,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) LambdaDestinationOptions.

        :param fn: -
        :param add_permissions: (experimental) Whether or not to add Lambda Permissions. Default: true

        :stability: experimental
        '''
        if __debug__:
            def stub(
                fn: _IFunction_6e14f09e,
                *,
                add_permissions: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        options = LambdaDestinationOptions(add_permissions=add_permissions)

        jsii.create(self.__class__, self, [fn, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _Construct_e78e779f,
        log_group: _ILogGroup_846e17a0,
    ) -> _LogSubscriptionDestinationConfig_29b34d24:
        '''(experimental) Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param log_group: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: _Construct_e78e779f,
                log_group: _ILogGroup_846e17a0,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        return typing.cast(_LogSubscriptionDestinationConfig_29b34d24, jsii.invoke(self, "bind", [scope, log_group]))


@jsii.data_type(
    jsii_type="monocdk.aws_logs_destinations.LambdaDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={"add_permissions": "addPermissions"},
)
class LambdaDestinationOptions:
    def __init__(
        self,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Options that may be provided to LambdaDestination.

        :param add_permissions: (experimental) Whether or not to add Lambda Permissions. Default: true

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_logs_destinations as logs_destinations
            
            lambda_destination_options = logs_destinations.LambdaDestinationOptions(
                add_permissions=False
            )
        '''
        if __debug__:
            def stub(*, add_permissions: typing.Optional[builtins.bool] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument add_permissions", value=add_permissions, expected_type=type_hints["add_permissions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if add_permissions is not None:
            self._values["add_permissions"] = add_permissions

    @builtins.property
    def add_permissions(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether or not to add Lambda Permissions.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("add_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KinesisDestination",
    "KinesisDestinationProps",
    "LambdaDestination",
    "LambdaDestinationOptions",
]

publication.publish()
