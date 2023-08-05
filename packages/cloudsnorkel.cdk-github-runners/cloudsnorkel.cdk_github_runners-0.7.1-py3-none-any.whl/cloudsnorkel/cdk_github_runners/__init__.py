'''
# GitHub Self-Hosted Runners CDK Constructs

[![NPM](https://img.shields.io/npm/v/@cloudsnorkel/cdk-github-runners?label=npm&logo=npm)](https://www.npmjs.com/package/@cloudsnorkel/cdk-github-runners)
[![PyPI](https://img.shields.io/pypi/v/cloudsnorkel.cdk-github-runners?label=pypi&logo=pypi)](https://pypi.org/project/cloudsnorkel.cdk-github-runners)
[![Maven Central](https://img.shields.io/maven-central/v/com.cloudsnorkel/cdk.github.runners.svg?label=Maven%20Central&logo=java)](https://search.maven.org/search?q=g:%22com.cloudsnorkel%22%20AND%20a:%22cdk.github.runners%22)
[![Go](https://img.shields.io/github/v/tag/CloudSnorkel/cdk-github-runners?color=red&label=go&logo=go)](https://pkg.go.dev/github.com/CloudSnorkel/cdk-github-runners-go/cloudsnorkelcdkgithubrunners)
[![Nuget](https://img.shields.io/nuget/v/CloudSnorkel.Cdk.Github.Runners?color=red&&logo=nuget)](https://www.nuget.org/packages/CloudSnorkel.Cdk.Github.Runners/)
[![Release](https://github.com/CloudSnorkel/cdk-github-runners/actions/workflows/release.yml/badge.svg)](https://github.com/CloudSnorkel/cdk-github-runners/actions/workflows/release.yml)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://github.com/CloudSnorkel/cdk-github-runners/blob/main/LICENSE)

Use this CDK construct to create ephemeral [self-hosted GitHub runners](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners) on-demand inside your AWS account.

* Easy to configure GitHub integration with a web-based interface
* Customizable runners with decent defaults
* Multiple runner configurations controlled by labels
* Everything fully hosted in your account
* Automatically updated build environment with latest runner version

Self-hosted runners in AWS are useful when:

* You need easy access to internal resources in your actions
* You want to pre-install some software for your actions
* You want to provide some basic AWS API access (but [aws-actions/configure-aws-credentials](https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions) has more security controls)

Ephemeral (or on-demand) runners are the [recommended way by GitHub](https://docs.github.com/en/actions/hosting-your-own-runners/autoscaling-with-self-hosted-runners#using-ephemeral-runners-for-autoscaling) for auto-scaling, and they make sure all jobs run with a clean image. Runners are started on-demand. You don't pay unless a job is running.

## API

The best way to browse API documentation is on [Constructs Hub](https://constructs.dev/packages/@cloudsnorkel/cdk-github-runners/). It is available in all supported programming languages.

## Providers

A runner provider creates compute resources on-demand and uses [actions/runner](https://github.com/actions/runner) to start a runner.

|                  | EC2               | CodeBuild                  | Fargate        | Lambda        |
|------------------|-------------------|----------------------------|----------------|---------------|
| **Time limit**   | Unlimited         | 8 hours                    | Unlimited      | 15 minutes    |
| **vCPUs**        | Unlimited         | 2, 4, 8, or 72             | 0.25 to 4      | 1 to 6        |
| **RAM**          | Unlimited         | 3gb, 7gb, 15gb, or 145gb   | 512mb to 30gb  | 128mb to 10gb |
| **Storage**      | Unlimited         | 50gb to 824gb              | 20gb to 200gb  | Up to 10gb    |
| **Architecture** | x86_64, ARM64     | x86_64, ARM64              | x86_64, ARM64  | x86_64, ARM64 |
| **sudo**         | ✔                 | ✔                         | ✔              | ❌           |
| **Docker**       | ✔                 | ✔ (Linux only)            | ❌              | ❌           |
| **Spot pricing** | ✔                 | ❌                         | ✔              | ❌           |
| **OS**           | Linux, Windows    | Linux, Windows             | Linux, Windows | Linux         |

The best provider to use mostly depends on your current infrastructure. When in doubt, CodeBuild is always a good choice. Execution history and logs are easy to view, and it has no restrictive limits unless you need to run for more than 8 hours.

You can also create your own provider by implementing `IRunnerProvider`.

## Installation

1. Confirm you're using CDK v2
2. Install the appropriate package

   1. [Python](https://pypi.org/project/cloudsnorkel.cdk-github-runners)

      ```
      pip install cloudsnorkel.cdk-github-runners
      ```
   2. [TypeScript or JavaScript](https://www.npmjs.com/package/@cloudsnorkel/cdk-github-runners)

      ```
      npm i @cloudsnorkel/cdk-github-runners
      ```
   3. [Java](https://search.maven.org/search?q=g:%22com.cloudsnorkel%22%20AND%20a:%22cdk.github.runners%22)

      ```xml
      <dependency>
      <groupId>com.cloudsnorkel</groupId>
      <artifactId>cdk.github.runners</artifactId>
      </dependency>
      ```
   4. [Go](https://pkg.go.dev/github.com/CloudSnorkel/cdk-github-runners-go/cloudsnorkelcdkgithubrunners)

      ```
      go get github.com/CloudSnorkel/cdk-github-runners-go/cloudsnorkelcdkgithubrunners
      ```
   5. [.NET](https://www.nuget.org/packages/CloudSnorkel.Cdk.Github.Runners/)

      ```
      dotnet add package CloudSnorkel.Cdk.Github.Runners
      ```
3. Use `GitHubRunners` construct in your code (starting with default arguments is fine)
4. Deploy your stack
5. Look for the status command output similar to `aws --region us-east-1 lambda invoke --function-name status-XYZ123 status.json`
6. Execute the status command (you may need to specify `--profile` too) and open the resulting `status.json` file
7. Open the URL in `github.setup.url` from `status.json` or [manually setup GitHub](SETUP_GITHUB.md) integration as an app or with personal access token
8. Run status command again to confirm `github.auth.status` and `github.webhook.status` are OK
9. Trigger a GitHub action that has a `self-hosted` label with `runs-on: [self-hosted, linux, codebuild]` or similar
10. If the action is not successful, see [troubleshooting](#Troubleshooting)

[![Demo](demo-thumbnail.jpg)](https://youtu.be/wlyv_3V8lIw)

## Customizing

The default providers configured by `GitHubRunners` are useful for testing but probably not too much for actual production work. They run in the default VPC or no VPC and have no added IAM permissions. You would usually want to configure the providers yourself.

For example:

```python
let vpc: ec2.Vpc;
let runnerSg: ec2.SecurityGroup;
let dbSg: ec2.SecurityGroup;
let bucket: s3.Bucket;

// create a custom CodeBuild provider
const myProvider = new CodeBuildRunner(this, 'codebuild runner', {
  label: 'my-codebuild',
  vpc: vpc,
  securityGroup: runnerSg,
});
// grant some permissions to the provider
bucket.grantReadWrite(myProvider);
dbSg.connections.allowFrom(runnerSg, ec2.Port.tcp(3306), 'allow runners to connect to MySQL database');

// create the runner infrastructure
new GitHubRunners(this, 'runners', {
   providers: [myProvider],
});
```

Another way to customize runners is by modifying the image used to spin them up. The image contains the [runner](https://github.com/actions/runner), any required dependencies, and integration code with the provider. You may choose to customize this image by adding more packages, for example.

```python
const myBuilder = new CodeBuildImageBuilder(this, 'image builder', {
  dockerfilePath: FargateRunner.LINUX_X64_DOCKERFILE_PATH,
  runnerVersion: RunnerVersion.specific('2.291.0'),
  rebuildInterval: Duration.days(14),
});
myBuilder.setBuildArg('EXTRA_PACKAGES', 'nginx xz-utils');

const myProvider = new FargateRunner(this, 'fargate runner', {
  label: 'customized-fargate',
  vpc: vpc,
  securityGroup: runnerSg,
  imageBuilder: myBuilder,
});

// create the runner infrastructure
new GitHubRunners(stack, 'runners', {
  providers: [myProvider],
});
```

Your workflow will then look like:

```yaml
name: self-hosted example
on: push
jobs:
  self-hosted:
    runs-on: [self-hosted, customized-fargate]
    steps:
      - run: echo hello world
```

Windows images must be built with AWS Image Builder.

```python
const myWindowsBuilder = new ContainerImageBuilder(this, 'Windows image builder', {
  architecture: Architecture.X86_64,
  os: Os.WINDOWS,
  runnerVersion: RunnerVersion.specific('2.291.0'),
  rebuildInterval: Duration.days(14),
});
myWindowsBuilder.addComponent(new ImageBuilderComponent(this, 'Ninja Component',
  {
    displayName: 'Ninja',
    description: 'Download and install Ninja build system',
    platform: 'Windows',
    commands: [
      'Invoke-WebRequest -UseBasicParsing -Uri "https://github.com/ninja-build/ninja/releases/download/v1.11.1/ninja-win.zip" -OutFile ninja.zip',
      'Expand-Archive ninja.zip -DestinationPath C:\\actions',
      'del ninja.zip',
    ],
  }
));

const myProvider = new FargateRunner(this, 'fargate runner', {
  label: 'customized-windows-fargate',
  vpc: vpc,
  securityGroup: runnerSg,
  imageBuiler: myWindowsBuilder,
});

// create the runner infrastructure
new GitHubRunners(stack, 'runners', {
  providers: [myProvider],
});
```

## Architecture

![Architecture diagram](architecture.svg)

## Troubleshooting

1. Always start with the status function, make sure no errors are reported, and confirm all status codes are OK
2. If jobs are stuck on pending:

   1. Make sure `runs-on` in the workflow matches the expected labels set in the runner provider
   2. If it happens every time, cancel the job and start it again
3. Confirm the webhook Lambda was called by visiting the URL in `troubleshooting.webhookHandlerUrl` from `status.json`

   1. If it's not called or logs errors, confirm the webhook settings on the GitHub side
   2. If you see too many errors, make sure you're only sending `workflow_job` events
4. When using GitHub app, make sure there are active installation in `github.auth.app.installations`
5. Check execution details of the orchestrator step function by visiting the URL in `troubleshooting.stepFunctionUrl` from `status.json`

   1. Use the details tab to find the specific execution of the provider (Lambda, CodeBuild, Fargate, etc.)
   2. Every step function execution should be successful, even if the runner action inside it failed

## Other Options

1. [philips-labs/terraform-aws-github-runner](https://github.com/philips-labs/terraform-aws-github-runner) if you're using Terraform
2. [actions-runner-controller/actions-runner-controller](https://github.com/actions-runner-controller/actions-runner-controller) if you're using Kubernetes
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

import aws_cdk
import aws_cdk.aws_codebuild
import aws_cdk.aws_ec2
import aws_cdk.aws_ecr
import aws_cdk.aws_ecs
import aws_cdk.aws_iam
import aws_cdk.aws_imagebuilder
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_s3_assets
import aws_cdk.aws_secretsmanager
import aws_cdk.aws_stepfunctions
import constructs


class Architecture(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.Architecture",
):
    '''(experimental) CPU architecture enum for an image.

    :stability: experimental
    '''

    @jsii.member(jsii_name="instanceTypeMatch")
    def instance_type_match(
        self,
        instance_type: aws_cdk.aws_ec2.InstanceType,
    ) -> builtins.bool:
        '''(experimental) Checks if a given EC2 instance type matches this architecture.

        :param instance_type: instance type to check.

        :stability: experimental
        '''
        if __debug__:
            def stub(instance_type: aws_cdk.aws_ec2.InstanceType) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        return typing.cast(builtins.bool, jsii.invoke(self, "instanceTypeMatch", [instance_type]))

    @jsii.member(jsii_name="is")
    def is_(self, arch: "Architecture") -> builtins.bool:
        '''(experimental) Checks if the given architecture is the same as this one.

        :param arch: architecture to compare.

        :stability: experimental
        '''
        if __debug__:
            def stub(arch: Architecture) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument arch", value=arch, expected_type=type_hints["arch"])
        return typing.cast(builtins.bool, jsii.invoke(self, "is", [arch]))

    @jsii.member(jsii_name="isIn")
    def is_in(self, arches: typing.Sequence["Architecture"]) -> builtins.bool:
        '''(experimental) Checks if this architecture is in a given list.

        :param arches: architectures to check.

        :stability: experimental
        '''
        if __debug__:
            def stub(arches: typing.Sequence[Architecture]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument arches", value=arches, expected_type=type_hints["arches"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isIn", [arches]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARM64")
    def ARM64(cls) -> "Architecture":
        '''(experimental) ARM64.

        :stability: experimental
        '''
        return typing.cast("Architecture", jsii.sget(cls, "ARM64"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="X86_64")
    def X86_64(cls) -> "Architecture":
        '''(experimental) X86_64.

        :stability: experimental
        '''
        return typing.cast("Architecture", jsii.sget(cls, "X86_64"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildImageBuilderProps",
    jsii_struct_bases=[],
    name_mapping={
        "dockerfile_path": "dockerfilePath",
        "architecture": "architecture",
        "compute_type": "computeType",
        "log_removal_policy": "logRemovalPolicy",
        "log_retention": "logRetention",
        "os": "os",
        "rebuild_interval": "rebuildInterval",
        "runner_version": "runnerVersion",
        "security_group": "securityGroup",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class CodeBuildImageBuilderProps:
    def __init__(
        self,
        *,
        dockerfile_path: builtins.str,
        architecture: typing.Optional[Architecture] = None,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional["Os"] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional["RunnerVersion"] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for CodeBuildImageBuilder construct.

        :param dockerfile_path: (experimental) Path to Dockerfile to be built. It can be a path to a Dockerfile, a folder containing a Dockerfile, or a zip file containing a Dockerfile.
        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (experimental) Security Group to assign to this instance. Default: public project with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to build the image in. Default: no VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                dockerfile_path: builtins.str,
                architecture: typing.Optional[Architecture] = None,
                compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
                log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                os: typing.Optional[Os] = None,
                rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
                runner_version: typing.Optional[RunnerVersion] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument log_removal_policy", value=log_removal_policy, expected_type=type_hints["log_removal_policy"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument rebuild_interval", value=rebuild_interval, expected_type=type_hints["rebuild_interval"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {
            "dockerfile_path": dockerfile_path,
        }
        if architecture is not None:
            self._values["architecture"] = architecture
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if log_removal_policy is not None:
            self._values["log_removal_policy"] = log_removal_policy
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if os is not None:
            self._values["os"] = os
        if rebuild_interval is not None:
            self._values["rebuild_interval"] = rebuild_interval
        if runner_version is not None:
            self._values["runner_version"] = runner_version
        if security_group is not None:
            self._values["security_group"] = security_group
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def dockerfile_path(self) -> builtins.str:
        '''(experimental) Path to Dockerfile to be built.

        It can be a path to a Dockerfile, a folder containing a Dockerfile, or a zip file containing a Dockerfile.

        :stability: experimental
        '''
        result = self._values.get("dockerfile_path")
        assert result is not None, "Required property 'dockerfile_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def architecture(self) -> typing.Optional[Architecture]:
        '''(experimental) Image architecture.

        :default: Architecture.X86_64

        :stability: experimental
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[Architecture], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[aws_cdk.aws_codebuild.ComputeType]:
        '''(experimental) The type of compute to use for this build.

        See the {@link ComputeType} enum for the possible values.

        :default: {@link ComputeType#SMALL}

        :stability: experimental
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[aws_cdk.aws_codebuild.ComputeType], result)

    @builtins.property
    def log_removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) Removal policy for logs of image builds.

        If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed.

        We try to not leave anything behind when removed. But sometimes a log staying behind is useful.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("log_removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def os(self) -> typing.Optional["Os"]:
        '''(experimental) Image OS.

        :default: OS.LINUX

        :stability: experimental
        '''
        result = self._values.get("os")
        return typing.cast(typing.Optional["Os"], result)

    @builtins.property
    def rebuild_interval(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) Schedule the image to be rebuilt every given interval.

        Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates.

        Set to zero to disable.

        :default: Duration.days(7)

        :stability: experimental
        '''
        result = self._values.get("rebuild_interval")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def runner_version(self) -> typing.Optional["RunnerVersion"]:
        '''(experimental) Version of GitHub Runners to install.

        :default: latest version available

        :stability: experimental
        '''
        result = self._values.get("runner_version")
        return typing.cast(typing.Optional["RunnerVersion"], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security Group to assign to this instance.

        :default: public project with no security group

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: no subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)

        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to build the image in.

        :default: no VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildImageBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.ContainerImageBuilderProps",
    jsii_struct_bases=[],
    name_mapping={
        "architecture": "architecture",
        "instance_type": "instanceType",
        "log_removal_policy": "logRemovalPolicy",
        "log_retention": "logRetention",
        "os": "os",
        "parent_image": "parentImage",
        "rebuild_interval": "rebuildInterval",
        "runner_version": "runnerVersion",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
    },
)
class ContainerImageBuilderProps:
    def __init__(
        self,
        *,
        architecture: typing.Optional[Architecture] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional["Os"] = None,
        parent_image: typing.Optional[builtins.str] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional["RunnerVersion"] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for ContainerImageBuilder construct.

        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param instance_type: (experimental) The instance type used to build the image. Default: m5.large
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param parent_image: (experimental) Parent image for the new Docker Image. You can use either Image Builder image ARN or public registry image. Default: 'mcr.microsoft.com/windows/servercore:ltsc2019-amd64'
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (deprecated) Security group to assign to launched builder instances. Default: new security group
        :param security_groups: (experimental) Security groups to assign to launched builder instances. Default: new security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: default VPC subnet
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                architecture: typing.Optional[Architecture] = None,
                instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
                log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                os: typing.Optional[Os] = None,
                parent_image: typing.Optional[builtins.str] = None,
                rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
                runner_version: typing.Optional[RunnerVersion] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument log_removal_policy", value=log_removal_policy, expected_type=type_hints["log_removal_policy"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument parent_image", value=parent_image, expected_type=type_hints["parent_image"])
            check_type(argname="argument rebuild_interval", value=rebuild_interval, expected_type=type_hints["rebuild_interval"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if architecture is not None:
            self._values["architecture"] = architecture
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if log_removal_policy is not None:
            self._values["log_removal_policy"] = log_removal_policy
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if os is not None:
            self._values["os"] = os
        if parent_image is not None:
            self._values["parent_image"] = parent_image
        if rebuild_interval is not None:
            self._values["rebuild_interval"] = rebuild_interval
        if runner_version is not None:
            self._values["runner_version"] = runner_version
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def architecture(self) -> typing.Optional[Architecture]:
        '''(experimental) Image architecture.

        :default: Architecture.X86_64

        :stability: experimental
        '''
        result = self._values.get("architecture")
        return typing.cast(typing.Optional[Architecture], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        '''(experimental) The instance type used to build the image.

        :default: m5.large

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.InstanceType], result)

    @builtins.property
    def log_removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) Removal policy for logs of image builds.

        If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed.

        We try to not leave anything behind when removed. But sometimes a log staying behind is useful.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("log_removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def os(self) -> typing.Optional["Os"]:
        '''(experimental) Image OS.

        :default: OS.LINUX

        :stability: experimental
        '''
        result = self._values.get("os")
        return typing.cast(typing.Optional["Os"], result)

    @builtins.property
    def parent_image(self) -> typing.Optional[builtins.str]:
        '''(experimental) Parent image for the new Docker Image.

        You can use either Image Builder image ARN or public registry image.

        :default: 'mcr.microsoft.com/windows/servercore:ltsc2019-amd64'

        :stability: experimental
        '''
        result = self._values.get("parent_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rebuild_interval(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) Schedule the image to be rebuilt every given interval.

        Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates.

        Set to zero to disable.

        :default: Duration.days(7)

        :stability: experimental
        '''
        result = self._values.get("rebuild_interval")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def runner_version(self) -> typing.Optional["RunnerVersion"]:
        '''(experimental) Version of GitHub Runners to install.

        :default: latest version available

        :stability: experimental
        '''
        result = self._values.get("runner_version")
        return typing.cast(typing.Optional["RunnerVersion"], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Security group to assign to launched builder instances.

        :default: new security group

        :deprecated: use {@link securityGroups}

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) Security groups to assign to launched builder instances.

        :default: new security group

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: default VPC subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: default account VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerImageBuilderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GitHubRunners(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.GitHubRunners",
):
    '''(experimental) Create all the required infrastructure to provide self-hosted GitHub runners.

    It creates a webhook, secrets, and a step function to orchestrate all runs. Secrets are not automatically filled. See README.md for instructions on how to setup GitHub integration.

    By default, this will create a runner provider of each available type with the defaults. This is good enough for the initial setup stage when you just want to get GitHub integration working::

       new GitHubRunners(this, 'runners');

    Usually you'd want to configure the runner providers so the runners can run in a certain VPC or have certain permissions::

       const vpc = ec2.Vpc.fromLookup(this, 'vpc', { vpcId: 'vpc-1234567' });
       const runnerSg = new ec2.SecurityGroup(this, 'runner security group', { vpc: vpc });
       const dbSg = ec2.SecurityGroup.fromSecurityGroupId(this, 'database security group', 'sg-1234567');
       const bucket = new s3.Bucket(this, 'runner bucket');

       // create a custom CodeBuild provider
       const myProvider = new CodeBuildRunner(
          this, 'codebuild runner',
          {
             label: 'my-codebuild',
             vpc: vpc,
             securityGroup: runnerSg,
          },
       );
       // grant some permissions to the provider
       bucket.grantReadWrite(myProvider);
       dbSg.connections.allowFrom(runnerSg, ec2.Port.tcp(3306), 'allow runners to connect to MySQL database');

       // create the runner infrastructure
       new GitHubRunners(
          this,
          'runners',
          {
            providers: [myProvider],
          }
       );

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        extra_certificates: typing.Optional[builtins.str] = None,
        idle_timeout: typing.Optional[aws_cdk.Duration] = None,
        providers: typing.Optional[typing.Sequence["IRunnerProvider"]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param allow_public_subnet: (experimental) Allow management functions to run in public subnets. Lambda Functions in a public subnet can NOT access the internet. Default: false
        :param extra_certificates: (experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed. You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates}:: const imageBuilder = new CodeBuildImageBuilder(this, 'Image Builder with Certs', { dockerfilePath: CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH, }); imageBuilder.addExtraCertificates('path-to-my-extra-certs-folder'); const provider = new CodeBuildRunner(this, 'CodeBuild', { imageBuilder: imageBuilder, }); new GitHubRunners( this, 'runners', { providers: [provider], extraCertificates: 'path-to-my-extra-certs-folder', } );
        :param idle_timeout: (experimental) Time to wait before stopping a runner that remains idle. If the user cancelled the job, or if another runner stole it, this stops the runner to avoid wasting resources. Default: 10 minutes
        :param providers: (experimental) List of runner providers to use. At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job. Default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)
        :param security_group: (experimental) Security group attached to all management functions. Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.
        :param vpc: (experimental) VPC used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
        :param vpc_subnets: (experimental) VPC subnets used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                allow_public_subnet: typing.Optional[builtins.bool] = None,
                extra_certificates: typing.Optional[builtins.str] = None,
                idle_timeout: typing.Optional[aws_cdk.Duration] = None,
                providers: typing.Optional[typing.Sequence[IRunnerProvider]] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GitHubRunnersProps(
            allow_public_subnet=allow_public_subnet,
            extra_certificates=extra_certificates,
            idle_timeout=idle_timeout,
            providers=providers,
            security_group=security_group,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="providers")
    def providers(self) -> typing.List["IRunnerProvider"]:
        '''(experimental) Configured runner providers.

        :stability: experimental
        '''
        return typing.cast(typing.List["IRunnerProvider"], jsii.get(self, "providers"))

    @builtins.property
    @jsii.member(jsii_name="secrets")
    def secrets(self) -> "Secrets":
        '''(experimental) Secrets for GitHub communication including webhook secret and runner authentication.

        :stability: experimental
        '''
        return typing.cast("Secrets", jsii.get(self, "secrets"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> typing.Optional["GitHubRunnersProps"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional["GitHubRunnersProps"], jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.GitHubRunnersProps",
    jsii_struct_bases=[],
    name_mapping={
        "allow_public_subnet": "allowPublicSubnet",
        "extra_certificates": "extraCertificates",
        "idle_timeout": "idleTimeout",
        "providers": "providers",
        "security_group": "securityGroup",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class GitHubRunnersProps:
    def __init__(
        self,
        *,
        allow_public_subnet: typing.Optional[builtins.bool] = None,
        extra_certificates: typing.Optional[builtins.str] = None,
        idle_timeout: typing.Optional[aws_cdk.Duration] = None,
        providers: typing.Optional[typing.Sequence["IRunnerProvider"]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for GitHubRunners.

        :param allow_public_subnet: (experimental) Allow management functions to run in public subnets. Lambda Functions in a public subnet can NOT access the internet. Default: false
        :param extra_certificates: (experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed. You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates}:: const imageBuilder = new CodeBuildImageBuilder(this, 'Image Builder with Certs', { dockerfilePath: CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH, }); imageBuilder.addExtraCertificates('path-to-my-extra-certs-folder'); const provider = new CodeBuildRunner(this, 'CodeBuild', { imageBuilder: imageBuilder, }); new GitHubRunners( this, 'runners', { providers: [provider], extraCertificates: 'path-to-my-extra-certs-folder', } );
        :param idle_timeout: (experimental) Time to wait before stopping a runner that remains idle. If the user cancelled the job, or if another runner stole it, this stops the runner to avoid wasting resources. Default: 10 minutes
        :param providers: (experimental) List of runner providers to use. At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job. Default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)
        :param security_group: (experimental) Security group attached to all management functions. Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.
        :param vpc: (experimental) VPC used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.
        :param vpc_subnets: (experimental) VPC subnets used for all management functions. Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                allow_public_subnet: typing.Optional[builtins.bool] = None,
                extra_certificates: typing.Optional[builtins.str] = None,
                idle_timeout: typing.Optional[aws_cdk.Duration] = None,
                providers: typing.Optional[typing.Sequence[IRunnerProvider]] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument allow_public_subnet", value=allow_public_subnet, expected_type=type_hints["allow_public_subnet"])
            check_type(argname="argument extra_certificates", value=extra_certificates, expected_type=type_hints["extra_certificates"])
            check_type(argname="argument idle_timeout", value=idle_timeout, expected_type=type_hints["idle_timeout"])
            check_type(argname="argument providers", value=providers, expected_type=type_hints["providers"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_public_subnet is not None:
            self._values["allow_public_subnet"] = allow_public_subnet
        if extra_certificates is not None:
            self._values["extra_certificates"] = extra_certificates
        if idle_timeout is not None:
            self._values["idle_timeout"] = idle_timeout
        if providers is not None:
            self._values["providers"] = providers
        if security_group is not None:
            self._values["security_group"] = security_group
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def allow_public_subnet(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Allow management functions to run in public subnets.

        Lambda Functions in a public subnet can NOT access the internet.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("allow_public_subnet")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def extra_certificates(self) -> typing.Optional[builtins.str]:
        '''(experimental) Path to a directory containing a file named certs.pem containing any additional certificates required to trust GitHub Enterprise Server. Use this when GitHub Enterprise Server certificates are self-signed.

        You may also want to use custom images for your runner providers that contain the same certificates. See {@link CodeBuildImageBuilder.addCertificates}::

           const imageBuilder = new CodeBuildImageBuilder(this, 'Image Builder with Certs', {
                dockerfilePath: CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH,
           });
           imageBuilder.addExtraCertificates('path-to-my-extra-certs-folder');

           const provider = new CodeBuildRunner(this, 'CodeBuild', {
                imageBuilder: imageBuilder,
           });

           new GitHubRunners(
              this,
              'runners',
              {
                providers: [provider],
                extraCertificates: 'path-to-my-extra-certs-folder',
              }
           );

        :stability: experimental
        '''
        result = self._values.get("extra_certificates")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def idle_timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) Time to wait before stopping a runner that remains idle.

        If the user cancelled the job, or if another runner stole it, this stops the runner to avoid wasting resources.

        :default: 10 minutes

        :stability: experimental
        '''
        result = self._values.get("idle_timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def providers(self) -> typing.Optional[typing.List["IRunnerProvider"]]:
        '''(experimental) List of runner providers to use.

        At least one provider is required. Provider will be selected when its label matches the labels requested by the workflow job.

        :default: CodeBuild, Lambda and Fargate runners with all the defaults (no VPC or default account VPC)

        :stability: experimental
        '''
        result = self._values.get("providers")
        return typing.cast(typing.Optional[typing.List["IRunnerProvider"]], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(experimental) Security group attached to all management functions.

        Use this with to provide access to GitHub Enterprise Server hosted inside a VPC.

        :stability: experimental
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC used for all management functions.

        Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) VPC subnets used for all management functions.

        Use this with GitHub Enterprise Server hosted that's inaccessible from outside the VPC.

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GitHubRunnersProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IAmiBuilder")
class IAmiBuilder(typing_extensions.Protocol):
    '''(experimental) Interface for constructs that build an AMI that can be used in {@link IRunnerProvider}.

    Anything that ends up with a launch template pointing to an AMI that runs GitHub self-hosted runners can be used. A simple implementation could even point to an existing AMI and nothing else.

    The AMI can be further updated over time manually or using a schedule as long as it is always written to the same launch template.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self) -> "RunnerAmi":
        '''(experimental) Finalize and return all required information about the AMI built by this builder.

        This method can be called multiple times if the image is bound to multiple providers. Make sure you cache the image when implementing or return an error if this builder doesn't support reusing images.

        :return: ami

        :stability: experimental
        '''
        ...


class _IAmiBuilderProxy:
    '''(experimental) Interface for constructs that build an AMI that can be used in {@link IRunnerProvider}.

    Anything that ends up with a launch template pointing to an AMI that runs GitHub self-hosted runners can be used. A simple implementation could even point to an existing AMI and nothing else.

    The AMI can be further updated over time manually or using a schedule as long as it is always written to the same launch template.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IAmiBuilder"

    @jsii.member(jsii_name="bind")
    def bind(self) -> "RunnerAmi":
        '''(experimental) Finalize and return all required information about the AMI built by this builder.

        This method can be called multiple times if the image is bound to multiple providers. Make sure you cache the image when implementing or return an error if this builder doesn't support reusing images.

        :return: ami

        :stability: experimental
        '''
        return typing.cast("RunnerAmi", jsii.invoke(self, "bind", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAmiBuilder).__jsii_proxy_class__ = lambda : _IAmiBuilderProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IImageBuilder")
class IImageBuilder(typing_extensions.Protocol):
    '''(experimental) Interface for constructs that build an image that can be used in {@link IRunnerProvider}.

    Anything that ends up with an ECR repository containing a Docker image that runs GitHub self-hosted runners can be used. A simple implementation could even point to an existing image and nothing else.

    It's important that the specified image tag be available at the time the repository is available. Providers usually assume the image is ready and will fail if it's not.

    The image can be further updated over time manually or using a schedule as long as it is always written to the same tag.

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self) -> "RunnerImage":
        '''(experimental) Finalize and return all required information about the Docker image built by this builder.

        This method can be called multiple times if the image is bound to multiple providers. Make sure you cache the image when implementing or return an error if this builder doesn't support reusing images.

        :return: image

        :stability: experimental
        '''
        ...


class _IImageBuilderProxy:
    '''(experimental) Interface for constructs that build an image that can be used in {@link IRunnerProvider}.

    Anything that ends up with an ECR repository containing a Docker image that runs GitHub self-hosted runners can be used. A simple implementation could even point to an existing image and nothing else.

    It's important that the specified image tag be available at the time the repository is available. Providers usually assume the image is ready and will fail if it's not.

    The image can be further updated over time manually or using a schedule as long as it is always written to the same tag.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IImageBuilder"

    @jsii.member(jsii_name="bind")
    def bind(self) -> "RunnerImage":
        '''(experimental) Finalize and return all required information about the Docker image built by this builder.

        This method can be called multiple times if the image is bound to multiple providers. Make sure you cache the image when implementing or return an error if this builder doesn't support reusing images.

        :return: image

        :stability: experimental
        '''
        return typing.cast("RunnerImage", jsii.invoke(self, "bind", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageBuilder).__jsii_proxy_class__ = lambda : _IImageBuilderProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IRunnerAmiStatus")
class IRunnerAmiStatus(typing_extensions.Protocol):
    '''(experimental) AMI status returned from runner providers to be displayed as output of status function.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> builtins.str:
        '''(experimental) Id of launch template pointing to the latest AMI built by the AMI builder.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="amiBuilderLogGroup")
    def ami_builder_log_group(self) -> typing.Optional[builtins.str]:
        '''(experimental) Log group name for the AMI builder where history of builds can be analyzed.

        :stability: experimental
        '''
        ...


class _IRunnerAmiStatusProxy:
    '''(experimental) AMI status returned from runner providers to be displayed as output of status function.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IRunnerAmiStatus"

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(self) -> builtins.str:
        '''(experimental) Id of launch template pointing to the latest AMI built by the AMI builder.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "launchTemplate"))

    @builtins.property
    @jsii.member(jsii_name="amiBuilderLogGroup")
    def ami_builder_log_group(self) -> typing.Optional[builtins.str]:
        '''(experimental) Log group name for the AMI builder where history of builds can be analyzed.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amiBuilderLogGroup"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunnerAmiStatus).__jsii_proxy_class__ = lambda : _IRunnerAmiStatusProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IRunnerImageStatus")
class IRunnerImageStatus(typing_extensions.Protocol):
    '''(experimental) Image status returned from runner providers to be displayed in status.json.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageRepository")
    def image_repository(self) -> builtins.str:
        '''(experimental) Image repository where image builder pushes runner images.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> builtins.str:
        '''(experimental) Tag of image that should be used.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="imageBuilderLogGroup")
    def image_builder_log_group(self) -> typing.Optional[builtins.str]:
        '''(experimental) Log group name for the image builder where history of image builds can be analyzed.

        :stability: experimental
        '''
        ...


class _IRunnerImageStatusProxy:
    '''(experimental) Image status returned from runner providers to be displayed in status.json.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IRunnerImageStatus"

    @builtins.property
    @jsii.member(jsii_name="imageRepository")
    def image_repository(self) -> builtins.str:
        '''(experimental) Image repository where image builder pushes runner images.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageRepository"))

    @builtins.property
    @jsii.member(jsii_name="imageTag")
    def image_tag(self) -> builtins.str:
        '''(experimental) Tag of image that should be used.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "imageTag"))

    @builtins.property
    @jsii.member(jsii_name="imageBuilderLogGroup")
    def image_builder_log_group(self) -> typing.Optional[builtins.str]:
        '''(experimental) Log group name for the image builder where history of image builds can be analyzed.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageBuilderLogGroup"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunnerImageStatus).__jsii_proxy_class__ = lambda : _IRunnerImageStatusProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IRunnerProvider")
class IRunnerProvider(
    aws_cdk.aws_ec2.IConnectable,
    aws_cdk.aws_iam.IGrantable,
    typing_extensions.Protocol,
):
    '''(experimental) Interface for all runner providers.

    Implementations create all required resources and return a step function task that starts those resources from {@link getStepFunctionTask}.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) GitHub Actions labels used for this provider.

        These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for
        based on runs-on. We use match the labels from the webhook with the labels specified here. If all the labels specified here are present in the
        job's labels, this provider will be chosen and spawn a new runner.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function tasks that execute the runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantStateMachine")
    def grant_state_machine(
        self,
        state_machine_role: aws_cdk.aws_iam.IGrantable,
    ) -> None:
        '''(experimental) An optional method that modifies the role of the state machine after all the tasks have been generated.

        This can be used to add additional policy
        statements to the state machine role that are not automatically added by the task returned from {@link getStepFunctionTask}.

        :param state_machine_role: role for the state machine that executes the task returned from {@link getStepFunctionTask}.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="status")
    def status(
        self,
        status_function_role: aws_cdk.aws_iam.IGrantable,
    ) -> "IRunnerProviderStatus":
        '''(experimental) Return status of the runner provider to be used in the main status function.

        Also gives the status function any needed permissions to query the Docker image or AMI.

        :param status_function_role: grantable for the status function.

        :stability: experimental
        '''
        ...


