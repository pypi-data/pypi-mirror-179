'''
<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
-->

# cdk-nag

[![PyPI version](https://img.shields.io/pypi/v/cdk-nag)](https://pypi.org/project/cdk-nag/)
[![npm version](https://img.shields.io/npm/v/cdk-nag)](https://www.npmjs.com/package/cdk-nag)
[![Maven version](https://img.shields.io/maven-central/v/io.github.cdklabs/cdknag)](https://search.maven.org/search?q=a:cdknag)
[![NuGet version](https://img.shields.io/nuget/v/Cdklabs.CdkNag)](https://www.nuget.org/packages/Cdklabs.CdkNag)
[![Go version](https://img.shields.io/github/go-mod/go-version/cdklabs/cdk-nag-go?color=blue&filename=cdknag%2Fgo.mod)](https://github.com/cdklabs/cdk-nag-go)

[![View on Construct Hub](https://constructs.dev/badge?package=cdk-nag)](https://constructs.dev/packages/cdk-nag)

Check CDK applications or [CloudFormation templates](#using-on-cloudformation-templates) for best practices using a combination of available rule packs. Inspired by [cfn_nag](https://github.com/stelligent/cfn_nag).

Check out [this blog post](https://aws.amazon.com/blogs/devops/manage-application-security-and-compliance-with-the-aws-cloud-development-kit-and-cdk-nag/) for a guided overview!

![demo](cdk_nag.gif)

## Available Rules and Packs

See [RULES](./RULES.md) for more information on all the available packs.

1. [AWS Solutions](./RULES.md#awssolutions)
2. [HIPAA Security](./RULES.md#hipaa-security)
3. [NIST 800-53 rev 4](./RULES.md#nist-800-53-rev-4)
4. [NIST 800-53 rev 5](./RULES.md#nist-800-53-rev-5)
5. [PCI DSS 3.2.1](./RULES.md#pci-dss-321)

[RULES](./RULES.md) also includes a collection of [additional rules](./RULES.md#additional-rules) that are not currently included in any of the pre-built NagPacks, but are still available for inclusion in custom NagPacks.

Read the [NagPack developer docs](./docs/NagPack.md) if you are interested in creating your own pack.

## Usage

For a full list of options See `NagPackProps` in the [API.md](./API.md#struct-nagpackprops)

<details>
<summary>Including in an application</summary>

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
// Simple rule informational messages
Aspects.of(app).add(new AwsSolutionsChecks());
// Additional explanations on the purpose of triggered rules
// Aspects.of(stack).add(new AwsSolutionsChecks({ verbose: true }));
```

</details>

## Suppressing a Rule

<details>
  <summary>Example 1) Default Construct</summary>

```python
import { SecurityGroup, Vpc, Peer, Port } from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const test = new SecurityGroup(this, 'test', {
      vpc: new Vpc(this, 'vpc'),
    });
    test.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    NagSuppressions.addResourceSuppressions(test, [
      { id: 'AwsSolutions-EC23', reason: 'lorem ipsum' },
    ]);
  }
}
```

</details><details>
  <summary>Example 2) On Multiple Constructs</summary>

```python
import { SecurityGroup, Vpc, Peer, Port } from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const vpc = new Vpc(this, 'vpc');
    const test1 = new SecurityGroup(this, 'test', { vpc });
    test1.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    const test2 = new SecurityGroup(this, 'test', { vpc });
    test2.addIngressRule(Peer.anyIpv4(), Port.allTraffic());
    NagSuppressions.addResourceSuppressions(
      [test1, test2],
      [{ id: 'AwsSolutions-EC23', reason: 'lorem ipsum' }]
    );
  }
}
```

</details><details>
  <summary>Example 3) Child Constructs</summary>

```python
import { User, PolicyStatement } from 'aws-cdk-lib/aws-iam';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const user = new User(this, 'rUser');
    user.addToPolicy(
      new PolicyStatement({
        actions: ['s3:PutObject'],
        resources: ['arn:aws:s3:::bucket_name/*'],
      })
    );
    // Enable adding suppressions to child constructs
    NagSuppressions.addResourceSuppressions(
      user,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'lorem ipsum',
          appliesTo: ['Resource::arn:aws:s3:::bucket_name/*'], // optional
        },
      ],
      true
    );
  }
}
```

</details><details>
  <summary>Example 4) Stack Level </summary>

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks, NagSuppressions } from 'cdk-nag';

const app = new App();
const stack = new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(new AwsSolutionsChecks());
NagSuppressions.addStackSuppressions(stack, [
  { id: 'AwsSolutions-EC23', reason: 'lorem ipsum' },
]);
```

</details><details>
  <summary>Example 5) Construct path</summary>

If you received the following error on synth/deploy

```bash
[Error at /StackName/Custom::CDKBucketDeployment8675309/ServiceRole/Resource] AwsSolutions-IAM4: The IAM user, role, or group uses AWS managed policies
```

```python
import { Bucket } from 'aws-cdk-lib/aws-s3';
import { BucketDeployment } from 'aws-cdk-lib/aws-s3-deployment';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new BucketDeployment(this, 'rDeployment', {
      sources: [],
      destinationBucket: Bucket.fromBucketName(this, 'rBucket', 'foo'),
    });
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/StackName/Custom::CDKBucketDeployment8675309/ServiceRole/Resource',
      [{ id: 'AwsSolutions-IAM4', reason: 'at least 10 characters' }]
    );
  }
}
```

</details><details>
  <summary>Example 6) Granular Suppressions of findings</summary>

Certain rules support granular suppressions of `findings`. If you received the following errors on synth/deploy

```bash
[Error at /StackName/rFirstUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Action::s3:*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
[Error at /StackName/rFirstUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Resource::*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
[Error at /StackName/rSecondUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Action::s3:*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
[Error at /StackName/rSecondUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Resource::*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
```

By applying the following suppressions

```python
import { User } from 'aws-cdk-lib/aws-iam';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const firstUser = new User(this, 'rFirstUser');
    firstUser.addToPolicy(
      new PolicyStatement({
        actions: ['s3:*'],
        resources: ['*'],
      })
    );
    const secondUser = new User(this, 'rSecondUser');
    secondUser.addToPolicy(
      new PolicyStatement({
        actions: ['s3:*'],
        resources: ['*'],
      })
    );
    const thirdUser = new User(this, 'rSecondUser');
    thirdUser.addToPolicy(
      new PolicyStatement({
        actions: ['sqs:CreateQueue'],
        resources: [`arn:aws:sqs:${this.region}:${this.account}:*`],
      })
    );
    NagSuppressions.addResourceSuppressions(
      firstUser,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason:
            "Only suppress AwsSolutions-IAM5 's3:*' finding on First User.",
          appliesTo: ['Action::s3:*'],
        },
      ],
      true
    );
    NagSuppressions.addResourceSuppressions(
      secondUser,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'Suppress all AwsSolutions-IAM5 findings on Second User.',
        },
      ],
      true
    );
    NagSuppressions.addResourceSuppressions(
      thirdUser,
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'Suppress AwsSolutions-IAM5 on the SQS resource.',
          appliesTo: [
            {
              regex: '/^Resource::arn:aws:sqs:(.*):\\*$/g',
            },
          ],
        },
      ],
      true
    );
  }
}
```

You would see the following error on synth/deploy

```bash
[Error at /StackName/rFirstUser/DefaultPolicy/Resource] AwsSolutions-IAM5[Resource::*]: The IAM entity contains wildcard permissions and does not have a cdk-nag rule suppression with evidence for those permission.
```

</details>

## Suppressing `aws-cdk-lib/pipelines` Violations

The [aws-cdk-lib/pipelines.CodePipeline](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.pipelines.CodePipeline.html) construct and its child constructs are not guaranteed to be "Visited" by `Aspects`, as they are not added during the "Construction" phase of the [cdk lifecycle](https://docs.aws.amazon.com/cdk/v2/guide/apps.html#lifecycle). Because of this behavior, you may experience problems such as rule violations not appearing or the inability to suppress violations on these constructs.

You can remediate these rule violation and suppression problems by forcing the pipeline construct creation forward by calling `.buildPipeline()` on your `CodePipeline` object. Otherwise you may see errors such as:

```
Error: Suppression path "/this/construct/path" did not match any resource. This can occur when a resource does not exist or if a suppression is applied before a resource is created.
```

See [this issue](https://github.com/aws/aws-cdk/issues/18440) for more information.

<details>
  <summary>Example) Supressing Violations in Pipelines</summary>

`example-app.ts`

```python
import { App, Aspects } from 'aws-cdk-lib';
import { AwsSolutionsChecks } from 'cdk-nag';
import { ExamplePipeline } from '../lib/example-pipeline';

const app = new App();
new ExamplePipeline(app, 'example-cdk-pipeline');
Aspects.of(app).add(new AwsSolutionsChecks({ verbose: true }));
app.synth();
```

`example-pipeline.ts`

```python
import { Stack, StackProps } from 'aws-cdk-lib';
import { Repository } from 'aws-cdk-lib/aws-codecommit';
import { CodePipeline, CodePipelineSource, ShellStep } from 'aws-cdk-lib/pipelines';
import { NagSuppressions } from 'cdk-nag';
import { Construct } from 'constructs';

export class ExamplePipeline extends Stack {
constructor(scope: Construct, id: string, props?: StackProps) {
  super(scope, id, props);

  const exampleSynth = new ShellStep('ExampleSynth', {
    commands: ['yarn build --frozen-lockfile'],
    input: CodePipelineSource.codeCommit(new Repository(this, 'ExampleRepo', { repositoryName: 'ExampleRepo' }), 'main'),
  });

  const ExamplePipeline = new CodePipeline(this, 'ExamplePipeline', {
    synth: exampleSynth,
  });

  // Force the pipeline construct creation forward before applying suppressions.
  // @See https://github.com/aws/aws-cdk/issues/18440
  ExamplePipeline.buildPipeline();

  // The path suppression will error if you comment out "ExamplePipeline.buildPipeline();""
  NagSuppressions.addResourceSuppressionsByPath(this, '/example-cdk-pipeline/ExamplePipeline/Pipeline/ArtifactsBucket/Resource', [
    {
      id: 'AwsSolutions-S1',
      reason: 'Because I said so',
    },
  ]);
}
}
```

</details>

## Rules and Property Overrides

In some cases L2 Constructs do not have a native option to remediate an issue and must be fixed via [Raw Overrides](https://docs.aws.amazon.com/cdk/latest/guide/cfn_layer.html#cfn_layer_raw). Since raw overrides take place after template synthesis these fixes are not caught by cdk-nag. In this case you should remediate the issue and suppress the issue like in the following example.

<details>
  <summary>Example) Property Overrides</summary>

```python
import {
  Instance,
  InstanceType,
  InstanceClass,
  MachineImage,
  Vpc,
  CfnInstance,
} from 'aws-cdk-lib/aws-ec2';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { NagSuppressions } from 'cdk-nag';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    const instance = new Instance(this, 'rInstance', {
      vpc: new Vpc(this, 'rVpc'),
      instanceType: new InstanceType(InstanceClass.T3),
      machineImage: MachineImage.latestAmazonLinux(),
    });
    const cfnIns = instance.node.defaultChild as CfnInstance;
    cfnIns.addPropertyOverride('DisableApiTermination', true);
    NagSuppressions.addResourceSuppressions(instance, [
      {
        id: 'AwsSolutions-EC29',
        reason: 'Remediated through property override.',
      },
    ]);
  }
}
```

</details>

## Using on CloudFormation templates

You can use cdk-nag on existing CloudFormation templates by using the [cloudformation-include](https://docs.aws.amazon.com/cdk/latest/guide/use_cfn_template.html#use_cfn_template_install) module.

<details>
  <summary>Example 1) CloudFormation template with suppression</summary>

Sample CloudFormation template with suppression

```json
{
  "Resources": {
    "rBucket": {
      "Type": "AWS::S3::Bucket",
      "Properties": {
        "BucketName": "some-bucket-name"
      },
      "Metadata": {
        "cdk_nag": {
          "rules_to_suppress": [
            {
              "id": "AwsSolutions-S1",
              "reason": "at least 10 characters"
            }
          ]
        }
      }
    }
  }
}
```

Sample App

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(new AwsSolutionsChecks());
```

Sample Stack with imported template

```python
import { CfnInclude } from 'aws-cdk-lib/cloudformation-include';
import { NagSuppressions } from 'cdk-nag';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new CfnInclude(this, 'Template', {
      templateFile: 'my-template.json',
    });
    // Add any additional suppressions
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/CdkNagDemo/Template/rBucket',
      [
        {
          id: 'AwsSolutions-S2',
          reason: 'at least 10 characters',
        },
      ]
    );
  }
}
```

</details><details>
  <summary>Example 2) CloudFormation template with granular suppressions</summary>

Sample CloudFormation template with suppression

```json
{
  "Resources": {
    "myPolicy": {
      "Type": "AWS::IAM::Policy",
      "Properties": {
        "PolicyDocument": {
          "Statement": [
            {
              "Action": [
                "kms:Decrypt",
                "kms:DescribeKey",
                "kms:Encrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*"
              ],
              "Effect": "Allow",
              "Resource": ["some-key-arn"]
            }
          ],
          "Version": "2012-10-17"
        }
      },
      "Metadata": {
        "cdk_nag": {
          "rules_to_suppress": [
            {
              "id": "AwsSolutions-IAM5",
              "reason": "Allow key data access",
              "applies_to": [
                "Action::kms:ReEncrypt*",
                "Action::kms:GenerateDataKey*"
              ]
            }
          ]
        }
      }
    }
  }
}
```

Sample App

```python
import { App, Aspects } from 'aws-cdk-lib';
import { CdkTestStack } from '../lib/cdk-test-stack';
import { AwsSolutionsChecks } from 'cdk-nag';

const app = new App();
new CdkTestStack(app, 'CdkNagDemo');
Aspects.of(app).add(new AwsSolutionsChecks());
```

Sample Stack with imported template

```python
import { CfnInclude } from 'aws-cdk-lib/cloudformation-include';
import { NagSuppressions } from 'cdk-nag';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class CdkTestStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    new CfnInclude(this, 'Template', {
      templateFile: 'my-template.json',
    });
    // Add any additional suppressions
    NagSuppressions.addResourceSuppressionsByPath(
      this,
      '/CdkNagDemo/Template/myPolicy',
      [
        {
          id: 'AwsSolutions-IAM5',
          reason: 'Allow key data access',
          appliesTo: ['Action::kms:ReEncrypt*', 'Action::kms:GenerateDataKey*'],
        },
      ]
    );
  }
}
```

</details>

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## License

This project is licensed under the Apache-2.0 License.
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
import constructs


@jsii.interface(jsii_type="cdk-nag.IApplyRule")
class IApplyRule(typing_extensions.Protocol):
    '''Interface for JSII interoperability for passing parameters and the Rule Callback to @applyRule method.'''

    @builtins.property
    @jsii.member(jsii_name="explanation")
    def explanation(self) -> builtins.str:
        '''Why the rule exists.'''
        ...

    @explanation.setter
    def explanation(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> builtins.str:
        '''Why the rule was triggered.'''
        ...

    @info.setter
    def info(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> "NagMessageLevel":
        '''The annotations message level to apply to the rule if triggered.'''
        ...

    @level.setter
    def level(self, value: "NagMessageLevel") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> aws_cdk.CfnResource:
        '''Ignores listed in cdk-nag metadata.'''
        ...

    @node.setter
    def node(self, value: aws_cdk.CfnResource) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="ruleSuffixOverride")
    def rule_suffix_override(self) -> typing.Optional[builtins.str]:
        '''Override for the suffix of the Rule ID for this rule.'''
        ...

    @rule_suffix_override.setter
    def rule_suffix_override(self, value: typing.Optional[builtins.str]) -> None:
        ...

    @jsii.member(jsii_name="rule")
    def rule(
        self,
        node: aws_cdk.CfnResource,
    ) -> typing.Union["NagRuleCompliance", typing.List[builtins.str]]:
        '''The callback to the rule.

        :param node: The CfnResource to check.
        '''
        ...


class _IApplyRuleProxy:
    '''Interface for JSII interoperability for passing parameters and the Rule Callback to @applyRule method.'''

    __jsii_type__: typing.ClassVar[str] = "cdk-nag.IApplyRule"

    @builtins.property
    @jsii.member(jsii_name="explanation")
    def explanation(self) -> builtins.str:
        '''Why the rule exists.'''
        return typing.cast(builtins.str, jsii.get(self, "explanation"))

    @explanation.setter
    def explanation(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "explanation", value)

    @builtins.property
    @jsii.member(jsii_name="info")
    def info(self) -> builtins.str:
        '''Why the rule was triggered.'''
        return typing.cast(builtins.str, jsii.get(self, "info"))

    @info.setter
    def info(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "info", value)

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> "NagMessageLevel":
        '''The annotations message level to apply to the rule if triggered.'''
        return typing.cast("NagMessageLevel", jsii.get(self, "level"))

    @level.setter
    def level(self, value: "NagMessageLevel") -> None:
        if __debug__:
            def stub(value: NagMessageLevel) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> aws_cdk.CfnResource:
        '''Ignores listed in cdk-nag metadata.'''
        return typing.cast(aws_cdk.CfnResource, jsii.get(self, "node"))

    @node.setter
    def node(self, value: aws_cdk.CfnResource) -> None:
        if __debug__:
            def stub(value: aws_cdk.CfnResource) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "node", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSuffixOverride")
    def rule_suffix_override(self) -> typing.Optional[builtins.str]:
        '''Override for the suffix of the Rule ID for this rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSuffixOverride"))

    @rule_suffix_override.setter
    def rule_suffix_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSuffixOverride", value)

    @jsii.member(jsii_name="rule")
    def rule(
        self,
        node: aws_cdk.CfnResource,
    ) -> typing.Union["NagRuleCompliance", typing.List[builtins.str]]:
        '''The callback to the rule.

        :param node: The CfnResource to check.
        '''
        if __debug__:
            def stub(node: aws_cdk.CfnResource) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(typing.Union["NagRuleCompliance", typing.List[builtins.str]], jsii.invoke(self, "rule", [node]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplyRule).__jsii_proxy_class__ = lambda : _IApplyRuleProxy


@jsii.enum(jsii_type="cdk-nag.NagMessageLevel")
class NagMessageLevel(enum.Enum):
    '''The level of the message that the rule applies.'''

    WARN = "WARN"
    ERROR = "ERROR"


@jsii.implements(aws_cdk.IAspect)
class NagPack(metaclass=jsii.JSIIAbstractClass, jsii_type="cdk-nag.NagPack"):
    '''Base class for all rule packs.'''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(log_ignores=log_ignores, reports=reports, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="applyRule")
    def _apply_rule(self, params: IApplyRule) -> None:
        '''Create a rule to be used in the NagPack.

        :param params: The.

        :IApplyRule: interface with rule details.
        '''
        if __debug__:
            def stub(params: IApplyRule) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
        return typing.cast(None, jsii.invoke(self, "applyRule", [params]))

    @jsii.member(jsii_name="createComplianceReportLine")
    def _create_compliance_report_line(
        self,
        params: IApplyRule,
        rule_id: builtins.str,
        compliance: typing.Union["NagRuleCompliance", builtins.str],
        explanation: typing.Optional[builtins.str] = None,
    ) -> builtins.str:
        '''Helper function to create a line for the compliance report.

        :param params: The.
        :param rule_id: The id of the rule.
        :param compliance: The compliance status of the rule.
        :param explanation: The explanation for suppressed rules.

        :IApplyRule: interface with rule details.
        '''
        if __debug__:
            def stub(
                params: IApplyRule,
                rule_id: builtins.str,
                compliance: typing.Union[NagRuleCompliance, builtins.str],
                explanation: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument compliance", value=compliance, expected_type=type_hints["compliance"])
            check_type(argname="argument explanation", value=explanation, expected_type=type_hints["explanation"])
        return typing.cast(builtins.str, jsii.invoke(self, "createComplianceReportLine", [params, rule_id, compliance, explanation]))

    @jsii.member(jsii_name="createMessage")
    def _create_message(
        self,
        rule_id: builtins.str,
        finding_id: builtins.str,
        info: builtins.str,
        explanation: builtins.str,
    ) -> builtins.str:
        '''The message to output to the console when a rule is triggered.

        :param rule_id: The id of the rule.
        :param finding_id: The id of the finding.
        :param info: Why the rule was triggered.
        :param explanation: Why the rule exists.

        :return: The formatted message string.
        '''
        if __debug__:
            def stub(
                rule_id: builtins.str,
                finding_id: builtins.str,
                info: builtins.str,
                explanation: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
            check_type(argname="argument info", value=info, expected_type=type_hints["info"])
            check_type(argname="argument explanation", value=explanation, expected_type=type_hints["explanation"])
        return typing.cast(builtins.str, jsii.invoke(self, "createMessage", [rule_id, finding_id, info, explanation]))

    @jsii.member(jsii_name="ignoreRule")
    def _ignore_rule(
        self,
        ignores: typing.Sequence[typing.Union["NagPackSuppression", typing.Dict[str, typing.Any]]],
        rule_id: builtins.str,
        finding_id: builtins.str,
    ) -> builtins.str:
        '''Check whether a specific rule should be ignored.

        :param ignores: The ignores listed in cdk-nag metadata.
        :param rule_id: The id of the rule to ignore.
        :param finding_id: The id of the finding that is being checked.

        :return: The reason the rule was ignored, or an empty string.
        '''
        if __debug__:
            def stub(
                ignores: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
                rule_id: builtins.str,
                finding_id: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ignores", value=ignores, expected_type=type_hints["ignores"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument finding_id", value=finding_id, expected_type=type_hints["finding_id"])
        return typing.cast(builtins.str, jsii.invoke(self, "ignoreRule", [ignores, rule_id, finding_id]))

    @jsii.member(jsii_name="initializeStackReport")
    def _initialize_stack_report(self, params: IApplyRule) -> None:
        '''Initialize the report for the rule pack's compliance report for the resource's Stack if it doesn't exist.

        :param params: -
        '''
        if __debug__:
            def stub(params: IApplyRule) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
        return typing.cast(None, jsii.invoke(self, "initializeStackReport", [params]))

    @jsii.member(jsii_name="visit")
    @abc.abstractmethod
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        ...

    @jsii.member(jsii_name="writeToStackComplianceReport")
    def _write_to_stack_compliance_report(
        self,
        params: IApplyRule,
        rule_id: builtins.str,
        compliance: typing.Union["NagRuleCompliance", builtins.str],
        explanation: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Write a line to the rule pack's compliance report for the resource's Stack.

        :param params: The.
        :param rule_id: The id of the rule.
        :param compliance: The compliance status of the rule.
        :param explanation: The explanation for suppressed rules.

        :IApplyRule: interface with rule details.
        '''
        if __debug__:
            def stub(
                params: IApplyRule,
                rule_id: builtins.str,
                compliance: typing.Union[NagRuleCompliance, builtins.str],
                explanation: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument params", value=params, expected_type=type_hints["params"])
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
            check_type(argname="argument compliance", value=compliance, expected_type=type_hints["compliance"])
            check_type(argname="argument explanation", value=explanation, expected_type=type_hints["explanation"])
        return typing.cast(None, jsii.invoke(self, "writeToStackComplianceReport", [params, rule_id, compliance, explanation]))

    @builtins.property
    @jsii.member(jsii_name="readPackName")
    def read_pack_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "readPackName"))

    @builtins.property
    @jsii.member(jsii_name="readReportStacks")
    def read_report_stacks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "readReportStacks"))

    @builtins.property
    @jsii.member(jsii_name="logIgnores")
    def _log_ignores(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "logIgnores"))

    @_log_ignores.setter
    def _log_ignores(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logIgnores", value)

    @builtins.property
    @jsii.member(jsii_name="packName")
    def _pack_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packName"))

    @_pack_name.setter
    def _pack_name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packName", value)

    @builtins.property
    @jsii.member(jsii_name="reports")
    def _reports(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "reports"))

    @_reports.setter
    def _reports(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reports", value)

    @builtins.property
    @jsii.member(jsii_name="reportStacks")
    def _report_stacks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "reportStacks"))

    @_report_stacks.setter
    def _report_stacks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reportStacks", value)

    @builtins.property
    @jsii.member(jsii_name="verbose")
    def _verbose(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.get(self, "verbose"))

    @_verbose.setter
    def _verbose(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verbose", value)


class _NagPackProxy(NagPack):
    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            def stub(node: constructs.IConstruct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, NagPack).__jsii_proxy_class__ = lambda : _NagPackProxy


@jsii.data_type(
    jsii_type="cdk-nag.NagPackProps",
    jsii_struct_bases=[],
    name_mapping={
        "log_ignores": "logIgnores",
        "reports": "reports",
        "verbose": "verbose",
    },
)
class NagPackProps:
    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Interface for creating a Nag rule pack.

        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        if __debug__:
            def stub(
                *,
                log_ignores: typing.Optional[builtins.bool] = None,
                reports: typing.Optional[builtins.bool] = None,
                verbose: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_ignores", value=log_ignores, expected_type=type_hints["log_ignores"])
            check_type(argname="argument reports", value=reports, expected_type=type_hints["reports"])
            check_type(argname="argument verbose", value=verbose, expected_type=type_hints["verbose"])
        self._values: typing.Dict[str, typing.Any] = {}
        if log_ignores is not None:
            self._values["log_ignores"] = log_ignores
        if reports is not None:
            self._values["reports"] = reports
        if verbose is not None:
            self._values["verbose"] = verbose

    @builtins.property
    def log_ignores(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to log triggered rules that have been suppressed as informational messages (default: false).'''
        result = self._values.get("log_ignores")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def reports(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).'''
        result = self._values.get("reports")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def verbose(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).'''
        result = self._values.get("verbose")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagPackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="cdk-nag.NagPackSuppression",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "reason": "reason", "applies_to": "appliesTo"},
)
class NagPackSuppression:
    def __init__(
        self,
        *,
        id: builtins.str,
        reason: builtins.str,
        applies_to: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union["RegexAppliesTo", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Interface for creating a rule suppression.

        :param id: The id of the rule to ignore.
        :param reason: The reason to ignore the rule (minimum 10 characters).
        :param applies_to: Rule specific granular suppressions.
        '''
        if __debug__:
            def stub(
                *,
                id: builtins.str,
                reason: builtins.str,
                applies_to: typing.Optional[typing.Sequence[typing.Union[builtins.str, typing.Union[RegexAppliesTo, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            check_type(argname="argument applies_to", value=applies_to, expected_type=type_hints["applies_to"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "reason": reason,
        }
        if applies_to is not None:
            self._values["applies_to"] = applies_to

    @builtins.property
    def id(self) -> builtins.str:
        '''The id of the rule to ignore.'''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reason(self) -> builtins.str:
        '''The reason to ignore the rule (minimum 10 characters).'''
        result = self._values.get("reason")
        assert result is not None, "Required property 'reason' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def applies_to(
        self,
    ) -> typing.Optional[typing.List[typing.Union[builtins.str, "RegexAppliesTo"]]]:
        '''Rule specific granular suppressions.'''
        result = self._values.get("applies_to")
        return typing.cast(typing.Optional[typing.List[typing.Union[builtins.str, "RegexAppliesTo"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NagPackSuppression(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="cdk-nag.NagRuleCompliance")
class NagRuleCompliance(enum.Enum):
    '''The compliance level of a resource in relation to a rule.'''

    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON_COMPLIANT"
    NOT_APPLICABLE = "NOT_APPLICABLE"


class NagRules(metaclass=jsii.JSIIMeta, jsii_type="cdk-nag.NagRules"):
    '''Helper class with methods for rule creation.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="resolveIfPrimitive")
    @builtins.classmethod
    def resolve_if_primitive(
        cls,
        node: aws_cdk.CfnResource,
        parameter: typing.Any,
    ) -> typing.Any:
        '''Use in cases where a primitive value must be known to pass a rule.

        https://developer.mozilla.org/en-US/docs/Glossary/Primitive

        :param node: The CfnResource to check.
        :param parameter: The value to attempt to resolve.

        :return: Return a value if resolves to a primitive data type, otherwise throw an error.
        '''
        if __debug__:
            def stub(node: aws_cdk.CfnResource, parameter: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolveIfPrimitive", [node, parameter]))

    @jsii.member(jsii_name="resolveResourceFromInstrinsic")
    @builtins.classmethod
    def resolve_resource_from_instrinsic(
        cls,
        node: aws_cdk.CfnResource,
        parameter: typing.Any,
    ) -> typing.Any:
        '''Use in cases where a token resolves to an intrinsic function and the referenced resource must be known to pass a rule.

        :param node: The CfnResource to check.
        :param parameter: The value to attempt to resolve.

        :return: Return the Logical resource Id if resolves to a intrinsic function, otherwise the resolved provided value.
        '''
        if __debug__:
            def stub(node: aws_cdk.CfnResource, parameter: typing.Any) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
            check_type(argname="argument parameter", value=parameter, expected_type=type_hints["parameter"])
        return typing.cast(typing.Any, jsii.sinvoke(cls, "resolveResourceFromInstrinsic", [node, parameter]))


class NagSuppressions(metaclass=jsii.JSIIMeta, jsii_type="cdk-nag.NagSuppressions"):
    '''Helper class with methods to add cdk-nag suppressions to cdk resources.'''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="addResourceSuppressions")
    @builtins.classmethod
    def add_resource_suppressions(
        cls,
        construct: typing.Union[constructs.IConstruct, typing.Sequence[constructs.IConstruct]],
        suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
        apply_to_children: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Add cdk-nag suppressions to a CfnResource and optionally its children.

        :param construct: The IConstruct(s) to apply the suppression to.
        :param suppressions: A list of suppressions to apply to the resource.
        :param apply_to_children: Apply the suppressions to children CfnResources (default:false).
        '''
        if __debug__:
            def stub(
                construct: typing.Union[constructs.IConstruct, typing.Sequence[constructs.IConstruct]],
                suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
                apply_to_children: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument apply_to_children", value=apply_to_children, expected_type=type_hints["apply_to_children"])
        return typing.cast(None, jsii.sinvoke(cls, "addResourceSuppressions", [construct, suppressions, apply_to_children]))

    @jsii.member(jsii_name="addResourceSuppressionsByPath")
    @builtins.classmethod
    def add_resource_suppressions_by_path(
        cls,
        stack: aws_cdk.Stack,
        path: typing.Union[builtins.str, typing.Sequence[builtins.str]],
        suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
        apply_to_children: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Add cdk-nag suppressions to a CfnResource and optionally its children via its path.

        :param stack: The Stack the construct belongs to.
        :param path: The path(s) to the construct in the provided stack.
        :param suppressions: A list of suppressions to apply to the resource.
        :param apply_to_children: Apply the suppressions to children CfnResources (default:false).
        '''
        if __debug__:
            def stub(
                stack: aws_cdk.Stack,
                path: typing.Union[builtins.str, typing.Sequence[builtins.str]],
                suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
                apply_to_children: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument apply_to_children", value=apply_to_children, expected_type=type_hints["apply_to_children"])
        return typing.cast(None, jsii.sinvoke(cls, "addResourceSuppressionsByPath", [stack, path, suppressions, apply_to_children]))

    @jsii.member(jsii_name="addStackSuppressions")
    @builtins.classmethod
    def add_stack_suppressions(
        cls,
        stack: aws_cdk.Stack,
        suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
        apply_to_nested_stacks: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Apply cdk-nag suppressions to a Stack and optionally nested stacks.

        :param stack: The Stack to apply the suppression to.
        :param suppressions: A list of suppressions to apply to the stack.
        :param apply_to_nested_stacks: Apply the suppressions to children stacks (default:false).
        '''
        if __debug__:
            def stub(
                stack: aws_cdk.Stack,
                suppressions: typing.Sequence[typing.Union[NagPackSuppression, typing.Dict[str, typing.Any]]],
                apply_to_nested_stacks: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stack", value=stack, expected_type=type_hints["stack"])
            check_type(argname="argument suppressions", value=suppressions, expected_type=type_hints["suppressions"])
            check_type(argname="argument apply_to_nested_stacks", value=apply_to_nested_stacks, expected_type=type_hints["apply_to_nested_stacks"])
        return typing.cast(None, jsii.sinvoke(cls, "addStackSuppressions", [stack, suppressions, apply_to_nested_stacks]))


class PCIDSS321Checks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.PCIDSS321Checks",
):
    '''Check for PCI DSS 3.2.1 compliance. Based on the PCI DSS 3.2.1 AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-pci-dss.html.'''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(log_ignores=log_ignores, reports=reports, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            def stub(node: constructs.IConstruct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


@jsii.data_type(
    jsii_type="cdk-nag.RegexAppliesTo",
    jsii_struct_bases=[],
    name_mapping={"regex": "regex"},
)
class RegexAppliesTo:
    def __init__(self, *, regex: builtins.str) -> None:
        '''A regular expression to apply to matching findings.

        :param regex: An ECMA-262 regex string.
        '''
        if __debug__:
            def stub(*, regex: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
        self._values: typing.Dict[str, typing.Any] = {
            "regex": regex,
        }

    @builtins.property
    def regex(self) -> builtins.str:
        '''An ECMA-262 regex string.'''
        result = self._values.get("regex")
        assert result is not None, "Required property 'regex' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegexAppliesTo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AwsSolutionsChecks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.AwsSolutionsChecks",
):
    '''Check Best practices based on AWS Solutions Security Matrix.'''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(log_ignores=log_ignores, reports=reports, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            def stub(node: constructs.IConstruct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


class HIPAASecurityChecks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.HIPAASecurityChecks",
):
    '''Check for HIPAA Security compliance.

    Based on the HIPAA Security AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-hipaa_security.html
    '''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(log_ignores=log_ignores, reports=reports, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            def stub(node: constructs.IConstruct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


class NIST80053R4Checks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.NIST80053R4Checks",
):
    '''Check for NIST 800-53 rev 4 compliance.

    Based on the NIST 800-53 rev 4 AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-nist-800-53_rev_4.html
    '''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(log_ignores=log_ignores, reports=reports, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            def stub(node: constructs.IConstruct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


class NIST80053R5Checks(
    NagPack,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-nag.NIST80053R5Checks",
):
    '''Check for NIST 800-53 rev 5 compliance.

    Based on the NIST 800-53 rev 5 AWS operational best practices: https://docs.aws.amazon.com/config/latest/developerguide/operational-best-practices-for-nist-800-53_rev_5.html
    '''

    def __init__(
        self,
        *,
        log_ignores: typing.Optional[builtins.bool] = None,
        reports: typing.Optional[builtins.bool] = None,
        verbose: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param log_ignores: Whether or not to log triggered rules that have been suppressed as informational messages (default: false).
        :param reports: Whether or not to generate CSV compliance reports for applied Stacks in the App's output directory (default: true).
        :param verbose: Whether or not to enable extended explanatory descriptions on warning, error, and logged ignore messages (default: false).
        '''
        props = NagPackProps(log_ignores=log_ignores, reports=reports, verbose=verbose)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="visit")
    def visit(self, node: constructs.IConstruct) -> None:
        '''All aspects can visit an IConstruct.

        :param node: -
        '''
        if __debug__:
            def stub(node: constructs.IConstruct) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument node", value=node, expected_type=type_hints["node"])
        return typing.cast(None, jsii.invoke(self, "visit", [node]))


__all__ = [
    "AwsSolutionsChecks",
    "HIPAASecurityChecks",
    "IApplyRule",
    "NIST80053R4Checks",
    "NIST80053R5Checks",
    "NagMessageLevel",
    "NagPack",
    "NagPackProps",
    "NagPackSuppression",
    "NagRuleCompliance",
    "NagRules",
    "NagSuppressions",
    "PCIDSS321Checks",
    "RegexAppliesTo",
]

publication.publish()
