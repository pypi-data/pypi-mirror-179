'''
# Additional Route53 Targets for AWS CDK

[![build](https://github.com/RenovoSolutions/cdk-library-route53targets/actions/workflows/build.yml/badge.svg)](https://github.com/RenovoSolutions/cdk-library-route53targets/actions/workflows/build.yml)

This repo's intention is to add additional avenues for defining Route53 targets or adding targets that might not be available otherwise. See the (limited) feature list below:

## Features

* Add a load balancer target using the load balancers attributes instead of the resource class [`LoadBalancer`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancing.LoadBalancer.html). This is useful in cases where you need to add a Classic Load Balancer as a target, but the load balancer wasn't created in the same CDK app. Since the [ELBv2 package in the `aws-cdk`](https://github.com/aws/aws-cdk/blob/main/packages/%40aws-cdk/aws-elasticloadbalancing/lib/load-balancer.ts) doesn't implement a [resource interface](https://github.com/aws/aws-cdk/blob/main/docs/DESIGN_GUIDELINES.md#owned-vs-unowned-constructs) (`ILoadBalancer`) or other typical L2 concepts ([abstract base class](https://github.com/aws/aws-cdk/blob/main/docs/DESIGN_GUIDELINES.md#abstract-base), ["imports" using `from` methods](https://github.com/aws/aws-cdk/blob/main/docs/DESIGN_GUIDELINES.md#imports)) for constructs the [`ClassicLoadBalancerTarget`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_route53_targets.ClassicLoadBalancerTarget.html) requires a [`LoadBalancer`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancing.LoadBalancer.html) outright. Since `LoadBalancer` is a concrete resource class we can't redefine something we want to target from another CDK app. So, this feature allows us to use data we know about the load balancer to set it as a target more directly.

## Examples

```python
const zone = new r53.HostedZone(stack, 'HostedZone', {
  zoneName: 'example.com',
});

new r53.ARecord(stack, 'AliasRecord', {
  zone,
  recordName: 'publiclb.example.com',
  target: r53.RecordTarget.fromAlias(new LoadBalancerTargetFromAttributes({
    dnsName: 'publiclb-1234567890.us-east-1.elb.amazonaws.com',
    hostedZoneId: 'A1AAAA0A79A41A',
  })),
});
```
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

import aws_cdk.aws_route53


@jsii.data_type(
    jsii_type="@renovosolutions/cdk-library-route53targets.LoadBalancerTargetAttributes",
    jsii_struct_bases=[],
    name_mapping={"dns_name": "dnsName", "hosted_zone_id": "hostedZoneId"},
)
class LoadBalancerTargetAttributes:
    def __init__(self, *, dns_name: builtins.str, hosted_zone_id: builtins.str) -> None:
        '''
        :param dns_name: The DNS name of the load balancer.
        :param hosted_zone_id: The hosted zone ID of the load balancer.
        '''
        if __debug__:
            def stub(*, dns_name: builtins.str, hosted_zone_id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_name": dns_name,
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''The DNS name of the load balancer.'''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The hosted zone ID of the load balancer.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerTargetAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_route53.IAliasRecordTarget)
class LoadBalancerTargetFromAttributes(
    metaclass=jsii.JSIIMeta,
    jsii_type="@renovosolutions/cdk-library-route53targets.LoadBalancerTargetFromAttributes",
):
    def __init__(self, *, dns_name: builtins.str, hosted_zone_id: builtins.str) -> None:
        '''
        :param dns_name: The DNS name of the load balancer.
        :param hosted_zone_id: The hosted zone ID of the load balancer.
        '''
        load_balancer_target_attributes = LoadBalancerTargetAttributes(
            dns_name=dns_name, hosted_zone_id=hosted_zone_id
        )

        jsii.create(self.__class__, self, [load_balancer_target_attributes])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: aws_cdk.aws_route53.IRecordSet,
        _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
    ) -> aws_cdk.aws_route53.AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            def stub(
                _record: aws_cdk.aws_route53.IRecordSet,
                _zone: typing.Optional[aws_cdk.aws_route53.IHostedZone] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(aws_cdk.aws_route53.AliasRecordTargetConfig, jsii.invoke(self, "bind", [_record, _zone]))


__all__ = [
    "LoadBalancerTargetAttributes",
    "LoadBalancerTargetFromAttributes",
]

publication.publish()