class _IRunnerProviderProxy(
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_iam.IGrantable), # type: ignore[misc]
):
    '''(experimental) Interface for all runner providers.

    Implementations create all required resources and return a step function task that starts those resources from {@link getStepFunctionTask}.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IRunnerProvider"

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) GitHub Actions labels used for this provider.

        These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for
        based on runs-on. We use match the labels from the webhook with the labels specified here. If all the labels specified here are present in the
        job's labels, this provider will be chosen and spawn a new runner.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function tasks that execute the runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.member(jsii_name="grantStateMachine")
    def grant_state_machine(
        self,
        state_machine_role: aws_cdk.aws_iam.IGrantable,
    ) -> None:
        '''(experimental) An optional method that modifies the role of the state machine after all the tasks have been generated.

        This can be used to add additional policy
        statements to the state machine role that are not automatically added by the task returned from {@link getStepFunctionTask}.

        :param state_machine_role: role for the state machine that executes the task returned from {@link getStepFunctionTask}.

        :stability: experimental
        '''
        if __debug__:
            def stub(state_machine_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument state_machine_role", value=state_machine_role, expected_type=type_hints["state_machine_role"])
        return typing.cast(None, jsii.invoke(self, "grantStateMachine", [state_machine_role]))

    @jsii.member(jsii_name="status")
    def status(
        self,
        status_function_role: aws_cdk.aws_iam.IGrantable,
    ) -> "IRunnerProviderStatus":
        '''(experimental) Return status of the runner provider to be used in the main status function.

        Also gives the status function any needed permissions to query the Docker image or AMI.

        :param status_function_role: grantable for the status function.

        :stability: experimental
        '''
        if __debug__:
            def stub(status_function_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_function_role", value=status_function_role, expected_type=type_hints["status_function_role"])
        return typing.cast("IRunnerProviderStatus", jsii.invoke(self, "status", [status_function_role]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunnerProvider).__jsii_proxy_class__ = lambda : _IRunnerProviderProxy


@jsii.interface(jsii_type="@cloudsnorkel/cdk-github-runners.IRunnerProviderStatus")
class IRunnerProviderStatus(typing_extensions.Protocol):
    '''(experimental) Interface for runner image status used by status.json.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) Labels associated with provider.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''(experimental) Runner provider type.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="ami")
    def ami(self) -> typing.Optional[IRunnerAmiStatus]:
        '''(experimental) Details about AMI used by this runner provider.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> typing.Optional[IRunnerImageStatus]:
        '''(experimental) Details about Docker image used by this runner provider.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) Role attached to runners.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Security groups attached to runners.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="vpcArn")
    def vpc_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) VPC where runners will be launched.

        :stability: experimental
        '''
        ...


class _IRunnerProviderStatusProxy:
    '''(experimental) Interface for runner image status used by status.json.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@cloudsnorkel/cdk-github-runners.IRunnerProviderStatus"

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) Labels associated with provider.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''(experimental) Runner provider type.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="ami")
    def ami(self) -> typing.Optional[IRunnerAmiStatus]:
        '''(experimental) Details about AMI used by this runner provider.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IRunnerAmiStatus], jsii.get(self, "ami"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> typing.Optional[IRunnerImageStatus]:
        '''(experimental) Details about Docker image used by this runner provider.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IRunnerImageStatus], jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) Role attached to runners.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) Security groups attached to runners.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroups"))

    @builtins.property
    @jsii.member(jsii_name="vpcArn")
    def vpc_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) VPC where runners will be launched.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunnerProviderStatus).__jsii_proxy_class__ = lambda : _IRunnerProviderStatusProxy


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.ImageBuilderAsset",
    jsii_struct_bases=[],
    name_mapping={"asset": "asset", "path": "path"},
)
class ImageBuilderAsset:
    def __init__(
        self,
        *,
        asset: aws_cdk.aws_s3_assets.Asset,
        path: builtins.str,
    ) -> None:
        '''(experimental) An asset including file or directory to place inside the built image.

        :param asset: (experimental) Asset to place in the image.
        :param path: (experimental) Path to place asset in the image.

        :stability: experimental
        '''
        if __debug__:
            def stub(*, asset: aws_cdk.aws_s3_assets.Asset, path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument asset", value=asset, expected_type=type_hints["asset"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {
            "asset": asset,
            "path": path,
        }

    @builtins.property
    def asset(self) -> aws_cdk.aws_s3_assets.Asset:
        '''(experimental) Asset to place in the image.

        :stability: experimental
        '''
        result = self._values.get("asset")
        assert result is not None, "Required property 'asset' is missing"
        return typing.cast(aws_cdk.aws_s3_assets.Asset, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''(experimental) Path to place asset in the image.

        :stability: experimental
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageBuilderAsset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ImageBuilderComponent(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.ImageBuilderComponent",
):
    '''(experimental) Components are a set of commands to run and optional files to add to an image.

    Components are the building blocks of images built by Image Builder.

    Example::

       new ImageBuilderComponent(this, 'AWS CLI', {
          platform: 'Windows',
          displayName: 'AWS CLI',
          description: 'Install latest version of AWS CLI',
          commands: [
            '$ErrorActionPreference = \\'Stop\\'',
            'Start-Process msiexec.exe -Wait -ArgumentList \\'/i https://awscli.amazonaws.com/AWSCLIV2.msi /qn\\'',
          ],
       }

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        commands: typing.Sequence[builtins.str],
        description: builtins.str,
        display_name: builtins.str,
        platform: builtins.str,
        assets: typing.Optional[typing.Sequence[typing.Union[ImageBuilderAsset, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param commands: (experimental) Shell commands to run when adding this component to the image. On Linux, these are bash commands. On Windows, there are PowerShell commands.
        :param description: (experimental) Component description.
        :param display_name: (experimental) Component display name.
        :param platform: (experimental) Component platform. Must match the builder platform.
        :param assets: (experimental) Optional assets to add to the built image.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                commands: typing.Sequence[builtins.str],
                description: builtins.str,
                display_name: builtins.str,
                platform: builtins.str,
                assets: typing.Optional[typing.Sequence[typing.Union[ImageBuilderAsset, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ImageBuilderComponentProperties(
            commands=commands,
            description=description,
            display_name=display_name,
            platform=platform,
            assets=assets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="grantAssetsRead")
    def grant_assets_read(self, grantee: aws_cdk.aws_iam.IGrantable) -> None:
        '''(experimental) Grants read permissions to the principal on the assets buckets.

        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            def stub(grantee: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(None, jsii.invoke(self, "grantAssetsRead", [grantee]))

    @jsii.member(jsii_name="version")
    def _version(
        self,
        type: builtins.str,
        name: builtins.str,
        data: typing.Any,
    ) -> builtins.str:
        '''
        :param type: -
        :param name: -
        :param data: -

        :stability: experimental
        '''
        if __debug__:
            def stub(type: builtins.str, name: builtins.str, data: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
        return typing.cast(builtins.str, jsii.invoke(self, "version", [type, name, data]))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) Component ARN.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''(experimental) Supported platform for the component.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "platform"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.ImageBuilderComponentProperties",
    jsii_struct_bases=[],
    name_mapping={
        "commands": "commands",
        "description": "description",
        "display_name": "displayName",
        "platform": "platform",
        "assets": "assets",
    },
)
class ImageBuilderComponentProperties:
    def __init__(
        self,
        *,
        commands: typing.Sequence[builtins.str],
        description: builtins.str,
        display_name: builtins.str,
        platform: builtins.str,
        assets: typing.Optional[typing.Sequence[typing.Union[ImageBuilderAsset, typing.Dict[str, typing.Any]]]] = None,
    ) -> None:
        '''(experimental) Properties for ImageBuilderComponent construct.

        :param commands: (experimental) Shell commands to run when adding this component to the image. On Linux, these are bash commands. On Windows, there are PowerShell commands.
        :param description: (experimental) Component description.
        :param display_name: (experimental) Component display name.
        :param platform: (experimental) Component platform. Must match the builder platform.
        :param assets: (experimental) Optional assets to add to the built image.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                commands: typing.Sequence[builtins.str],
                description: builtins.str,
                display_name: builtins.str,
                platform: builtins.str,
                assets: typing.Optional[typing.Sequence[typing.Union[ImageBuilderAsset, typing.Dict[str, typing.Any]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument commands", value=commands, expected_type=type_hints["commands"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument assets", value=assets, expected_type=type_hints["assets"])
        self._values: typing.Dict[str, typing.Any] = {
            "commands": commands,
            "description": description,
            "display_name": display_name,
            "platform": platform,
        }
        if assets is not None:
            self._values["assets"] = assets

    @builtins.property
    def commands(self) -> typing.List[builtins.str]:
        '''(experimental) Shell commands to run when adding this component to the image.

        On Linux, these are bash commands. On Windows, there are PowerShell commands.

        :stability: experimental
        '''
        result = self._values.get("commands")
        assert result is not None, "Required property 'commands' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> builtins.str:
        '''(experimental) Component description.

        :stability: experimental
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''(experimental) Component display name.

        :stability: experimental
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''(experimental) Component platform.

        Must match the builder platform.

        :stability: experimental
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assets(self) -> typing.Optional[typing.List[ImageBuilderAsset]]:
        '''(experimental) Optional assets to add to the built image.

        :stability: experimental
        '''
        result = self._values.get("assets")
        return typing.cast(typing.Optional[typing.List[ImageBuilderAsset]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageBuilderComponentProperties(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRunnerProvider)
class LambdaRunner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.LambdaRunner",
):
    '''(experimental) GitHub Actions runner provider using Lambda to execute jobs.

    Creates a Docker-based function that gets executed for each job.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ephemeral_storage_size: (experimental) The size of the function’s /tmp directory in MiB. Default: 10 GiB
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. The default command (``CMD``) should be ``["runner.handler"]`` which points to an included ``runner.js`` with a function named ``handler``. The function should start the GitHub runner. Default: image builder with LambdaRunner.LINUX_X64_DOCKERFILE_PATH as Dockerfile
        :param label: (deprecated) GitHub Actions label used for this provider. Default: undefined
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['lambda']
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 2048
        :param security_group: (deprecated) Security group to assign to this instance. Default: public lambda with no security group
        :param security_groups: (experimental) Security groups to assign to this instance. Default: public lambda with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
                image_builder: typing.Optional[IImageBuilder] = None,
                label: typing.Optional[builtins.str] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                memory_size: typing.Optional[jsii.Number] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaRunnerProps(
            ephemeral_storage_size=ephemeral_storage_size,
            image_builder=image_builder,
            label=label,
            labels=labels,
            memory_size=memory_size,
            security_group=security_group,
            security_groups=security_groups,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.member(jsii_name="grantStateMachine")
    def grant_state_machine(self, _: aws_cdk.aws_iam.IGrantable) -> None:
        '''(experimental) An optional method that modifies the role of the state machine after all the tasks have been generated.

        This can be used to add additional policy
        statements to the state machine role that are not automatically added by the task returned from {@link getStepFunctionTask}.

        :param _: -

        :stability: experimental
        '''
        if __debug__:
            def stub(_: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        return typing.cast(None, jsii.invoke(self, "grantStateMachine", [_]))

    @jsii.member(jsii_name="labelsFromProperties")
    def _labels_from_properties(
        self,
        default_label: builtins.str,
        props_label: typing.Optional[builtins.str] = None,
        props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> typing.List[builtins.str]:
        '''
        :param default_label: -
        :param props_label: -
        :param props_labels: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                default_label: builtins.str,
                props_label: typing.Optional[builtins.str] = None,
                props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_label", value=default_label, expected_type=type_hints["default_label"])
            check_type(argname="argument props_label", value=props_label, expected_type=type_hints["props_label"])
            check_type(argname="argument props_labels", value=props_labels, expected_type=type_hints["props_labels"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "labelsFromProperties", [default_label, props_label, props_labels]))

    @jsii.member(jsii_name="status")
    def status(
        self,
        status_function_role: aws_cdk.aws_iam.IGrantable,
    ) -> IRunnerProviderStatus:
        '''(experimental) Return status of the runner provider to be used in the main status function.

        Also gives the status function any needed permissions to query the Docker image or AMI.

        :param status_function_role: -

        :stability: experimental
        '''
        if __debug__:
            def stub(status_function_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_function_role", value=status_function_role, expected_type=type_hints["status_function_role"])
        return typing.cast(IRunnerProviderStatus, jsii.invoke(self, "status", [status_function_role]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64_DOCKERFILE_PATH")
    def LINUX_ARM64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux ARM64 with all the requirement for Lambda runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be similar to public.ecr.aws/lambda/nodejs:14.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_ARM64_DOCKERFILE_PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_X64_DOCKERFILE_PATH")
    def LINUX_X64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux x64 with all the requirement for Lambda runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be similar to public.ecr.aws/lambda/nodejs:14.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_X64_DOCKERFILE_PATH"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> aws_cdk.aws_lambda.Function:
        '''(experimental) The function hosting the GitHub runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_lambda.Function, jsii.get(self, "function"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> "RunnerImage":
        '''(experimental) Docker image loaded with GitHub Actions Runner and its prerequisites.

        The image is built by an image builder and is specific to Lambda.

        :stability: experimental
        '''
        return typing.cast("RunnerImage", jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) Labels associated with this provider.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))


class LinuxUbuntuComponents(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.LinuxUbuntuComponents",
):
    '''(experimental) Components for Ubuntu Linux that can be used with AWS Image Builder based builders.

    These cannot be used by {@link CodeBuildImageBuilder}.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="awsCli")
    @builtins.classmethod
    def aws_cli(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "awsCli", [scope, id, architecture]))

    @jsii.member(jsii_name="docker")
    @builtins.classmethod
    def docker(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        _architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param _architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                _architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument _architecture", value=_architecture, expected_type=type_hints["_architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "docker", [scope, id, _architecture]))

    @jsii.member(jsii_name="extraCertificates")
    @builtins.classmethod
    def extra_certificates(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        path: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param path: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                path: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "extraCertificates", [scope, id, path]))

    @jsii.member(jsii_name="git")
    @builtins.classmethod
    def git(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        _architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param _architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                _architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument _architecture", value=_architecture, expected_type=type_hints["_architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "git", [scope, id, _architecture]))

    @jsii.member(jsii_name="githubCli")
    @builtins.classmethod
    def github_cli(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        _architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param _architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                _architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument _architecture", value=_architecture, expected_type=type_hints["_architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "githubCli", [scope, id, _architecture]))

    @jsii.member(jsii_name="githubRunner")
    @builtins.classmethod
    def github_runner(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        runner_version: "RunnerVersion",
        architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param runner_version: -
        :param architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                runner_version: RunnerVersion,
                architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "githubRunner", [scope, id, runner_version, architecture]))

    @jsii.member(jsii_name="requiredPackages")
    @builtins.classmethod
    def required_packages(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "requiredPackages", [scope, id, architecture]))

    @jsii.member(jsii_name="runnerUser")
    @builtins.classmethod
    def runner_user(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        _architecture: Architecture,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param _architecture: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                _architecture: Architecture,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument _architecture", value=_architecture, expected_type=type_hints["_architecture"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "runnerUser", [scope, id, _architecture]))


class Os(metaclass=jsii.JSIIMeta, jsii_type="@cloudsnorkel/cdk-github-runners.Os"):
    '''(experimental) OS enum for an image.

    :stability: experimental
    '''

    @jsii.member(jsii_name="is")
    def is_(self, os: "Os") -> builtins.bool:
        '''(experimental) Checks if the given OS is the same as this one.

        :param os: OS to compare.

        :stability: experimental
        '''
        if __debug__:
            def stub(os: Os) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        return typing.cast(builtins.bool, jsii.invoke(self, "is", [os]))

    @jsii.member(jsii_name="isIn")
    def is_in(self, oses: typing.Sequence["Os"]) -> builtins.bool:
        '''(experimental) Checks if this OS is in a given list.

        :param oses: list of OS to check.

        :stability: experimental
        '''
        if __debug__:
            def stub(oses: typing.Sequence[Os]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument oses", value=oses, expected_type=type_hints["oses"])
        return typing.cast(builtins.bool, jsii.invoke(self, "isIn", [oses]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX")
    def LINUX(cls) -> "Os":
        '''(experimental) Linux.

        :stability: experimental
        '''
        return typing.cast("Os", jsii.sget(cls, "LINUX"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WINDOWS")
    def WINDOWS(cls) -> "Os":
        '''(experimental) Windows.

        :stability: experimental
        '''
        return typing.cast("Os", jsii.sget(cls, "WINDOWS"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerAmi",
    jsii_struct_bases=[],
    name_mapping={
        "architecture": "architecture",
        "launch_template": "launchTemplate",
        "os": "os",
        "runner_version": "runnerVersion",
        "log_group": "logGroup",
    },
)
class RunnerAmi:
    def __init__(
        self,
        *,
        architecture: Architecture,
        launch_template: aws_cdk.aws_ec2.ILaunchTemplate,
        os: Os,
        runner_version: "RunnerVersion",
        log_group: typing.Optional[aws_cdk.aws_logs.LogGroup] = None,
    ) -> None:
        '''(experimental) Description of a AMI built by {@link IAmiBuilder}.

        :param architecture: (experimental) Architecture of the image.
        :param launch_template: (experimental) Launch template pointing to the latest AMI.
        :param os: (experimental) OS type of the image.
        :param runner_version: (experimental) Installed runner version.
        :param log_group: (experimental) Log group where image builds are logged.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                architecture: Architecture,
                launch_template: aws_cdk.aws_ec2.ILaunchTemplate,
                os: Os,
                runner_version: RunnerVersion,
                log_group: typing.Optional[aws_cdk.aws_logs.LogGroup] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "architecture": architecture,
            "launch_template": launch_template,
            "os": os,
            "runner_version": runner_version,
        }
        if log_group is not None:
            self._values["log_group"] = log_group

    @builtins.property
    def architecture(self) -> Architecture:
        '''(experimental) Architecture of the image.

        :stability: experimental
        '''
        result = self._values.get("architecture")
        assert result is not None, "Required property 'architecture' is missing"
        return typing.cast(Architecture, result)

    @builtins.property
    def launch_template(self) -> aws_cdk.aws_ec2.ILaunchTemplate:
        '''(experimental) Launch template pointing to the latest AMI.

        :stability: experimental
        '''
        result = self._values.get("launch_template")
        assert result is not None, "Required property 'launch_template' is missing"
        return typing.cast(aws_cdk.aws_ec2.ILaunchTemplate, result)

    @builtins.property
    def os(self) -> Os:
        '''(experimental) OS type of the image.

        :stability: experimental
        '''
        result = self._values.get("os")
        assert result is not None, "Required property 'os' is missing"
        return typing.cast(Os, result)

    @builtins.property
    def runner_version(self) -> "RunnerVersion":
        '''(experimental) Installed runner version.

        :stability: experimental
        '''
        result = self._values.get("runner_version")
        assert result is not None, "Required property 'runner_version' is missing"
        return typing.cast("RunnerVersion", result)

    @builtins.property
    def log_group(self) -> typing.Optional[aws_cdk.aws_logs.LogGroup]:
        '''(experimental) Log group where image builds are logged.

        :stability: experimental
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.LogGroup], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerAmi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerImage",
    jsii_struct_bases=[],
    name_mapping={
        "architecture": "architecture",
        "image_repository": "imageRepository",
        "image_tag": "imageTag",
        "os": "os",
        "runner_version": "runnerVersion",
        "log_group": "logGroup",
    },
)
class RunnerImage:
    def __init__(
        self,
        *,
        architecture: Architecture,
        image_repository: aws_cdk.aws_ecr.IRepository,
        image_tag: builtins.str,
        os: Os,
        runner_version: "RunnerVersion",
        log_group: typing.Optional[aws_cdk.aws_logs.LogGroup] = None,
    ) -> None:
        '''(experimental) Description of a Docker image built by {@link IImageBuilder}.

        :param architecture: (experimental) Architecture of the image.
        :param image_repository: (experimental) ECR repository containing the image.
        :param image_tag: (experimental) Static image tag where the image will be pushed.
        :param os: (experimental) OS type of the image.
        :param runner_version: (experimental) Installed runner version.
        :param log_group: (experimental) Log group where image builds are logged.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                architecture: Architecture,
                image_repository: aws_cdk.aws_ecr.IRepository,
                image_tag: builtins.str,
                os: Os,
                runner_version: RunnerVersion,
                log_group: typing.Optional[aws_cdk.aws_logs.LogGroup] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument image_repository", value=image_repository, expected_type=type_hints["image_repository"])
            check_type(argname="argument image_tag", value=image_tag, expected_type=type_hints["image_tag"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "architecture": architecture,
            "image_repository": image_repository,
            "image_tag": image_tag,
            "os": os,
            "runner_version": runner_version,
        }
        if log_group is not None:
            self._values["log_group"] = log_group

    @builtins.property
    def architecture(self) -> Architecture:
        '''(experimental) Architecture of the image.

        :stability: experimental
        '''
        result = self._values.get("architecture")
        assert result is not None, "Required property 'architecture' is missing"
        return typing.cast(Architecture, result)

    @builtins.property
    def image_repository(self) -> aws_cdk.aws_ecr.IRepository:
        '''(experimental) ECR repository containing the image.

        :stability: experimental
        '''
        result = self._values.get("image_repository")
        assert result is not None, "Required property 'image_repository' is missing"
        return typing.cast(aws_cdk.aws_ecr.IRepository, result)

    @builtins.property
    def image_tag(self) -> builtins.str:
        '''(experimental) Static image tag where the image will be pushed.

        :stability: experimental
        '''
        result = self._values.get("image_tag")
        assert result is not None, "Required property 'image_tag' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def os(self) -> Os:
        '''(experimental) OS type of the image.

        :stability: experimental
        '''
        result = self._values.get("os")
        assert result is not None, "Required property 'os' is missing"
        return typing.cast(Os, result)

    @builtins.property
    def runner_version(self) -> "RunnerVersion":
        '''(experimental) Installed runner version.

        :stability: experimental
        '''
        result = self._values.get("runner_version")
        assert result is not None, "Required property 'runner_version' is missing"
        return typing.cast("RunnerVersion", result)

    @builtins.property
    def log_group(self) -> typing.Optional[aws_cdk.aws_logs.LogGroup]:
        '''(experimental) Log group where image builds are logged.

        :stability: experimental
        '''
        result = self._values.get("log_group")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.LogGroup], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerProviderProps",
    jsii_struct_bases=[],
    name_mapping={"log_retention": "logRetention"},
)
class RunnerProviderProps:
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''(experimental) Common properties for all runner providers.

        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerRuntimeParameters",
    jsii_struct_bases=[],
    name_mapping={
        "github_domain_path": "githubDomainPath",
        "owner_path": "ownerPath",
        "repo_path": "repoPath",
        "runner_name_path": "runnerNamePath",
        "runner_token_path": "runnerTokenPath",
    },
)
class RunnerRuntimeParameters:
    def __init__(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> None:
        '''(experimental) Workflow job parameters as parsed from the webhook event. Pass these into your runner executor and run something like:.

        Example::

           ./config.sh --unattended --url "https://${GITHUB_DOMAIN}/${OWNER}/${REPO}" --token "${RUNNER_TOKEN}" --ephemeral --work _work --labels "${RUNNER_LABEL}" --name "${RUNNER_NAME}" --disableupdate

        All parameters are specified as step function paths and therefore must be used only in step function task parameters.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                github_domain_path: builtins.str,
                owner_path: builtins.str,
                repo_path: builtins.str,
                runner_name_path: builtins.str,
                runner_token_path: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument github_domain_path", value=github_domain_path, expected_type=type_hints["github_domain_path"])
            check_type(argname="argument owner_path", value=owner_path, expected_type=type_hints["owner_path"])
            check_type(argname="argument repo_path", value=repo_path, expected_type=type_hints["repo_path"])
            check_type(argname="argument runner_name_path", value=runner_name_path, expected_type=type_hints["runner_name_path"])
            check_type(argname="argument runner_token_path", value=runner_token_path, expected_type=type_hints["runner_token_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "github_domain_path": github_domain_path,
            "owner_path": owner_path,
            "repo_path": repo_path,
            "runner_name_path": runner_name_path,
            "runner_token_path": runner_token_path,
        }

    @builtins.property
    def github_domain_path(self) -> builtins.str:
        '''(experimental) Path to GitHub domain.

        Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.

        :stability: experimental
        '''
        result = self._values.get("github_domain_path")
        assert result is not None, "Required property 'github_domain_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner_path(self) -> builtins.str:
        '''(experimental) Path to repostiroy owner name.

        :stability: experimental
        '''
        result = self._values.get("owner_path")
        assert result is not None, "Required property 'owner_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repo_path(self) -> builtins.str:
        '''(experimental) Path to repository name.

        :stability: experimental
        '''
        result = self._values.get("repo_path")
        assert result is not None, "Required property 'repo_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runner_name_path(self) -> builtins.str:
        '''(experimental) Path to desired runner name.

        We specifically set the name to make troubleshooting easier.

        :stability: experimental
        '''
        result = self._values.get("runner_name_path")
        assert result is not None, "Required property 'runner_name_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def runner_token_path(self) -> builtins.str:
        '''(experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        result = self._values.get("runner_token_path")
        assert result is not None, "Required property 'runner_token_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunnerRuntimeParameters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RunnerVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.RunnerVersion",
):
    '''(experimental) Defines desired GitHub Actions runner version.

    :stability: experimental
    '''

    def __init__(self, version: builtins.str) -> None:
        '''
        :param version: -

        :stability: experimental
        '''
        if __debug__:
            def stub(version: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        jsii.create(self.__class__, self, [version])

    @jsii.member(jsii_name="latest")
    @builtins.classmethod
    def latest(cls) -> "RunnerVersion":
        '''(experimental) Use the latest version available at the time the runner provider image is built.

        :stability: experimental
        '''
        return typing.cast("RunnerVersion", jsii.sinvoke(cls, "latest", []))

    @jsii.member(jsii_name="specific")
    @builtins.classmethod
    def specific(cls, version: builtins.str) -> "RunnerVersion":
        '''(experimental) Use a specific version.

        :param version: GitHub Runner version.

        :see: https://github.com/actions/runner/releases
        :stability: experimental
        '''
        if __debug__:
            def stub(version: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("RunnerVersion", jsii.sinvoke(cls, "specific", [version]))

    @jsii.member(jsii_name="is")
    def is_(self, other: "RunnerVersion") -> builtins.bool:
        '''(experimental) Check if two versions are the same.

        :param other: version to compare.

        :stability: experimental
        '''
        if __debug__:
            def stub(other: RunnerVersion) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument other", value=other, expected_type=type_hints["other"])
        return typing.cast(builtins.bool, jsii.invoke(self, "is", [other]))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


class Secrets(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.Secrets",
):
    '''(experimental) Secrets required for GitHub runners operation.

    :stability: experimental
    '''

    def __init__(self, scope: constructs.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) Authentication secret for GitHub containing either app details or personal authentication token.

        This secret is used to register runners and
        cancel jobs when the runner fails to start.

        This secret is meant to be edited by the user after being created.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="githubPrivateKey")
    def github_private_key(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) GitHub app private key. Not needed when using personal authentication tokens.

        This secret is meant to be edited by the user after being created. It is separate than the main GitHub secret because inserting private keys into JSON is hard.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "githubPrivateKey"))

    @builtins.property
    @jsii.member(jsii_name="setup")
    def setup(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) Setup secret used to authenticate user for our setup wizard.

        Should be empty after setup has been completed.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "setup"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> aws_cdk.aws_secretsmanager.Secret:
        '''(experimental) Webhook secret used to confirm events are coming from GitHub and nowhere else.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_secretsmanager.Secret, jsii.get(self, "webhook"))


class StaticRunnerImage(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.StaticRunnerImage",
):
    '''(experimental) Helper class with methods to use static images that are built outside the context of this project.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromDockerHub")
    @builtins.classmethod
    def from_docker_hub(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        image: builtins.str,
        architecture: typing.Optional[Architecture] = None,
        os: typing.Optional[Os] = None,
    ) -> IImageBuilder:
        '''(experimental) Create a builder from an existing Docker Hub image.

        The image must already have GitHub Actions runner installed. You are responsible to update it and remove it when done.

        We create a CodeBuild image builder behind the scenes to copy the image over to ECR. This helps avoid Docker Hub rate limits and prevent failures.

        :param scope: -
        :param id: -
        :param image: Docker Hub image with optional tag.
        :param architecture: image architecture.
        :param os: image OS.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                image: builtins.str,
                architecture: typing.Optional[Architecture] = None,
                os: typing.Optional[Os] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        return typing.cast(IImageBuilder, jsii.sinvoke(cls, "fromDockerHub", [scope, id, image, architecture, os]))

    @jsii.member(jsii_name="fromEcrRepository")
    @builtins.classmethod
    def from_ecr_repository(
        cls,
        repository: aws_cdk.aws_ecr.IRepository,
        tag: typing.Optional[builtins.str] = None,
        architecture: typing.Optional[Architecture] = None,
        os: typing.Optional[Os] = None,
    ) -> IImageBuilder:
        '''(experimental) Create a builder (that doesn't actually build anything) from an existing image in an existing repository.

        The image must already have GitHub Actions runner installed. You are responsible to update it and remove it when done.

        :param repository: ECR repository.
        :param tag: image tag.
        :param architecture: image architecture.
        :param os: image OS.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                repository: aws_cdk.aws_ecr.IRepository,
                tag: typing.Optional[builtins.str] = None,
                architecture: typing.Optional[Architecture] = None,
                os: typing.Optional[Os] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
            check_type(argname="argument os", value=os, expected_type=type_hints["os"])
        return typing.cast(IImageBuilder, jsii.sinvoke(cls, "fromEcrRepository", [repository, tag, architecture, os]))


class WindowsComponents(
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.WindowsComponents",
):
    '''(experimental) Components for Windows that can be used with AWS Image Builder based builders.

    These cannot be used by {@link CodeBuildImageBuilder}.

    :stability: experimental
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="awsCli")
    @builtins.classmethod
    def aws_cli(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "awsCli", [scope, id]))

    @jsii.member(jsii_name="cloudwatchAgent")
    @builtins.classmethod
    def cloudwatch_agent(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "cloudwatchAgent", [scope, id]))

    @jsii.member(jsii_name="docker")
    @builtins.classmethod
    def docker(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "docker", [scope, id]))

    @jsii.member(jsii_name="extraCertificates")
    @builtins.classmethod
    def extra_certificates(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        path: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param path: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                path: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "extraCertificates", [scope, id, path]))

    @jsii.member(jsii_name="git")
    @builtins.classmethod
    def git(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "git", [scope, id]))

    @jsii.member(jsii_name="githubCli")
    @builtins.classmethod
    def github_cli(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -

        :stability: experimental
        '''
        if __debug__:
            def stub(scope: constructs.Construct, id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "githubCli", [scope, id]))

    @jsii.member(jsii_name="githubRunner")
    @builtins.classmethod
    def github_runner(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        runner_version: RunnerVersion,
    ) -> ImageBuilderComponent:
        '''
        :param scope: -
        :param id: -
        :param runner_version: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                runner_version: RunnerVersion,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument runner_version", value=runner_version, expected_type=type_hints["runner_version"])
        return typing.cast(ImageBuilderComponent, jsii.sinvoke(cls, "githubRunner", [scope, id, runner_version]))


@jsii.implements(IImageBuilder)
class CodeBuildImageBuilder(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildImageBuilder",
):
    '''(experimental) An image builder that uses CodeBuild to build Docker images pre-baked with all the GitHub Actions runner requirements.

    Builders can be used with runner providers.

    Each builder re-runs automatically at a set interval to make sure the images contain the latest versions of everything.

    You can create an instance of this construct to customize the image used to spin-up runners. Each provider has its own requirements for what an image should do. That's why they each provide their own Dockerfile.

    For example, to set a specific runner version, rebuild the image every 2 weeks, and add a few packages for the Fargate provider, use::

       const builder = new CodeBuildImageBuilder(this, 'Builder', {
            dockerfilePath: FargateProvider.LINUX_X64_DOCKERFILE_PATH,
            runnerVersion: RunnerVersion.specific('2.293.0'),
            rebuildInterval: Duration.days(14),
       });
       builder.setBuildArg('EXTRA_PACKAGES', 'nginx xz-utils');
       new FargateRunner(this, 'Fargate provider', {
            label: 'customized-fargate',
            imageBuilder: builder,
       });

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        dockerfile_path: builtins.str,
        architecture: typing.Optional[Architecture] = None,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional[Os] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional[RunnerVersion] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dockerfile_path: (experimental) Path to Dockerfile to be built. It can be a path to a Dockerfile, a folder containing a Dockerfile, or a zip file containing a Dockerfile.
        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (experimental) Security Group to assign to this instance. Default: public project with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to build the image in. Default: no VPC

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                dockerfile_path: builtins.str,
                architecture: typing.Optional[Architecture] = None,
                compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
                log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                os: typing.Optional[Os] = None,
                rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
                runner_version: typing.Optional[RunnerVersion] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CodeBuildImageBuilderProps(
            dockerfile_path=dockerfile_path,
            architecture=architecture,
            compute_type=compute_type,
            log_removal_policy=log_removal_policy,
            log_retention=log_retention,
            os=os,
            rebuild_interval=rebuild_interval,
            runner_version=runner_version,
            security_group=security_group,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addExtraCertificates")
    def add_extra_certificates(self, path: builtins.str) -> None:
        '''(experimental) Add extra trusted certificates. This helps deal with self-signed certificates for GitHub Enterprise Server.

        All first party Dockerfiles support this. Others may not.

        :param path: path to directory containing a file called certs.pem containing all the required certificates.

        :stability: experimental
        '''
        if __debug__:
            def stub(path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(None, jsii.invoke(self, "addExtraCertificates", [path]))

    @jsii.member(jsii_name="addFiles")
    def add_files(self, source_path: builtins.str, dest_name: builtins.str) -> None:
        '''(experimental) Uploads a folder to the build server at a given folder name.

        :param source_path: path to source directory.
        :param dest_name: name of destination folder.

        :stability: experimental
        '''
        if __debug__:
            def stub(source_path: builtins.str, dest_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            check_type(argname="argument dest_name", value=dest_name, expected_type=type_hints["dest_name"])
        return typing.cast(None, jsii.invoke(self, "addFiles", [source_path, dest_name]))

    @jsii.member(jsii_name="addPolicyStatement")
    def add_policy_statement(self, statement: aws_cdk.aws_iam.PolicyStatement) -> None:
        '''(experimental) Add a policy statement to the builder to access resources required to the image build.

        :param statement: IAM policy statement.

        :stability: experimental
        '''
        if __debug__:
            def stub(statement: aws_cdk.aws_iam.PolicyStatement) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addPolicyStatement", [statement]))

    @jsii.member(jsii_name="addPostBuildCommand")
    def add_post_build_command(self, command: builtins.str) -> None:
        '''(experimental) Adds a command that runs after ``docker build`` and ``docker push``.

        :param command: command to add.

        :stability: experimental
        '''
        if __debug__:
            def stub(command: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
        return typing.cast(None, jsii.invoke(self, "addPostBuildCommand", [command]))

    @jsii.member(jsii_name="addPreBuildCommand")
    def add_pre_build_command(self, command: builtins.str) -> None:
        '''(experimental) Adds a command that runs before ``docker build``.

        :param command: command to add.

        :stability: experimental
        '''
        if __debug__:
            def stub(command: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
        return typing.cast(None, jsii.invoke(self, "addPreBuildCommand", [command]))

    @jsii.member(jsii_name="bind")
    def bind(self) -> RunnerImage:
        '''(experimental) Called by IRunnerProvider to finalize settings and create the image builder.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.invoke(self, "bind", []))

    @jsii.member(jsii_name="setBuildArg")
    def set_build_arg(self, name: builtins.str, value: builtins.str) -> None:
        '''(experimental) Adds a build argument for Docker.

        See the documentation for the Dockerfile you're using for a list of supported build arguments.

        :param name: build argument name.
        :param value: build argument value.

        :stability: experimental
        '''
        if __debug__:
            def stub(name: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "setBuildArg", [name, value]))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> CodeBuildImageBuilderProps:
        '''
        :stability: experimental
        '''
        return typing.cast(CodeBuildImageBuilderProps, jsii.get(self, "props"))


