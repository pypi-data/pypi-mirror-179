'''
# `aws_codedeploy_deployment_group`

Refer to the Terraform Registory for docs: [`aws_codedeploy_deployment_group`](https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group).
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

import cdktf
import constructs


class CodedeployDeploymentGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group aws_codedeploy_deployment_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        app_name: builtins.str,
        deployment_group_name: builtins.str,
        service_role_arn: builtins.str,
        alarm_configuration: typing.Optional[typing.Union["CodedeployDeploymentGroupAlarmConfiguration", typing.Dict[str, typing.Any]]] = None,
        auto_rollback_configuration: typing.Optional[typing.Union["CodedeployDeploymentGroupAutoRollbackConfiguration", typing.Dict[str, typing.Any]]] = None,
        autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        blue_green_deployment_config: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfig", typing.Dict[str, typing.Any]]] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        deployment_style: typing.Optional[typing.Union["CodedeployDeploymentGroupDeploymentStyle", typing.Dict[str, typing.Any]]] = None,
        ec2_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagFilter", typing.Dict[str, typing.Any]]]]] = None,
        ec2_tag_set: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSet", typing.Dict[str, typing.Any]]]]] = None,
        ecs_service: typing.Optional[typing.Union["CodedeployDeploymentGroupEcsService", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfo", typing.Dict[str, typing.Any]]] = None,
        on_premises_instance_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupOnPremisesInstanceTagFilter", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trigger_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupTriggerConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group aws_codedeploy_deployment_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param app_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#app_name CodedeployDeploymentGroup#app_name}.
        :param deployment_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_group_name CodedeployDeploymentGroup#deployment_group_name}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_role_arn CodedeployDeploymentGroup#service_role_arn}.
        :param alarm_configuration: alarm_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarm_configuration CodedeployDeploymentGroup#alarm_configuration}
        :param auto_rollback_configuration: auto_rollback_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#auto_rollback_configuration CodedeployDeploymentGroup#auto_rollback_configuration}
        :param autoscaling_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#autoscaling_groups CodedeployDeploymentGroup#autoscaling_groups}.
        :param blue_green_deployment_config: blue_green_deployment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#blue_green_deployment_config CodedeployDeploymentGroup#blue_green_deployment_config}
        :param deployment_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_config_name CodedeployDeploymentGroup#deployment_config_name}.
        :param deployment_style: deployment_style block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_style CodedeployDeploymentGroup#deployment_style}
        :param ec2_tag_filter: ec2_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        :param ec2_tag_set: ec2_tag_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_set CodedeployDeploymentGroup#ec2_tag_set}
        :param ecs_service: ecs_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ecs_service CodedeployDeploymentGroup#ecs_service}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#id CodedeployDeploymentGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_info: load_balancer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#load_balancer_info CodedeployDeploymentGroup#load_balancer_info}
        :param on_premises_instance_tag_filter: on_premises_instance_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#on_premises_instance_tag_filter CodedeployDeploymentGroup#on_premises_instance_tag_filter}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags CodedeployDeploymentGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags_all CodedeployDeploymentGroup#tags_all}.
        :param trigger_configuration: trigger_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_configuration CodedeployDeploymentGroup#trigger_configuration}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id_: builtins.str,
                *,
                app_name: builtins.str,
                deployment_group_name: builtins.str,
                service_role_arn: builtins.str,
                alarm_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAlarmConfiguration, typing.Dict[str, typing.Any]]] = None,
                auto_rollback_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAutoRollbackConfiguration, typing.Dict[str, typing.Any]]] = None,
                autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                blue_green_deployment_config: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfig, typing.Dict[str, typing.Any]]] = None,
                deployment_config_name: typing.Optional[builtins.str] = None,
                deployment_style: typing.Optional[typing.Union[CodedeployDeploymentGroupDeploymentStyle, typing.Dict[str, typing.Any]]] = None,
                ec2_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagFilter, typing.Dict[str, typing.Any]]]]] = None,
                ec2_tag_set: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSet, typing.Dict[str, typing.Any]]]]] = None,
                ecs_service: typing.Optional[typing.Union[CodedeployDeploymentGroupEcsService, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                load_balancer_info: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfo, typing.Dict[str, typing.Any]]] = None,
                on_premises_instance_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                trigger_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, typing.Dict[str, typing.Any]]]]] = None,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CodedeployDeploymentGroupConfig(
            app_name=app_name,
            deployment_group_name=deployment_group_name,
            service_role_arn=service_role_arn,
            alarm_configuration=alarm_configuration,
            auto_rollback_configuration=auto_rollback_configuration,
            autoscaling_groups=autoscaling_groups,
            blue_green_deployment_config=blue_green_deployment_config,
            deployment_config_name=deployment_config_name,
            deployment_style=deployment_style,
            ec2_tag_filter=ec2_tag_filter,
            ec2_tag_set=ec2_tag_set,
            ecs_service=ecs_service,
            id=id,
            load_balancer_info=load_balancer_info,
            on_premises_instance_tag_filter=on_premises_instance_tag_filter,
            tags=tags,
            tags_all=tags_all,
            trigger_configuration=trigger_configuration,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlarmConfiguration")
    def put_alarm_configuration(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarms CodedeployDeploymentGroup#alarms}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param ignore_poll_alarm_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ignore_poll_alarm_failure CodedeployDeploymentGroup#ignore_poll_alarm_failure}.
        '''
        value = CodedeployDeploymentGroupAlarmConfiguration(
            alarms=alarms,
            enabled=enabled,
            ignore_poll_alarm_failure=ignore_poll_alarm_failure,
        )

        return typing.cast(None, jsii.invoke(self, "putAlarmConfiguration", [value]))

    @jsii.member(jsii_name="putAutoRollbackConfiguration")
    def put_auto_rollback_configuration(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#events CodedeployDeploymentGroup#events}.
        '''
        value = CodedeployDeploymentGroupAutoRollbackConfiguration(
            enabled=enabled, events=events
        )

        return typing.cast(None, jsii.invoke(self, "putAutoRollbackConfiguration", [value]))

    @jsii.member(jsii_name="putBlueGreenDeploymentConfig")
    def put_blue_green_deployment_config(
        self,
        *,
        deployment_ready_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption", typing.Dict[str, typing.Any]]] = None,
        green_fleet_provisioning_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption", typing.Dict[str, typing.Any]]] = None,
        terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param deployment_ready_option: deployment_ready_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_ready_option CodedeployDeploymentGroup#deployment_ready_option}
        :param green_fleet_provisioning_option: green_fleet_provisioning_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#green_fleet_provisioning_option CodedeployDeploymentGroup#green_fleet_provisioning_option}
        :param terminate_blue_instances_on_deployment_success: terminate_blue_instances_on_deployment_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#terminate_blue_instances_on_deployment_success CodedeployDeploymentGroup#terminate_blue_instances_on_deployment_success}
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfig(
            deployment_ready_option=deployment_ready_option,
            green_fleet_provisioning_option=green_fleet_provisioning_option,
            terminate_blue_instances_on_deployment_success=terminate_blue_instances_on_deployment_success,
        )

        return typing.cast(None, jsii.invoke(self, "putBlueGreenDeploymentConfig", [value]))

    @jsii.member(jsii_name="putDeploymentStyle")
    def put_deployment_style(
        self,
        *,
        deployment_option: typing.Optional[builtins.str] = None,
        deployment_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_option CodedeployDeploymentGroup#deployment_option}.
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_type CodedeployDeploymentGroup#deployment_type}.
        '''
        value = CodedeployDeploymentGroupDeploymentStyle(
            deployment_option=deployment_option, deployment_type=deployment_type
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentStyle", [value]))

    @jsii.member(jsii_name="putEc2TagFilter")
    def put_ec2_tag_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagFilter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2TagFilter", [value]))

    @jsii.member(jsii_name="putEc2TagSet")
    def put_ec2_tag_set(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSet", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSet, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2TagSet", [value]))

    @jsii.member(jsii_name="putEcsService")
    def put_ecs_service(
        self,
        *,
        cluster_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#cluster_name CodedeployDeploymentGroup#cluster_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_name CodedeployDeploymentGroup#service_name}.
        '''
        value = CodedeployDeploymentGroupEcsService(
            cluster_name=cluster_name, service_name=service_name
        )

        return typing.cast(None, jsii.invoke(self, "putEcsService", [value]))

    @jsii.member(jsii_name="putLoadBalancerInfo")
    def put_load_balancer_info(
        self,
        *,
        elb_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoElbInfo", typing.Dict[str, typing.Any]]]]] = None,
        target_group_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo", typing.Dict[str, typing.Any]]]]] = None,
        target_group_pair_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_info: elb_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#elb_info CodedeployDeploymentGroup#elb_info}
        :param target_group_info: target_group_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_info CodedeployDeploymentGroup#target_group_info}
        :param target_group_pair_info: target_group_pair_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_pair_info CodedeployDeploymentGroup#target_group_pair_info}
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfo(
            elb_info=elb_info,
            target_group_info=target_group_info,
            target_group_pair_info=target_group_pair_info,
        )

        return typing.cast(None, jsii.invoke(self, "putLoadBalancerInfo", [value]))

    @jsii.member(jsii_name="putOnPremisesInstanceTagFilter")
    def put_on_premises_instance_tag_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupOnPremisesInstanceTagFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOnPremisesInstanceTagFilter", [value]))

    @jsii.member(jsii_name="putTriggerConfiguration")
    def put_trigger_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupTriggerConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTriggerConfiguration", [value]))

    @jsii.member(jsii_name="resetAlarmConfiguration")
    def reset_alarm_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarmConfiguration", []))

    @jsii.member(jsii_name="resetAutoRollbackConfiguration")
    def reset_auto_rollback_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoRollbackConfiguration", []))

    @jsii.member(jsii_name="resetAutoscalingGroups")
    def reset_autoscaling_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoscalingGroups", []))

    @jsii.member(jsii_name="resetBlueGreenDeploymentConfig")
    def reset_blue_green_deployment_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlueGreenDeploymentConfig", []))

    @jsii.member(jsii_name="resetDeploymentConfigName")
    def reset_deployment_config_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentConfigName", []))

    @jsii.member(jsii_name="resetDeploymentStyle")
    def reset_deployment_style(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentStyle", []))

    @jsii.member(jsii_name="resetEc2TagFilter")
    def reset_ec2_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2TagFilter", []))

    @jsii.member(jsii_name="resetEc2TagSet")
    def reset_ec2_tag_set(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2TagSet", []))

    @jsii.member(jsii_name="resetEcsService")
    def reset_ecs_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEcsService", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLoadBalancerInfo")
    def reset_load_balancer_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerInfo", []))

    @jsii.member(jsii_name="resetOnPremisesInstanceTagFilter")
    def reset_on_premises_instance_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnPremisesInstanceTagFilter", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="resetTriggerConfiguration")
    def reset_trigger_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTriggerConfiguration", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alarmConfiguration")
    def alarm_configuration(
        self,
    ) -> "CodedeployDeploymentGroupAlarmConfigurationOutputReference":
        return typing.cast("CodedeployDeploymentGroupAlarmConfigurationOutputReference", jsii.get(self, "alarmConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfiguration")
    def auto_rollback_configuration(
        self,
    ) -> "CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference":
        return typing.cast("CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference", jsii.get(self, "autoRollbackConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenDeploymentConfig")
    def blue_green_deployment_config(
        self,
    ) -> "CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference":
        return typing.cast("CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference", jsii.get(self, "blueGreenDeploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "computePlatform"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupId")
    def deployment_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupId"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStyle")
    def deployment_style(
        self,
    ) -> "CodedeployDeploymentGroupDeploymentStyleOutputReference":
        return typing.cast("CodedeployDeploymentGroupDeploymentStyleOutputReference", jsii.get(self, "deploymentStyle"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilter")
    def ec2_tag_filter(self) -> "CodedeployDeploymentGroupEc2TagFilterList":
        return typing.cast("CodedeployDeploymentGroupEc2TagFilterList", jsii.get(self, "ec2TagFilter"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagSet")
    def ec2_tag_set(self) -> "CodedeployDeploymentGroupEc2TagSetList":
        return typing.cast("CodedeployDeploymentGroupEc2TagSetList", jsii.get(self, "ec2TagSet"))

    @builtins.property
    @jsii.member(jsii_name="ecsService")
    def ecs_service(self) -> "CodedeployDeploymentGroupEcsServiceOutputReference":
        return typing.cast("CodedeployDeploymentGroupEcsServiceOutputReference", jsii.get(self, "ecsService"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInfo")
    def load_balancer_info(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoOutputReference", jsii.get(self, "loadBalancerInfo"))

    @builtins.property
    @jsii.member(jsii_name="onPremisesInstanceTagFilter")
    def on_premises_instance_tag_filter(
        self,
    ) -> "CodedeployDeploymentGroupOnPremisesInstanceTagFilterList":
        return typing.cast("CodedeployDeploymentGroupOnPremisesInstanceTagFilterList", jsii.get(self, "onPremisesInstanceTagFilter"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfiguration")
    def trigger_configuration(
        self,
    ) -> "CodedeployDeploymentGroupTriggerConfigurationList":
        return typing.cast("CodedeployDeploymentGroupTriggerConfigurationList", jsii.get(self, "triggerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="alarmConfigurationInput")
    def alarm_configuration_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupAlarmConfiguration"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupAlarmConfiguration"], jsii.get(self, "alarmConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="appNameInput")
    def app_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfigurationInput")
    def auto_rollback_configuration_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupAutoRollbackConfiguration"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupAutoRollbackConfiguration"], jsii.get(self, "autoRollbackConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroupsInput")
    def autoscaling_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoscalingGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="blueGreenDeploymentConfigInput")
    def blue_green_deployment_config_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfig"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfig"], jsii.get(self, "blueGreenDeploymentConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigNameInput")
    def deployment_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupNameInput")
    def deployment_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentStyleInput")
    def deployment_style_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupDeploymentStyle"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupDeploymentStyle"], jsii.get(self, "deploymentStyleInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilterInput")
    def ec2_tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]], jsii.get(self, "ec2TagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagSetInput")
    def ec2_tag_set_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]], jsii.get(self, "ec2TagSetInput"))

    @builtins.property
    @jsii.member(jsii_name="ecsServiceInput")
    def ecs_service_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupEcsService"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupEcsService"], jsii.get(self, "ecsServiceInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInfoInput")
    def load_balancer_info_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"], jsii.get(self, "loadBalancerInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="onPremisesInstanceTagFilterInput")
    def on_premises_instance_tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]], jsii.get(self, "onPremisesInstanceTagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArnInput")
    def service_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerConfigurationInput")
    def trigger_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]], jsii.get(self, "triggerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="appName")
    def app_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appName"))

    @app_name.setter
    def app_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appName", value)

    @builtins.property
    @jsii.member(jsii_name="autoscalingGroups")
    def autoscaling_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "autoscalingGroups"))

    @autoscaling_groups.setter
    def autoscaling_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoscalingGroups", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))

    @deployment_config_name.setter
    def deployment_config_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @deployment_group_name.setter
    def deployment_group_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAlarmConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "enabled": "enabled",
        "ignore_poll_alarm_failure": "ignorePollAlarmFailure",
    },
)
class CodedeployDeploymentGroupAlarmConfiguration:
    def __init__(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param alarms: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarms CodedeployDeploymentGroup#alarms}.
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param ignore_poll_alarm_failure: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ignore_poll_alarm_failure CodedeployDeploymentGroup#ignore_poll_alarm_failure}.
        '''
        if __debug__:
            def stub(
                *,
                alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument ignore_poll_alarm_failure", value=ignore_poll_alarm_failure, expected_type=type_hints["ignore_poll_alarm_failure"])
        self._values: typing.Dict[str, typing.Any] = {}
        if alarms is not None:
            self._values["alarms"] = alarms
        if enabled is not None:
            self._values["enabled"] = enabled
        if ignore_poll_alarm_failure is not None:
            self._values["ignore_poll_alarm_failure"] = ignore_poll_alarm_failure

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarms CodedeployDeploymentGroup#alarms}.'''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ignore_poll_alarm_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ignore_poll_alarm_failure CodedeployDeploymentGroup#ignore_poll_alarm_failure}.'''
        result = self._values.get("ignore_poll_alarm_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupAlarmConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupAlarmConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAlarmConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAlarms")
    def reset_alarms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlarms", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetIgnorePollAlarmFailure")
    def reset_ignore_poll_alarm_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnorePollAlarmFailure", []))

    @builtins.property
    @jsii.member(jsii_name="alarmsInput")
    def alarms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "alarmsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ignorePollAlarmFailureInput")
    def ignore_poll_alarm_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignorePollAlarmFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="alarms")
    def alarms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "alarms"))

    @alarms.setter
    def alarms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarms", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="ignorePollAlarmFailure")
    def ignore_poll_alarm_failure(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignorePollAlarmFailure"))

    @ignore_poll_alarm_failure.setter
    def ignore_poll_alarm_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignorePollAlarmFailure", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAlarmConfiguration]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAlarmConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupAlarmConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupAlarmConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAutoRollbackConfiguration",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "events": "events"},
)
class CodedeployDeploymentGroupAutoRollbackConfiguration:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        events: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.
        :param events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#events CodedeployDeploymentGroup#events}.
        '''
        if __debug__:
            def stub(
                *,
                enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                events: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if events is not None:
            self._values["events"] = events

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#enabled CodedeployDeploymentGroup#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#events CodedeployDeploymentGroup#events}.'''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupAutoRollbackConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEvents")
    def reset_events(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvents", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="eventsInput")
    def events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "events"))

    @events.setter
    def events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfig",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_ready_option": "deploymentReadyOption",
        "green_fleet_provisioning_option": "greenFleetProvisioningOption",
        "terminate_blue_instances_on_deployment_success": "terminateBlueInstancesOnDeploymentSuccess",
    },
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfig:
    def __init__(
        self,
        *,
        deployment_ready_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption", typing.Dict[str, typing.Any]]] = None,
        green_fleet_provisioning_option: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption", typing.Dict[str, typing.Any]]] = None,
        terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param deployment_ready_option: deployment_ready_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_ready_option CodedeployDeploymentGroup#deployment_ready_option}
        :param green_fleet_provisioning_option: green_fleet_provisioning_option block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#green_fleet_provisioning_option CodedeployDeploymentGroup#green_fleet_provisioning_option}
        :param terminate_blue_instances_on_deployment_success: terminate_blue_instances_on_deployment_success block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#terminate_blue_instances_on_deployment_success CodedeployDeploymentGroup#terminate_blue_instances_on_deployment_success}
        '''
        if isinstance(deployment_ready_option, dict):
            deployment_ready_option = CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(**deployment_ready_option)
        if isinstance(green_fleet_provisioning_option, dict):
            green_fleet_provisioning_option = CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(**green_fleet_provisioning_option)
        if isinstance(terminate_blue_instances_on_deployment_success, dict):
            terminate_blue_instances_on_deployment_success = CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(**terminate_blue_instances_on_deployment_success)
        if __debug__:
            def stub(
                *,
                deployment_ready_option: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption, typing.Dict[str, typing.Any]]] = None,
                green_fleet_provisioning_option: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption, typing.Dict[str, typing.Any]]] = None,
                terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument deployment_ready_option", value=deployment_ready_option, expected_type=type_hints["deployment_ready_option"])
            check_type(argname="argument green_fleet_provisioning_option", value=green_fleet_provisioning_option, expected_type=type_hints["green_fleet_provisioning_option"])
            check_type(argname="argument terminate_blue_instances_on_deployment_success", value=terminate_blue_instances_on_deployment_success, expected_type=type_hints["terminate_blue_instances_on_deployment_success"])
        self._values: typing.Dict[str, typing.Any] = {}
        if deployment_ready_option is not None:
            self._values["deployment_ready_option"] = deployment_ready_option
        if green_fleet_provisioning_option is not None:
            self._values["green_fleet_provisioning_option"] = green_fleet_provisioning_option
        if terminate_blue_instances_on_deployment_success is not None:
            self._values["terminate_blue_instances_on_deployment_success"] = terminate_blue_instances_on_deployment_success

    @builtins.property
    def deployment_ready_option(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption"]:
        '''deployment_ready_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_ready_option CodedeployDeploymentGroup#deployment_ready_option}
        '''
        result = self._values.get("deployment_ready_option")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption"], result)

    @builtins.property
    def green_fleet_provisioning_option(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption"]:
        '''green_fleet_provisioning_option block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#green_fleet_provisioning_option CodedeployDeploymentGroup#green_fleet_provisioning_option}
        '''
        result = self._values.get("green_fleet_provisioning_option")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption"], result)

    @builtins.property
    def terminate_blue_instances_on_deployment_success(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"]:
        '''terminate_blue_instances_on_deployment_success block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#terminate_blue_instances_on_deployment_success CodedeployDeploymentGroup#terminate_blue_instances_on_deployment_success}
        '''
        result = self._values.get("terminate_blue_instances_on_deployment_success")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption",
    jsii_struct_bases=[],
    name_mapping={
        "action_on_timeout": "actionOnTimeout",
        "wait_time_in_minutes": "waitTimeInMinutes",
    },
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption:
    def __init__(
        self,
        *,
        action_on_timeout: typing.Optional[builtins.str] = None,
        wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action_on_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action_on_timeout CodedeployDeploymentGroup#action_on_timeout}.
        :param wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#wait_time_in_minutes CodedeployDeploymentGroup#wait_time_in_minutes}.
        '''
        if __debug__:
            def stub(
                *,
                action_on_timeout: typing.Optional[builtins.str] = None,
                wait_time_in_minutes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action_on_timeout", value=action_on_timeout, expected_type=type_hints["action_on_timeout"])
            check_type(argname="argument wait_time_in_minutes", value=wait_time_in_minutes, expected_type=type_hints["wait_time_in_minutes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action_on_timeout is not None:
            self._values["action_on_timeout"] = action_on_timeout
        if wait_time_in_minutes is not None:
            self._values["wait_time_in_minutes"] = wait_time_in_minutes

    @builtins.property
    def action_on_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action_on_timeout CodedeployDeploymentGroup#action_on_timeout}.'''
        result = self._values.get("action_on_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#wait_time_in_minutes CodedeployDeploymentGroup#wait_time_in_minutes}.'''
        result = self._values.get("wait_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetActionOnTimeout")
    def reset_action_on_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionOnTimeout", []))

    @jsii.member(jsii_name="resetWaitTimeInMinutes")
    def reset_wait_time_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitTimeInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="actionOnTimeoutInput")
    def action_on_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionOnTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="waitTimeInMinutesInput")
    def wait_time_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "waitTimeInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="actionOnTimeout")
    def action_on_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionOnTimeout"))

    @action_on_timeout.setter
    def action_on_timeout(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionOnTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="waitTimeInMinutes")
    def wait_time_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "waitTimeInMinutes"))

    @wait_time_in_minutes.setter
    def wait_time_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitTimeInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption",
    jsii_struct_bases=[],
    name_mapping={"action": "action"},
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption:
    def __init__(self, *, action: typing.Optional[builtins.str] = None) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        '''
        if __debug__:
            def stub(*, action: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeploymentReadyOption")
    def put_deployment_ready_option(
        self,
        *,
        action_on_timeout: typing.Optional[builtins.str] = None,
        wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action_on_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action_on_timeout CodedeployDeploymentGroup#action_on_timeout}.
        :param wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#wait_time_in_minutes CodedeployDeploymentGroup#wait_time_in_minutes}.
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption(
            action_on_timeout=action_on_timeout,
            wait_time_in_minutes=wait_time_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putDeploymentReadyOption", [value]))

    @jsii.member(jsii_name="putGreenFleetProvisioningOption")
    def put_green_fleet_provisioning_option(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption(
            action=action
        )

        return typing.cast(None, jsii.invoke(self, "putGreenFleetProvisioningOption", [value]))

    @jsii.member(jsii_name="putTerminateBlueInstancesOnDeploymentSuccess")
    def put_terminate_blue_instances_on_deployment_success(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        :param termination_wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#termination_wait_time_in_minutes CodedeployDeploymentGroup#termination_wait_time_in_minutes}.
        '''
        value = CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(
            action=action,
            termination_wait_time_in_minutes=termination_wait_time_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putTerminateBlueInstancesOnDeploymentSuccess", [value]))

    @jsii.member(jsii_name="resetDeploymentReadyOption")
    def reset_deployment_ready_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentReadyOption", []))

    @jsii.member(jsii_name="resetGreenFleetProvisioningOption")
    def reset_green_fleet_provisioning_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGreenFleetProvisioningOption", []))

    @jsii.member(jsii_name="resetTerminateBlueInstancesOnDeploymentSuccess")
    def reset_terminate_blue_instances_on_deployment_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminateBlueInstancesOnDeploymentSuccess", []))

    @builtins.property
    @jsii.member(jsii_name="deploymentReadyOption")
    def deployment_ready_option(
        self,
    ) -> CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference:
        return typing.cast(CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference, jsii.get(self, "deploymentReadyOption"))

    @builtins.property
    @jsii.member(jsii_name="greenFleetProvisioningOption")
    def green_fleet_provisioning_option(
        self,
    ) -> CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference:
        return typing.cast(CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference, jsii.get(self, "greenFleetProvisioningOption"))

    @builtins.property
    @jsii.member(jsii_name="terminateBlueInstancesOnDeploymentSuccess")
    def terminate_blue_instances_on_deployment_success(
        self,
    ) -> "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference":
        return typing.cast("CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference", jsii.get(self, "terminateBlueInstancesOnDeploymentSuccess"))

    @builtins.property
    @jsii.member(jsii_name="deploymentReadyOptionInput")
    def deployment_ready_option_input(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption], jsii.get(self, "deploymentReadyOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="greenFleetProvisioningOptionInput")
    def green_fleet_provisioning_option_input(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption], jsii.get(self, "greenFleetProvisioningOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="terminateBlueInstancesOnDeploymentSuccessInput")
    def terminate_blue_instances_on_deployment_success_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess"], jsii.get(self, "terminateBlueInstancesOnDeploymentSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "termination_wait_time_in_minutes": "terminationWaitTimeInMinutes",
    },
)
class CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess:
    def __init__(
        self,
        *,
        action: typing.Optional[builtins.str] = None,
        termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.
        :param termination_wait_time_in_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#termination_wait_time_in_minutes CodedeployDeploymentGroup#termination_wait_time_in_minutes}.
        '''
        if __debug__:
            def stub(
                *,
                action: typing.Optional[builtins.str] = None,
                termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument termination_wait_time_in_minutes", value=termination_wait_time_in_minutes, expected_type=type_hints["termination_wait_time_in_minutes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if action is not None:
            self._values["action"] = action
        if termination_wait_time_in_minutes is not None:
            self._values["termination_wait_time_in_minutes"] = termination_wait_time_in_minutes

    @builtins.property
    def action(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#action CodedeployDeploymentGroup#action}.'''
        result = self._values.get("action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def termination_wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#termination_wait_time_in_minutes CodedeployDeploymentGroup#termination_wait_time_in_minutes}.'''
        result = self._values.get("termination_wait_time_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAction")
    def reset_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAction", []))

    @jsii.member(jsii_name="resetTerminationWaitTimeInMinutes")
    def reset_termination_wait_time_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTerminationWaitTimeInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="terminationWaitTimeInMinutesInput")
    def termination_wait_time_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "terminationWaitTimeInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="terminationWaitTimeInMinutes")
    def termination_wait_time_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "terminationWaitTimeInMinutes"))

    @termination_wait_time_in_minutes.setter
    def termination_wait_time_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminationWaitTimeInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "app_name": "appName",
        "deployment_group_name": "deploymentGroupName",
        "service_role_arn": "serviceRoleArn",
        "alarm_configuration": "alarmConfiguration",
        "auto_rollback_configuration": "autoRollbackConfiguration",
        "autoscaling_groups": "autoscalingGroups",
        "blue_green_deployment_config": "blueGreenDeploymentConfig",
        "deployment_config_name": "deploymentConfigName",
        "deployment_style": "deploymentStyle",
        "ec2_tag_filter": "ec2TagFilter",
        "ec2_tag_set": "ec2TagSet",
        "ecs_service": "ecsService",
        "id": "id",
        "load_balancer_info": "loadBalancerInfo",
        "on_premises_instance_tag_filter": "onPremisesInstanceTagFilter",
        "tags": "tags",
        "tags_all": "tagsAll",
        "trigger_configuration": "triggerConfiguration",
    },
)
class CodedeployDeploymentGroupConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        app_name: builtins.str,
        deployment_group_name: builtins.str,
        service_role_arn: builtins.str,
        alarm_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAlarmConfiguration, typing.Dict[str, typing.Any]]] = None,
        auto_rollback_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAutoRollbackConfiguration, typing.Dict[str, typing.Any]]] = None,
        autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        blue_green_deployment_config: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfig, typing.Dict[str, typing.Any]]] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        deployment_style: typing.Optional[typing.Union["CodedeployDeploymentGroupDeploymentStyle", typing.Dict[str, typing.Any]]] = None,
        ec2_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagFilter", typing.Dict[str, typing.Any]]]]] = None,
        ec2_tag_set: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSet", typing.Dict[str, typing.Any]]]]] = None,
        ecs_service: typing.Optional[typing.Union["CodedeployDeploymentGroupEcsService", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        load_balancer_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfo", typing.Dict[str, typing.Any]]] = None,
        on_premises_instance_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupOnPremisesInstanceTagFilter", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trigger_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupTriggerConfiguration", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param app_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#app_name CodedeployDeploymentGroup#app_name}.
        :param deployment_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_group_name CodedeployDeploymentGroup#deployment_group_name}.
        :param service_role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_role_arn CodedeployDeploymentGroup#service_role_arn}.
        :param alarm_configuration: alarm_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarm_configuration CodedeployDeploymentGroup#alarm_configuration}
        :param auto_rollback_configuration: auto_rollback_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#auto_rollback_configuration CodedeployDeploymentGroup#auto_rollback_configuration}
        :param autoscaling_groups: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#autoscaling_groups CodedeployDeploymentGroup#autoscaling_groups}.
        :param blue_green_deployment_config: blue_green_deployment_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#blue_green_deployment_config CodedeployDeploymentGroup#blue_green_deployment_config}
        :param deployment_config_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_config_name CodedeployDeploymentGroup#deployment_config_name}.
        :param deployment_style: deployment_style block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_style CodedeployDeploymentGroup#deployment_style}
        :param ec2_tag_filter: ec2_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        :param ec2_tag_set: ec2_tag_set block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_set CodedeployDeploymentGroup#ec2_tag_set}
        :param ecs_service: ecs_service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ecs_service CodedeployDeploymentGroup#ecs_service}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#id CodedeployDeploymentGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param load_balancer_info: load_balancer_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#load_balancer_info CodedeployDeploymentGroup#load_balancer_info}
        :param on_premises_instance_tag_filter: on_premises_instance_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#on_premises_instance_tag_filter CodedeployDeploymentGroup#on_premises_instance_tag_filter}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags CodedeployDeploymentGroup#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags_all CodedeployDeploymentGroup#tags_all}.
        :param trigger_configuration: trigger_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_configuration CodedeployDeploymentGroup#trigger_configuration}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alarm_configuration, dict):
            alarm_configuration = CodedeployDeploymentGroupAlarmConfiguration(**alarm_configuration)
        if isinstance(auto_rollback_configuration, dict):
            auto_rollback_configuration = CodedeployDeploymentGroupAutoRollbackConfiguration(**auto_rollback_configuration)
        if isinstance(blue_green_deployment_config, dict):
            blue_green_deployment_config = CodedeployDeploymentGroupBlueGreenDeploymentConfig(**blue_green_deployment_config)
        if isinstance(deployment_style, dict):
            deployment_style = CodedeployDeploymentGroupDeploymentStyle(**deployment_style)
        if isinstance(ecs_service, dict):
            ecs_service = CodedeployDeploymentGroupEcsService(**ecs_service)
        if isinstance(load_balancer_info, dict):
            load_balancer_info = CodedeployDeploymentGroupLoadBalancerInfo(**load_balancer_info)
        if __debug__:
            def stub(
                *,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
                app_name: builtins.str,
                deployment_group_name: builtins.str,
                service_role_arn: builtins.str,
                alarm_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAlarmConfiguration, typing.Dict[str, typing.Any]]] = None,
                auto_rollback_configuration: typing.Optional[typing.Union[CodedeployDeploymentGroupAutoRollbackConfiguration, typing.Dict[str, typing.Any]]] = None,
                autoscaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                blue_green_deployment_config: typing.Optional[typing.Union[CodedeployDeploymentGroupBlueGreenDeploymentConfig, typing.Dict[str, typing.Any]]] = None,
                deployment_config_name: typing.Optional[builtins.str] = None,
                deployment_style: typing.Optional[typing.Union[CodedeployDeploymentGroupDeploymentStyle, typing.Dict[str, typing.Any]]] = None,
                ec2_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagFilter, typing.Dict[str, typing.Any]]]]] = None,
                ec2_tag_set: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSet, typing.Dict[str, typing.Any]]]]] = None,
                ecs_service: typing.Optional[typing.Union[CodedeployDeploymentGroupEcsService, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                load_balancer_info: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfo, typing.Dict[str, typing.Any]]] = None,
                on_premises_instance_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, typing.Dict[str, typing.Any]]]]] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                trigger_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument app_name", value=app_name, expected_type=type_hints["app_name"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument alarm_configuration", value=alarm_configuration, expected_type=type_hints["alarm_configuration"])
            check_type(argname="argument auto_rollback_configuration", value=auto_rollback_configuration, expected_type=type_hints["auto_rollback_configuration"])
            check_type(argname="argument autoscaling_groups", value=autoscaling_groups, expected_type=type_hints["autoscaling_groups"])
            check_type(argname="argument blue_green_deployment_config", value=blue_green_deployment_config, expected_type=type_hints["blue_green_deployment_config"])
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument deployment_style", value=deployment_style, expected_type=type_hints["deployment_style"])
            check_type(argname="argument ec2_tag_filter", value=ec2_tag_filter, expected_type=type_hints["ec2_tag_filter"])
            check_type(argname="argument ec2_tag_set", value=ec2_tag_set, expected_type=type_hints["ec2_tag_set"])
            check_type(argname="argument ecs_service", value=ecs_service, expected_type=type_hints["ecs_service"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument load_balancer_info", value=load_balancer_info, expected_type=type_hints["load_balancer_info"])
            check_type(argname="argument on_premises_instance_tag_filter", value=on_premises_instance_tag_filter, expected_type=type_hints["on_premises_instance_tag_filter"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
            check_type(argname="argument trigger_configuration", value=trigger_configuration, expected_type=type_hints["trigger_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "app_name": app_name,
            "deployment_group_name": deployment_group_name,
            "service_role_arn": service_role_arn,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if alarm_configuration is not None:
            self._values["alarm_configuration"] = alarm_configuration
        if auto_rollback_configuration is not None:
            self._values["auto_rollback_configuration"] = auto_rollback_configuration
        if autoscaling_groups is not None:
            self._values["autoscaling_groups"] = autoscaling_groups
        if blue_green_deployment_config is not None:
            self._values["blue_green_deployment_config"] = blue_green_deployment_config
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if deployment_style is not None:
            self._values["deployment_style"] = deployment_style
        if ec2_tag_filter is not None:
            self._values["ec2_tag_filter"] = ec2_tag_filter
        if ec2_tag_set is not None:
            self._values["ec2_tag_set"] = ec2_tag_set
        if ecs_service is not None:
            self._values["ecs_service"] = ecs_service
        if id is not None:
            self._values["id"] = id
        if load_balancer_info is not None:
            self._values["load_balancer_info"] = load_balancer_info
        if on_premises_instance_tag_filter is not None:
            self._values["on_premises_instance_tag_filter"] = on_premises_instance_tag_filter
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all
        if trigger_configuration is not None:
            self._values["trigger_configuration"] = trigger_configuration

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def app_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#app_name CodedeployDeploymentGroup#app_name}.'''
        result = self._values.get("app_name")
        assert result is not None, "Required property 'app_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_group_name CodedeployDeploymentGroup#deployment_group_name}.'''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_role_arn CodedeployDeploymentGroup#service_role_arn}.'''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_configuration(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAlarmConfiguration]:
        '''alarm_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#alarm_configuration CodedeployDeploymentGroup#alarm_configuration}
        '''
        result = self._values.get("alarm_configuration")
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAlarmConfiguration], result)

    @builtins.property
    def auto_rollback_configuration(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration]:
        '''auto_rollback_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#auto_rollback_configuration CodedeployDeploymentGroup#auto_rollback_configuration}
        '''
        result = self._values.get("auto_rollback_configuration")
        return typing.cast(typing.Optional[CodedeployDeploymentGroupAutoRollbackConfiguration], result)

    @builtins.property
    def autoscaling_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#autoscaling_groups CodedeployDeploymentGroup#autoscaling_groups}.'''
        result = self._values.get("autoscaling_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def blue_green_deployment_config(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig]:
        '''blue_green_deployment_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#blue_green_deployment_config CodedeployDeploymentGroup#blue_green_deployment_config}
        '''
        result = self._values.get("blue_green_deployment_config")
        return typing.cast(typing.Optional[CodedeployDeploymentGroupBlueGreenDeploymentConfig], result)

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_config_name CodedeployDeploymentGroup#deployment_config_name}.'''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_style(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupDeploymentStyle"]:
        '''deployment_style block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_style CodedeployDeploymentGroup#deployment_style}
        '''
        result = self._values.get("deployment_style")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupDeploymentStyle"], result)

    @builtins.property
    def ec2_tag_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]]:
        '''ec2_tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        '''
        result = self._values.get("ec2_tag_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagFilter"]]], result)

    @builtins.property
    def ec2_tag_set(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]]:
        '''ec2_tag_set block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_set CodedeployDeploymentGroup#ec2_tag_set}
        '''
        result = self._values.get("ec2_tag_set")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSet"]]], result)

    @builtins.property
    def ecs_service(self) -> typing.Optional["CodedeployDeploymentGroupEcsService"]:
        '''ecs_service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ecs_service CodedeployDeploymentGroup#ecs_service}
        '''
        result = self._values.get("ecs_service")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupEcsService"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#id CodedeployDeploymentGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def load_balancer_info(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"]:
        '''load_balancer_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#load_balancer_info CodedeployDeploymentGroup#load_balancer_info}
        '''
        result = self._values.get("load_balancer_info")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfo"], result)

    @builtins.property
    def on_premises_instance_tag_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]]:
        '''on_premises_instance_tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#on_premises_instance_tag_filter CodedeployDeploymentGroup#on_premises_instance_tag_filter}
        '''
        result = self._values.get("on_premises_instance_tag_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupOnPremisesInstanceTagFilter"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags CodedeployDeploymentGroup#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#tags_all CodedeployDeploymentGroup#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def trigger_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]]:
        '''trigger_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_configuration CodedeployDeploymentGroup#trigger_configuration}
        '''
        result = self._values.get("trigger_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupTriggerConfiguration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupDeploymentStyle",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_option": "deploymentOption",
        "deployment_type": "deploymentType",
    },
)
class CodedeployDeploymentGroupDeploymentStyle:
    def __init__(
        self,
        *,
        deployment_option: typing.Optional[builtins.str] = None,
        deployment_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param deployment_option: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_option CodedeployDeploymentGroup#deployment_option}.
        :param deployment_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_type CodedeployDeploymentGroup#deployment_type}.
        '''
        if __debug__:
            def stub(
                *,
                deployment_option: typing.Optional[builtins.str] = None,
                deployment_type: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument deployment_option", value=deployment_option, expected_type=type_hints["deployment_option"])
            check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if deployment_option is not None:
            self._values["deployment_option"] = deployment_option
        if deployment_type is not None:
            self._values["deployment_type"] = deployment_type

    @builtins.property
    def deployment_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_option CodedeployDeploymentGroup#deployment_option}.'''
        result = self._values.get("deployment_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#deployment_type CodedeployDeploymentGroup#deployment_type}.'''
        result = self._values.get("deployment_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupDeploymentStyle(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupDeploymentStyleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupDeploymentStyleOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDeploymentOption")
    def reset_deployment_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentOption", []))

    @jsii.member(jsii_name="resetDeploymentType")
    def reset_deployment_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeploymentType", []))

    @builtins.property
    @jsii.member(jsii_name="deploymentOptionInput")
    def deployment_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentTypeInput")
    def deployment_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="deploymentOption")
    def deployment_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentOption"))

    @deployment_option.setter
    def deployment_option(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentOption", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentType")
    def deployment_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "deploymentType"))

    @deployment_type.setter
    def deployment_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupDeploymentStyle]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupDeploymentStyle], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupDeploymentStyle],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupDeploymentStyle],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CodedeployDeploymentGroupEc2TagFilter:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEc2TagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupEc2TagFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagFilterList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupEc2TagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupEc2TagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagFilter]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagFilter, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSet",
    jsii_struct_bases=[],
    name_mapping={"ec2_tag_filter": "ec2TagFilter"},
)
class CodedeployDeploymentGroupEc2TagSet:
    def __init__(
        self,
        *,
        ec2_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupEc2TagSetEc2TagFilter", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param ec2_tag_filter: ec2_tag_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        '''
        if __debug__:
            def stub(
                *,
                ec2_tag_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ec2_tag_filter", value=ec2_tag_filter, expected_type=type_hints["ec2_tag_filter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ec2_tag_filter is not None:
            self._values["ec2_tag_filter"] = ec2_tag_filter

    @builtins.property
    def ec2_tag_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSetEc2TagFilter"]]]:
        '''ec2_tag_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#ec2_tag_filter CodedeployDeploymentGroup#ec2_tag_filter}
        '''
        result = self._values.get("ec2_tag_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupEc2TagSetEc2TagFilter"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEc2TagSet(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetEc2TagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CodedeployDeploymentGroupEc2TagSetEc2TagFilter:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEc2TagSetEc2TagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupEc2TagSetEc2TagFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetEc2TagFilterList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagSetList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupEc2TagSetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupEc2TagSetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSet]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupEc2TagSetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEc2TagSetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEc2TagFilter")
    def put_ec2_tag_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupEc2TagSetEc2TagFilter, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEc2TagFilter", [value]))

    @jsii.member(jsii_name="resetEc2TagFilter")
    def reset_ec2_tag_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2TagFilter", []))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilter")
    def ec2_tag_filter(self) -> CodedeployDeploymentGroupEc2TagSetEc2TagFilterList:
        return typing.cast(CodedeployDeploymentGroupEc2TagSetEc2TagFilterList, jsii.get(self, "ec2TagFilter"))

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilterInput")
    def ec2_tag_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupEc2TagSetEc2TagFilter]]], jsii.get(self, "ec2TagFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupEc2TagSet, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEcsService",
    jsii_struct_bases=[],
    name_mapping={"cluster_name": "clusterName", "service_name": "serviceName"},
)
class CodedeployDeploymentGroupEcsService:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''
        :param cluster_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#cluster_name CodedeployDeploymentGroup#cluster_name}.
        :param service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_name CodedeployDeploymentGroup#service_name}.
        '''
        if __debug__:
            def stub(*, cluster_name: builtins.str, service_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
            "service_name": service_name,
        }

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#cluster_name CodedeployDeploymentGroup#cluster_name}.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#service_name CodedeployDeploymentGroup#service_name}.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupEcsService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupEcsServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupEcsServiceOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceNameInput")
    def service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CodedeployDeploymentGroupEcsService]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupEcsService], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupEcsService],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupEcsService],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfo",
    jsii_struct_bases=[],
    name_mapping={
        "elb_info": "elbInfo",
        "target_group_info": "targetGroupInfo",
        "target_group_pair_info": "targetGroupPairInfo",
    },
)
class CodedeployDeploymentGroupLoadBalancerInfo:
    def __init__(
        self,
        *,
        elb_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoElbInfo", typing.Dict[str, typing.Any]]]]] = None,
        target_group_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo", typing.Dict[str, typing.Any]]]]] = None,
        target_group_pair_info: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param elb_info: elb_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#elb_info CodedeployDeploymentGroup#elb_info}
        :param target_group_info: target_group_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_info CodedeployDeploymentGroup#target_group_info}
        :param target_group_pair_info: target_group_pair_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_pair_info CodedeployDeploymentGroup#target_group_pair_info}
        '''
        if isinstance(target_group_pair_info, dict):
            target_group_pair_info = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo(**target_group_pair_info)
        if __debug__:
            def stub(
                *,
                elb_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, typing.Dict[str, typing.Any]]]]] = None,
                target_group_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, typing.Dict[str, typing.Any]]]]] = None,
                target_group_pair_info: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument elb_info", value=elb_info, expected_type=type_hints["elb_info"])
            check_type(argname="argument target_group_info", value=target_group_info, expected_type=type_hints["target_group_info"])
            check_type(argname="argument target_group_pair_info", value=target_group_pair_info, expected_type=type_hints["target_group_pair_info"])
        self._values: typing.Dict[str, typing.Any] = {}
        if elb_info is not None:
            self._values["elb_info"] = elb_info
        if target_group_info is not None:
            self._values["target_group_info"] = target_group_info
        if target_group_pair_info is not None:
            self._values["target_group_pair_info"] = target_group_pair_info

    @builtins.property
    def elb_info(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoElbInfo"]]]:
        '''elb_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#elb_info CodedeployDeploymentGroup#elb_info}
        '''
        result = self._values.get("elb_info")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoElbInfo"]]], result)

    @builtins.property
    def target_group_info(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]]:
        '''target_group_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_info CodedeployDeploymentGroup#target_group_info}
        '''
        result = self._values.get("target_group_info")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]], result)

    @builtins.property
    def target_group_pair_info(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"]:
        '''target_group_pair_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group_pair_info CodedeployDeploymentGroup#target_group_pair_info}
        '''
        result = self._values.get("target_group_pair_info")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoElbInfo",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CodedeployDeploymentGroupLoadBalancerInfoElbInfo:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.
        '''
        if __debug__:
            def stub(*, name: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoElbInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoElbInfoList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoElbInfoList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putElbInfo")
    def put_elb_info(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoElbInfo, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putElbInfo", [value]))

    @jsii.member(jsii_name="putTargetGroupInfo")
    def put_target_group_info(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGroupInfo", [value]))

    @jsii.member(jsii_name="putTargetGroupPairInfo")
    def put_target_group_pair_info(
        self,
        *,
        prod_traffic_route: typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute", typing.Dict[str, typing.Any]],
        target_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup", typing.Dict[str, typing.Any]]]],
        test_traffic_route: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param prod_traffic_route: prod_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#prod_traffic_route CodedeployDeploymentGroup#prod_traffic_route}
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group CodedeployDeploymentGroup#target_group}
        :param test_traffic_route: test_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#test_traffic_route CodedeployDeploymentGroup#test_traffic_route}
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo(
            prod_traffic_route=prod_traffic_route,
            target_group=target_group,
            test_traffic_route=test_traffic_route,
        )

        return typing.cast(None, jsii.invoke(self, "putTargetGroupPairInfo", [value]))

    @jsii.member(jsii_name="resetElbInfo")
    def reset_elb_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElbInfo", []))

    @jsii.member(jsii_name="resetTargetGroupInfo")
    def reset_target_group_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupInfo", []))

    @jsii.member(jsii_name="resetTargetGroupPairInfo")
    def reset_target_group_pair_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetGroupPairInfo", []))

    @builtins.property
    @jsii.member(jsii_name="elbInfo")
    def elb_info(self) -> CodedeployDeploymentGroupLoadBalancerInfoElbInfoList:
        return typing.cast(CodedeployDeploymentGroupLoadBalancerInfoElbInfoList, jsii.get(self, "elbInfo"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInfo")
    def target_group_info(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList", jsii.get(self, "targetGroupInfo"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupPairInfo")
    def target_group_pair_info(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference", jsii.get(self, "targetGroupPairInfo"))

    @builtins.property
    @jsii.member(jsii_name="elbInfoInput")
    def elb_info_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoElbInfo]]], jsii.get(self, "elbInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInfoInput")
    def target_group_info_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo"]]], jsii.get(self, "targetGroupInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupPairInfoInput")
    def target_group_pair_info_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo"], jsii.get(self, "targetGroupPairInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.
        '''
        if __debug__:
            def stub(*, name: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo",
    jsii_struct_bases=[],
    name_mapping={
        "prod_traffic_route": "prodTrafficRoute",
        "target_group": "targetGroup",
        "test_traffic_route": "testTrafficRoute",
    },
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo:
    def __init__(
        self,
        *,
        prod_traffic_route: typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute", typing.Dict[str, typing.Any]],
        target_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup", typing.Dict[str, typing.Any]]]],
        test_traffic_route: typing.Optional[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param prod_traffic_route: prod_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#prod_traffic_route CodedeployDeploymentGroup#prod_traffic_route}
        :param target_group: target_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group CodedeployDeploymentGroup#target_group}
        :param test_traffic_route: test_traffic_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#test_traffic_route CodedeployDeploymentGroup#test_traffic_route}
        '''
        if isinstance(prod_traffic_route, dict):
            prod_traffic_route = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(**prod_traffic_route)
        if isinstance(test_traffic_route, dict):
            test_traffic_route = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(**test_traffic_route)
        if __debug__:
            def stub(
                *,
                prod_traffic_route: typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute, typing.Dict[str, typing.Any]],
                target_group: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, typing.Dict[str, typing.Any]]]],
                test_traffic_route: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prod_traffic_route", value=prod_traffic_route, expected_type=type_hints["prod_traffic_route"])
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
            check_type(argname="argument test_traffic_route", value=test_traffic_route, expected_type=type_hints["test_traffic_route"])
        self._values: typing.Dict[str, typing.Any] = {
            "prod_traffic_route": prod_traffic_route,
            "target_group": target_group,
        }
        if test_traffic_route is not None:
            self._values["test_traffic_route"] = test_traffic_route

    @builtins.property
    def prod_traffic_route(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute":
        '''prod_traffic_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#prod_traffic_route CodedeployDeploymentGroup#prod_traffic_route}
        '''
        result = self._values.get("prod_traffic_route")
        assert result is not None, "Required property 'prod_traffic_route' is missing"
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute", result)

    @builtins.property
    def target_group(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]]:
        '''target_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#target_group CodedeployDeploymentGroup#target_group}
        '''
        result = self._values.get("target_group")
        assert result is not None, "Required property 'target_group' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]], result)

    @builtins.property
    def test_traffic_route(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"]:
        '''test_traffic_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#test_traffic_route CodedeployDeploymentGroup#test_traffic_route}
        '''
        result = self._values.get("test_traffic_route")
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putProdTrafficRoute")
    def put_prod_traffic_route(
        self,
        *,
        listener_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(
            listener_arns=listener_arns
        )

        return typing.cast(None, jsii.invoke(self, "putProdTrafficRoute", [value]))

    @jsii.member(jsii_name="putTargetGroup")
    def put_target_group(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetGroup", [value]))

    @jsii.member(jsii_name="putTestTrafficRoute")
    def put_test_traffic_route(
        self,
        *,
        listener_arns: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        value = CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(
            listener_arns=listener_arns
        )

        return typing.cast(None, jsii.invoke(self, "putTestTrafficRoute", [value]))

    @jsii.member(jsii_name="resetTestTrafficRoute")
    def reset_test_traffic_route(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestTrafficRoute", []))

    @builtins.property
    @jsii.member(jsii_name="prodTrafficRoute")
    def prod_traffic_route(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference", jsii.get(self, "prodTrafficRoute"))

    @builtins.property
    @jsii.member(jsii_name="targetGroup")
    def target_group(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList", jsii.get(self, "targetGroup"))

    @builtins.property
    @jsii.member(jsii_name="testTrafficRoute")
    def test_traffic_route(
        self,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference":
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference", jsii.get(self, "testTrafficRoute"))

    @builtins.property
    @jsii.member(jsii_name="prodTrafficRouteInput")
    def prod_traffic_route_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute"], jsii.get(self, "prodTrafficRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="targetGroupInput")
    def target_group_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup"]]], jsii.get(self, "targetGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="testTrafficRouteInput")
    def test_traffic_route_input(
        self,
    ) -> typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"]:
        return typing.cast(typing.Optional["CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute"], jsii.get(self, "testTrafficRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute",
    jsii_struct_bases=[],
    name_mapping={"listener_arns": "listenerArns"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute:
    def __init__(self, *, listener_arns: typing.Sequence[builtins.str]) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        if __debug__:
            def stub(*, listener_arns: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument listener_arns", value=listener_arns, expected_type=type_hints["listener_arns"])
        self._values: typing.Dict[str, typing.Any] = {
            "listener_arns": listener_arns,
        }

    @builtins.property
    def listener_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.'''
        result = self._values.get("listener_arns")
        assert result is not None, "Required property 'listener_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="listenerArnsInput")
    def listener_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listenerArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerArns")
    def listener_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listenerArns"))

    @listener_arns.setter
    def listener_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup:
    def __init__(self, *, name: builtins.str) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.
        '''
        if __debug__:
            def stub(*, name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#name CodedeployDeploymentGroup#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute",
    jsii_struct_bases=[],
    name_mapping={"listener_arns": "listenerArns"},
)
class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute:
    def __init__(self, *, listener_arns: typing.Sequence[builtins.str]) -> None:
        '''
        :param listener_arns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.
        '''
        if __debug__:
            def stub(*, listener_arns: typing.Sequence[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument listener_arns", value=listener_arns, expected_type=type_hints["listener_arns"])
        self._values: typing.Dict[str, typing.Any] = {
            "listener_arns": listener_arns,
        }

    @builtins.property
    def listener_arns(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#listener_arns CodedeployDeploymentGroup#listener_arns}.'''
        result = self._values.get("listener_arns")
        assert result is not None, "Required property 'listener_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="listenerArnsInput")
    def listener_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "listenerArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="listenerArns")
    def listener_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "listenerArns"))

    @listener_arns.setter
    def listener_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "listenerArns", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute]:
        return typing.cast(typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupOnPremisesInstanceTagFilter",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "type": "type", "value": "value"},
)
class CodedeployDeploymentGroupOnPremisesInstanceTagFilter:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.
        '''
        if __debug__:
            def stub(
                *,
                key: typing.Optional[builtins.str] = None,
                type: typing.Optional[builtins.str] = None,
                value: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#key CodedeployDeploymentGroup#key}.'''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#type CodedeployDeploymentGroup#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#value CodedeployDeploymentGroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupOnPremisesInstanceTagFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupOnPremisesInstanceTagFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupOnPremisesInstanceTagFilterList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupOnPremisesInstanceTagFilter]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupOnPremisesInstanceTagFilter, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupTriggerConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "trigger_events": "triggerEvents",
        "trigger_name": "triggerName",
        "trigger_target_arn": "triggerTargetArn",
    },
)
class CodedeployDeploymentGroupTriggerConfiguration:
    def __init__(
        self,
        *,
        trigger_events: typing.Sequence[builtins.str],
        trigger_name: builtins.str,
        trigger_target_arn: builtins.str,
    ) -> None:
        '''
        :param trigger_events: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_events CodedeployDeploymentGroup#trigger_events}.
        :param trigger_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_name CodedeployDeploymentGroup#trigger_name}.
        :param trigger_target_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_target_arn CodedeployDeploymentGroup#trigger_target_arn}.
        '''
        if __debug__:
            def stub(
                *,
                trigger_events: typing.Sequence[builtins.str],
                trigger_name: builtins.str,
                trigger_target_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument trigger_events", value=trigger_events, expected_type=type_hints["trigger_events"])
            check_type(argname="argument trigger_name", value=trigger_name, expected_type=type_hints["trigger_name"])
            check_type(argname="argument trigger_target_arn", value=trigger_target_arn, expected_type=type_hints["trigger_target_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "trigger_events": trigger_events,
            "trigger_name": trigger_name,
            "trigger_target_arn": trigger_target_arn,
        }

    @builtins.property
    def trigger_events(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_events CodedeployDeploymentGroup#trigger_events}.'''
        result = self._values.get("trigger_events")
        assert result is not None, "Required property 'trigger_events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def trigger_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_name CodedeployDeploymentGroup#trigger_name}.'''
        result = self._values.get("trigger_name")
        assert result is not None, "Required property 'trigger_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_target_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/codedeploy_deployment_group#trigger_target_arn CodedeployDeploymentGroup#trigger_target_arn}.'''
        result = self._values.get("trigger_target_arn")
        assert result is not None, "Required property 'trigger_target_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodedeployDeploymentGroupTriggerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CodedeployDeploymentGroupTriggerConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupTriggerConfigurationList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CodedeployDeploymentGroupTriggerConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CodedeployDeploymentGroupTriggerConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CodedeployDeploymentGroupTriggerConfiguration]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CodedeployDeploymentGroupTriggerConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.codedeployDeploymentGroup.CodedeployDeploymentGroupTriggerConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="triggerEventsInput")
    def trigger_events_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "triggerEventsInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerNameInput")
    def trigger_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerTargetArnInput")
    def trigger_target_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerTargetArnInput"))

    @builtins.property
    @jsii.member(jsii_name="triggerEvents")
    def trigger_events(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "triggerEvents"))

    @trigger_events.setter
    def trigger_events(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerEvents", value)

    @builtins.property
    @jsii.member(jsii_name="triggerName")
    def trigger_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerName"))

    @trigger_name.setter
    def trigger_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerName", value)

    @builtins.property
    @jsii.member(jsii_name="triggerTargetArn")
    def trigger_target_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "triggerTargetArn"))

    @trigger_target_arn.setter
    def trigger_target_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[CodedeployDeploymentGroupTriggerConfiguration, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CodedeployDeploymentGroup",
    "CodedeployDeploymentGroupAlarmConfiguration",
    "CodedeployDeploymentGroupAlarmConfigurationOutputReference",
    "CodedeployDeploymentGroupAutoRollbackConfiguration",
    "CodedeployDeploymentGroupAutoRollbackConfigurationOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfig",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOption",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigDeploymentReadyOptionOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOption",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigGreenFleetProvisioningOptionOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigOutputReference",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccess",
    "CodedeployDeploymentGroupBlueGreenDeploymentConfigTerminateBlueInstancesOnDeploymentSuccessOutputReference",
    "CodedeployDeploymentGroupConfig",
    "CodedeployDeploymentGroupDeploymentStyle",
    "CodedeployDeploymentGroupDeploymentStyleOutputReference",
    "CodedeployDeploymentGroupEc2TagFilter",
    "CodedeployDeploymentGroupEc2TagFilterList",
    "CodedeployDeploymentGroupEc2TagFilterOutputReference",
    "CodedeployDeploymentGroupEc2TagSet",
    "CodedeployDeploymentGroupEc2TagSetEc2TagFilter",
    "CodedeployDeploymentGroupEc2TagSetEc2TagFilterList",
    "CodedeployDeploymentGroupEc2TagSetEc2TagFilterOutputReference",
    "CodedeployDeploymentGroupEc2TagSetList",
    "CodedeployDeploymentGroupEc2TagSetOutputReference",
    "CodedeployDeploymentGroupEcsService",
    "CodedeployDeploymentGroupEcsServiceOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoElbInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoElbInfoList",
    "CodedeployDeploymentGroupLoadBalancerInfoElbInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoList",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfo",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRoute",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoProdTrafficRouteOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroup",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupList",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTargetGroupOutputReference",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRoute",
    "CodedeployDeploymentGroupLoadBalancerInfoTargetGroupPairInfoTestTrafficRouteOutputReference",
    "CodedeployDeploymentGroupOnPremisesInstanceTagFilter",
    "CodedeployDeploymentGroupOnPremisesInstanceTagFilterList",
    "CodedeployDeploymentGroupOnPremisesInstanceTagFilterOutputReference",
    "CodedeployDeploymentGroupTriggerConfiguration",
    "CodedeployDeploymentGroupTriggerConfigurationList",
    "CodedeployDeploymentGroupTriggerConfigurationOutputReference",
]

publication.publish()
