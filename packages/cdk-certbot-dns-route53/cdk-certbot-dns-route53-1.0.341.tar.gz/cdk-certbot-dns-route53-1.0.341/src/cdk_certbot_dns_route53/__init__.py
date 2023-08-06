'''
[![NPM version](https://badge.fury.io/js/cdk-certbot-dns-route53.svg)](https://badge.fury.io/js/cdk-certbot-dns-route53)
[![PyPI version](https://badge.fury.io/py/cdk-certbot-dns-route53.svg)](https://badge.fury.io/py/cdk-certbot-dns-route53)
[![Release](https://github.com/neilkuan/cdk-certbot-dns-route53/actions/workflows/release.yml/badge.svg?branch=main)](https://github.com/neilkuan/cdk-certbot-dns-route53/actions/workflows/release.yml)

# cdk-certbot-dns-route53

**cdk-certbot-dns-route53** is a CDK construct library that allows you to create [Certbot](https://github.com/certbot/certbot) Lambda Function on AWS with CDK, and setting schedule cron job to renew certificate to store on S3 Bucket.

## Install

```bash
Use the npm dist tag to opt in CDKv1 or CDKv2:

// for CDKv2
npm install cdk-certbot-dns-route53
or
npm install cdk-certbot-dns-route53@latest

// for CDKv1
npm install cdk-certbot-dns-route53@cdkv1
```

```python
import * as r53 from '@aws-cdk/aws-route53';
import * as s3 from '@aws-cdk/aws-s3';
import * as cdk from '@aws-cdk/core';
import { CertbotDnsRoute53Job } from 'cdk-certbot-dns-route53';

const devEnv = {
  account: process.env.CDK_DEFAULT_ACCOUNT,
  region: process.env.CDK_DEFAULT_REGION,
};

const app = new cdk.App();

const stack = new cdk.Stack(app, 'lambda-certbot-dev', { env: devEnv });

new CertbotDnsRoute53Job(stack, 'Demo', {
  certbotOptions: {
    domainName: '*.example.com',
    email: 'user@example.com',
  },
  zone: r53.HostedZone.fromHostedZoneAttributes(stack, 'myZone', {
    zoneName: 'example.com',
    hostedZoneId:  'mockId',
  }),
  destinationBucket: s3.Bucket.fromBucketName(stack, 'myBucket', 'mybucket'),
});
```

### You can define Lambda Image Architecture now. 2022/04/19

```python
import * as r53 from '@aws-cdk/aws-route53';
import * as s3 from '@aws-cdk/aws-s3';
import * as cdk from '@aws-cdk/core';
import * as lambda from '@aws-cdk/aws-lambda';
import { CertbotDnsRoute53Job } from 'cdk-certbot-dns-route53';
const mockApp = new cdk.App();
const stack = new cdk.Stack(mockApp, 'teststack', { env: devEnv });
const bucket = new s3.Bucket(stack, 'testingBucket');
const zone = r53.HostedZone.fromHostedZoneAttributes(stack, 'zone', {
  zoneName: mock.zoneName, hostedZoneId: mock.zoneId,
});
new CertbotDnsRoute53Job(stack, 'Testtask', {
  certbotOptions: {
    domainName: 'example.com',
    email: 'user@example.com',
    customPrefixDirectory: '/',
  },
  zone,
  destinationBucket: bucket,
  schedule: events.Schedule.cron({ month: '2' }),
  architecture: lambda.Architecture.ARM_64, // <- like this way.
});
```

### Example: Invoke Lambda Function log.

![](./images/lambda-logs.png)

### Example: Renew certificate to store on S3 Bucket

![](./images/s3-bucket.png)
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

import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_lambda
import aws_cdk.aws_route53
import aws_cdk.aws_s3
import aws_cdk.core


class BashExecFunction(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-certbot-dns-route53.BashExecFunction",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        script: builtins.str,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        dockerfile: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param script: The path of the shell script to be executed.
        :param architecture: Custom lambda Image Architecture. Default: - lambda.Architecture.X86_64
        :param dockerfile: The path of your custom dockerfile.
        :param environment: Lambda environment variables.
        :param role: Custom lambda execution role. Default: - auto generated role.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: - Duration.seconds(60)
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                script: builtins.str,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                dockerfile: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                timeout: typing.Optional[aws_cdk.core.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BashExecFunctionProps(
            script=script,
            architecture=architecture,
            dockerfile=dockerfile,
            environment=environment,
            role=role,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> aws_cdk.aws_lambda.DockerImageFunction:
        return typing.cast(aws_cdk.aws_lambda.DockerImageFunction, jsii.get(self, "handler"))


@jsii.data_type(
    jsii_type="cdk-certbot-dns-route53.BashExecFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "script": "script",
        "architecture": "architecture",
        "dockerfile": "dockerfile",
        "environment": "environment",
        "role": "role",
        "timeout": "timeout",
    },
)
class BashExecFunctionProps:
    def __init__(
        self,
        *,
        script: builtins.str,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        dockerfile: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        timeout: typing.Optional[aws_cdk.core.Duration] = None,
    ) -> None:
        '''
        :param script: The path of the shell script to be executed.
        :param architecture: Custom lambda Image Architecture. Default: - lambda.Architecture.X86_64
        :param dockerfile: The path of your custom dockerfile.
        :param environment: Lambda environment variables.
        :param role: Custom lambda execution role. Default: - auto generated role.
        :param timeout: The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: - Duration.seconds(60)
        '''
        if __debug__:
            def stub(
                *,
                script: builtins.str,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                dockerfile: typing.Optional[builtins.str] = None,
                environment: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                timeout: typing.Optional[aws_cdk.core.Duration] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument script", value=script, expected_type=type_hints["script"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument dockerfile", value=dockerfile, expected_type=type_hints["dockerfile"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "script": script,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if dockerfile is not None:
            self._values["dockerfile"] = dockerfile
        if environment is not None:
            self._values["environment"] = environment
        if role is not None:
            self._values["role"] = role
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def script(self) -> builtins.str:
        '''The path of the shell script to be executed.'''
        result = self._values.get("script")
        assert result is not None, "Required property 'script' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[aws_cdk.aws_lambda.Architecture]:
        '''Custom lambda Image Architecture.

        :default: - lambda.Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Architecture], result)

    @builtins.property
    def dockerfile(self) -> typing.Optional[builtins.str]:
        '''The path of your custom dockerfile.'''
        result = self._values.get("dockerfile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Lambda environment variables.'''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''Custom lambda execution role.

        :default: - auto generated role.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value based on the function's expected execution time.

        :default: - Duration.seconds(60)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BashExecFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CertbotDnsRoute53Job(
    aws_cdk.core.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-certbot-dns-route53.CertbotDnsRoute53Job",
):
    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        certbot_options: typing.Union["CertbotOptions", typing.Dict[str, typing.Any]],
        destination_bucket: aws_cdk.aws_s3.IBucket,
        zone: aws_cdk.aws_route53.IHostedZone,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        schedule: typing.Optional[aws_cdk.aws_events.Schedule] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param certbot_options: certbot cmd options.
        :param destination_bucket: The S3 bucket to store certificate.
        :param zone: The HostZone on route53 to dns-01 challenge.
        :param architecture: Custom lambda Image Architecture. Default: - lambda.Architecture.X86_64
        :param schedule: run the Job with defined schedule. Default: - no shedule
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                certbot_options: typing.Union[CertbotOptions, typing.Dict[str, typing.Any]],
                destination_bucket: aws_cdk.aws_s3.IBucket,
                zone: aws_cdk.aws_route53.IHostedZone,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                schedule: typing.Optional[aws_cdk.aws_events.Schedule] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CertbotDnsRoute53JobProps(
            certbot_options=certbot_options,
            destination_bucket=destination_bucket,
            zone=zone,
            architecture=architecture,
            schedule=schedule,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="cdk-certbot-dns-route53.CertbotDnsRoute53JobProps",
    jsii_struct_bases=[],
    name_mapping={
        "certbot_options": "certbotOptions",
        "destination_bucket": "destinationBucket",
        "zone": "zone",
        "architecture": "architecture",
        "schedule": "schedule",
    },
)
class CertbotDnsRoute53JobProps:
    def __init__(
        self,
        *,
        certbot_options: typing.Union["CertbotOptions", typing.Dict[str, typing.Any]],
        destination_bucket: aws_cdk.aws_s3.IBucket,
        zone: aws_cdk.aws_route53.IHostedZone,
        architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
        schedule: typing.Optional[aws_cdk.aws_events.Schedule] = None,
    ) -> None:
        '''
        :param certbot_options: certbot cmd options.
        :param destination_bucket: The S3 bucket to store certificate.
        :param zone: The HostZone on route53 to dns-01 challenge.
        :param architecture: Custom lambda Image Architecture. Default: - lambda.Architecture.X86_64
        :param schedule: run the Job with defined schedule. Default: - no shedule
        '''
        if isinstance(certbot_options, dict):
            certbot_options = CertbotOptions(**certbot_options)
        if __debug__:
            def stub(
                *,
                certbot_options: typing.Union[CertbotOptions, typing.Dict[str, typing.Any]],
                destination_bucket: aws_cdk.aws_s3.IBucket,
                zone: aws_cdk.aws_route53.IHostedZone,
                architecture: typing.Optional[aws_cdk.aws_lambda.Architecture] = None,
                schedule: typing.Optional[aws_cdk.aws_events.Schedule] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certbot_options", value=certbot_options, expected_type=type_hints["certbot_options"])
            check_type(argname="argument destination_bucket", value=destination_bucket, expected_type=type_hints["destination_bucket"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[str, typing.Any] = {
            "certbot_options": certbot_options,
            "destination_bucket": destination_bucket,
            "zone": zone,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if schedule is not None:
            self._values["schedule"] = schedule

    @builtins.property
    def certbot_options(self) -> "CertbotOptions":
        '''certbot cmd options.'''
        result = self._values.get("certbot_options")
        assert result is not None, "Required property 'certbot_options' is missing"
        return typing.cast("CertbotOptions", result)

    @builtins.property
    def destination_bucket(self) -> aws_cdk.aws_s3.IBucket:
        '''The S3 bucket to store certificate.'''
        result = self._values.get("destination_bucket")
        assert result is not None, "Required property 'destination_bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.IBucket, result)

    @builtins.property
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        '''The HostZone on route53 to dns-01 challenge.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(aws_cdk.aws_route53.IHostedZone, result)

    @builtins.property
    def architecture(self) -> typing.Optional[aws_cdk.aws_lambda.Architecture]:
        '''Custom lambda Image Architecture.

        :default: - lambda.Architecture.X86_64
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[aws_cdk.aws_lambda.Architecture], result)

    @builtins.property
    def schedule(self) -> typing.Optional[aws_cdk.aws_events.Schedule]:
        '''run the Job with defined schedule.

        :default: - no shedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[aws_cdk.aws_events.Schedule], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertbotDnsRoute53JobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-certbot-dns-route53.CertbotOptions",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "email": "email",
        "custom_prefix_directory": "customPrefixDirectory",
    },
)
class CertbotOptions:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        email: builtins.str,
        custom_prefix_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: the domain must host on route53 like example.com.
        :param email: Email address for important account notifications.
        :param custom_prefix_directory: Custom prefix directory on s3 bucket object path. Default: - ``s3://YOUR_BUCKET_NAME/2021-01-01/your.domain.name/``
        '''
        if __debug__:
            def stub(
                *,
                domain_name: builtins.str,
                email: builtins.str,
                custom_prefix_directory: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument custom_prefix_directory", value=custom_prefix_directory, expected_type=type_hints["custom_prefix_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "email": email,
        }
        if custom_prefix_directory is not None:
            self._values["custom_prefix_directory"] = custom_prefix_directory

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''the domain must host on route53 like example.com.

        Example::

            - `*.example.com` or `a.example.com` .
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''Email address for important account notifications.'''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_prefix_directory(self) -> typing.Optional[builtins.str]:
        '''Custom prefix directory on s3 bucket object path.

        :default: - ``s3://YOUR_BUCKET_NAME/2021-01-01/your.domain.name/``

        Example::

            - customPrefixDirectory: 'abc' -> `s3://YOUR_BUCKET_NAME/abc/your.domain.name/`
        '''
        result = self._values.get("custom_prefix_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertbotOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BashExecFunction",
    "BashExecFunctionProps",
    "CertbotDnsRoute53Job",
    "CertbotDnsRoute53JobProps",
    "CertbotOptions",
]

publication.publish()