@jsii.implements(IRunnerProvider)
class CodeBuildRunner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildRunner",
):
    '''(experimental) GitHub Actions runner provider using CodeBuild to execute jobs.

    Creates a project that gets started for each job.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param image_builder: (experimental) Image builder for CodeBuild image with GitHub runner pre-configured. A user named ``runner`` is expected to exist with access to Docker-in-Docker. Default: image builder with ``CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (deprecated) GitHub Actions label used for this provider. Default: undefined
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['codebuild']
        :param security_group: (deprecated) Security group to assign to this instance. Default: public project with no security group
        :param security_groups: (experimental) Security groups to assign to this instance. Default: a new security group, if {@link vpc} is used
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
                image_builder: typing.Optional[IImageBuilder] = None,
                label: typing.Optional[builtins.str] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CodeBuildRunnerProps(
            compute_type=compute_type,
            image_builder=image_builder,
            label=label,
            labels=labels,
            security_group=security_group,
            security_groups=security_groups,
            subnet_selection=subnet_selection,
            timeout=timeout,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.member(jsii_name="grantStateMachine")
    def grant_state_machine(self, _: aws_cdk.aws_iam.IGrantable) -> None:
        '''(experimental) An optional method that modifies the role of the state machine after all the tasks have been generated.

        This can be used to add additional policy
        statements to the state machine role that are not automatically added by the task returned from {@link getStepFunctionTask}.

        :param _: -

        :stability: experimental
        '''
        if __debug__:
            def stub(_: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        return typing.cast(None, jsii.invoke(self, "grantStateMachine", [_]))

    @jsii.member(jsii_name="labelsFromProperties")
    def _labels_from_properties(
        self,
        default_label: builtins.str,
        props_label: typing.Optional[builtins.str] = None,
        props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> typing.List[builtins.str]:
        '''
        :param default_label: -
        :param props_label: -
        :param props_labels: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                default_label: builtins.str,
                props_label: typing.Optional[builtins.str] = None,
                props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_label", value=default_label, expected_type=type_hints["default_label"])
            check_type(argname="argument props_label", value=props_label, expected_type=type_hints["props_label"])
            check_type(argname="argument props_labels", value=props_labels, expected_type=type_hints["props_labels"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "labelsFromProperties", [default_label, props_label, props_labels]))

    @jsii.member(jsii_name="status")
    def status(
        self,
        status_function_role: aws_cdk.aws_iam.IGrantable,
    ) -> IRunnerProviderStatus:
        '''(experimental) Return status of the runner provider to be used in the main status function.

        Also gives the status function any needed permissions to query the Docker image or AMI.

        :param status_function_role: -

        :stability: experimental
        '''
        if __debug__:
            def stub(status_function_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_function_role", value=status_function_role, expected_type=type_hints["status_function_role"])
        return typing.cast(IRunnerProviderStatus, jsii.invoke(self, "status", [status_function_role]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64_DOCKERFILE_PATH")
    def LINUX_ARM64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux ARM64 with all the requirements for CodeBuild runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.
        - ``DOCKER_CHANNEL`` overrides the channel from which Docker will be downloaded. Defaults to ``"stable"``.
        - ``DIND_COMMIT`` overrides the commit where dind is found.
        - ``DOCKER_VERSION`` overrides the installed Docker version.
        - ``DOCKER_COMPOSE_VERSION`` overrides the installed docker-compose version.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_ARM64_DOCKERFILE_PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_X64_DOCKERFILE_PATH")
    def LINUX_X64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux x64 with all the requirements for CodeBuild runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.
        - ``DOCKER_CHANNEL`` overrides the channel from which Docker will be downloaded. Defaults to ``"stable"``.
        - ``DIND_COMMIT`` overrides the commit where dind is found.
        - ``DOCKER_VERSION`` overrides the installed Docker version.
        - ``DOCKER_COMPOSE_VERSION`` overrides the installed docker-compose version.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_X64_DOCKERFILE_PATH"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> RunnerImage:
        '''(experimental) Docker image loaded with GitHub Actions Runner and its prerequisites.

        The image is built by an image builder and is specific to CodeBuild.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) Labels associated with this provider.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> aws_cdk.aws_codebuild.Project:
        '''(experimental) CodeBuild project hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_codebuild.Project, jsii.get(self, "project"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.CodeBuildRunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "compute_type": "computeType",
        "image_builder": "imageBuilder",
        "label": "label",
        "labels": "labels",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class CodeBuildRunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param compute_type: (experimental) The type of compute to use for this build. See the {@link ComputeType} enum for the possible values. Default: {@link ComputeType#SMALL}
        :param image_builder: (experimental) Image builder for CodeBuild image with GitHub runner pre-configured. A user named ``runner`` is expected to exist with access to Docker-in-Docker. Default: image builder with ``CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (deprecated) GitHub Actions label used for this provider. Default: undefined
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['codebuild']
        :param security_group: (deprecated) Security group to assign to this instance. Default: public project with no security group
        :param security_groups: (experimental) Security groups to assign to this instance. Default: a new security group, if {@link vpc} is used
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete. For valid values, see the timeoutInMinutes field in the AWS CodeBuild User Guide. Default: Duration.hours(1)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                compute_type: typing.Optional[aws_cdk.aws_codebuild.ComputeType] = None,
                image_builder: typing.Optional[IImageBuilder] = None,
                label: typing.Optional[builtins.str] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument image_builder", value=image_builder, expected_type=type_hints["image_builder"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if image_builder is not None:
            self._values["image_builder"] = image_builder
        if label is not None:
            self._values["label"] = label
        if labels is not None:
            self._values["labels"] = labels
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[aws_cdk.aws_codebuild.ComputeType]:
        '''(experimental) The type of compute to use for this build.

        See the {@link ComputeType} enum for the possible values.

        :default: {@link ComputeType#SMALL}

        :stability: experimental
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[aws_cdk.aws_codebuild.ComputeType], result)

    @builtins.property
    def image_builder(self) -> typing.Optional[IImageBuilder]:
        '''(experimental) Image builder for CodeBuild image with GitHub runner pre-configured.

        A user named ``runner`` is expected to exist with access to Docker-in-Docker.

        :default: image builder with ``CodeBuildRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile

        :stability: experimental
        '''
        result = self._values.get("image_builder")
        return typing.cast(typing.Optional[IImageBuilder], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(deprecated) GitHub Actions label used for this provider.

        :default: undefined

        :deprecated: use {@link labels} instead

        :stability: deprecated
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) GitHub Actions labels used for this provider.

        These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for
        based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the
        job's labels, this provider will be chosen and spawn a new runner.

        :default: ['codebuild']

        :stability: experimental
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Security group to assign to this instance.

        :default: public project with no security group

        :deprecated: use {@link securityGroups}

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) Security groups to assign to this instance.

        :default: a new security group, if {@link vpc} is used

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: no subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) The number of minutes after which AWS CodeBuild stops the build if it's not complete.

        For valid values, see the timeoutInMinutes field in the AWS
        CodeBuild User Guide.

        :default: Duration.hours(1)

        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: no VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IImageBuilder, aws_cdk.aws_ec2.IConnectable)
class ContainerImageBuilder(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.ContainerImageBuilder",
):
    '''(experimental) An image builder that uses AWS Image Builder to build Docker images pre-baked with all the GitHub Actions runner requirements.

    Builders can be used with runner providers.

    The CodeBuild builder is better and faster. Only use this one if you have no choice. For example, if you need Windows containers.

    Each builder re-runs automatically at a set interval to make sure the images contain the latest versions of everything.

    You can create an instance of this construct to customize the image used to spin-up runners. Some runner providers may require custom components. Check the runner provider documentation. The default components work with CodeBuild and Fargate.

    For example, to set a specific runner version, rebuild the image every 2 weeks, and add a few packages for the Fargate provider, use::

       const builder = new ContainerImageBuilder(this, 'Builder', {
            runnerVersion: RunnerVersion.specific('2.293.0'),
            rebuildInterval: Duration.days(14),
       });
       new CodeBuildRunner(this, 'CodeBuild provider', {
            label: 'custom-codebuild',
            imageBuilder: builder,
       });

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        architecture: typing.Optional[Architecture] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        os: typing.Optional[Os] = None,
        parent_image: typing.Optional[builtins.str] = None,
        rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
        runner_version: typing.Optional[RunnerVersion] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param architecture: (experimental) Image architecture. Default: Architecture.X86_64
        :param instance_type: (experimental) The instance type used to build the image. Default: m5.large
        :param log_removal_policy: (experimental) Removal policy for logs of image builds. If deployment fails on the custom resource, try setting this to ``RemovalPolicy.RETAIN``. This way the CodeBuild logs can still be viewed, and you can see why the build failed. We try to not leave anything behind when removed. But sometimes a log staying behind is useful. Default: RemovalPolicy.DESTROY
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param os: (experimental) Image OS. Default: OS.LINUX
        :param parent_image: (experimental) Parent image for the new Docker Image. You can use either Image Builder image ARN or public registry image. Default: 'mcr.microsoft.com/windows/servercore:ltsc2019-amd64'
        :param rebuild_interval: (experimental) Schedule the image to be rebuilt every given interval. Useful for keeping the image up-do-date with the latest GitHub runner version and latest OS updates. Set to zero to disable. Default: Duration.days(7)
        :param runner_version: (experimental) Version of GitHub Runners to install. Default: latest version available
        :param security_group: (deprecated) Security group to assign to launched builder instances. Default: new security group
        :param security_groups: (experimental) Security groups to assign to launched builder instances. Default: new security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: default VPC subnet
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                architecture: typing.Optional[Architecture] = None,
                instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
                log_removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                os: typing.Optional[Os] = None,
                parent_image: typing.Optional[builtins.str] = None,
                rebuild_interval: typing.Optional[aws_cdk.Duration] = None,
                runner_version: typing.Optional[RunnerVersion] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ContainerImageBuilderProps(
            architecture=architecture,
            instance_type=instance_type,
            log_removal_policy=log_removal_policy,
            log_retention=log_retention,
            os=os,
            parent_image=parent_image,
            rebuild_interval=rebuild_interval,
            runner_version=runner_version,
            security_group=security_group,
            security_groups=security_groups,
            subnet_selection=subnet_selection,
            vpc=vpc,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addComponent")
    def add_component(self, component: ImageBuilderComponent) -> None:
        '''(experimental) Add a component to be installed.

        :param component: -

        :stability: experimental
        '''
        if __debug__:
            def stub(component: ImageBuilderComponent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
        return typing.cast(None, jsii.invoke(self, "addComponent", [component]))

    @jsii.member(jsii_name="addExtraCertificates")
    def add_extra_certificates(self, path: builtins.str) -> None:
        '''(experimental) Add extra trusted certificates. This helps deal with self-signed certificates for GitHub Enterprise Server.

        All first party Dockerfiles support this. Others may not.

        :param path: path to directory containing a file called certs.pem containing all the required certificates.

        :stability: experimental
        '''
        if __debug__:
            def stub(path: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        return typing.cast(None, jsii.invoke(self, "addExtraCertificates", [path]))

    @jsii.member(jsii_name="bind")
    def bind(self) -> RunnerImage:
        '''(experimental) Called by IRunnerProvider to finalize settings and create the image builder.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.invoke(self, "bind", []))

    @jsii.member(jsii_name="createImage")
    def _create_image(
        self,
        infra: aws_cdk.aws_imagebuilder.CfnInfrastructureConfiguration,
        dist: aws_cdk.aws_imagebuilder.CfnDistributionConfiguration,
        log: aws_cdk.aws_logs.LogGroup,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        container_recipe_arn: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_imagebuilder.CfnImage:
        '''
        :param infra: -
        :param dist: -
        :param log: -
        :param image_recipe_arn: -
        :param container_recipe_arn: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                infra: aws_cdk.aws_imagebuilder.CfnInfrastructureConfiguration,
                dist: aws_cdk.aws_imagebuilder.CfnDistributionConfiguration,
                log: aws_cdk.aws_logs.LogGroup,
                image_recipe_arn: typing.Optional[builtins.str] = None,
                container_recipe_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument infra", value=infra, expected_type=type_hints["infra"])
            check_type(argname="argument dist", value=dist, expected_type=type_hints["dist"])
            check_type(argname="argument log", value=log, expected_type=type_hints["log"])
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
        return typing.cast(aws_cdk.aws_imagebuilder.CfnImage, jsii.invoke(self, "createImage", [infra, dist, log, image_recipe_arn, container_recipe_arn]))

    @jsii.member(jsii_name="createInfrastructure")
    def _create_infrastructure(
        self,
        managed_policies: typing.Sequence[aws_cdk.aws_iam.IManagedPolicy],
    ) -> aws_cdk.aws_imagebuilder.CfnInfrastructureConfiguration:
        '''
        :param managed_policies: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                managed_policies: typing.Sequence[aws_cdk.aws_iam.IManagedPolicy],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
        return typing.cast(aws_cdk.aws_imagebuilder.CfnInfrastructureConfiguration, jsii.invoke(self, "createInfrastructure", [managed_policies]))

    @jsii.member(jsii_name="createLog")
    def _create_log(self, recipe_name: builtins.str) -> aws_cdk.aws_logs.LogGroup:
        '''
        :param recipe_name: -

        :stability: experimental
        '''
        if __debug__:
            def stub(recipe_name: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument recipe_name", value=recipe_name, expected_type=type_hints["recipe_name"])
        return typing.cast(aws_cdk.aws_logs.LogGroup, jsii.invoke(self, "createLog", [recipe_name]))

    @jsii.member(jsii_name="createPipeline")
    def _create_pipeline(
        self,
        infra: aws_cdk.aws_imagebuilder.CfnInfrastructureConfiguration,
        dist: aws_cdk.aws_imagebuilder.CfnDistributionConfiguration,
        log: aws_cdk.aws_logs.LogGroup,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        container_recipe_arn: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_imagebuilder.CfnImagePipeline:
        '''
        :param infra: -
        :param dist: -
        :param log: -
        :param image_recipe_arn: -
        :param container_recipe_arn: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                infra: aws_cdk.aws_imagebuilder.CfnInfrastructureConfiguration,
                dist: aws_cdk.aws_imagebuilder.CfnDistributionConfiguration,
                log: aws_cdk.aws_logs.LogGroup,
                image_recipe_arn: typing.Optional[builtins.str] = None,
                container_recipe_arn: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument infra", value=infra, expected_type=type_hints["infra"])
            check_type(argname="argument dist", value=dist, expected_type=type_hints["dist"])
            check_type(argname="argument log", value=log, expected_type=type_hints["log"])
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
        return typing.cast(aws_cdk.aws_imagebuilder.CfnImagePipeline, jsii.invoke(self, "createPipeline", [infra, dist, log, image_recipe_arn, container_recipe_arn]))

    @jsii.member(jsii_name="prependComponent")
    def prepend_component(self, component: ImageBuilderComponent) -> None:
        '''(experimental) Add a component to be installed before any other components.

        Useful for required system settings like certificates or proxy settings.

        :param component: -

        :stability: experimental
        '''
        if __debug__:
            def stub(component: ImageBuilderComponent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
        return typing.cast(None, jsii.invoke(self, "prependComponent", [component]))

    @builtins.property
    @jsii.member(jsii_name="architecture")
    def _architecture(self) -> Architecture:
        '''
        :stability: experimental
        '''
        return typing.cast(Architecture, jsii.get(self, "architecture"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def _description(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @builtins.property
    @jsii.member(jsii_name="os")
    def _os(self) -> Os:
        '''
        :stability: experimental
        '''
        return typing.cast(Os, jsii.get(self, "os"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def _platform(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> aws_cdk.aws_ecr.IRepository:
        '''
        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecr.IRepository, jsii.get(self, "repository"))

    @builtins.property
    @jsii.member(jsii_name="runnerVersion")
    def _runner_version(self) -> RunnerVersion:
        '''
        :stability: experimental
        '''
        return typing.cast(RunnerVersion, jsii.get(self, "runnerVersion"))

    @builtins.property
    @jsii.member(jsii_name="components")
    def _components(self) -> typing.List[ImageBuilderComponent]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.List[ImageBuilderComponent], jsii.get(self, "components"))

    @_components.setter
    def _components(self, value: typing.List[ImageBuilderComponent]) -> None:
        if __debug__:
            def stub(value: typing.List[ImageBuilderComponent]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)


@jsii.implements(IRunnerProvider)
class Ec2Runner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.Ec2Runner",
):
    '''(experimental) GitHub Actions runner provider using EC2 to execute jobs.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        ami_builder: typing.Optional[IAmiBuilder] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        spot: typing.Optional[builtins.bool] = None,
        spot_max_price: typing.Optional[builtins.str] = None,
        storage_size: typing.Optional[aws_cdk.Size] = None,
        subnet: typing.Optional[aws_cdk.aws_ec2.ISubnet] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ami_builder: (experimental) AMI builder that creates AMIs with GitHub runner pre-configured. On Linux, a user named ``runner`` is expected to exist with access to Docker. Default: AMI builder for Ubuntu Linux on the same subnet as configured by {@link vpc} and {@link subnetSelection}
        :param instance_type: (experimental) Instance type for launched runner instances. Default: m5.large
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['ec2']
        :param security_group: (deprecated) Security Group to assign to launched runner instances. Default: a new security group
        :param security_groups: (experimental) Security groups to assign to launched runner instances. Default: a new security group
        :param spot: (experimental) Use spot instances to save money. Spot instances are cheaper but not always available and can be stopped prematurely. Default: false
        :param spot_max_price: (experimental) Set a maximum price for spot instances. Default: no max price (you will pay current spot price)
        :param storage_size: (experimental) Size of volume available for launched runner instances. This modifies the boot volume size and doesn't add any additional volumes. Default: 30GB
        :param subnet: (deprecated) Subnet where the runner instances will be launched. Default: default subnet of account's default VPC
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Only the first matched subnet will be used. Default: default VPC subnet
        :param vpc: (experimental) VPC where runner instances will be launched. Default: default account VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                ami_builder: typing.Optional[IAmiBuilder] = None,
                instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                spot: typing.Optional[builtins.bool] = None,
                spot_max_price: typing.Optional[builtins.str] = None,
                storage_size: typing.Optional[aws_cdk.Size] = None,
                subnet: typing.Optional[aws_cdk.aws_ec2.ISubnet] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = Ec2RunnerProps(
            ami_builder=ami_builder,
            instance_type=instance_type,
            labels=labels,
            security_group=security_group,
            security_groups=security_groups,
            spot=spot,
            spot_max_price=spot_max_price,
            storage_size=storage_size,
            subnet=subnet,
            subnet_selection=subnet_selection,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.member(jsii_name="grantStateMachine")
    def grant_state_machine(
        self,
        state_machine_role: aws_cdk.aws_iam.IGrantable,
    ) -> None:
        '''(experimental) An optional method that modifies the role of the state machine after all the tasks have been generated.

        This can be used to add additional policy
        statements to the state machine role that are not automatically added by the task returned from {@link getStepFunctionTask}.

        :param state_machine_role: -

        :stability: experimental
        '''
        if __debug__:
            def stub(state_machine_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument state_machine_role", value=state_machine_role, expected_type=type_hints["state_machine_role"])
        return typing.cast(None, jsii.invoke(self, "grantStateMachine", [state_machine_role]))

    @jsii.member(jsii_name="labelsFromProperties")
    def _labels_from_properties(
        self,
        default_label: builtins.str,
        props_label: typing.Optional[builtins.str] = None,
        props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> typing.List[builtins.str]:
        '''
        :param default_label: -
        :param props_label: -
        :param props_labels: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                default_label: builtins.str,
                props_label: typing.Optional[builtins.str] = None,
                props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_label", value=default_label, expected_type=type_hints["default_label"])
            check_type(argname="argument props_label", value=props_label, expected_type=type_hints["props_label"])
            check_type(argname="argument props_labels", value=props_labels, expected_type=type_hints["props_labels"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "labelsFromProperties", [default_label, props_label, props_labels]))

    @jsii.member(jsii_name="status")
    def status(
        self,
        status_function_role: aws_cdk.aws_iam.IGrantable,
    ) -> IRunnerProviderStatus:
        '''(experimental) Return status of the runner provider to be used in the main status function.

        Also gives the status function any needed permissions to query the Docker image or AMI.

        :param status_function_role: -

        :stability: experimental
        '''
        if __debug__:
            def stub(status_function_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_function_role", value=status_function_role, expected_type=type_hints["status_function_role"])
        return typing.cast(IRunnerProviderStatus, jsii.invoke(self, "status", [status_function_role]))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) Labels associated with this provider.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.Ec2RunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "ami_builder": "amiBuilder",
        "instance_type": "instanceType",
        "labels": "labels",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "spot": "spot",
        "spot_max_price": "spotMaxPrice",
        "storage_size": "storageSize",
        "subnet": "subnet",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
    },
)
class Ec2RunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        ami_builder: typing.Optional[IAmiBuilder] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        spot: typing.Optional[builtins.bool] = None,
        spot_max_price: typing.Optional[builtins.str] = None,
        storage_size: typing.Optional[aws_cdk.Size] = None,
        subnet: typing.Optional[aws_cdk.aws_ec2.ISubnet] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for {@link Ec2Runner} construct.

        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param ami_builder: (experimental) AMI builder that creates AMIs with GitHub runner pre-configured. On Linux, a user named ``runner`` is expected to exist with access to Docker. Default: AMI builder for Ubuntu Linux on the same subnet as configured by {@link vpc} and {@link subnetSelection}
        :param instance_type: (experimental) Instance type for launched runner instances. Default: m5.large
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['ec2']
        :param security_group: (deprecated) Security Group to assign to launched runner instances. Default: a new security group
        :param security_groups: (experimental) Security groups to assign to launched runner instances. Default: a new security group
        :param spot: (experimental) Use spot instances to save money. Spot instances are cheaper but not always available and can be stopped prematurely. Default: false
        :param spot_max_price: (experimental) Set a maximum price for spot instances. Default: no max price (you will pay current spot price)
        :param storage_size: (experimental) Size of volume available for launched runner instances. This modifies the boot volume size and doesn't add any additional volumes. Default: 30GB
        :param subnet: (deprecated) Subnet where the runner instances will be launched. Default: default subnet of account's default VPC
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Only the first matched subnet will be used. Default: default VPC subnet
        :param vpc: (experimental) VPC where runner instances will be launched. Default: default account VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                ami_builder: typing.Optional[IAmiBuilder] = None,
                instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                spot: typing.Optional[builtins.bool] = None,
                spot_max_price: typing.Optional[builtins.str] = None,
                storage_size: typing.Optional[aws_cdk.Size] = None,
                subnet: typing.Optional[aws_cdk.aws_ec2.ISubnet] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument ami_builder", value=ami_builder, expected_type=type_hints["ami_builder"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
            check_type(argname="argument spot_max_price", value=spot_max_price, expected_type=type_hints["spot_max_price"])
            check_type(argname="argument storage_size", value=storage_size, expected_type=type_hints["storage_size"])
            check_type(argname="argument subnet", value=subnet, expected_type=type_hints["subnet"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if ami_builder is not None:
            self._values["ami_builder"] = ami_builder
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if labels is not None:
            self._values["labels"] = labels
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if spot is not None:
            self._values["spot"] = spot
        if spot_max_price is not None:
            self._values["spot_max_price"] = spot_max_price
        if storage_size is not None:
            self._values["storage_size"] = storage_size
        if subnet is not None:
            self._values["subnet"] = subnet
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def ami_builder(self) -> typing.Optional[IAmiBuilder]:
        '''(experimental) AMI builder that creates AMIs with GitHub runner pre-configured.

        On Linux, a user named ``runner`` is expected to exist with access to Docker.

        :default: AMI builder for Ubuntu Linux on the same subnet as configured by {@link vpc} and {@link subnetSelection}

        :stability: experimental
        '''
        result = self._values.get("ami_builder")
        return typing.cast(typing.Optional[IAmiBuilder], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        '''(experimental) Instance type for launched runner instances.

        :default: m5.large

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.InstanceType], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) GitHub Actions labels used for this provider.

        These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for
        based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the
        job's labels, this provider will be chosen and spawn a new runner.

        :default: ['ec2']

        :stability: experimental
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Security Group to assign to launched runner instances.

        :default: a new security group

        :deprecated: use {@link securityGroups}

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) Security groups to assign to launched runner instances.

        :default: a new security group

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def spot(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Use spot instances to save money.

        Spot instances are cheaper but not always available and can be stopped prematurely.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def spot_max_price(self) -> typing.Optional[builtins.str]:
        '''(experimental) Set a maximum price for spot instances.

        :default: no max price (you will pay current spot price)

        :stability: experimental
        '''
        result = self._values.get("spot_max_price")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_size(self) -> typing.Optional[aws_cdk.Size]:
        '''(experimental) Size of volume available for launched runner instances.

        This modifies the boot volume size and doesn't add any additional volumes.

        :default: 30GB

        :stability: experimental
        '''
        result = self._values.get("storage_size")
        return typing.cast(typing.Optional[aws_cdk.Size], result)

    @builtins.property
    def subnet(self) -> typing.Optional[aws_cdk.aws_ec2.ISubnet]:
        '''(deprecated) Subnet where the runner instances will be launched.

        :default: default subnet of account's default VPC

        :deprecated: use {@link vpc} and {@link subnetSelection}

        :stability: deprecated
        '''
        result = self._values.get("subnet")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISubnet], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        Only the first matched subnet will be used.

        :default: default VPC subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC where runner instances will be launched.

        :default: default account VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Ec2RunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRunnerProvider)
class FargateRunner(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cloudsnorkel/cdk-github-runners.FargateRunner",
):
    '''(experimental) GitHub Actions runner provider using Fargate to execute jobs.

    Creates a task definition with a single container that gets started for each job.

    This construct is not meant to be used by itself. It should be passed in the providers property for GitHubRunners.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        cluster: typing.Optional[aws_cdk.aws_ecs.Cluster] = None,
        cpu: typing.Optional[jsii.Number] = None,
        ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        spot: typing.Optional[builtins.bool] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param assign_public_ip: (experimental) Assign public IP to the runner task. Make sure the task will have access to GitHub. A public IP might be required unless you have NAT gateway. Default: true
        :param cluster: (experimental) Existing Fargate cluster to use. Default: a new cluster
        :param cpu: (experimental) The number of cpu units used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) Default: 1024
        :param ephemeral_storage_gib: (experimental) The amount (in GiB) of ephemeral storage to be allocated to the task. The maximum supported value is 200 GiB. NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later. Default: 20
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. A user named ``runner`` is expected to exist. Default: image builder with ``FargateRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (deprecated) GitHub Actions label used for this provider. Default: undefined
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['fargate']
        :param memory_limit_mib: (experimental) The amount (in MiB) of memory used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Default: 2048
        :param security_group: (deprecated) Security group to assign to the task. Default: a new security group
        :param security_groups: (experimental) Security groups to assign to the task. Default: a new security group
        :param spot: (experimental) Use Fargate spot capacity provider to save money. - Runners may fail to start due to missing capacity. - Runners might be stopped prematurely with spot pricing. Default: false
        :param subnet_selection: (experimental) Subnets to run the runners in. Default: Fargate default
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                assign_public_ip: typing.Optional[builtins.bool] = None,
                cluster: typing.Optional[aws_cdk.aws_ecs.Cluster] = None,
                cpu: typing.Optional[jsii.Number] = None,
                ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
                image_builder: typing.Optional[IImageBuilder] = None,
                label: typing.Optional[builtins.str] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                memory_limit_mib: typing.Optional[jsii.Number] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                spot: typing.Optional[builtins.bool] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = FargateRunnerProps(
            assign_public_ip=assign_public_ip,
            cluster=cluster,
            cpu=cpu,
            ephemeral_storage_gib=ephemeral_storage_gib,
            image_builder=image_builder,
            label=label,
            labels=labels,
            memory_limit_mib=memory_limit_mib,
            security_group=security_group,
            security_groups=security_groups,
            spot=spot,
            subnet_selection=subnet_selection,
            vpc=vpc,
            log_retention=log_retention,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="getStepFunctionTask")
    def get_step_function_task(
        self,
        *,
        github_domain_path: builtins.str,
        owner_path: builtins.str,
        repo_path: builtins.str,
        runner_name_path: builtins.str,
        runner_token_path: builtins.str,
    ) -> aws_cdk.aws_stepfunctions.IChainable:
        '''(experimental) Generate step function task(s) to start a new runner.

        Called by GithubRunners and shouldn't be called manually.

        :param github_domain_path: (experimental) Path to GitHub domain. Most of the time this will be github.com but for self-hosted GitHub instances, this will be different.
        :param owner_path: (experimental) Path to repostiroy owner name.
        :param repo_path: (experimental) Path to repository name.
        :param runner_name_path: (experimental) Path to desired runner name. We specifically set the name to make troubleshooting easier.
        :param runner_token_path: (experimental) Path to runner token used to register token.

        :stability: experimental
        '''
        parameters = RunnerRuntimeParameters(
            github_domain_path=github_domain_path,
            owner_path=owner_path,
            repo_path=repo_path,
            runner_name_path=runner_name_path,
            runner_token_path=runner_token_path,
        )

        return typing.cast(aws_cdk.aws_stepfunctions.IChainable, jsii.invoke(self, "getStepFunctionTask", [parameters]))

    @jsii.member(jsii_name="grantStateMachine")
    def grant_state_machine(self, _: aws_cdk.aws_iam.IGrantable) -> None:
        '''(experimental) An optional method that modifies the role of the state machine after all the tasks have been generated.

        This can be used to add additional policy
        statements to the state machine role that are not automatically added by the task returned from {@link getStepFunctionTask}.

        :param _: -

        :stability: experimental
        '''
        if __debug__:
            def stub(_: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _", value=_, expected_type=type_hints["_"])
        return typing.cast(None, jsii.invoke(self, "grantStateMachine", [_]))

    @jsii.member(jsii_name="labelsFromProperties")
    def _labels_from_properties(
        self,
        default_label: builtins.str,
        props_label: typing.Optional[builtins.str] = None,
        props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> typing.List[builtins.str]:
        '''
        :param default_label: -
        :param props_label: -
        :param props_labels: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                default_label: builtins.str,
                props_label: typing.Optional[builtins.str] = None,
                props_labels: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument default_label", value=default_label, expected_type=type_hints["default_label"])
            check_type(argname="argument props_label", value=props_label, expected_type=type_hints["props_label"])
            check_type(argname="argument props_labels", value=props_labels, expected_type=type_hints["props_labels"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "labelsFromProperties", [default_label, props_label, props_labels]))

    @jsii.member(jsii_name="status")
    def status(
        self,
        status_function_role: aws_cdk.aws_iam.IGrantable,
    ) -> IRunnerProviderStatus:
        '''(experimental) Return status of the runner provider to be used in the main status function.

        Also gives the status function any needed permissions to query the Docker image or AMI.

        :param status_function_role: -

        :stability: experimental
        '''
        if __debug__:
            def stub(status_function_role: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument status_function_role", value=status_function_role, expected_type=type_hints["status_function_role"])
        return typing.cast(IRunnerProviderStatus, jsii.invoke(self, "status", [status_function_role]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_ARM64_DOCKERFILE_PATH")
    def LINUX_ARM64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux ARM64 with all the requirement for Fargate runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_ARM64_DOCKERFILE_PATH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINUX_X64_DOCKERFILE_PATH")
    def LINUX_X64_DOCKERFILE_PATH(cls) -> builtins.str:
        '''(experimental) Path to Dockerfile for Linux x64 with all the requirement for Fargate runner.

        Use this Dockerfile unless you need to customize it further than allowed by hooks.

        Available build arguments that can be set in the image builder:

        - ``BASE_IMAGE`` sets the ``FROM`` line. This should be an Ubuntu compatible image.
        - ``EXTRA_PACKAGES`` can be used to install additional packages.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LINUX_X64_DOCKERFILE_PATH"))

    @builtins.property
    @jsii.member(jsii_name="assignPublicIp")
    def assign_public_ip(self) -> builtins.bool:
        '''(experimental) Whether runner task will have a public IP.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "assignPublicIp"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> aws_cdk.aws_ecs.Cluster:
        '''(experimental) Cluster hosting the task hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecs.Cluster, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The network connections associated with this resource.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> aws_cdk.aws_ecs.ContainerDefinition:
        '''(experimental) Container definition hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecs.ContainerDefinition, jsii.get(self, "container"))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> aws_cdk.aws_iam.IPrincipal:
        '''(experimental) Grant principal used to add permissions to the runner role.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_iam.IPrincipal, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> RunnerImage:
        '''(experimental) Docker image loaded with GitHub Actions Runner and its prerequisites.

        The image is built by an image builder and is specific to Fargate tasks.

        :stability: experimental
        '''
        return typing.cast(RunnerImage, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.List[builtins.str]:
        '''(experimental) Labels associated with this provider.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "labels"))

    @builtins.property
    @jsii.member(jsii_name="spot")
    def spot(self) -> builtins.bool:
        '''(experimental) Use spot pricing for Fargate tasks.

        :stability: experimental
        '''
        return typing.cast(builtins.bool, jsii.get(self, "spot"))

    @builtins.property
    @jsii.member(jsii_name="task")
    def task(self) -> aws_cdk.aws_ecs.FargateTaskDefinition:
        '''(experimental) Fargate task hosting the runner.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ecs.FargateTaskDefinition, jsii.get(self, "task"))

    @builtins.property
    @jsii.member(jsii_name="subnetSelection")
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Subnets used for hosting the runner task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], jsii.get(self, "subnetSelection"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC used for hosting the runner task.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], jsii.get(self, "vpc"))


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.FargateRunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "assign_public_ip": "assignPublicIp",
        "cluster": "cluster",
        "cpu": "cpu",
        "ephemeral_storage_gib": "ephemeralStorageGiB",
        "image_builder": "imageBuilder",
        "label": "label",
        "labels": "labels",
        "memory_limit_mib": "memoryLimitMiB",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "spot": "spot",
        "subnet_selection": "subnetSelection",
        "vpc": "vpc",
    },
)
class FargateRunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        assign_public_ip: typing.Optional[builtins.bool] = None,
        cluster: typing.Optional[aws_cdk.aws_ecs.Cluster] = None,
        cpu: typing.Optional[jsii.Number] = None,
        ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_limit_mib: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        spot: typing.Optional[builtins.bool] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''(experimental) Properties for FargateRunner.

        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param assign_public_ip: (experimental) Assign public IP to the runner task. Make sure the task will have access to GitHub. A public IP might be required unless you have NAT gateway. Default: true
        :param cluster: (experimental) Existing Fargate cluster to use. Default: a new cluster
        :param cpu: (experimental) The number of cpu units used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the memory parameter: 256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) 512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) 1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) 2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) 4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) Default: 1024
        :param ephemeral_storage_gib: (experimental) The amount (in GiB) of ephemeral storage to be allocated to the task. The maximum supported value is 200 GiB. NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later. Default: 20
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. A user named ``runner`` is expected to exist. Default: image builder with ``FargateRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile
        :param label: (deprecated) GitHub Actions label used for this provider. Default: undefined
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['fargate']
        :param memory_limit_mib: (experimental) The amount (in MiB) of memory used by the task. For tasks using the Fargate launch type, this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU) 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU) 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU) Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU) Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU) Default: 2048
        :param security_group: (deprecated) Security group to assign to the task. Default: a new security group
        :param security_groups: (experimental) Security groups to assign to the task. Default: a new security group
        :param spot: (experimental) Use Fargate spot capacity provider to save money. - Runners may fail to start due to missing capacity. - Runners might be stopped prematurely with spot pricing. Default: false
        :param subnet_selection: (experimental) Subnets to run the runners in. Default: Fargate default
        :param vpc: (experimental) VPC to launch the runners in. Default: default account VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                assign_public_ip: typing.Optional[builtins.bool] = None,
                cluster: typing.Optional[aws_cdk.aws_ecs.Cluster] = None,
                cpu: typing.Optional[jsii.Number] = None,
                ephemeral_storage_gib: typing.Optional[jsii.Number] = None,
                image_builder: typing.Optional[IImageBuilder] = None,
                label: typing.Optional[builtins.str] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                memory_limit_mib: typing.Optional[jsii.Number] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                spot: typing.Optional[builtins.bool] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument assign_public_ip", value=assign_public_ip, expected_type=type_hints["assign_public_ip"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument ephemeral_storage_gib", value=ephemeral_storage_gib, expected_type=type_hints["ephemeral_storage_gib"])
            check_type(argname="argument image_builder", value=image_builder, expected_type=type_hints["image_builder"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument memory_limit_mib", value=memory_limit_mib, expected_type=type_hints["memory_limit_mib"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument spot", value=spot, expected_type=type_hints["spot"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if assign_public_ip is not None:
            self._values["assign_public_ip"] = assign_public_ip
        if cluster is not None:
            self._values["cluster"] = cluster
        if cpu is not None:
            self._values["cpu"] = cpu
        if ephemeral_storage_gib is not None:
            self._values["ephemeral_storage_gib"] = ephemeral_storage_gib
        if image_builder is not None:
            self._values["image_builder"] = image_builder
        if label is not None:
            self._values["label"] = label
        if labels is not None:
            self._values["labels"] = labels
        if memory_limit_mib is not None:
            self._values["memory_limit_mib"] = memory_limit_mib
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if spot is not None:
            self._values["spot"] = spot
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def assign_public_ip(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Assign public IP to the runner task.

        Make sure the task will have access to GitHub. A public IP might be required unless you have NAT gateway.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("assign_public_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cluster(self) -> typing.Optional[aws_cdk.aws_ecs.Cluster]:
        '''(experimental) Existing Fargate cluster to use.

        :default: a new cluster

        :stability: experimental
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[aws_cdk.aws_ecs.Cluster], result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of cpu units used by the task.

        For tasks using the Fargate launch type,
        this field is required and you must use one of the following values,
        which determines your range of valid values for the memory parameter:

        256 (.25 vCPU) - Available memory values: 512 (0.5 GB), 1024 (1 GB), 2048 (2 GB)

        512 (.5 vCPU) - Available memory values: 1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB)

        1024 (1 vCPU) - Available memory values: 2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

        2048 (2 vCPU) - Available memory values: Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

        4096 (4 vCPU) - Available memory values: Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)

        :default: 1024

        :stability: experimental
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ephemeral_storage_gib(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount (in GiB) of ephemeral storage to be allocated to the task.

        The maximum supported value is 200 GiB.

        NOTE: This parameter is only supported for tasks hosted on AWS Fargate using platform version 1.4.0 or later.

        :default: 20

        :stability: experimental
        '''
        result = self._values.get("ephemeral_storage_gib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image_builder(self) -> typing.Optional[IImageBuilder]:
        '''(experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured.

        A user named ``runner`` is expected to exist.

        :default: image builder with ``FargateRunner.LINUX_X64_DOCKERFILE_PATH`` as Dockerfile

        :stability: experimental
        '''
        result = self._values.get("image_builder")
        return typing.cast(typing.Optional[IImageBuilder], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(deprecated) GitHub Actions label used for this provider.

        :default: undefined

        :deprecated: use {@link labels} instead

        :stability: deprecated
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) GitHub Actions labels used for this provider.

        These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for
        based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the
        job's labels, this provider will be chosen and spawn a new runner.

        :default: ['fargate']

        :stability: experimental
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_limit_mib(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount (in MiB) of memory used by the task.

        For tasks using the Fargate launch type,
        this field is required and you must use one of the following values, which determines your range of valid values for the cpu parameter:

        512 (0.5 GB), 1024 (1 GB), 2048 (2 GB) - Available cpu values: 256 (.25 vCPU)

        1024 (1 GB), 2048 (2 GB), 3072 (3 GB), 4096 (4 GB) - Available cpu values: 512 (.5 vCPU)

        2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB) - Available cpu values: 1024 (1 vCPU)

        Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB) - Available cpu values: 2048 (2 vCPU)

        Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB) - Available cpu values: 4096 (4 vCPU)

        :default: 2048

        :stability: experimental
        '''
        result = self._values.get("memory_limit_mib")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Security group to assign to the task.

        :default: a new security group

        :deprecated: use {@link securityGroups}

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) Security groups to assign to the task.

        :default: a new security group

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def spot(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Use Fargate spot capacity provider to save money.

        - Runners may fail to start due to missing capacity.
        - Runners might be stopped prematurely with spot pricing.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("spot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Subnets to run the runners in.

        :default: Fargate default

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: default account VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cloudsnorkel/cdk-github-runners.LambdaRunnerProps",
    jsii_struct_bases=[RunnerProviderProps],
    name_mapping={
        "log_retention": "logRetention",
        "ephemeral_storage_size": "ephemeralStorageSize",
        "image_builder": "imageBuilder",
        "label": "label",
        "labels": "labels",
        "memory_size": "memorySize",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "timeout": "timeout",
        "vpc": "vpc",
    },
)
class LambdaRunnerProps(RunnerProviderProps):
    def __init__(
        self,
        *,
        log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
        image_builder: typing.Optional[IImageBuilder] = None,
        label: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[aws_cdk.Duration] = None,
        vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
    ) -> None:
        '''
        :param log_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.ONE_MONTH
        :param ephemeral_storage_size: (experimental) The size of the function’s /tmp directory in MiB. Default: 10 GiB
        :param image_builder: (experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured. The default command (``CMD``) should be ``["runner.handler"]`` which points to an included ``runner.js`` with a function named ``handler``. The function should start the GitHub runner. Default: image builder with LambdaRunner.LINUX_X64_DOCKERFILE_PATH as Dockerfile
        :param label: (deprecated) GitHub Actions label used for this provider. Default: undefined
        :param labels: (experimental) GitHub Actions labels used for this provider. These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the job's labels, this provider will be chosen and spawn a new runner. Default: ['lambda']
        :param memory_size: (experimental) The amount of memory, in MB, that is allocated to your Lambda function. Lambda uses this value to proportionally allocate the amount of CPU power. For more information, see Resource Model in the AWS Lambda Developer Guide. Default: 2048
        :param security_group: (deprecated) Security group to assign to this instance. Default: public lambda with no security group
        :param security_groups: (experimental) Security groups to assign to this instance. Default: public lambda with no security group
        :param subnet_selection: (experimental) Where to place the network interfaces within the VPC. Default: no subnet
        :param timeout: (experimental) The function execution time (in seconds) after which Lambda terminates the function. Because the execution time affects cost, set this value based on the function's expected execution time. Default: Duration.minutes(15)
        :param vpc: (experimental) VPC to launch the runners in. Default: no VPC

        :stability: experimental
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                log_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                ephemeral_storage_size: typing.Optional[aws_cdk.Size] = None,
                image_builder: typing.Optional[IImageBuilder] = None,
                label: typing.Optional[builtins.str] = None,
                labels: typing.Optional[typing.Sequence[builtins.str]] = None,
                memory_size: typing.Optional[jsii.Number] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                timeout: typing.Optional[aws_cdk.Duration] = None,
                vpc: typing.Optional[aws_cdk.aws_ec2.IVpc] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument ephemeral_storage_size", value=ephemeral_storage_size, expected_type=type_hints["ephemeral_storage_size"])
            check_type(argname="argument image_builder", value=image_builder, expected_type=type_hints["image_builder"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if ephemeral_storage_size is not None:
            self._values["ephemeral_storage_size"] = ephemeral_storage_size
        if image_builder is not None:
            self._values["image_builder"] = image_builder
        if label is not None:
            self._values["label"] = label
        if labels is not None:
            self._values["labels"] = labels
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if timeout is not None:
            self._values["timeout"] = timeout
        if vpc is not None:
            self._values["vpc"] = vpc

    @builtins.property
    def log_retention(self) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.ONE_MONTH

        :stability: experimental
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def ephemeral_storage_size(self) -> typing.Optional[aws_cdk.Size]:
        '''(experimental) The size of the function’s /tmp directory in MiB.

        :default: 10 GiB

        :stability: experimental
        '''
        result = self._values.get("ephemeral_storage_size")
        return typing.cast(typing.Optional[aws_cdk.Size], result)

    @builtins.property
    def image_builder(self) -> typing.Optional[IImageBuilder]:
        '''(experimental) Provider running an image to run inside CodeBuild with GitHub runner pre-configured.

        The default command (``CMD``) should be ``["runner.handler"]`` which points to an included ``runner.js`` with a function named ``handler``. The function should start the GitHub runner.

        :default: image builder with LambdaRunner.LINUX_X64_DOCKERFILE_PATH as Dockerfile

        :see: https://github.com/CloudSnorkel/cdk-github-runners/tree/main/src/providers/docker-images/lambda
        :stability: experimental
        '''
        result = self._values.get("image_builder")
        return typing.cast(typing.Optional[IImageBuilder], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''(deprecated) GitHub Actions label used for this provider.

        :default: undefined

        :deprecated: use {@link labels} instead

        :stability: deprecated
        '''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) GitHub Actions labels used for this provider.

        These labels are used to identify which provider should spawn a new on-demand runner. Every job sends a webhook with the labels it's looking for
        based on runs-on. We match the labels from the webhook with the labels specified here. If all the labels specified here are present in the
        job's labels, this provider will be chosen and spawn a new runner.

        :default: ['lambda']

        :stability: experimental
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The amount of memory, in MB, that is allocated to your Lambda function.

        Lambda uses this value to proportionally allocate the amount of CPU
        power. For more information, see Resource Model in the AWS Lambda
        Developer Guide.

        :default: 2048

        :stability: experimental
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Security group to assign to this instance.

        :default: public lambda with no security group

        :deprecated: use {@link securityGroups}

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) Security groups to assign to this instance.

        :default: public lambda with no security group

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the network interfaces within the VPC.

        :default: no subnet

        :stability: experimental
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def timeout(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) The function execution time (in seconds) after which Lambda terminates the function.

        Because the execution time affects cost, set this value
        based on the function's expected execution time.

        :default: Duration.minutes(15)

        :stability: experimental
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[aws_cdk.aws_ec2.IVpc]:
        '''(experimental) VPC to launch the runners in.

        :default: no VPC

        :stability: experimental
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.IVpc], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaRunnerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Architecture",
    "CodeBuildImageBuilder",
    "CodeBuildImageBuilderProps",
    "CodeBuildRunner",
    "CodeBuildRunnerProps",
    "ContainerImageBuilder",
    "ContainerImageBuilderProps",
    "Ec2Runner",
    "Ec2RunnerProps",
    "FargateRunner",
    "FargateRunnerProps",
    "GitHubRunners",
    "GitHubRunnersProps",
    "IAmiBuilder",
    "IImageBuilder",
    "IRunnerAmiStatus",
    "IRunnerImageStatus",
    "IRunnerProvider",
    "IRunnerProviderStatus",
    "ImageBuilderAsset",
    "ImageBuilderComponent",
    "ImageBuilderComponentProperties",
    "LambdaRunner",
    "LambdaRunnerProps",
    "LinuxUbuntuComponents",
    "Os",
    "RunnerAmi",
    "RunnerImage",
    "RunnerProviderProps",
    "RunnerRuntimeParameters",
    "RunnerVersion",
    "Secrets",
    "StaticRunnerImage",
    "WindowsComponents",
]

publication.publish()
