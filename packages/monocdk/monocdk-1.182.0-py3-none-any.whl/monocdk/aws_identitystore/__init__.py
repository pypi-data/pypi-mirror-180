'''
# AWS::IdentityStore Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import monocdk as identitystore
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IdentityStore construct libraries](https://constructs.dev/search?q=identitystore)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IdentityStore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IdentityStore.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IdentityStore](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IdentityStore.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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

from .. import (
    CfnResource as _CfnResource_e0a482dc,
    Construct as _Construct_e78e779f,
    IInspectable as _IInspectable_82c04a63,
    IResolvable as _IResolvable_a771d0ef,
    TreeInspector as _TreeInspector_1cd1894e,
)


@jsii.implements(_IInspectable_82c04a63)
class CfnGroup(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_identitystore.CfnGroup",
):
    '''A CloudFormation ``AWS::IdentityStore::Group``.

    A group object, which contains a specified group’s metadata and attributes.

    :cloudformationResource: AWS::IdentityStore::Group
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_identitystore as identitystore
        
        cfn_group = identitystore.CfnGroup(self, "MyCfnGroup",
            display_name="displayName",
            identity_store_id="identityStoreId",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        display_name: builtins.str,
        identity_store_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::IdentityStore::Group``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param display_name: ``AWS::IdentityStore::Group.DisplayName``.
        :param identity_store_id: ``AWS::IdentityStore::Group.IdentityStoreId``.
        :param description: A string containing the description of the group.
        '''
        if __debug__:
            def stub(
                scope: _Construct_e78e779f,
                id: builtins.str,
                *,
                display_name: builtins.str,
                identity_store_id: builtins.str,
                description: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupProps(
            display_name=display_name,
            identity_store_id=identity_store_id,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: _TreeInspector_1cd1894e) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGroupId")
    def attr_group_id(self) -> builtins.str:
        '''The identifier of the newly created group in the identity store.

        :cloudformationAttribute: GroupId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGroupId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        '''``AWS::IdentityStore::Group.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-displayname
        '''
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''``AWS::IdentityStore::Group.IdentityStoreId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-identitystoreid
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A string containing the description of the group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-description
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.implements(_IInspectable_82c04a63)
class CfnGroupMembership(
    _CfnResource_e0a482dc,
    metaclass=jsii.JSIIMeta,
    jsii_type="monocdk.aws_identitystore.CfnGroupMembership",
):
    '''A CloudFormation ``AWS::IdentityStore::GroupMembership``.

    Contains the identifiers for a group, a group member, and a ``GroupMembership`` object in the identity store.

    :cloudformationResource: AWS::IdentityStore::GroupMembership
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from monocdk import aws_identitystore as identitystore
        
        cfn_group_membership = identitystore.CfnGroupMembership(self, "MyCfnGroupMembership",
            group_id="groupId",
            identity_store_id="identityStoreId",
            member_id=identitystore.CfnGroupMembership.MemberIdProperty(
                user_id="userId"
            )
        )
    '''

    def __init__(
        self,
        scope: _Construct_e78e779f,
        id: builtins.str,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
        member_id: typing.Union[typing.Union["CfnGroupMembership.MemberIdProperty", typing.Dict[str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Create a new ``AWS::IdentityStore::GroupMembership``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param group_id: ``AWS::IdentityStore::GroupMembership.GroupId``.
        :param identity_store_id: ``AWS::IdentityStore::GroupMembership.IdentityStoreId``.
        :param member_id: An object containing the identifier of a group member. Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.
        '''
        if __debug__:
            def stub(
                scope: _Construct_e78e779f,
                id: builtins.str,
                *,
                group_id: builtins.str,
                identity_store_id: builtins.str,
                member_id: typing.Union[typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[str, typing.Any]], _IResolvable_a771d0ef],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGroupMembershipProps(
            group_id=group_id, identity_store_id=identity_store_id, member_id=member_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_1cd1894e) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: _TreeInspector_1cd1894e) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            def stub(props: typing.Mapping[builtins.str, typing.Any]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMembershipId")
    def attr_membership_id(self) -> builtins.str:
        '''The identifier for a ``GroupMembership`` in the identity store.

        :cloudformationAttribute: MembershipId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMembershipId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="groupId")
    def group_id(self) -> builtins.str:
        '''``AWS::IdentityStore::GroupMembership.GroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-groupid
        '''
        return typing.cast(builtins.str, jsii.get(self, "groupId"))

    @group_id.setter
    def group_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupId", value)

    @builtins.property
    @jsii.member(jsii_name="identityStoreId")
    def identity_store_id(self) -> builtins.str:
        '''``AWS::IdentityStore::GroupMembership.IdentityStoreId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-identitystoreid
        '''
        return typing.cast(builtins.str, jsii.get(self, "identityStoreId"))

    @identity_store_id.setter
    def identity_store_id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityStoreId", value)

    @builtins.property
    @jsii.member(jsii_name="memberId")
    def member_id(
        self,
    ) -> typing.Union["CfnGroupMembership.MemberIdProperty", _IResolvable_a771d0ef]:
        '''An object containing the identifier of a group member.

        Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-memberid
        '''
        return typing.cast(typing.Union["CfnGroupMembership.MemberIdProperty", _IResolvable_a771d0ef], jsii.get(self, "memberId"))

    @member_id.setter
    def member_id(
        self,
        value: typing.Union["CfnGroupMembership.MemberIdProperty", _IResolvable_a771d0ef],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[CfnGroupMembership.MemberIdProperty, _IResolvable_a771d0ef],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memberId", value)

    @jsii.data_type(
        jsii_type="monocdk.aws_identitystore.CfnGroupMembership.MemberIdProperty",
        jsii_struct_bases=[],
        name_mapping={"user_id": "userId"},
    )
    class MemberIdProperty:
        def __init__(self, *, user_id: builtins.str) -> None:
            '''An object that contains the identifier of a group member.

            Setting the ``UserID`` field to the specific identifier for a user indicates that the user is a member of the group.

            :param user_id: ``CfnGroupMembership.MemberIdProperty.UserId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from monocdk import aws_identitystore as identitystore
                
                member_id_property = identitystore.CfnGroupMembership.MemberIdProperty(
                    user_id="userId"
                )
            '''
            if __debug__:
                def stub(*, user_id: builtins.str) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            self._values: typing.Dict[str, typing.Any] = {
                "user_id": user_id,
            }

        @builtins.property
        def user_id(self) -> builtins.str:
            '''``CfnGroupMembership.MemberIdProperty.UserId``.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-identitystore-groupmembership-memberid.html#cfn-identitystore-groupmembership-memberid-userid
            '''
            result = self._values.get("user_id")
            assert result is not None, "Required property 'user_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemberIdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="monocdk.aws_identitystore.CfnGroupMembershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "group_id": "groupId",
        "identity_store_id": "identityStoreId",
        "member_id": "memberId",
    },
)
class CfnGroupMembershipProps:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
        member_id: typing.Union[typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[str, typing.Any]], _IResolvable_a771d0ef],
    ) -> None:
        '''Properties for defining a ``CfnGroupMembership``.

        :param group_id: ``AWS::IdentityStore::GroupMembership.GroupId``.
        :param identity_store_id: ``AWS::IdentityStore::GroupMembership.IdentityStoreId``.
        :param member_id: An object containing the identifier of a group member. Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_identitystore as identitystore
            
            cfn_group_membership_props = identitystore.CfnGroupMembershipProps(
                group_id="groupId",
                identity_store_id="identityStoreId",
                member_id=identitystore.CfnGroupMembership.MemberIdProperty(
                    user_id="userId"
                )
            )
        '''
        if __debug__:
            def stub(
                *,
                group_id: builtins.str,
                identity_store_id: builtins.str,
                member_id: typing.Union[typing.Union[CfnGroupMembership.MemberIdProperty, typing.Dict[str, typing.Any]], _IResolvable_a771d0ef],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_id": group_id,
            "identity_store_id": identity_store_id,
            "member_id": member_id,
        }

    @builtins.property
    def group_id(self) -> builtins.str:
        '''``AWS::IdentityStore::GroupMembership.GroupId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-groupid
        '''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''``AWS::IdentityStore::GroupMembership.IdentityStoreId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(
        self,
    ) -> typing.Union[CfnGroupMembership.MemberIdProperty, _IResolvable_a771d0ef]:
        '''An object containing the identifier of a group member.

        Setting ``MemberId`` 's ``UserId`` field to a specific User's ID indicates we should consider that User as a group member.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-groupmembership.html#cfn-identitystore-groupmembership-memberid
        '''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(typing.Union[CfnGroupMembership.MemberIdProperty, _IResolvable_a771d0ef], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupMembershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="monocdk.aws_identitystore.CfnGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "display_name": "displayName",
        "identity_store_id": "identityStoreId",
        "description": "description",
    },
)
class CfnGroupProps:
    def __init__(
        self,
        *,
        display_name: builtins.str,
        identity_store_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnGroup``.

        :param display_name: ``AWS::IdentityStore::Group.DisplayName``.
        :param identity_store_id: ``AWS::IdentityStore::Group.IdentityStoreId``.
        :param description: A string containing the description of the group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from monocdk import aws_identitystore as identitystore
            
            cfn_group_props = identitystore.CfnGroupProps(
                display_name="displayName",
                identity_store_id="identityStoreId",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            def stub(
                *,
                display_name: builtins.str,
                identity_store_id: builtins.str,
                description: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "identity_store_id": identity_store_id,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def display_name(self) -> builtins.str:
        '''``AWS::IdentityStore::Group.DisplayName``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-displayname
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''``AWS::IdentityStore::Group.IdentityStoreId``.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-identitystoreid
        '''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A string containing the description of the group.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-identitystore-group.html#cfn-identitystore-group-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnGroup",
    "CfnGroupMembership",
    "CfnGroupMembershipProps",
    "CfnGroupProps",
]

publication.publish()
