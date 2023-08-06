'''
# Amazon Managed Streaming for Apache Kafka Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

[Amazon MSK](https://aws.amazon.com/msk/) is a fully managed service that makes it easy for you to build and run applications that use Apache Kafka to process streaming data.

The following example creates an MSK Cluster.

```python
# vpc: ec2.Vpc

cluster = msk.Cluster(self, "Cluster",
    cluster_name="myCluster",
    kafka_version=msk.KafkaVersion.V2_8_1,
    vpc=vpc
)
```

## Allowing Connections

To control who can access the Cluster, use the `.connections` attribute. For a list of ports used by MSK, refer to the [MSK documentation](https://docs.aws.amazon.com/msk/latest/developerguide/client-access.html#port-info).

```python
# vpc: ec2.Vpc

cluster = msk.Cluster(self, "Cluster",
    cluster_name="myCluster",
    kafka_version=msk.KafkaVersion.V2_8_1,
    vpc=vpc
)

cluster.connections.allow_from(
    ec2.Peer.ipv4("1.2.3.4/8"),
    ec2.Port.tcp(2181))
cluster.connections.allow_from(
    ec2.Peer.ipv4("1.2.3.4/8"),
    ec2.Port.tcp(9094))
```

## Cluster Endpoints

You can use the following attributes to get a list of the Kafka broker or ZooKeeper node endpoints

```python
# cluster: msk.Cluster

CfnOutput(self, "BootstrapBrokers", value=cluster.bootstrap_brokers)
CfnOutput(self, "BootstrapBrokersTls", value=cluster.bootstrap_brokers_tls)
CfnOutput(self, "BootstrapBrokersSaslScram", value=cluster.bootstrap_brokers_sasl_scram)
CfnOutput(self, "ZookeeperConnection", value=cluster.zookeeper_connection_string)
CfnOutput(self, "ZookeeperConnectionTls", value=cluster.zookeeper_connection_string_tls)
```

## Importing an existing Cluster

To import an existing MSK cluster into your CDK app use the `.fromClusterArn()` method.

```python
cluster = msk.Cluster.from_cluster_arn(self, "Cluster", "arn:aws:kafka:us-west-2:1234567890:cluster/a-cluster/11111111-1111-1111-1111-111111111111-1")
```

## Client Authentication

[MSK supports](https://docs.aws.amazon.com/msk/latest/developerguide/kafka_apis_iam.html) the following authentication mechanisms.

> Only one authentication method can be enabled.

### TLS

To enable client authentication with TLS set the `certificateAuthorityArns` property to reference your ACM Private CA. [More info on Private CAs.](https://docs.aws.amazon.com/msk/latest/developerguide/msk-authentication.html)

```python
import aws_cdk.aws_acmpca as acmpca

# vpc: ec2.Vpc

cluster = msk.Cluster(self, "Cluster",
    cluster_name="myCluster",
    kafka_version=msk.KafkaVersion.V2_8_1,
    vpc=vpc,
    encryption_in_transit=msk.EncryptionInTransitConfig(
        client_broker=msk.ClientBrokerEncryption.TLS
    ),
    client_authentication=msk.ClientAuthentication.tls(
        certificate_authorities=[
            acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CertificateAuthority", "arn:aws:acm-pca:us-west-2:1234567890:certificate-authority/11111111-1111-1111-1111-111111111111")
        ]
    )
)
```

### SASL/SCRAM

Enable client authentication with [SASL/SCRAM](https://docs.aws.amazon.com/msk/latest/developerguide/msk-password.html):

```python
# vpc: ec2.Vpc

cluster = msk.Cluster(self, "cluster",
    cluster_name="myCluster",
    kafka_version=msk.KafkaVersion.V2_8_1,
    vpc=vpc,
    encryption_in_transit=msk.EncryptionInTransitConfig(
        client_broker=msk.ClientBrokerEncryption.TLS
    ),
    client_authentication=msk.ClientAuthentication.sasl(
        scram=True
    )
)
```

### SASL/IAM

Enable client authentication with [IAM](https://docs.aws.amazon.com/msk/latest/developerguide/iam-access-control.html):

```python
# vpc: ec2.Vpc

cluster = msk.Cluster(self, "cluster",
    cluster_name="myCluster",
    kafka_version=msk.KafkaVersion.V2_8_1,
    vpc=vpc,
    encryption_in_transit=msk.EncryptionInTransitConfig(
        client_broker=msk.ClientBrokerEncryption.TLS
    ),
    client_authentication=msk.ClientAuthentication.sasl(
        iam=True
    )
)
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

import aws_cdk.aws_acmpca
import aws_cdk.aws_ec2
import aws_cdk.aws_kms
import aws_cdk.aws_logs
import aws_cdk.aws_s3
import aws_cdk.core
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.BrokerLogging",
    jsii_struct_bases=[],
    name_mapping={
        "cloudwatch_log_group": "cloudwatchLogGroup",
        "firehose_delivery_stream_name": "firehoseDeliveryStreamName",
        "s3": "s3",
    },
)
class BrokerLogging:
    def __init__(
        self,
        *,
        cloudwatch_log_group: typing.Optional[aws_cdk.aws_logs.ILogGroup] = None,
        firehose_delivery_stream_name: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["S3LoggingConfiguration", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Configuration details related to broker logs.

        :param cloudwatch_log_group: (experimental) The CloudWatch Logs group that is the destination for broker logs. Default: - disabled
        :param firehose_delivery_stream_name: (experimental) The Kinesis Data Firehose delivery stream that is the destination for broker logs. Default: - disabled
        :param s3: (experimental) Details of the Amazon S3 destination for broker logs. Default: - disabled

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_logs as logs
            import aws_cdk.aws_msk as msk
            import aws_cdk.aws_s3 as s3
            
            # bucket: s3.Bucket
            # log_group: logs.LogGroup
            
            broker_logging = msk.BrokerLogging(
                cloudwatch_log_group=log_group,
                firehose_delivery_stream_name="firehoseDeliveryStreamName",
                s3=msk.S3LoggingConfiguration(
                    bucket=bucket,
            
                    # the properties below are optional
                    prefix="prefix"
                )
            )
        '''
        if isinstance(s3, dict):
            s3 = S3LoggingConfiguration(**s3)
        if __debug__:
            def stub(
                *,
                cloudwatch_log_group: typing.Optional[aws_cdk.aws_logs.ILogGroup] = None,
                firehose_delivery_stream_name: typing.Optional[builtins.str] = None,
                s3: typing.Optional[typing.Union[S3LoggingConfiguration, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cloudwatch_log_group", value=cloudwatch_log_group, expected_type=type_hints["cloudwatch_log_group"])
            check_type(argname="argument firehose_delivery_stream_name", value=firehose_delivery_stream_name, expected_type=type_hints["firehose_delivery_stream_name"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cloudwatch_log_group is not None:
            self._values["cloudwatch_log_group"] = cloudwatch_log_group
        if firehose_delivery_stream_name is not None:
            self._values["firehose_delivery_stream_name"] = firehose_delivery_stream_name
        if s3 is not None:
            self._values["s3"] = s3

    @builtins.property
    def cloudwatch_log_group(self) -> typing.Optional[aws_cdk.aws_logs.ILogGroup]:
        '''(experimental) The CloudWatch Logs group that is the destination for broker logs.

        :default: - disabled

        :stability: experimental
        '''
        result = self._values.get("cloudwatch_log_group")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.ILogGroup], result)

    @builtins.property
    def firehose_delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The Kinesis Data Firehose delivery stream that is the destination for broker logs.

        :default: - disabled

        :stability: experimental
        '''
        result = self._values.get("firehose_delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional["S3LoggingConfiguration"]:
        '''(experimental) Details of the Amazon S3 destination for broker logs.

        :default: - disabled

        :stability: experimental
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["S3LoggingConfiguration"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrokerLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnBatchScramSecret(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-msk.CfnBatchScramSecret",
):
    '''A CloudFormation ``AWS::MSK::BatchScramSecret``.

    Represents a secret stored in the Amazon Secrets Manager that can be used to authenticate with a cluster using a user name and a password.

    :cloudformationResource: AWS::MSK::BatchScramSecret
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_msk as msk
        
        cfn_batch_scram_secret = msk.CfnBatchScramSecret(self, "MyCfnBatchScramSecret",
            cluster_arn="clusterArn",
        
            # the properties below are optional
            secret_arn_list=["secretArnList"]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        cluster_arn: builtins.str,
        secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::MSK::BatchScramSecret``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param cluster_arn: The Amazon Resource Name (ARN) of the MSK cluster.
        :param secret_arn_list: A list of Amazon Secrets Manager secret ARNs.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                cluster_arn: builtins.str,
                secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBatchScramSecretProps(
            cluster_arn=cluster_arn, secret_arn_list=secret_arn_list
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the MSK cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-clusterarn
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @cluster_arn.setter
    def cluster_arn(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterArn", value)

    @builtins.property
    @jsii.member(jsii_name="secretArnList")
    def secret_arn_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Secrets Manager secret ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-secretarnlist
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secretArnList"))

    @secret_arn_list.setter
    def secret_arn_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretArnList", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.CfnBatchScramSecretProps",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn", "secret_arn_list": "secretArnList"},
)
class CfnBatchScramSecretProps:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBatchScramSecret``.

        :param cluster_arn: The Amazon Resource Name (ARN) of the MSK cluster.
        :param secret_arn_list: A list of Amazon Secrets Manager secret ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            
            cfn_batch_scram_secret_props = msk.CfnBatchScramSecretProps(
                cluster_arn="clusterArn",
            
                # the properties below are optional
                secret_arn_list=["secretArnList"]
            )
        '''
        if __debug__:
            def stub(
                *,
                cluster_arn: builtins.str,
                secret_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument secret_arn_list", value=secret_arn_list, expected_type=type_hints["secret_arn_list"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }
        if secret_arn_list is not None:
            self._values["secret_arn_list"] = secret_arn_list

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the MSK cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-clusterarn
        '''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_arn_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of Amazon Secrets Manager secret ARNs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-batchscramsecret.html#cfn-msk-batchscramsecret-secretarnlist
        '''
        result = self._values.get("secret_arn_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBatchScramSecretProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-msk.CfnCluster",
):
    '''A CloudFormation ``AWS::MSK::Cluster``.

    The ``AWS::MSK::Cluster`` resource creates an Amazon MSK cluster . For more information, see `What Is Amazon MSK? <https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html>`_ in the *Amazon MSK Developer Guide* .

    :cloudformationResource: AWS::MSK::Cluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_msk as msk
        
        cfn_cluster = msk.CfnCluster(self, "MyCfnCluster",
            broker_node_group_info=msk.CfnCluster.BrokerNodeGroupInfoProperty(
                client_subnets=["clientSubnets"],
                instance_type="instanceType",
        
                # the properties below are optional
                broker_az_distribution="brokerAzDistribution",
                connectivity_info=msk.CfnCluster.ConnectivityInfoProperty(
                    public_access=msk.CfnCluster.PublicAccessProperty(
                        type="type"
                    )
                ),
                security_groups=["securityGroups"],
                storage_info=msk.CfnCluster.StorageInfoProperty(
                    ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                        provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                            enabled=False,
                            volume_throughput=123
                        ),
                        volume_size=123
                    )
                )
            ),
            cluster_name="clusterName",
            kafka_version="kafkaVersion",
            number_of_broker_nodes=123,
        
            # the properties below are optional
            client_authentication=msk.CfnCluster.ClientAuthenticationProperty(
                sasl=msk.CfnCluster.SaslProperty(
                    iam=msk.CfnCluster.IamProperty(
                        enabled=False
                    ),
                    scram=msk.CfnCluster.ScramProperty(
                        enabled=False
                    )
                ),
                tls=msk.CfnCluster.TlsProperty(
                    certificate_authority_arn_list=["certificateAuthorityArnList"],
                    enabled=False
                ),
                unauthenticated=msk.CfnCluster.UnauthenticatedProperty(
                    enabled=False
                )
            ),
            configuration_info=msk.CfnCluster.ConfigurationInfoProperty(
                arn="arn",
                revision=123
            ),
            current_version="currentVersion",
            encryption_info=msk.CfnCluster.EncryptionInfoProperty(
                encryption_at_rest=msk.CfnCluster.EncryptionAtRestProperty(
                    data_volume_kms_key_id="dataVolumeKmsKeyId"
                ),
                encryption_in_transit=msk.CfnCluster.EncryptionInTransitProperty(
                    client_broker="clientBroker",
                    in_cluster=False
                )
            ),
            enhanced_monitoring="enhancedMonitoring",
            logging_info=msk.CfnCluster.LoggingInfoProperty(
                broker_logs=msk.CfnCluster.BrokerLogsProperty(
                    cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                        enabled=False,
        
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=msk.CfnCluster.FirehoseProperty(
                        enabled=False,
        
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=msk.CfnCluster.S3Property(
                        enabled=False,
        
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            ),
            open_monitoring=msk.CfnCluster.OpenMonitoringProperty(
                prometheus=msk.CfnCluster.PrometheusProperty(
                    jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                        enabled_in_broker=False
                    ),
                    node_exporter=msk.CfnCluster.NodeExporterProperty(
                        enabled_in_broker=False
                    )
                )
            ),
            storage_mode="storageMode",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        broker_node_group_info: typing.Union[typing.Union["CfnCluster.BrokerNodeGroupInfoProperty", typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable],
        cluster_name: builtins.str,
        kafka_version: builtins.str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.ClientAuthenticationProperty", typing.Dict[str, typing.Any]]]] = None,
        configuration_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.ConfigurationInfoProperty", typing.Dict[str, typing.Any]]]] = None,
        current_version: typing.Optional[builtins.str] = None,
        encryption_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.EncryptionInfoProperty", typing.Dict[str, typing.Any]]]] = None,
        enhanced_monitoring: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.LoggingInfoProperty", typing.Dict[str, typing.Any]]]] = None,
        open_monitoring: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.OpenMonitoringProperty", typing.Dict[str, typing.Any]]]] = None,
        storage_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::MSK::Cluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param broker_node_group_info: The setup to be used for brokers in the cluster. AWS CloudFormation may replace the cluster when you update certain ``BrokerNodeGroupInfo`` properties. To understand the update behavior for your use case, you should review the child properties for ```BrokerNodeGroupInfo`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#aws-properties-msk-cluster-brokernodegroupinfo-properties>`_ .
        :param cluster_name: The name of the cluster.
        :param kafka_version: The version of Apache Kafka. For more information, see `Supported Apache Kafka versions <https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html>`_ in the Amazon MSK Developer Guide.
        :param number_of_broker_nodes: The number of broker nodes you want in the Amazon MSK cluster. You can submit an update to increase the number of broker nodes in a cluster.
        :param client_authentication: Includes information related to client authentication.
        :param configuration_info: The Amazon MSK configuration to use for the cluster.
        :param current_version: The version of the cluster that you want to update.
        :param encryption_info: Includes all encryption-related information.
        :param enhanced_monitoring: Specifies the level of monitoring for the MSK cluster. The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .
        :param logging_info: You can configure your Amazon MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.
        :param open_monitoring: The settings for open monitoring.
        :param storage_mode: This controls storage mode for supported storage tiers.
        :param tags: A map of key:value pairs to apply to this resource. Both key and value are of type String.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                broker_node_group_info: typing.Union[typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable],
                cluster_name: builtins.str,
                kafka_version: builtins.str,
                number_of_broker_nodes: jsii.Number,
                client_authentication: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ClientAuthenticationProperty, typing.Dict[str, typing.Any]]]] = None,
                configuration_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ConfigurationInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                current_version: typing.Optional[builtins.str] = None,
                encryption_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.EncryptionInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                enhanced_monitoring: typing.Optional[builtins.str] = None,
                logging_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.LoggingInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                open_monitoring: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.OpenMonitoringProperty, typing.Dict[str, typing.Any]]]] = None,
                storage_mode: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnClusterProps(
            broker_node_group_info=broker_node_group_info,
            cluster_name=cluster_name,
            kafka_version=kafka_version,
            number_of_broker_nodes=number_of_broker_nodes,
            client_authentication=client_authentication,
            configuration_info=configuration_info,
            current_version=current_version,
            encryption_info=encryption_info,
            enhanced_monitoring=enhanced_monitoring,
            logging_info=logging_info,
            open_monitoring=open_monitoring,
            storage_mode=storage_mode,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''A map of key:value pairs to apply to this resource.

        Both key and value are of type String.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="brokerNodeGroupInfo")
    def broker_node_group_info(
        self,
    ) -> typing.Union["CfnCluster.BrokerNodeGroupInfoProperty", aws_cdk.core.IResolvable]:
        '''The setup to be used for brokers in the cluster.

        AWS CloudFormation may replace the cluster when you update certain ``BrokerNodeGroupInfo`` properties. To understand the update behavior for your use case, you should review the child properties for ```BrokerNodeGroupInfo`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#aws-properties-msk-cluster-brokernodegroupinfo-properties>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo
        '''
        return typing.cast(typing.Union["CfnCluster.BrokerNodeGroupInfoProperty", aws_cdk.core.IResolvable], jsii.get(self, "brokerNodeGroupInfo"))

    @broker_node_group_info.setter
    def broker_node_group_info(
        self,
        value: typing.Union["CfnCluster.BrokerNodeGroupInfoProperty", aws_cdk.core.IResolvable],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, aws_cdk.core.IResolvable],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "brokerNodeGroupInfo", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername
        '''
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
    @jsii.member(jsii_name="kafkaVersion")
    def kafka_version(self) -> builtins.str:
        '''The version of Apache Kafka.

        For more information, see `Supported Apache Kafka versions <https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html>`_ in the Amazon MSK Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion
        '''
        return typing.cast(builtins.str, jsii.get(self, "kafkaVersion"))

    @kafka_version.setter
    def kafka_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaVersion", value)

    @builtins.property
    @jsii.member(jsii_name="numberOfBrokerNodes")
    def number_of_broker_nodes(self) -> jsii.Number:
        '''The number of broker nodes you want in the Amazon MSK cluster.

        You can submit an update to increase the number of broker nodes in a cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes
        '''
        return typing.cast(jsii.Number, jsii.get(self, "numberOfBrokerNodes"))

    @number_of_broker_nodes.setter
    def number_of_broker_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberOfBrokerNodes", value)

    @builtins.property
    @jsii.member(jsii_name="clientAuthentication")
    def client_authentication(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ClientAuthenticationProperty"]]:
        '''Includes information related to client authentication.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ClientAuthenticationProperty"]], jsii.get(self, "clientAuthentication"))

    @client_authentication.setter
    def client_authentication(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ClientAuthenticationProperty"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ClientAuthenticationProperty]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="configurationInfo")
    def configuration_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationInfoProperty"]]:
        '''The Amazon MSK configuration to use for the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationInfoProperty"]], jsii.get(self, "configurationInfo"))

    @configuration_info.setter
    def configuration_info(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConfigurationInfoProperty"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ConfigurationInfoProperty]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationInfo", value)

    @builtins.property
    @jsii.member(jsii_name="currentVersion")
    def current_version(self) -> typing.Optional[builtins.str]:
        '''The version of the cluster that you want to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-currentversion
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "currentVersion"))

    @current_version.setter
    def current_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "currentVersion", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionInfo")
    def encryption_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionInfoProperty"]]:
        '''Includes all encryption-related information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionInfoProperty"]], jsii.get(self, "encryptionInfo"))

    @encryption_info.setter
    def encryption_info(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionInfoProperty"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.EncryptionInfoProperty]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionInfo", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedMonitoring")
    def enhanced_monitoring(self) -> typing.Optional[builtins.str]:
        '''Specifies the level of monitoring for the MSK cluster.

        The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enhancedMonitoring"))

    @enhanced_monitoring.setter
    def enhanced_monitoring(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="loggingInfo")
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.LoggingInfoProperty"]]:
        '''You can configure your Amazon MSK cluster to send broker logs to different destination types.

        This is a container for the configuration details related to broker logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.LoggingInfoProperty"]], jsii.get(self, "loggingInfo"))

    @logging_info.setter
    def logging_info(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.LoggingInfoProperty"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.LoggingInfoProperty]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingInfo", value)

    @builtins.property
    @jsii.member(jsii_name="openMonitoring")
    def open_monitoring(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.OpenMonitoringProperty"]]:
        '''The settings for open monitoring.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
        '''
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.OpenMonitoringProperty"]], jsii.get(self, "openMonitoring"))

    @open_monitoring.setter
    def open_monitoring(
        self,
        value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.OpenMonitoringProperty"]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.OpenMonitoringProperty]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openMonitoring", value)

    @builtins.property
    @jsii.member(jsii_name="storageMode")
    def storage_mode(self) -> typing.Optional[builtins.str]:
        '''This controls storage mode for supported storage tiers.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-storagemode
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageMode"))

    @storage_mode.setter
    def storage_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageMode", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.BrokerLogsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs": "cloudWatchLogs",
            "firehose": "firehose",
            "s3": "s3",
        },
    )
    class BrokerLogsProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.CloudWatchLogsProperty", typing.Dict[str, typing.Any]]]] = None,
            firehose: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.FirehoseProperty", typing.Dict[str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.S3Property", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''You can configure your Amazon MSK cluster to send broker logs to different destination types.

            This configuration specifies the details of these destinations.

            :param cloud_watch_logs: Details of the CloudWatch Logs destination for broker logs.
            :param firehose: Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs.
            :param s3: Details of the Amazon MSK destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                broker_logs_property = msk.CfnCluster.BrokerLogsProperty(
                    cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                        enabled=False,
                
                        # the properties below are optional
                        log_group="logGroup"
                    ),
                    firehose=msk.CfnCluster.FirehoseProperty(
                        enabled=False,
                
                        # the properties below are optional
                        delivery_stream="deliveryStream"
                    ),
                    s3=msk.CfnCluster.S3Property(
                        enabled=False,
                
                        # the properties below are optional
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    cloud_watch_logs: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.CloudWatchLogsProperty, typing.Dict[str, typing.Any]]]] = None,
                    firehose: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.FirehoseProperty, typing.Dict[str, typing.Any]]]] = None,
                    s3: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.S3Property, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[str, typing.Any] = {}
            if cloud_watch_logs is not None:
                self._values["cloud_watch_logs"] = cloud_watch_logs
            if firehose is not None:
                self._values["firehose"] = firehose
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.CloudWatchLogsProperty"]]:
            '''Details of the CloudWatch Logs destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.CloudWatchLogsProperty"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.FirehoseProperty"]]:
            '''Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.FirehoseProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.S3Property"]]:
            '''Details of the Amazon MSK destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokerlogs.html#cfn-msk-cluster-brokerlogs-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.S3Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrokerLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.BrokerNodeGroupInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_subnets": "clientSubnets",
            "instance_type": "instanceType",
            "broker_az_distribution": "brokerAzDistribution",
            "connectivity_info": "connectivityInfo",
            "security_groups": "securityGroups",
            "storage_info": "storageInfo",
        },
    )
    class BrokerNodeGroupInfoProperty:
        def __init__(
            self,
            *,
            client_subnets: typing.Sequence[builtins.str],
            instance_type: builtins.str,
            broker_az_distribution: typing.Optional[builtins.str] = None,
            connectivity_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.ConnectivityInfoProperty", typing.Dict[str, typing.Any]]]] = None,
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            storage_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.StorageInfoProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''The setup to be used for brokers in the cluster.

            :param client_subnets: The list of subnets to connect to in the client virtual private cloud (VPC). Amazon creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. If you use the US West (N. California) Region, specify exactly two subnets. For other Regions where Amazon MSK is available, you can specify either two or three subnets. The subnets that you specify must be in distinct Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly across the subnets that you specify. Client subnets can't occupy the Availability Zone with ID ``use1-az3`` .
            :param instance_type: The type of Amazon EC2 instances to use for brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, and kafka.m5.24xlarge.
            :param broker_az_distribution: This parameter is currently not in use.
            :param connectivity_info: Information about the cluster's connectivity setting.
            :param security_groups: The security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the ``ec2:DescribeSecurityGroups`` permission.
            :param storage_info: Contains information about storage volumes attached to Amazon MSK broker nodes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                broker_node_group_info_property = msk.CfnCluster.BrokerNodeGroupInfoProperty(
                    client_subnets=["clientSubnets"],
                    instance_type="instanceType",
                
                    # the properties below are optional
                    broker_az_distribution="brokerAzDistribution",
                    connectivity_info=msk.CfnCluster.ConnectivityInfoProperty(
                        public_access=msk.CfnCluster.PublicAccessProperty(
                            type="type"
                        )
                    ),
                    security_groups=["securityGroups"],
                    storage_info=msk.CfnCluster.StorageInfoProperty(
                        ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                            provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                                enabled=False,
                                volume_throughput=123
                            ),
                            volume_size=123
                        )
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    client_subnets: typing.Sequence[builtins.str],
                    instance_type: builtins.str,
                    broker_az_distribution: typing.Optional[builtins.str] = None,
                    connectivity_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ConnectivityInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                    storage_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.StorageInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument client_subnets", value=client_subnets, expected_type=type_hints["client_subnets"])
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument broker_az_distribution", value=broker_az_distribution, expected_type=type_hints["broker_az_distribution"])
                check_type(argname="argument connectivity_info", value=connectivity_info, expected_type=type_hints["connectivity_info"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument storage_info", value=storage_info, expected_type=type_hints["storage_info"])
            self._values: typing.Dict[str, typing.Any] = {
                "client_subnets": client_subnets,
                "instance_type": instance_type,
            }
            if broker_az_distribution is not None:
                self._values["broker_az_distribution"] = broker_az_distribution
            if connectivity_info is not None:
                self._values["connectivity_info"] = connectivity_info
            if security_groups is not None:
                self._values["security_groups"] = security_groups
            if storage_info is not None:
                self._values["storage_info"] = storage_info

        @builtins.property
        def client_subnets(self) -> typing.List[builtins.str]:
            '''The list of subnets to connect to in the client virtual private cloud (VPC).

            Amazon creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data.

            If you use the US West (N. California) Region, specify exactly two subnets. For other Regions where Amazon MSK is available, you can specify either two or three subnets. The subnets that you specify must be in distinct Availability Zones. When you create a cluster, Amazon MSK distributes the broker nodes evenly across the subnets that you specify.

            Client subnets can't occupy the Availability Zone with ID ``use1-az3`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-clientsubnets
            '''
            result = self._values.get("client_subnets")
            assert result is not None, "Required property 'client_subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''The type of Amazon EC2 instances to use for brokers.

            The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.8xlarge, kafka.m5.12xlarge, kafka.m5.16xlarge, and kafka.m5.24xlarge.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def broker_az_distribution(self) -> typing.Optional[builtins.str]:
            '''This parameter is currently not in use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-brokerazdistribution
            '''
            result = self._values.get("broker_az_distribution")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connectivity_info(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConnectivityInfoProperty"]]:
            '''Information about the cluster's connectivity setting.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-connectivityinfo
            '''
            result = self._values.get("connectivity_info")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ConnectivityInfoProperty"]], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster.

            If you don't specify a security group, Amazon MSK uses the default security group associated with the VPC. If you specify security groups that were shared with you, you must ensure that you have permissions to them. Specifically, you need the ``ec2:DescribeSecurityGroups`` permission.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def storage_info(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.StorageInfoProperty"]]:
            '''Contains information about storage volumes attached to Amazon MSK broker nodes.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#cfn-msk-cluster-brokernodegroupinfo-storageinfo
            '''
            result = self._values.get("storage_info")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.StorageInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrokerNodeGroupInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.ClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sasl": "sasl",
            "tls": "tls",
            "unauthenticated": "unauthenticated",
        },
    )
    class ClientAuthenticationProperty:
        def __init__(
            self,
            *,
            sasl: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.SaslProperty", typing.Dict[str, typing.Any]]]] = None,
            tls: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.TlsProperty", typing.Dict[str, typing.Any]]]] = None,
            unauthenticated: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.UnauthenticatedProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''Includes information related to client authentication.

            :param sasl: Details for ClientAuthentication using SASL.
            :param tls: Details for client authentication using TLS.
            :param unauthenticated: Details for ClientAuthentication using no authentication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                client_authentication_property = msk.CfnCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnCluster.SaslProperty(
                        iam=msk.CfnCluster.IamProperty(
                            enabled=False
                        ),
                        scram=msk.CfnCluster.ScramProperty(
                            enabled=False
                        )
                    ),
                    tls=msk.CfnCluster.TlsProperty(
                        certificate_authority_arn_list=["certificateAuthorityArnList"],
                        enabled=False
                    ),
                    unauthenticated=msk.CfnCluster.UnauthenticatedProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    sasl: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.SaslProperty, typing.Dict[str, typing.Any]]]] = None,
                    tls: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.TlsProperty, typing.Dict[str, typing.Any]]]] = None,
                    unauthenticated: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.UnauthenticatedProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument sasl", value=sasl, expected_type=type_hints["sasl"])
                check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
                check_type(argname="argument unauthenticated", value=unauthenticated, expected_type=type_hints["unauthenticated"])
            self._values: typing.Dict[str, typing.Any] = {}
            if sasl is not None:
                self._values["sasl"] = sasl
            if tls is not None:
                self._values["tls"] = tls
            if unauthenticated is not None:
                self._values["unauthenticated"] = unauthenticated

        @builtins.property
        def sasl(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SaslProperty"]]:
            '''Details for ClientAuthentication using SASL.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-sasl
            '''
            result = self._values.get("sasl")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.SaslProperty"]], result)

        @builtins.property
        def tls(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.TlsProperty"]]:
            '''Details for client authentication using TLS.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-tls
            '''
            result = self._values.get("tls")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.TlsProperty"]], result)

        @builtins.property
        def unauthenticated(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.UnauthenticatedProperty"]]:
            '''Details for ClientAuthentication using no authentication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-clientauthentication.html#cfn-msk-cluster-clientauthentication-unauthenticated
            '''
            result = self._values.get("unauthenticated")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.UnauthenticatedProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.CloudWatchLogsProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "log_group": "logGroup"},
    )
    class CloudWatchLogsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            log_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details of the CloudWatch Logs destination for broker logs.

            :param enabled: Specifies whether broker logs get sent to the specified CloudWatch Logs destination.
            :param log_group: The CloudWatch Logs group that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                cloud_watch_logs_property = msk.CfnCluster.CloudWatchLogsProperty(
                    enabled=False,
                
                    # the properties below are optional
                    log_group="logGroup"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                    log_group: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if log_group is not None:
                self._values["log_group"] = log_group

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Specifies whether broker logs get sent to the specified CloudWatch Logs destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''The CloudWatch Logs group that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-cloudwatchlogs.html#cfn-msk-cluster-cloudwatchlogs-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.ConfigurationInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "revision": "revision"},
    )
    class ConfigurationInfoProperty:
        def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
            '''Specifies the Amazon MSK configuration to use for the brokers.

            :param arn: The Amazon Resource Name (ARN) of the MSK configuration to use. For example, ``arn:aws:kafka:us-east-1:123456789012:configuration/example-configuration-name/abcdabcd-1234-abcd-1234-abcd123e8e8e-1`` .
            :param revision: The revision of the Amazon MSK configuration to use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                configuration_info_property = msk.CfnCluster.ConfigurationInfoProperty(
                    arn="arn",
                    revision=123
                )
            '''
            if __debug__:
                def stub(*, arn: builtins.str, revision: jsii.Number) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
            self._values: typing.Dict[str, typing.Any] = {
                "arn": arn,
                "revision": revision,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the MSK configuration to use.

            For example, ``arn:aws:kafka:us-east-1:123456789012:configuration/example-configuration-name/abcdabcd-1234-abcd-1234-abcd123e8e8e-1`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def revision(self) -> jsii.Number:
            '''The revision of the Amazon MSK configuration to use.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-configurationinfo.html#cfn-msk-cluster-configurationinfo-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.ConnectivityInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"public_access": "publicAccess"},
    )
    class ConnectivityInfoProperty:
        def __init__(
            self,
            *,
            public_access: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.PublicAccessProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies whether the cluster's brokers are publicly accessible.

            By default, they are not.

            :param public_access: Specifies whether the cluster's brokers are accessible from the internet. Public access is off by default.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                connectivity_info_property = msk.CfnCluster.ConnectivityInfoProperty(
                    public_access=msk.CfnCluster.PublicAccessProperty(
                        type="type"
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    public_access: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.PublicAccessProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument public_access", value=public_access, expected_type=type_hints["public_access"])
            self._values: typing.Dict[str, typing.Any] = {}
            if public_access is not None:
                self._values["public_access"] = public_access

        @builtins.property
        def public_access(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PublicAccessProperty"]]:
            '''Specifies whether the cluster's brokers are accessible from the internet.

            Public access is off by default.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-connectivityinfo.html#cfn-msk-cluster-connectivityinfo-publicaccess
            '''
            result = self._values.get("public_access")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PublicAccessProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectivityInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.EBSStorageInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provisioned_throughput": "provisionedThroughput",
            "volume_size": "volumeSize",
        },
    )
    class EBSStorageInfoProperty:
        def __init__(
            self,
            *,
            provisioned_throughput: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.ProvisionedThroughputProperty", typing.Dict[str, typing.Any]]]] = None,
            volume_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains information about the EBS storage volumes attached to brokers.

            :param provisioned_throughput: Specifies whether provisioned throughput is turned on and the volume throughput target.
            :param volume_size: The size in GiB of the EBS volume for the data drive on each broker node.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                e_bSStorage_info_property = msk.CfnCluster.EBSStorageInfoProperty(
                    provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                        enabled=False,
                        volume_throughput=123
                    ),
                    volume_size=123
                )
            '''
            if __debug__:
                def stub(
                    *,
                    provisioned_throughput: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ProvisionedThroughputProperty, typing.Dict[str, typing.Any]]]] = None,
                    volume_size: typing.Optional[jsii.Number] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument provisioned_throughput", value=provisioned_throughput, expected_type=type_hints["provisioned_throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
            self._values: typing.Dict[str, typing.Any] = {}
            if provisioned_throughput is not None:
                self._values["provisioned_throughput"] = provisioned_throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size

        @builtins.property
        def provisioned_throughput(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ProvisionedThroughputProperty"]]:
            '''Specifies whether provisioned throughput is turned on and the volume throughput target.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-provisionedthroughput
            '''
            result = self._values.get("provisioned_throughput")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ProvisionedThroughputProperty"]], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''The size in GiB of the EBS volume for the data drive on each broker node.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-ebsstorageinfo.html#cfn-msk-cluster-ebsstorageinfo-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EBSStorageInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.EncryptionAtRestProperty",
        jsii_struct_bases=[],
        name_mapping={"data_volume_kms_key_id": "dataVolumeKmsKeyId"},
    )
    class EncryptionAtRestProperty:
        def __init__(self, *, data_volume_kms_key_id: builtins.str) -> None:
            '''The data volume encryption details.

            :param data_volume_kms_key_id: The ARN of the Amazon KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it on your behalf.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                encryption_at_rest_property = msk.CfnCluster.EncryptionAtRestProperty(
                    data_volume_kms_key_id="dataVolumeKmsKeyId"
                )
            '''
            if __debug__:
                def stub(*, data_volume_kms_key_id: builtins.str) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument data_volume_kms_key_id", value=data_volume_kms_key_id, expected_type=type_hints["data_volume_kms_key_id"])
            self._values: typing.Dict[str, typing.Any] = {
                "data_volume_kms_key_id": data_volume_kms_key_id,
            }

        @builtins.property
        def data_volume_kms_key_id(self) -> builtins.str:
            '''The ARN of the Amazon KMS key for encrypting data at rest.

            If you don't specify a KMS key, MSK creates one for you and uses it on your behalf.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionatrest.html#cfn-msk-cluster-encryptionatrest-datavolumekmskeyid
            '''
            result = self._values.get("data_volume_kms_key_id")
            assert result is not None, "Required property 'data_volume_kms_key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionAtRestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.EncryptionInTransitProperty",
        jsii_struct_bases=[],
        name_mapping={"client_broker": "clientBroker", "in_cluster": "inCluster"},
    )
    class EncryptionInTransitProperty:
        def __init__(
            self,
            *,
            client_broker: typing.Optional[builtins.str] = None,
            in_cluster: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''The settings for encrypting data in transit.

            :param client_broker: Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values. - ``TLS`` means that client-broker communication is enabled with TLS only. - ``TLS_PLAINTEXT`` means that client-broker communication is enabled for both TLS-encrypted, as well as plain text data. - ``PLAINTEXT`` means that client-broker communication is enabled in plain text only. The default value is ``TLS`` .
            :param in_cluster: When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plain text. The default value is true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                encryption_in_transit_property = msk.CfnCluster.EncryptionInTransitProperty(
                    client_broker="clientBroker",
                    in_cluster=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    client_broker: typing.Optional[builtins.str] = None,
                    in_cluster: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument client_broker", value=client_broker, expected_type=type_hints["client_broker"])
                check_type(argname="argument in_cluster", value=in_cluster, expected_type=type_hints["in_cluster"])
            self._values: typing.Dict[str, typing.Any] = {}
            if client_broker is not None:
                self._values["client_broker"] = client_broker
            if in_cluster is not None:
                self._values["in_cluster"] = in_cluster

        @builtins.property
        def client_broker(self) -> typing.Optional[builtins.str]:
            '''Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.

            - ``TLS`` means that client-broker communication is enabled with TLS only.
            - ``TLS_PLAINTEXT`` means that client-broker communication is enabled for both TLS-encrypted, as well as plain text data.
            - ``PLAINTEXT`` means that client-broker communication is enabled in plain text only.

            The default value is ``TLS`` .

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-clientbroker
            '''
            result = self._values.get("client_broker")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def in_cluster(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted.

            When set to false, the communication happens in plain text. The default value is true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptionintransit.html#cfn-msk-cluster-encryptionintransit-incluster
            '''
            result = self._values.get("in_cluster")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionInTransitProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.EncryptionInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_at_rest": "encryptionAtRest",
            "encryption_in_transit": "encryptionInTransit",
        },
    )
    class EncryptionInfoProperty:
        def __init__(
            self,
            *,
            encryption_at_rest: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.EncryptionAtRestProperty", typing.Dict[str, typing.Any]]]] = None,
            encryption_in_transit: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.EncryptionInTransitProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''Includes encryption-related information, such as the Amazon KMS key used for encrypting data at rest and whether you want MSK to encrypt your data in transit.

            :param encryption_at_rest: The data-volume encryption details.
            :param encryption_in_transit: The details for encryption in transit.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                encryption_info_property = msk.CfnCluster.EncryptionInfoProperty(
                    encryption_at_rest=msk.CfnCluster.EncryptionAtRestProperty(
                        data_volume_kms_key_id="dataVolumeKmsKeyId"
                    ),
                    encryption_in_transit=msk.CfnCluster.EncryptionInTransitProperty(
                        client_broker="clientBroker",
                        in_cluster=False
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    encryption_at_rest: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.EncryptionAtRestProperty, typing.Dict[str, typing.Any]]]] = None,
                    encryption_in_transit: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.EncryptionInTransitProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument encryption_at_rest", value=encryption_at_rest, expected_type=type_hints["encryption_at_rest"])
                check_type(argname="argument encryption_in_transit", value=encryption_in_transit, expected_type=type_hints["encryption_in_transit"])
            self._values: typing.Dict[str, typing.Any] = {}
            if encryption_at_rest is not None:
                self._values["encryption_at_rest"] = encryption_at_rest
            if encryption_in_transit is not None:
                self._values["encryption_in_transit"] = encryption_in_transit

        @builtins.property
        def encryption_at_rest(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionAtRestProperty"]]:
            '''The data-volume encryption details.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionatrest
            '''
            result = self._values.get("encryption_at_rest")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionAtRestProperty"]], result)

        @builtins.property
        def encryption_in_transit(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionInTransitProperty"]]:
            '''The details for encryption in transit.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-encryptioninfo.html#cfn-msk-cluster-encryptioninfo-encryptionintransit
            '''
            result = self._values.get("encryption_in_transit")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EncryptionInTransitProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.FirehoseProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "delivery_stream": "deliveryStream"},
    )
    class FirehoseProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            delivery_stream: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details of the Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :param enabled: Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream.
            :param delivery_stream: The Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                firehose_property = msk.CfnCluster.FirehoseProperty(
                    enabled=False,
                
                    # the properties below are optional
                    delivery_stream="deliveryStream"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                    delivery_stream: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument delivery_stream", value=delivery_stream, expected_type=type_hints["delivery_stream"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if delivery_stream is not None:
                self._values["delivery_stream"] = delivery_stream

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Specifies whether broker logs get sent to the specified Kinesis Data Firehose delivery stream.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def delivery_stream(self) -> typing.Optional[builtins.str]:
            '''The Kinesis Data Firehose delivery stream that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-firehose.html#cfn-msk-cluster-firehose-deliverystream
            '''
            result = self._values.get("delivery_stream")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.IamProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class IamProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''Details for IAM access control.

            :param enabled: Whether IAM access control is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                iam_property = msk.CfnCluster.IamProperty(
                    enabled=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Whether IAM access control is enabled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-iam.html#cfn-msk-cluster-iam-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.JmxExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_in_broker": "enabledInBroker"},
    )
    class JmxExporterProperty:
        def __init__(
            self,
            *,
            enabled_in_broker: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''Indicates whether you want to enable or disable the JMX Exporter.

            :param enabled_in_broker: Indicates whether you want to enable or disable the JMX Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                jmx_exporter_property = msk.CfnCluster.JmxExporterProperty(
                    enabled_in_broker=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled_in_broker: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled_in_broker", value=enabled_in_broker, expected_type=type_hints["enabled_in_broker"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled_in_broker": enabled_in_broker,
            }

        @builtins.property
        def enabled_in_broker(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Indicates whether you want to enable or disable the JMX Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-jmxexporter.html#cfn-msk-cluster-jmxexporter-enabledinbroker
            '''
            result = self._values.get("enabled_in_broker")
            assert result is not None, "Required property 'enabled_in_broker' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JmxExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.LoggingInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"broker_logs": "brokerLogs"},
    )
    class LoggingInfoProperty:
        def __init__(
            self,
            *,
            broker_logs: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.BrokerLogsProperty", typing.Dict[str, typing.Any]]],
        ) -> None:
            '''You can configure your Amazon MSK cluster to send broker logs to different destination types.

            This is a container for the configuration details related to broker logs.

            :param broker_logs: You can configure your Amazon MSK cluster to send broker logs to different destination types. This configuration specifies the details of these destinations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                logging_info_property = msk.CfnCluster.LoggingInfoProperty(
                    broker_logs=msk.CfnCluster.BrokerLogsProperty(
                        cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                            enabled=False,
                
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=msk.CfnCluster.FirehoseProperty(
                            enabled=False,
                
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=msk.CfnCluster.S3Property(
                            enabled=False,
                
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    broker_logs: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.BrokerLogsProperty, typing.Dict[str, typing.Any]]],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument broker_logs", value=broker_logs, expected_type=type_hints["broker_logs"])
            self._values: typing.Dict[str, typing.Any] = {
                "broker_logs": broker_logs,
            }

        @builtins.property
        def broker_logs(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.BrokerLogsProperty"]:
            '''You can configure your Amazon MSK cluster to send broker logs to different destination types.

            This configuration specifies the details of these destinations.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-logginginfo.html#cfn-msk-cluster-logginginfo-brokerlogs
            '''
            result = self._values.get("broker_logs")
            assert result is not None, "Required property 'broker_logs' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.BrokerLogsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.NodeExporterProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled_in_broker": "enabledInBroker"},
    )
    class NodeExporterProperty:
        def __init__(
            self,
            *,
            enabled_in_broker: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''Indicates whether you want to enable or disable the Node Exporter.

            :param enabled_in_broker: Indicates whether you want to enable or disable the Node Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                node_exporter_property = msk.CfnCluster.NodeExporterProperty(
                    enabled_in_broker=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled_in_broker: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled_in_broker", value=enabled_in_broker, expected_type=type_hints["enabled_in_broker"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled_in_broker": enabled_in_broker,
            }

        @builtins.property
        def enabled_in_broker(
            self,
        ) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Indicates whether you want to enable or disable the Node Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-nodeexporter.html#cfn-msk-cluster-nodeexporter-enabledinbroker
            '''
            result = self._values.get("enabled_in_broker")
            assert result is not None, "Required property 'enabled_in_broker' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeExporterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.OpenMonitoringProperty",
        jsii_struct_bases=[],
        name_mapping={"prometheus": "prometheus"},
    )
    class OpenMonitoringProperty:
        def __init__(
            self,
            *,
            prometheus: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.PrometheusProperty", typing.Dict[str, typing.Any]]],
        ) -> None:
            '''JMX and Node monitoring for the MSK cluster.

            :param prometheus: Prometheus exporter settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                open_monitoring_property = msk.CfnCluster.OpenMonitoringProperty(
                    prometheus=msk.CfnCluster.PrometheusProperty(
                        jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                            enabled_in_broker=False
                        ),
                        node_exporter=msk.CfnCluster.NodeExporterProperty(
                            enabled_in_broker=False
                        )
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    prometheus: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.PrometheusProperty, typing.Dict[str, typing.Any]]],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument prometheus", value=prometheus, expected_type=type_hints["prometheus"])
            self._values: typing.Dict[str, typing.Any] = {
                "prometheus": prometheus,
            }

        @builtins.property
        def prometheus(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PrometheusProperty"]:
            '''Prometheus exporter settings.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-openmonitoring.html#cfn-msk-cluster-openmonitoring-prometheus
            '''
            result = self._values.get("prometheus")
            assert result is not None, "Required property 'prometheus' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnCluster.PrometheusProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenMonitoringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.PrometheusProperty",
        jsii_struct_bases=[],
        name_mapping={"jmx_exporter": "jmxExporter", "node_exporter": "nodeExporter"},
    )
    class PrometheusProperty:
        def __init__(
            self,
            *,
            jmx_exporter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.JmxExporterProperty", typing.Dict[str, typing.Any]]]] = None,
            node_exporter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.NodeExporterProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''Prometheus settings for open monitoring.

            :param jmx_exporter: Indicates whether you want to enable or disable the JMX Exporter.
            :param node_exporter: Indicates whether you want to enable or disable the Node Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                prometheus_property = msk.CfnCluster.PrometheusProperty(
                    jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                        enabled_in_broker=False
                    ),
                    node_exporter=msk.CfnCluster.NodeExporterProperty(
                        enabled_in_broker=False
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    jmx_exporter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.JmxExporterProperty, typing.Dict[str, typing.Any]]]] = None,
                    node_exporter: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.NodeExporterProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument jmx_exporter", value=jmx_exporter, expected_type=type_hints["jmx_exporter"])
                check_type(argname="argument node_exporter", value=node_exporter, expected_type=type_hints["node_exporter"])
            self._values: typing.Dict[str, typing.Any] = {}
            if jmx_exporter is not None:
                self._values["jmx_exporter"] = jmx_exporter
            if node_exporter is not None:
                self._values["node_exporter"] = node_exporter

        @builtins.property
        def jmx_exporter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.JmxExporterProperty"]]:
            '''Indicates whether you want to enable or disable the JMX Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-jmxexporter
            '''
            result = self._values.get("jmx_exporter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.JmxExporterProperty"]], result)

        @builtins.property
        def node_exporter(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.NodeExporterProperty"]]:
            '''Indicates whether you want to enable or disable the Node Exporter.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-prometheus.html#cfn-msk-cluster-prometheus-nodeexporter
            '''
            result = self._values.get("node_exporter")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.NodeExporterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrometheusProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.ProvisionedThroughputProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "volume_throughput": "volumeThroughput"},
    )
    class ProvisionedThroughputProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
            volume_throughput: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies whether provisioned throughput is turned on and the volume throughput target.

            :param enabled: Specifies whether provisioned throughput is turned on for the cluster.
            :param volume_throughput: The provisioned throughput rate in MiB per second.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                provisioned_throughput_property = msk.CfnCluster.ProvisionedThroughputProperty(
                    enabled=False,
                    volume_throughput=123
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
                    volume_throughput: typing.Optional[jsii.Number] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument volume_throughput", value=volume_throughput, expected_type=type_hints["volume_throughput"])
            self._values: typing.Dict[str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if volume_throughput is not None:
                self._values["volume_throughput"] = volume_throughput

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''Specifies whether provisioned throughput is turned on for the cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        @builtins.property
        def volume_throughput(self) -> typing.Optional[jsii.Number]:
            '''The provisioned throughput rate in MiB per second.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-provisionedthroughput.html#cfn-msk-cluster-provisionedthroughput-volumethroughput
            '''
            result = self._values.get("volume_throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedThroughputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.PublicAccessProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class PublicAccessProperty:
        def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
            '''Specifies whether the cluster's brokers are accessible from the internet.

            Public access is off by default.

            :param type: Set to ``DISABLED`` to turn off public access or to ``SERVICE_PROVIDED_EIPS`` to turn it on. Public access if off by default.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                public_access_property = msk.CfnCluster.PublicAccessProperty(
                    type="type"
                )
            '''
            if __debug__:
                def stub(*, type: typing.Optional[builtins.str] = None) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Set to ``DISABLED`` to turn off public access or to ``SERVICE_PROVIDED_EIPS`` to turn it on.

            Public access if off by default.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-publicaccess.html#cfn-msk-cluster-publicaccess-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicAccessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.S3Property",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "bucket": "bucket", "prefix": "prefix"},
    )
    class S3Property:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
            bucket: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the Amazon S3 destination for broker logs.

            :param enabled: Specifies whether broker logs get sent to the specified Amazon S3 destination.
            :param bucket: The name of the S3 bucket that is the destination for broker logs.
            :param prefix: The S3 prefix that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                s3_property = msk.CfnCluster.S3Property(
                    enabled=False,
                
                    # the properties below are optional
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                    bucket: typing.Optional[builtins.str] = None,
                    prefix: typing.Optional[builtins.str] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }
            if bucket is not None:
                self._values["bucket"] = bucket
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Specifies whether broker logs get sent to the specified Amazon S3 destination.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The S3 prefix that is the destination for broker logs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-s3.html#cfn-msk-cluster-s3-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.SaslProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam", "scram": "scram"},
    )
    class SaslProperty:
        def __init__(
            self,
            *,
            iam: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.IamProperty", typing.Dict[str, typing.Any]]]] = None,
            scram: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.ScramProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :param iam: Details for IAM access control.
            :param scram: Details for SASL/SCRAM client authentication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                sasl_property = msk.CfnCluster.SaslProperty(
                    iam=msk.CfnCluster.IamProperty(
                        enabled=False
                    ),
                    scram=msk.CfnCluster.ScramProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    iam: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.IamProperty, typing.Dict[str, typing.Any]]]] = None,
                    scram: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ScramProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
                check_type(argname="argument scram", value=scram, expected_type=type_hints["scram"])
            self._values: typing.Dict[str, typing.Any] = {}
            if iam is not None:
                self._values["iam"] = iam
            if scram is not None:
                self._values["scram"] = scram

        @builtins.property
        def iam(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.IamProperty"]]:
            '''Details for IAM access control.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.IamProperty"]], result)

        @builtins.property
        def scram(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScramProperty"]]:
            '''Details for SASL/SCRAM client authentication.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-sasl.html#cfn-msk-cluster-sasl-scram
            '''
            result = self._values.get("scram")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.ScramProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SaslProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.ScramProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class ScramProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''Details for SASL/SCRAM client authentication.

            :param enabled: SASL/SCRAM authentication is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                scram_property = msk.CfnCluster.ScramProperty(
                    enabled=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''SASL/SCRAM authentication is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-scram.html#cfn-msk-cluster-scram-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScramProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.StorageInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"ebs_storage_info": "ebsStorageInfo"},
    )
    class StorageInfoProperty:
        def __init__(
            self,
            *,
            ebs_storage_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnCluster.EBSStorageInfoProperty", typing.Dict[str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about storage volumes attached to Amazon MSK broker nodes.

            :param ebs_storage_info: EBS volume information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                storage_info_property = msk.CfnCluster.StorageInfoProperty(
                    ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                        provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                            enabled=False,
                            volume_throughput=123
                        ),
                        volume_size=123
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    ebs_storage_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.EBSStorageInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument ebs_storage_info", value=ebs_storage_info, expected_type=type_hints["ebs_storage_info"])
            self._values: typing.Dict[str, typing.Any] = {}
            if ebs_storage_info is not None:
                self._values["ebs_storage_info"] = ebs_storage_info

        @builtins.property
        def ebs_storage_info(
            self,
        ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EBSStorageInfoProperty"]]:
            '''EBS volume information.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-storageinfo.html#cfn-msk-cluster-storageinfo-ebsstorageinfo
            '''
            result = self._values.get("ebs_storage_info")
            return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, "CfnCluster.EBSStorageInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.TlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_authority_arn_list": "certificateAuthorityArnList",
            "enabled": "enabled",
        },
    )
    class TlsProperty:
        def __init__(
            self,
            *,
            certificate_authority_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
        ) -> None:
            '''Details for client authentication using TLS.

            :param certificate_authority_arn_list: List of ACM Certificate Authority ARNs.
            :param enabled: TLS authentication is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                tls_property = msk.CfnCluster.TlsProperty(
                    certificate_authority_arn_list=["certificateAuthorityArnList"],
                    enabled=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    certificate_authority_arn_list: typing.Optional[typing.Sequence[builtins.str]] = None,
                    enabled: typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument certificate_authority_arn_list", value=certificate_authority_arn_list, expected_type=type_hints["certificate_authority_arn_list"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {}
            if certificate_authority_arn_list is not None:
                self._values["certificate_authority_arn_list"] = certificate_authority_arn_list
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def certificate_authority_arn_list(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''List of ACM Certificate Authority ARNs.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-certificateauthorityarnlist
            '''
            result = self._values.get("certificate_authority_arn_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]]:
            '''TLS authentication is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-tls.html#cfn-msk-cluster-tls-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, aws_cdk.core.IResolvable]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnCluster.UnauthenticatedProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class UnauthenticatedProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''Details for allowing no client authentication.

            :param enabled: Unauthenticated is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                unauthenticated_property = msk.CfnCluster.UnauthenticatedProperty(
                    enabled=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''Unauthenticated is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-unauthenticated.html#cfn-msk-cluster-unauthenticated-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UnauthenticatedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.CfnClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "broker_node_group_info": "brokerNodeGroupInfo",
        "cluster_name": "clusterName",
        "kafka_version": "kafkaVersion",
        "number_of_broker_nodes": "numberOfBrokerNodes",
        "client_authentication": "clientAuthentication",
        "configuration_info": "configurationInfo",
        "current_version": "currentVersion",
        "encryption_info": "encryptionInfo",
        "enhanced_monitoring": "enhancedMonitoring",
        "logging_info": "loggingInfo",
        "open_monitoring": "openMonitoring",
        "storage_mode": "storageMode",
        "tags": "tags",
    },
)
class CfnClusterProps:
    def __init__(
        self,
        *,
        broker_node_group_info: typing.Union[typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable],
        cluster_name: builtins.str,
        kafka_version: builtins.str,
        number_of_broker_nodes: jsii.Number,
        client_authentication: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ClientAuthenticationProperty, typing.Dict[str, typing.Any]]]] = None,
        configuration_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ConfigurationInfoProperty, typing.Dict[str, typing.Any]]]] = None,
        current_version: typing.Optional[builtins.str] = None,
        encryption_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.EncryptionInfoProperty, typing.Dict[str, typing.Any]]]] = None,
        enhanced_monitoring: typing.Optional[builtins.str] = None,
        logging_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.LoggingInfoProperty, typing.Dict[str, typing.Any]]]] = None,
        open_monitoring: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.OpenMonitoringProperty, typing.Dict[str, typing.Any]]]] = None,
        storage_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCluster``.

        :param broker_node_group_info: The setup to be used for brokers in the cluster. AWS CloudFormation may replace the cluster when you update certain ``BrokerNodeGroupInfo`` properties. To understand the update behavior for your use case, you should review the child properties for ```BrokerNodeGroupInfo`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#aws-properties-msk-cluster-brokernodegroupinfo-properties>`_ .
        :param cluster_name: The name of the cluster.
        :param kafka_version: The version of Apache Kafka. For more information, see `Supported Apache Kafka versions <https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html>`_ in the Amazon MSK Developer Guide.
        :param number_of_broker_nodes: The number of broker nodes you want in the Amazon MSK cluster. You can submit an update to increase the number of broker nodes in a cluster.
        :param client_authentication: Includes information related to client authentication.
        :param configuration_info: The Amazon MSK configuration to use for the cluster.
        :param current_version: The version of the cluster that you want to update.
        :param encryption_info: Includes all encryption-related information.
        :param enhanced_monitoring: Specifies the level of monitoring for the MSK cluster. The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .
        :param logging_info: You can configure your Amazon MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.
        :param open_monitoring: The settings for open monitoring.
        :param storage_mode: This controls storage mode for supported storage tiers.
        :param tags: A map of key:value pairs to apply to this resource. Both key and value are of type String.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            
            cfn_cluster_props = msk.CfnClusterProps(
                broker_node_group_info=msk.CfnCluster.BrokerNodeGroupInfoProperty(
                    client_subnets=["clientSubnets"],
                    instance_type="instanceType",
            
                    # the properties below are optional
                    broker_az_distribution="brokerAzDistribution",
                    connectivity_info=msk.CfnCluster.ConnectivityInfoProperty(
                        public_access=msk.CfnCluster.PublicAccessProperty(
                            type="type"
                        )
                    ),
                    security_groups=["securityGroups"],
                    storage_info=msk.CfnCluster.StorageInfoProperty(
                        ebs_storage_info=msk.CfnCluster.EBSStorageInfoProperty(
                            provisioned_throughput=msk.CfnCluster.ProvisionedThroughputProperty(
                                enabled=False,
                                volume_throughput=123
                            ),
                            volume_size=123
                        )
                    )
                ),
                cluster_name="clusterName",
                kafka_version="kafkaVersion",
                number_of_broker_nodes=123,
            
                # the properties below are optional
                client_authentication=msk.CfnCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnCluster.SaslProperty(
                        iam=msk.CfnCluster.IamProperty(
                            enabled=False
                        ),
                        scram=msk.CfnCluster.ScramProperty(
                            enabled=False
                        )
                    ),
                    tls=msk.CfnCluster.TlsProperty(
                        certificate_authority_arn_list=["certificateAuthorityArnList"],
                        enabled=False
                    ),
                    unauthenticated=msk.CfnCluster.UnauthenticatedProperty(
                        enabled=False
                    )
                ),
                configuration_info=msk.CfnCluster.ConfigurationInfoProperty(
                    arn="arn",
                    revision=123
                ),
                current_version="currentVersion",
                encryption_info=msk.CfnCluster.EncryptionInfoProperty(
                    encryption_at_rest=msk.CfnCluster.EncryptionAtRestProperty(
                        data_volume_kms_key_id="dataVolumeKmsKeyId"
                    ),
                    encryption_in_transit=msk.CfnCluster.EncryptionInTransitProperty(
                        client_broker="clientBroker",
                        in_cluster=False
                    )
                ),
                enhanced_monitoring="enhancedMonitoring",
                logging_info=msk.CfnCluster.LoggingInfoProperty(
                    broker_logs=msk.CfnCluster.BrokerLogsProperty(
                        cloud_watch_logs=msk.CfnCluster.CloudWatchLogsProperty(
                            enabled=False,
            
                            # the properties below are optional
                            log_group="logGroup"
                        ),
                        firehose=msk.CfnCluster.FirehoseProperty(
                            enabled=False,
            
                            # the properties below are optional
                            delivery_stream="deliveryStream"
                        ),
                        s3=msk.CfnCluster.S3Property(
                            enabled=False,
            
                            # the properties below are optional
                            bucket="bucket",
                            prefix="prefix"
                        )
                    )
                ),
                open_monitoring=msk.CfnCluster.OpenMonitoringProperty(
                    prometheus=msk.CfnCluster.PrometheusProperty(
                        jmx_exporter=msk.CfnCluster.JmxExporterProperty(
                            enabled_in_broker=False
                        ),
                        node_exporter=msk.CfnCluster.NodeExporterProperty(
                            enabled_in_broker=False
                        )
                    )
                ),
                storage_mode="storageMode",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            def stub(
                *,
                broker_node_group_info: typing.Union[typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, typing.Dict[str, typing.Any]], aws_cdk.core.IResolvable],
                cluster_name: builtins.str,
                kafka_version: builtins.str,
                number_of_broker_nodes: jsii.Number,
                client_authentication: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ClientAuthenticationProperty, typing.Dict[str, typing.Any]]]] = None,
                configuration_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.ConfigurationInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                current_version: typing.Optional[builtins.str] = None,
                encryption_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.EncryptionInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                enhanced_monitoring: typing.Optional[builtins.str] = None,
                logging_info: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.LoggingInfoProperty, typing.Dict[str, typing.Any]]]] = None,
                open_monitoring: typing.Optional[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnCluster.OpenMonitoringProperty, typing.Dict[str, typing.Any]]]] = None,
                storage_mode: typing.Optional[builtins.str] = None,
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument broker_node_group_info", value=broker_node_group_info, expected_type=type_hints["broker_node_group_info"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument kafka_version", value=kafka_version, expected_type=type_hints["kafka_version"])
            check_type(argname="argument number_of_broker_nodes", value=number_of_broker_nodes, expected_type=type_hints["number_of_broker_nodes"])
            check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            check_type(argname="argument configuration_info", value=configuration_info, expected_type=type_hints["configuration_info"])
            check_type(argname="argument current_version", value=current_version, expected_type=type_hints["current_version"])
            check_type(argname="argument encryption_info", value=encryption_info, expected_type=type_hints["encryption_info"])
            check_type(argname="argument enhanced_monitoring", value=enhanced_monitoring, expected_type=type_hints["enhanced_monitoring"])
            check_type(argname="argument logging_info", value=logging_info, expected_type=type_hints["logging_info"])
            check_type(argname="argument open_monitoring", value=open_monitoring, expected_type=type_hints["open_monitoring"])
            check_type(argname="argument storage_mode", value=storage_mode, expected_type=type_hints["storage_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "broker_node_group_info": broker_node_group_info,
            "cluster_name": cluster_name,
            "kafka_version": kafka_version,
            "number_of_broker_nodes": number_of_broker_nodes,
        }
        if client_authentication is not None:
            self._values["client_authentication"] = client_authentication
        if configuration_info is not None:
            self._values["configuration_info"] = configuration_info
        if current_version is not None:
            self._values["current_version"] = current_version
        if encryption_info is not None:
            self._values["encryption_info"] = encryption_info
        if enhanced_monitoring is not None:
            self._values["enhanced_monitoring"] = enhanced_monitoring
        if logging_info is not None:
            self._values["logging_info"] = logging_info
        if open_monitoring is not None:
            self._values["open_monitoring"] = open_monitoring
        if storage_mode is not None:
            self._values["storage_mode"] = storage_mode
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def broker_node_group_info(
        self,
    ) -> typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, aws_cdk.core.IResolvable]:
        '''The setup to be used for brokers in the cluster.

        AWS CloudFormation may replace the cluster when you update certain ``BrokerNodeGroupInfo`` properties. To understand the update behavior for your use case, you should review the child properties for ```BrokerNodeGroupInfo`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-cluster-brokernodegroupinfo.html#aws-properties-msk-cluster-brokernodegroupinfo-properties>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-brokernodegroupinfo
        '''
        result = self._values.get("broker_node_group_info")
        assert result is not None, "Required property 'broker_node_group_info' is missing"
        return typing.cast(typing.Union[CfnCluster.BrokerNodeGroupInfoProperty, aws_cdk.core.IResolvable], result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kafka_version(self) -> builtins.str:
        '''The version of Apache Kafka.

        For more information, see `Supported Apache Kafka versions <https://docs.aws.amazon.com/msk/latest/developerguide/supported-kafka-versions.html>`_ in the Amazon MSK Developer Guide.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-kafkaversion
        '''
        result = self._values.get("kafka_version")
        assert result is not None, "Required property 'kafka_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def number_of_broker_nodes(self) -> jsii.Number:
        '''The number of broker nodes you want in the Amazon MSK cluster.

        You can submit an update to increase the number of broker nodes in a cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-numberofbrokernodes
        '''
        result = self._values.get("number_of_broker_nodes")
        assert result is not None, "Required property 'number_of_broker_nodes' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def client_authentication(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ClientAuthenticationProperty]]:
        '''Includes information related to client authentication.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-clientauthentication
        '''
        result = self._values.get("client_authentication")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ClientAuthenticationProperty]], result)

    @builtins.property
    def configuration_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ConfigurationInfoProperty]]:
        '''The Amazon MSK configuration to use for the cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-configurationinfo
        '''
        result = self._values.get("configuration_info")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.ConfigurationInfoProperty]], result)

    @builtins.property
    def current_version(self) -> typing.Optional[builtins.str]:
        '''The version of the cluster that you want to update.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-currentversion
        '''
        result = self._values.get("current_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.EncryptionInfoProperty]]:
        '''Includes all encryption-related information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-encryptioninfo
        '''
        result = self._values.get("encryption_info")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.EncryptionInfoProperty]], result)

    @builtins.property
    def enhanced_monitoring(self) -> typing.Optional[builtins.str]:
        '''Specifies the level of monitoring for the MSK cluster.

        The possible values are ``DEFAULT`` , ``PER_BROKER`` , and ``PER_TOPIC_PER_BROKER`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-enhancedmonitoring
        '''
        result = self._values.get("enhanced_monitoring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_info(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.LoggingInfoProperty]]:
        '''You can configure your Amazon MSK cluster to send broker logs to different destination types.

        This is a container for the configuration details related to broker logs.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-logginginfo
        '''
        result = self._values.get("logging_info")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.LoggingInfoProperty]], result)

    @builtins.property
    def open_monitoring(
        self,
    ) -> typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.OpenMonitoringProperty]]:
        '''The settings for open monitoring.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-openmonitoring
        '''
        result = self._values.get("open_monitoring")
        return typing.cast(typing.Optional[typing.Union[aws_cdk.core.IResolvable, CfnCluster.OpenMonitoringProperty]], result)

    @builtins.property
    def storage_mode(self) -> typing.Optional[builtins.str]:
        '''This controls storage mode for supported storage tiers.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-storagemode
        '''
        result = self._values.get("storage_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key:value pairs to apply to this resource.

        Both key and value are of type String.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html#cfn-msk-cluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnConfiguration(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-msk.CfnConfiguration",
):
    '''A CloudFormation ``AWS::MSK::Configuration``.

    Creates a new MSK configuration.

    :cloudformationResource: AWS::MSK::Configuration
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_msk as msk
        
        cfn_configuration = msk.CfnConfiguration(self, "MyCfnConfiguration",
            name="name",
            server_properties="serverProperties",
        
            # the properties below are optional
            description="description",
            kafka_versions_list=["kafkaVersionsList"]
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        server_properties: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::MSK::Configuration``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param name: The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".
        :param server_properties: Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.
        :param description: The description of the configuration.
        :param kafka_versions_list: A list of the versions of Apache Kafka with which you can use this MSK configuration. You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this list.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                name: builtins.str,
                server_properties: builtins.str,
                description: typing.Optional[builtins.str] = None,
                kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationProps(
            name=name,
            server_properties=server_properties,
            description=description,
            kafka_versions_list=kafka_versions_list,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the configuration.

        Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-name
        '''
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
    @jsii.member(jsii_name="serverProperties")
    def server_properties(self) -> builtins.str:
        '''Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-serverproperties
        '''
        return typing.cast(builtins.str, jsii.get(self, "serverProperties"))

    @server_properties.setter
    def server_properties(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverProperties", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-description
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

    @builtins.property
    @jsii.member(jsii_name="kafkaVersionsList")
    def kafka_versions_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the versions of Apache Kafka with which you can use this MSK configuration.

        You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-kafkaversionslist
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "kafkaVersionsList"))

    @kafka_versions_list.setter
    def kafka_versions_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[builtins.str]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaVersionsList", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.CfnConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "server_properties": "serverProperties",
        "description": "description",
        "kafka_versions_list": "kafkaVersionsList",
    },
)
class CfnConfigurationProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        server_properties: builtins.str,
        description: typing.Optional[builtins.str] = None,
        kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfiguration``.

        :param name: The name of the configuration. Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".
        :param server_properties: Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.
        :param description: The description of the configuration.
        :param kafka_versions_list: A list of the versions of Apache Kafka with which you can use this MSK configuration. You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            
            cfn_configuration_props = msk.CfnConfigurationProps(
                name="name",
                server_properties="serverProperties",
            
                # the properties below are optional
                description="description",
                kafka_versions_list=["kafkaVersionsList"]
            )
        '''
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                server_properties: builtins.str,
                description: typing.Optional[builtins.str] = None,
                kafka_versions_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument server_properties", value=server_properties, expected_type=type_hints["server_properties"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kafka_versions_list", value=kafka_versions_list, expected_type=type_hints["kafka_versions_list"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "server_properties": server_properties,
        }
        if description is not None:
            self._values["description"] = description
        if kafka_versions_list is not None:
            self._values["kafka_versions_list"] = kafka_versions_list

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the configuration.

        Configuration names are strings that match the regex "^[0-9A-Za-z][0-9A-Za-z-]{0,}$".

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_properties(self) -> builtins.str:
        '''Contents of the server.properties file. When using the API, you must ensure that the contents of the file are base64 encoded. When using the console, the SDK, or the CLI, the contents of server.properties can be in plaintext.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-serverproperties
        '''
        result = self._values.get("server_properties")
        assert result is not None, "Required property 'server_properties' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the configuration.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka_versions_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of the versions of Apache Kafka with which you can use this MSK configuration.

        You can use this configuration for an MSK cluster only if the Apache Kafka version specified for the cluster appears in this list.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-configuration.html#cfn-msk-configuration-kafkaversionslist
        '''
        result = self._values.get("kafka_versions_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.core.IInspectable)
class CfnServerlessCluster(
    aws_cdk.core.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-msk.CfnServerlessCluster",
):
    '''A CloudFormation ``AWS::MSK::ServerlessCluster``.

    The ``AWS::MSK::ServerlessCluster`` resource creates an Amazon MSK Serverless cluster. For more information, see `MSK Serverless <https://docs.aws.amazon.com/msk/latest/developerguide/serverless.html>`_ in the *Amazon MSK Developer Guide*

    :cloudformationResource: AWS::MSK::ServerlessCluster
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_msk as msk
        
        cfn_serverless_cluster = msk.CfnServerlessCluster(self, "MyCfnServerlessCluster",
            client_authentication=msk.CfnServerlessCluster.ClientAuthenticationProperty(
                sasl=msk.CfnServerlessCluster.SaslProperty(
                    iam=msk.CfnServerlessCluster.IamProperty(
                        enabled=False
                    )
                )
            ),
            cluster_name="clusterName",
            vpc_configs=[msk.CfnServerlessCluster.VpcConfigProperty(
                subnet_ids=["subnetIds"],
        
                # the properties below are optional
                security_groups=["securityGroups"]
            )],
        
            # the properties below are optional
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: aws_cdk.core.Construct,
        id: builtins.str,
        *,
        client_authentication: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnServerlessCluster.ClientAuthenticationProperty", typing.Dict[str, typing.Any]]],
        cluster_name: builtins.str,
        vpc_configs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnServerlessCluster.VpcConfigProperty", typing.Dict[str, typing.Any]]]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::MSK::ServerlessCluster``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param client_authentication: Specifies client authentication information for the serverless cluster.
        :param cluster_name: The name of the serverless cluster.
        :param vpc_configs: VPC configuration information.
        :param tags: A map of key:value pairs to apply to this serverless cluster.
        '''
        if __debug__:
            def stub(
                scope: aws_cdk.core.Construct,
                id: builtins.str,
                *,
                client_authentication: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.ClientAuthenticationProperty, typing.Dict[str, typing.Any]]],
                cluster_name: builtins.str,
                vpc_configs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.VpcConfigProperty, typing.Dict[str, typing.Any]]]]],
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerlessClusterProps(
            client_authentication=client_authentication,
            cluster_name=cluster_name,
            vpc_configs=vpc_configs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: aws_cdk.core.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            def stub(inspector: aws_cdk.core.TreeInspector) -> None:
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN of the serverless cluster.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> aws_cdk.core.TagManager:
        '''A map of key:value pairs to apply to this serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-tags
        '''
        return typing.cast(aws_cdk.core.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="clientAuthentication")
    def client_authentication(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.ClientAuthenticationProperty"]:
        '''Specifies client authentication information for the serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clientauthentication
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.ClientAuthenticationProperty"], jsii.get(self, "clientAuthentication"))

    @client_authentication.setter
    def client_authentication(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.ClientAuthenticationProperty"],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, CfnServerlessCluster.ClientAuthenticationProperty],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''The name of the serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clustername
        '''
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
    @jsii.member(jsii_name="vpcConfigs")
    def vpc_configs(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.VpcConfigProperty"]]]:
        '''VPC configuration information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-vpcconfigs
        '''
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.VpcConfigProperty"]]], jsii.get(self, "vpcConfigs"))

    @vpc_configs.setter
    def vpc_configs(
        self,
        value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.VpcConfigProperty"]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnServerlessCluster.VpcConfigProperty]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfigs", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnServerlessCluster.ClientAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={"sasl": "sasl"},
    )
    class ClientAuthenticationProperty:
        def __init__(
            self,
            *,
            sasl: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnServerlessCluster.SaslProperty", typing.Dict[str, typing.Any]]],
        ) -> None:
            '''Includes all client authentication information.

            :param sasl: Details for client authentication using SASL. To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                client_authentication_property = msk.CfnServerlessCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnServerlessCluster.SaslProperty(
                        iam=msk.CfnServerlessCluster.IamProperty(
                            enabled=False
                        )
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    sasl: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.SaslProperty, typing.Dict[str, typing.Any]]],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument sasl", value=sasl, expected_type=type_hints["sasl"])
            self._values: typing.Dict[str, typing.Any] = {
                "sasl": sasl,
            }

        @builtins.property
        def sasl(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.SaslProperty"]:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-clientauthentication.html#cfn-msk-serverlesscluster-clientauthentication-sasl
            '''
            result = self._values.get("sasl")
            assert result is not None, "Required property 'sasl' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.SaslProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClientAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnServerlessCluster.IamProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class IamProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
        ) -> None:
            '''Details for IAM client authentication.

            :param enabled: SASL/IAM authentication is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                iam_property = msk.CfnServerlessCluster.IamProperty(
                    enabled=False
                )
            '''
            if __debug__:
                def stub(
                    *,
                    enabled: typing.Union[builtins.bool, aws_cdk.core.IResolvable],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, aws_cdk.core.IResolvable]:
            '''SASL/IAM authentication is enabled or not.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-iam.html#cfn-msk-serverlesscluster-iam-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, aws_cdk.core.IResolvable], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnServerlessCluster.SaslProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam"},
    )
    class SaslProperty:
        def __init__(
            self,
            *,
            iam: typing.Union[aws_cdk.core.IResolvable, typing.Union["CfnServerlessCluster.IamProperty", typing.Dict[str, typing.Any]]],
        ) -> None:
            '''Details for client authentication using SASL.

            To turn on SASL, you must also turn on ``EncryptionInTransit`` by setting ``inCluster`` to true. You must set ``clientBroker`` to either ``TLS`` or ``TLS_PLAINTEXT`` . If you choose ``TLS_PLAINTEXT`` , then you must also set ``unauthenticated`` to true.

            :param iam: Details for client authentication using IAM.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                sasl_property = msk.CfnServerlessCluster.SaslProperty(
                    iam=msk.CfnServerlessCluster.IamProperty(
                        enabled=False
                    )
                )
            '''
            if __debug__:
                def stub(
                    *,
                    iam: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.IamProperty, typing.Dict[str, typing.Any]]],
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            self._values: typing.Dict[str, typing.Any] = {
                "iam": iam,
            }

        @builtins.property
        def iam(
            self,
        ) -> typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.IamProperty"]:
            '''Details for client authentication using IAM.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-sasl.html#cfn-msk-serverlesscluster-sasl-iam
            '''
            result = self._values.get("iam")
            assert result is not None, "Required property 'iam' is missing"
            return typing.cast(typing.Union[aws_cdk.core.IResolvable, "CfnServerlessCluster.IamProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SaslProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-msk.CfnServerlessCluster.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_ids": "subnetIds", "security_groups": "securityGroups"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            subnet_ids: typing.Sequence[builtins.str],
            security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies information about subnets and security groups for the VPC that your clients will use to connect with the serverless cluster.

            :param subnet_ids: A list of subnets in at least two different Availability Zones that host your client applications. We recommend that you specify a backup subnet in a different Availability Zone for failover in case of an outage.
            :param security_groups: Specifies up to five security groups that control inbound and outbound traffic for the serverless cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_msk as msk
                
                vpc_config_property = msk.CfnServerlessCluster.VpcConfigProperty(
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    security_groups=["securityGroups"]
                )
            '''
            if __debug__:
                def stub(
                    *,
                    subnet_ids: typing.Sequence[builtins.str],
                    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
                ) -> None:
                    ...
                type_hints = typing.get_type_hints(stub)
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            self._values: typing.Dict[str, typing.Any] = {
                "subnet_ids": subnet_ids,
            }
            if security_groups is not None:
                self._values["security_groups"] = security_groups

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of subnets in at least two different Availability Zones that host your client applications.

            We recommend that you specify a backup subnet in a different Availability Zone for failover in case of an outage.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html#cfn-msk-serverlesscluster-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies up to five security groups that control inbound and outbound traffic for the serverless cluster.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-msk-serverlesscluster-vpcconfig.html#cfn-msk-serverlesscluster-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.CfnServerlessClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "client_authentication": "clientAuthentication",
        "cluster_name": "clusterName",
        "vpc_configs": "vpcConfigs",
        "tags": "tags",
    },
)
class CfnServerlessClusterProps:
    def __init__(
        self,
        *,
        client_authentication: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.ClientAuthenticationProperty, typing.Dict[str, typing.Any]]],
        cluster_name: builtins.str,
        vpc_configs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.VpcConfigProperty, typing.Dict[str, typing.Any]]]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServerlessCluster``.

        :param client_authentication: Specifies client authentication information for the serverless cluster.
        :param cluster_name: The name of the serverless cluster.
        :param vpc_configs: VPC configuration information.
        :param tags: A map of key:value pairs to apply to this serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            
            cfn_serverless_cluster_props = msk.CfnServerlessClusterProps(
                client_authentication=msk.CfnServerlessCluster.ClientAuthenticationProperty(
                    sasl=msk.CfnServerlessCluster.SaslProperty(
                        iam=msk.CfnServerlessCluster.IamProperty(
                            enabled=False
                        )
                    )
                ),
                cluster_name="clusterName",
                vpc_configs=[msk.CfnServerlessCluster.VpcConfigProperty(
                    subnet_ids=["subnetIds"],
            
                    # the properties below are optional
                    security_groups=["securityGroups"]
                )],
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            def stub(
                *,
                client_authentication: typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.ClientAuthenticationProperty, typing.Dict[str, typing.Any]]],
                cluster_name: builtins.str,
                vpc_configs: typing.Union[aws_cdk.core.IResolvable, typing.Sequence[typing.Union[aws_cdk.core.IResolvable, typing.Union[CfnServerlessCluster.VpcConfigProperty, typing.Dict[str, typing.Any]]]]],
                tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument vpc_configs", value=vpc_configs, expected_type=type_hints["vpc_configs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_authentication": client_authentication,
            "cluster_name": cluster_name,
            "vpc_configs": vpc_configs,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def client_authentication(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, CfnServerlessCluster.ClientAuthenticationProperty]:
        '''Specifies client authentication information for the serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clientauthentication
        '''
        result = self._values.get("client_authentication")
        assert result is not None, "Required property 'client_authentication' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, CfnServerlessCluster.ClientAuthenticationProperty], result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-clustername
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_configs(
        self,
    ) -> typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnServerlessCluster.VpcConfigProperty]]]:
        '''VPC configuration information.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-vpcconfigs
        '''
        result = self._values.get("vpc_configs")
        assert result is not None, "Required property 'vpc_configs' is missing"
        return typing.cast(typing.Union[aws_cdk.core.IResolvable, typing.List[typing.Union[aws_cdk.core.IResolvable, CfnServerlessCluster.VpcConfigProperty]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key:value pairs to apply to this serverless cluster.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-serverlesscluster.html#cfn-msk-serverlesscluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerlessClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ClientAuthentication(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-msk.ClientAuthentication",
):
    '''(experimental) Configuration properties for client authentication.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        cluster = msk.Cluster(self, "cluster",
            cluster_name="myCluster",
            kafka_version=msk.KafkaVersion.V2_8_1,
            vpc=vpc,
            encryption_in_transit=msk.EncryptionInTransitConfig(
                client_broker=msk.ClientBrokerEncryption.TLS
            ),
            client_authentication=msk.ClientAuthentication.sasl(
                scram=True
            )
        )
    '''

    @jsii.member(jsii_name="sasl")
    @builtins.classmethod
    def sasl(
        cls,
        *,
        iam: typing.Optional[builtins.bool] = None,
        key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        scram: typing.Optional[builtins.bool] = None,
    ) -> "ClientAuthentication":
        '''(experimental) SASL authentication.

        :param iam: (experimental) Enable IAM access control. Default: false
        :param key: (experimental) KMS Key to encrypt SASL/SCRAM secrets. You must use a customer master key (CMK) when creating users in secrets manager. You cannot use a Secret with Amazon MSK that uses the default Secrets Manager encryption key. Default: - CMK will be created with alias msk/{clusterName}/sasl/scram
        :param scram: (experimental) Enable SASL/SCRAM authentication. Default: false

        :stability: experimental
        '''
        props = SaslAuthProps(iam=iam, key=key, scram=scram)

        return typing.cast("ClientAuthentication", jsii.sinvoke(cls, "sasl", [props]))

    @jsii.member(jsii_name="tls")
    @builtins.classmethod
    def tls(
        cls,
        *,
        certificate_authorities: typing.Optional[typing.Sequence[aws_cdk.aws_acmpca.ICertificateAuthority]] = None,
    ) -> "ClientAuthentication":
        '''(experimental) TLS authentication.

        :param certificate_authorities: (experimental) List of ACM Certificate Authorities to enable TLS authentication. Default: - none

        :stability: experimental
        '''
        props = TlsAuthProps(certificate_authorities=certificate_authorities)

        return typing.cast("ClientAuthentication", jsii.sinvoke(cls, "tls", [props]))

    @builtins.property
    @jsii.member(jsii_name="saslProps")
    def sasl_props(self) -> typing.Optional["SaslAuthProps"]:
        '''(experimental) - properties for SASL authentication.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["SaslAuthProps"], jsii.get(self, "saslProps"))

    @builtins.property
    @jsii.member(jsii_name="tlsProps")
    def tls_props(self) -> typing.Optional["TlsAuthProps"]:
        '''(experimental) - properties for TLS authentication.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["TlsAuthProps"], jsii.get(self, "tlsProps"))


@jsii.enum(jsii_type="@aws-cdk/aws-msk.ClientBrokerEncryption")
class ClientBrokerEncryption(enum.Enum):
    '''(experimental) Indicates the encryption setting for data in transit between clients and brokers.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        cluster = msk.Cluster(self, "cluster",
            cluster_name="myCluster",
            kafka_version=msk.KafkaVersion.V2_8_1,
            vpc=vpc,
            encryption_in_transit=msk.EncryptionInTransitConfig(
                client_broker=msk.ClientBrokerEncryption.TLS
            ),
            client_authentication=msk.ClientAuthentication.sasl(
                scram=True
            )
        )
    '''

    TLS = "TLS"
    '''(experimental) TLS means that client-broker communication is enabled with TLS only.

    :stability: experimental
    '''
    TLS_PLAINTEXT = "TLS_PLAINTEXT"
    '''(experimental) TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.

    :stability: experimental
    '''
    PLAINTEXT = "PLAINTEXT"
    '''(experimental) PLAINTEXT means that client-broker communication is enabled in plaintext only.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.ClusterConfigurationInfo",
    jsii_struct_bases=[],
    name_mapping={"arn": "arn", "revision": "revision"},
)
class ClusterConfigurationInfo:
    def __init__(self, *, arn: builtins.str, revision: jsii.Number) -> None:
        '''(experimental) The Amazon MSK configuration to use for the cluster.

        Note: There is currently no Cloudformation Resource to create a Configuration

        :param arn: (experimental) The Amazon Resource Name (ARN) of the MSK configuration to use. For example, arn:aws:kafka:us-east-1:123456789012:configuration/example-configuration-name/abcdabcd-1234-abcd-1234-abcd123e8e8e-1.
        :param revision: (experimental) The revision of the Amazon MSK configuration to use.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            
            cluster_configuration_info = msk.ClusterConfigurationInfo(
                arn="arn",
                revision=123
            )
        '''
        if __debug__:
            def stub(*, arn: builtins.str, revision: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
        self._values: typing.Dict[str, typing.Any] = {
            "arn": arn,
            "revision": revision,
        }

    @builtins.property
    def arn(self) -> builtins.str:
        '''(experimental) The Amazon Resource Name (ARN) of the MSK configuration to use.

        For example, arn:aws:kafka:us-east-1:123456789012:configuration/example-configuration-name/abcdabcd-1234-abcd-1234-abcd123e8e8e-1.

        :stability: experimental
        '''
        result = self._values.get("arn")
        assert result is not None, "Required property 'arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision(self) -> jsii.Number:
        '''(experimental) The revision of the Amazon MSK configuration to use.

        :stability: experimental
        '''
        result = self._values.get("revision")
        assert result is not None, "Required property 'revision' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterConfigurationInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-msk.ClusterMonitoringLevel")
class ClusterMonitoringLevel(enum.Enum):
    '''(experimental) The level of monitoring for the MSK cluster.

    :see: https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html#metrics-details
    :stability: experimental
    '''

    DEFAULT = "DEFAULT"
    '''(experimental) Default metrics are the essential metrics to monitor.

    :stability: experimental
    '''
    PER_BROKER = "PER_BROKER"
    '''(experimental) Per Broker metrics give you metrics at the broker level.

    :stability: experimental
    '''
    PER_TOPIC_PER_BROKER = "PER_TOPIC_PER_BROKER"
    '''(experimental) Per Topic Per Broker metrics help you understand volume at the topic level.

    :stability: experimental
    '''
    PER_TOPIC_PER_PARTITION = "PER_TOPIC_PER_PARTITION"
    '''(experimental) Per Topic Per Partition metrics help you understand consumer group lag at the topic partition level.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.ClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "kafka_version": "kafkaVersion",
        "vpc": "vpc",
        "client_authentication": "clientAuthentication",
        "configuration_info": "configurationInfo",
        "ebs_storage_info": "ebsStorageInfo",
        "encryption_in_transit": "encryptionInTransit",
        "instance_type": "instanceType",
        "logging": "logging",
        "monitoring": "monitoring",
        "number_of_broker_nodes": "numberOfBrokerNodes",
        "removal_policy": "removalPolicy",
        "security_groups": "securityGroups",
        "vpc_subnets": "vpcSubnets",
    },
)
class ClusterProps:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        kafka_version: "KafkaVersion",
        vpc: aws_cdk.aws_ec2.IVpc,
        client_authentication: typing.Optional[ClientAuthentication] = None,
        configuration_info: typing.Optional[typing.Union[ClusterConfigurationInfo, typing.Dict[str, typing.Any]]] = None,
        ebs_storage_info: typing.Optional[typing.Union["EbsStorageInfo", typing.Dict[str, typing.Any]]] = None,
        encryption_in_transit: typing.Optional[typing.Union["EncryptionInTransitConfig", typing.Dict[str, typing.Any]]] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        logging: typing.Optional[typing.Union[BrokerLogging, typing.Dict[str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union["MonitoringConfiguration", typing.Dict[str, typing.Any]]] = None,
        number_of_broker_nodes: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for a MSK Cluster.

        :param cluster_name: (experimental) The physical name of the cluster.
        :param kafka_version: (experimental) The version of Apache Kafka.
        :param vpc: (experimental) Defines the virtual networking environment for this cluster. Must have at least 2 subnets in two different AZs.
        :param client_authentication: (experimental) Configuration properties for client authentication. MSK supports using private TLS certificates or SASL/SCRAM to authenticate the identity of clients. Default: - disabled
        :param configuration_info: (experimental) The Amazon MSK configuration to use for the cluster. Default: - none
        :param ebs_storage_info: (experimental) Information about storage volumes attached to MSK broker nodes. Default: - 1000 GiB EBS volume
        :param encryption_in_transit: (experimental) Config details for encryption in transit. Default: - enabled
        :param instance_type: (experimental) The EC2 instance type that you want Amazon MSK to use when it creates your brokers. Default: kafka.m5.large
        :param logging: (experimental) Configure your MSK cluster to send broker logs to different destination types. Default: - disabled
        :param monitoring: (experimental) Cluster monitoring configuration. Default: - DEFAULT monitoring level
        :param number_of_broker_nodes: (experimental) Number of Apache Kafka brokers deployed in each Availability Zone. Default: 1
        :param removal_policy: (experimental) What to do when this resource is deleted from a stack. Default: RemovalPolicy.RETAIN
        :param security_groups: (experimental) The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. Default: - create new security group
        :param vpc_subnets: (experimental) Where to place the nodes within the VPC. Amazon MSK distributes the broker nodes evenly across the subnets that you specify. The subnets that you specify must be in distinct Availability Zones. Client subnets can't be in Availability Zone us-east-1e. Default: - the Vpc default strategy if not specified.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # vpc: ec2.Vpc
            
            cluster = msk.Cluster(self, "cluster",
                cluster_name="myCluster",
                kafka_version=msk.KafkaVersion.V2_8_1,
                vpc=vpc,
                encryption_in_transit=msk.EncryptionInTransitConfig(
                    client_broker=msk.ClientBrokerEncryption.TLS
                ),
                client_authentication=msk.ClientAuthentication.sasl(
                    scram=True
                )
            )
        '''
        if isinstance(configuration_info, dict):
            configuration_info = ClusterConfigurationInfo(**configuration_info)
        if isinstance(ebs_storage_info, dict):
            ebs_storage_info = EbsStorageInfo(**ebs_storage_info)
        if isinstance(encryption_in_transit, dict):
            encryption_in_transit = EncryptionInTransitConfig(**encryption_in_transit)
        if isinstance(logging, dict):
            logging = BrokerLogging(**logging)
        if isinstance(monitoring, dict):
            monitoring = MonitoringConfiguration(**monitoring)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                cluster_name: builtins.str,
                kafka_version: KafkaVersion,
                vpc: aws_cdk.aws_ec2.IVpc,
                client_authentication: typing.Optional[ClientAuthentication] = None,
                configuration_info: typing.Optional[typing.Union[ClusterConfigurationInfo, typing.Dict[str, typing.Any]]] = None,
                ebs_storage_info: typing.Optional[typing.Union[EbsStorageInfo, typing.Dict[str, typing.Any]]] = None,
                encryption_in_transit: typing.Optional[typing.Union[EncryptionInTransitConfig, typing.Dict[str, typing.Any]]] = None,
                instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
                logging: typing.Optional[typing.Union[BrokerLogging, typing.Dict[str, typing.Any]]] = None,
                monitoring: typing.Optional[typing.Union[MonitoringConfiguration, typing.Dict[str, typing.Any]]] = None,
                number_of_broker_nodes: typing.Optional[jsii.Number] = None,
                removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument kafka_version", value=kafka_version, expected_type=type_hints["kafka_version"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument client_authentication", value=client_authentication, expected_type=type_hints["client_authentication"])
            check_type(argname="argument configuration_info", value=configuration_info, expected_type=type_hints["configuration_info"])
            check_type(argname="argument ebs_storage_info", value=ebs_storage_info, expected_type=type_hints["ebs_storage_info"])
            check_type(argname="argument encryption_in_transit", value=encryption_in_transit, expected_type=type_hints["encryption_in_transit"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument monitoring", value=monitoring, expected_type=type_hints["monitoring"])
            check_type(argname="argument number_of_broker_nodes", value=number_of_broker_nodes, expected_type=type_hints["number_of_broker_nodes"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
            "kafka_version": kafka_version,
            "vpc": vpc,
        }
        if client_authentication is not None:
            self._values["client_authentication"] = client_authentication
        if configuration_info is not None:
            self._values["configuration_info"] = configuration_info
        if ebs_storage_info is not None:
            self._values["ebs_storage_info"] = ebs_storage_info
        if encryption_in_transit is not None:
            self._values["encryption_in_transit"] = encryption_in_transit
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if logging is not None:
            self._values["logging"] = logging
        if monitoring is not None:
            self._values["monitoring"] = monitoring
        if number_of_broker_nodes is not None:
            self._values["number_of_broker_nodes"] = number_of_broker_nodes
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''(experimental) The physical name of the cluster.

        :stability: experimental
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kafka_version(self) -> "KafkaVersion":
        '''(experimental) The version of Apache Kafka.

        :stability: experimental
        '''
        result = self._values.get("kafka_version")
        assert result is not None, "Required property 'kafka_version' is missing"
        return typing.cast("KafkaVersion", result)

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) Defines the virtual networking environment for this cluster.

        Must have at least 2 subnets in two different AZs.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    @builtins.property
    def client_authentication(self) -> typing.Optional[ClientAuthentication]:
        '''(experimental) Configuration properties for client authentication.

        MSK supports using private TLS certificates or SASL/SCRAM to authenticate the identity of clients.

        :default: - disabled

        :stability: experimental
        '''
        result = self._values.get("client_authentication")
        return typing.cast(typing.Optional[ClientAuthentication], result)

    @builtins.property
    def configuration_info(self) -> typing.Optional[ClusterConfigurationInfo]:
        '''(experimental) The Amazon MSK configuration to use for the cluster.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("configuration_info")
        return typing.cast(typing.Optional[ClusterConfigurationInfo], result)

    @builtins.property
    def ebs_storage_info(self) -> typing.Optional["EbsStorageInfo"]:
        '''(experimental) Information about storage volumes attached to MSK broker nodes.

        :default: - 1000 GiB EBS volume

        :stability: experimental
        '''
        result = self._values.get("ebs_storage_info")
        return typing.cast(typing.Optional["EbsStorageInfo"], result)

    @builtins.property
    def encryption_in_transit(self) -> typing.Optional["EncryptionInTransitConfig"]:
        '''(experimental) Config details for encryption in transit.

        :default: - enabled

        :stability: experimental
        '''
        result = self._values.get("encryption_in_transit")
        return typing.cast(typing.Optional["EncryptionInTransitConfig"], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[aws_cdk.aws_ec2.InstanceType]:
        '''(experimental) The EC2 instance type that you want Amazon MSK to use when it creates your brokers.

        :default: kafka.m5.large

        :see: https://docs.aws.amazon.com/msk/latest/developerguide/msk-create-cluster.html#broker-instance-types
        :stability: experimental
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.InstanceType], result)

    @builtins.property
    def logging(self) -> typing.Optional[BrokerLogging]:
        '''(experimental) Configure your MSK cluster to send broker logs to different destination types.

        :default: - disabled

        :stability: experimental
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[BrokerLogging], result)

    @builtins.property
    def monitoring(self) -> typing.Optional["MonitoringConfiguration"]:
        '''(experimental) Cluster monitoring configuration.

        :default: - DEFAULT monitoring level

        :stability: experimental
        '''
        result = self._values.get("monitoring")
        return typing.cast(typing.Optional["MonitoringConfiguration"], result)

    @builtins.property
    def number_of_broker_nodes(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Number of Apache Kafka brokers deployed in each Availability Zone.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("number_of_broker_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.core.RemovalPolicy]:
        '''(experimental) What to do when this resource is deleted from a stack.

        :default: RemovalPolicy.RETAIN

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.core.RemovalPolicy], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster.

        :default: - create new security group

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the nodes within the VPC.

        Amazon MSK distributes the broker nodes evenly across the subnets that you specify.
        The subnets that you specify must be in distinct Availability Zones.
        Client subnets can't be in Availability Zone us-east-1e.

        :default: - the Vpc default strategy if not specified.

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.EbsStorageInfo",
    jsii_struct_bases=[],
    name_mapping={"encryption_key": "encryptionKey", "volume_size": "volumeSize"},
)
class EbsStorageInfo:
    def __init__(
        self,
        *,
        encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        volume_size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) EBS volume information.

        :param encryption_key: (experimental) The AWS KMS key for encrypting data at rest. Default: Uses AWS managed CMK (aws/kafka)
        :param volume_size: (experimental) The size in GiB of the EBS volume for the data drive on each broker node. Default: 1000

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_kms as kms
            import aws_cdk.aws_msk as msk
            
            # key: kms.Key
            
            ebs_storage_info = msk.EbsStorageInfo(
                encryption_key=key,
                volume_size=123
            )
        '''
        if __debug__:
            def stub(
                *,
                encryption_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                volume_size: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
        self._values: typing.Dict[str, typing.Any] = {}
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if volume_size is not None:
            self._values["volume_size"] = volume_size

    @builtins.property
    def encryption_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(experimental) The AWS KMS key for encrypting data at rest.

        :default: Uses AWS managed CMK (aws/kafka)

        :stability: experimental
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def volume_size(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The size in GiB of the EBS volume for the data drive on each broker node.

        :default: 1000

        :stability: experimental
        '''
        result = self._values.get("volume_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EbsStorageInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.EncryptionInTransitConfig",
    jsii_struct_bases=[],
    name_mapping={
        "client_broker": "clientBroker",
        "enable_in_cluster": "enableInCluster",
    },
)
class EncryptionInTransitConfig:
    def __init__(
        self,
        *,
        client_broker: typing.Optional[ClientBrokerEncryption] = None,
        enable_in_cluster: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) The settings for encrypting data in transit.

        :param client_broker: (experimental) Indicates the encryption setting for data in transit between clients and brokers. Default: - TLS
        :param enable_in_cluster: (experimental) Indicates that data communication among the broker nodes of the cluster is encrypted. Default: true

        :see: https://docs.aws.amazon.com/msk/latest/developerguide/msk-encryption.html#msk-encryption-in-transit
        :stability: experimental
        :exampleMetadata: infused

        Example::

            # vpc: ec2.Vpc
            
            cluster = msk.Cluster(self, "cluster",
                cluster_name="myCluster",
                kafka_version=msk.KafkaVersion.V2_8_1,
                vpc=vpc,
                encryption_in_transit=msk.EncryptionInTransitConfig(
                    client_broker=msk.ClientBrokerEncryption.TLS
                ),
                client_authentication=msk.ClientAuthentication.sasl(
                    scram=True
                )
            )
        '''
        if __debug__:
            def stub(
                *,
                client_broker: typing.Optional[ClientBrokerEncryption] = None,
                enable_in_cluster: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument client_broker", value=client_broker, expected_type=type_hints["client_broker"])
            check_type(argname="argument enable_in_cluster", value=enable_in_cluster, expected_type=type_hints["enable_in_cluster"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_broker is not None:
            self._values["client_broker"] = client_broker
        if enable_in_cluster is not None:
            self._values["enable_in_cluster"] = enable_in_cluster

    @builtins.property
    def client_broker(self) -> typing.Optional[ClientBrokerEncryption]:
        '''(experimental) Indicates the encryption setting for data in transit between clients and brokers.

        :default: - TLS

        :stability: experimental
        '''
        result = self._values.get("client_broker")
        return typing.cast(typing.Optional[ClientBrokerEncryption], result)

    @builtins.property
    def enable_in_cluster(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that data communication among the broker nodes of the cluster is encrypted.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("enable_in_cluster")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncryptionInTransitConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-msk.ICluster")
class ICluster(
    aws_cdk.core.IResource,
    aws_cdk.aws_ec2.IConnectable,
    typing_extensions.Protocol,
):
    '''(experimental) Represents a MSK Cluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''(experimental) The ARN of cluster.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''(experimental) The physical name of the cluster.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IClusterProxy(
    jsii.proxy_for(aws_cdk.core.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
):
    '''(experimental) Represents a MSK Cluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-msk.ICluster"

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''(experimental) The ARN of cluster.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''(experimental) The physical name of the cluster.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICluster).__jsii_proxy_class__ = lambda : _IClusterProxy


class KafkaVersion(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-msk.KafkaVersion"):
    '''(experimental) Kafka cluster version.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        cluster = msk.Cluster(self, "cluster",
            cluster_name="myCluster",
            kafka_version=msk.KafkaVersion.V2_8_1,
            vpc=vpc,
            encryption_in_transit=msk.EncryptionInTransitConfig(
                client_broker=msk.ClientBrokerEncryption.TLS
            ),
            client_authentication=msk.ClientAuthentication.sasl(
                scram=True
            )
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, version: builtins.str) -> "KafkaVersion":
        '''(experimental) Custom cluster version.

        :param version: custom version number.

        :stability: experimental
        '''
        if __debug__:
            def stub(version: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        return typing.cast("KafkaVersion", jsii.sinvoke(cls, "of", [version]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_1_1")
    def V1_1_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 1.1.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V1_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_2_1")
    def V2_2_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.2.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_2_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_3_1")
    def V2_3_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.3.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_3_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_4_1_1")
    def V2_4_1_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.4.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_4_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_5_1")
    def V2_5_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.5.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_5_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_0")
    def V2_6_0(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.6.0.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_6_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_1")
    def V2_6_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.6.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_6_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_2")
    def V2_6_2(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.6.2.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_6_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_6_3")
    def V2_6_3(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.6.3.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_6_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_7_0")
    def V2_7_0(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.7.0.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_7_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_7_1")
    def V2_7_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.7.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_7_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_7_2")
    def V2_7_2(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.7.2.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_7_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_8_0")
    def V2_8_0(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.8.0.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_8_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V2_8_1")
    def V2_8_1(cls) -> "KafkaVersion":
        '''(experimental) Kafka version 2.8.1.

        :stability: experimental
        '''
        return typing.cast("KafkaVersion", jsii.sget(cls, "V2_8_1"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) cluster version number.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.MonitoringConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_monitoring_level": "clusterMonitoringLevel",
        "enable_prometheus_jmx_exporter": "enablePrometheusJmxExporter",
        "enable_prometheus_node_exporter": "enablePrometheusNodeExporter",
    },
)
class MonitoringConfiguration:
    def __init__(
        self,
        *,
        cluster_monitoring_level: typing.Optional[ClusterMonitoringLevel] = None,
        enable_prometheus_jmx_exporter: typing.Optional[builtins.bool] = None,
        enable_prometheus_node_exporter: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Monitoring Configuration.

        :param cluster_monitoring_level: (experimental) Specifies the level of monitoring for the MSK cluster. Default: DEFAULT
        :param enable_prometheus_jmx_exporter: (experimental) Indicates whether you want to enable or disable the JMX Exporter. Default: false
        :param enable_prometheus_node_exporter: (experimental) Indicates whether you want to enable or disable the Prometheus Node Exporter. You can use the Prometheus Node Exporter to get CPU and disk metrics for the broker nodes. Default: false

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            
            monitoring_configuration = msk.MonitoringConfiguration(
                cluster_monitoring_level=msk.ClusterMonitoringLevel.DEFAULT,
                enable_prometheus_jmx_exporter=False,
                enable_prometheus_node_exporter=False
            )
        '''
        if __debug__:
            def stub(
                *,
                cluster_monitoring_level: typing.Optional[ClusterMonitoringLevel] = None,
                enable_prometheus_jmx_exporter: typing.Optional[builtins.bool] = None,
                enable_prometheus_node_exporter: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster_monitoring_level", value=cluster_monitoring_level, expected_type=type_hints["cluster_monitoring_level"])
            check_type(argname="argument enable_prometheus_jmx_exporter", value=enable_prometheus_jmx_exporter, expected_type=type_hints["enable_prometheus_jmx_exporter"])
            check_type(argname="argument enable_prometheus_node_exporter", value=enable_prometheus_node_exporter, expected_type=type_hints["enable_prometheus_node_exporter"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_monitoring_level is not None:
            self._values["cluster_monitoring_level"] = cluster_monitoring_level
        if enable_prometheus_jmx_exporter is not None:
            self._values["enable_prometheus_jmx_exporter"] = enable_prometheus_jmx_exporter
        if enable_prometheus_node_exporter is not None:
            self._values["enable_prometheus_node_exporter"] = enable_prometheus_node_exporter

    @builtins.property
    def cluster_monitoring_level(self) -> typing.Optional[ClusterMonitoringLevel]:
        '''(experimental) Specifies the level of monitoring for the MSK cluster.

        :default: DEFAULT

        :stability: experimental
        '''
        result = self._values.get("cluster_monitoring_level")
        return typing.cast(typing.Optional[ClusterMonitoringLevel], result)

    @builtins.property
    def enable_prometheus_jmx_exporter(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether you want to enable or disable the JMX Exporter.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("enable_prometheus_jmx_exporter")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def enable_prometheus_node_exporter(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether you want to enable or disable the Prometheus Node Exporter.

        You can use the Prometheus Node Exporter to get CPU and disk metrics for the broker nodes.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("enable_prometheus_node_exporter")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitoringConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.S3LoggingConfiguration",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "prefix": "prefix"},
)
class S3LoggingConfiguration:
    def __init__(
        self,
        *,
        bucket: aws_cdk.aws_s3.IBucket,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Details of the Amazon S3 destination for broker logs.

        :param bucket: (experimental) The S3 bucket that is the destination for broker logs.
        :param prefix: (experimental) The S3 prefix that is the destination for broker logs. Default: - no prefix

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_msk as msk
            import aws_cdk.aws_s3 as s3
            
            # bucket: s3.Bucket
            
            s3_logging_configuration = msk.S3LoggingConfiguration(
                bucket=bucket,
            
                # the properties below are optional
                prefix="prefix"
            )
        '''
        if __debug__:
            def stub(
                *,
                bucket: aws_cdk.aws_s3.IBucket,
                prefix: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket": bucket,
        }
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> aws_cdk.aws_s3.IBucket:
        '''(experimental) The S3 bucket that is the destination for broker logs.

        :stability: experimental
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(aws_cdk.aws_s3.IBucket, result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''(experimental) The S3 prefix that is the destination for broker logs.

        :default: - no prefix

        :stability: experimental
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3LoggingConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.SaslAuthProps",
    jsii_struct_bases=[],
    name_mapping={"iam": "iam", "key": "key", "scram": "scram"},
)
class SaslAuthProps:
    def __init__(
        self,
        *,
        iam: typing.Optional[builtins.bool] = None,
        key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        scram: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) SASL authentication properties.

        :param iam: (experimental) Enable IAM access control. Default: false
        :param key: (experimental) KMS Key to encrypt SASL/SCRAM secrets. You must use a customer master key (CMK) when creating users in secrets manager. You cannot use a Secret with Amazon MSK that uses the default Secrets Manager encryption key. Default: - CMK will be created with alias msk/{clusterName}/sasl/scram
        :param scram: (experimental) Enable SASL/SCRAM authentication. Default: false

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # vpc: ec2.Vpc
            
            cluster = msk.Cluster(self, "cluster",
                cluster_name="myCluster",
                kafka_version=msk.KafkaVersion.V2_8_1,
                vpc=vpc,
                encryption_in_transit=msk.EncryptionInTransitConfig(
                    client_broker=msk.ClientBrokerEncryption.TLS
                ),
                client_authentication=msk.ClientAuthentication.sasl(
                    scram=True
                )
            )
        '''
        if __debug__:
            def stub(
                *,
                iam: typing.Optional[builtins.bool] = None,
                key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                scram: typing.Optional[builtins.bool] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scram", value=scram, expected_type=type_hints["scram"])
        self._values: typing.Dict[str, typing.Any] = {}
        if iam is not None:
            self._values["iam"] = iam
        if key is not None:
            self._values["key"] = key
        if scram is not None:
            self._values["scram"] = scram

    @builtins.property
    def iam(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable IAM access control.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("iam")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(experimental) KMS Key to encrypt SASL/SCRAM secrets.

        You must use a customer master key (CMK) when creating users in secrets manager.
        You cannot use a Secret with Amazon MSK that uses the default Secrets Manager encryption key.

        :default: - CMK will be created with alias msk/{clusterName}/sasl/scram

        :stability: experimental
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def scram(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Enable SASL/SCRAM authentication.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("scram")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SaslAuthProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-msk.TlsAuthProps",
    jsii_struct_bases=[],
    name_mapping={"certificate_authorities": "certificateAuthorities"},
)
class TlsAuthProps:
    def __init__(
        self,
        *,
        certificate_authorities: typing.Optional[typing.Sequence[aws_cdk.aws_acmpca.ICertificateAuthority]] = None,
    ) -> None:
        '''(experimental) TLS authentication properties.

        :param certificate_authorities: (experimental) List of ACM Certificate Authorities to enable TLS authentication. Default: - none

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_acmpca as acmpca
            
            # vpc: ec2.Vpc
            
            cluster = msk.Cluster(self, "Cluster",
                cluster_name="myCluster",
                kafka_version=msk.KafkaVersion.V2_8_1,
                vpc=vpc,
                encryption_in_transit=msk.EncryptionInTransitConfig(
                    client_broker=msk.ClientBrokerEncryption.TLS
                ),
                client_authentication=msk.ClientAuthentication.tls(
                    certificate_authorities=[
                        acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CertificateAuthority", "arn:aws:acm-pca:us-west-2:1234567890:certificate-authority/11111111-1111-1111-1111-111111111111")
                    ]
                )
            )
        '''
        if __debug__:
            def stub(
                *,
                certificate_authorities: typing.Optional[typing.Sequence[aws_cdk.aws_acmpca.ICertificateAuthority]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument certificate_authorities", value=certificate_authorities, expected_type=type_hints["certificate_authorities"])
        self._values: typing.Dict[str, typing.Any] = {}
        if certificate_authorities is not None:
            self._values["certificate_authorities"] = certificate_authorities

    @builtins.property
    def certificate_authorities(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_acmpca.ICertificateAuthority]]:
        '''(experimental) List of ACM Certificate Authorities to enable TLS authentication.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("certificate_authorities")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_acmpca.ICertificateAuthority]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TlsAuthProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ICluster)
class Cluster(
    aws_cdk.core.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-msk.Cluster",
):
    '''(experimental) Create a MSK Cluster.

    :stability: experimental
    :resource: AWS::MSK::Cluster
    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        cluster = msk.Cluster(self, "cluster",
            cluster_name="myCluster",
            kafka_version=msk.KafkaVersion.V2_8_1,
            vpc=vpc,
            encryption_in_transit=msk.EncryptionInTransitConfig(
                client_broker=msk.ClientBrokerEncryption.TLS
            ),
            client_authentication=msk.ClientAuthentication.sasl(
                scram=True
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_name: builtins.str,
        kafka_version: KafkaVersion,
        vpc: aws_cdk.aws_ec2.IVpc,
        client_authentication: typing.Optional[ClientAuthentication] = None,
        configuration_info: typing.Optional[typing.Union[ClusterConfigurationInfo, typing.Dict[str, typing.Any]]] = None,
        ebs_storage_info: typing.Optional[typing.Union[EbsStorageInfo, typing.Dict[str, typing.Any]]] = None,
        encryption_in_transit: typing.Optional[typing.Union[EncryptionInTransitConfig, typing.Dict[str, typing.Any]]] = None,
        instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
        logging: typing.Optional[typing.Union[BrokerLogging, typing.Dict[str, typing.Any]]] = None,
        monitoring: typing.Optional[typing.Union[MonitoringConfiguration, typing.Dict[str, typing.Any]]] = None,
        number_of_broker_nodes: typing.Optional[jsii.Number] = None,
        removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster_name: (experimental) The physical name of the cluster.
        :param kafka_version: (experimental) The version of Apache Kafka.
        :param vpc: (experimental) Defines the virtual networking environment for this cluster. Must have at least 2 subnets in two different AZs.
        :param client_authentication: (experimental) Configuration properties for client authentication. MSK supports using private TLS certificates or SASL/SCRAM to authenticate the identity of clients. Default: - disabled
        :param configuration_info: (experimental) The Amazon MSK configuration to use for the cluster. Default: - none
        :param ebs_storage_info: (experimental) Information about storage volumes attached to MSK broker nodes. Default: - 1000 GiB EBS volume
        :param encryption_in_transit: (experimental) Config details for encryption in transit. Default: - enabled
        :param instance_type: (experimental) The EC2 instance type that you want Amazon MSK to use when it creates your brokers. Default: kafka.m5.large
        :param logging: (experimental) Configure your MSK cluster to send broker logs to different destination types. Default: - disabled
        :param monitoring: (experimental) Cluster monitoring configuration. Default: - DEFAULT monitoring level
        :param number_of_broker_nodes: (experimental) Number of Apache Kafka brokers deployed in each Availability Zone. Default: 1
        :param removal_policy: (experimental) What to do when this resource is deleted from a stack. Default: RemovalPolicy.RETAIN
        :param security_groups: (experimental) The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. Default: - create new security group
        :param vpc_subnets: (experimental) Where to place the nodes within the VPC. Amazon MSK distributes the broker nodes evenly across the subnets that you specify. The subnets that you specify must be in distinct Availability Zones. Client subnets can't be in Availability Zone us-east-1e. Default: - the Vpc default strategy if not specified.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                cluster_name: builtins.str,
                kafka_version: KafkaVersion,
                vpc: aws_cdk.aws_ec2.IVpc,
                client_authentication: typing.Optional[ClientAuthentication] = None,
                configuration_info: typing.Optional[typing.Union[ClusterConfigurationInfo, typing.Dict[str, typing.Any]]] = None,
                ebs_storage_info: typing.Optional[typing.Union[EbsStorageInfo, typing.Dict[str, typing.Any]]] = None,
                encryption_in_transit: typing.Optional[typing.Union[EncryptionInTransitConfig, typing.Dict[str, typing.Any]]] = None,
                instance_type: typing.Optional[aws_cdk.aws_ec2.InstanceType] = None,
                logging: typing.Optional[typing.Union[BrokerLogging, typing.Dict[str, typing.Any]]] = None,
                monitoring: typing.Optional[typing.Union[MonitoringConfiguration, typing.Dict[str, typing.Any]]] = None,
                number_of_broker_nodes: typing.Optional[jsii.Number] = None,
                removal_policy: typing.Optional[aws_cdk.core.RemovalPolicy] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterProps(
            cluster_name=cluster_name,
            kafka_version=kafka_version,
            vpc=vpc,
            client_authentication=client_authentication,
            configuration_info=configuration_info,
            ebs_storage_info=ebs_storage_info,
            encryption_in_transit=encryption_in_transit,
            instance_type=instance_type,
            logging=logging,
            monitoring=monitoring,
            number_of_broker_nodes=number_of_broker_nodes,
            removal_policy=removal_policy,
            security_groups=security_groups,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClusterArn")
    @builtins.classmethod
    def from_cluster_arn(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        cluster_arn: builtins.str,
    ) -> ICluster:
        '''(experimental) Reference an existing cluster, defined outside of the CDK code, by name.

        :param scope: -
        :param id: -
        :param cluster_arn: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                cluster_arn: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
        return typing.cast(ICluster, jsii.sinvoke(cls, "fromClusterArn", [scope, id, cluster_arn]))

    @jsii.member(jsii_name="addUser")
    def add_user(self, *usernames: builtins.str) -> None:
        '''(experimental) A list of usersnames to register with the cluster.

        The password will automatically be generated using Secrets
        Manager and the { username, password } JSON object stored in Secrets Manager as ``AmazonMSK_username``.

        Must be using the SASL/SCRAM authentication mechanism.

        :param usernames: - username(s) to register with the cluster.

        :stability: experimental
        '''
        if __debug__:
            def stub(*usernames: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument usernames", value=usernames, expected_type=typing.Tuple[type_hints["usernames"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addUser", [*usernames]))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokers")
    def bootstrap_brokers(self) -> builtins.str:
        '''(experimental) Get the list of brokers that a client application can use to bootstrap.

        Uses a Custom Resource to make an API call to ``getBootstrapBrokers`` using the Javascript SDK

        :return: - A string containing one or more hostname:port pairs.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokers"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersSaslScram")
    def bootstrap_brokers_sasl_scram(self) -> builtins.str:
        '''(experimental) Get the list of brokers that a SASL/SCRAM authenticated client application can use to bootstrap.

        Uses a Custom Resource to make an API call to ``getBootstrapBrokers`` using the Javascript SDK

        :return: - A string containing one or more dns name (or IP) and SASL SCRAM port pairs.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersSaslScram"))

    @builtins.property
    @jsii.member(jsii_name="bootstrapBrokersTls")
    def bootstrap_brokers_tls(self) -> builtins.str:
        '''(experimental) Get the list of brokers that a TLS authenticated client application can use to bootstrap.

        Uses a Custom Resource to make an API call to ``getBootstrapBrokers`` using the Javascript SDK

        :return: - A string containing one or more DNS names (or IP) and TLS port pairs.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "bootstrapBrokersTls"))

    @builtins.property
    @jsii.member(jsii_name="clusterArn")
    def cluster_arn(self) -> builtins.str:
        '''(experimental) The ARN of cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterArn"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        '''(experimental) The physical name of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) Manages connections for the cluster.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="zookeeperConnectionString")
    def zookeeper_connection_string(self) -> builtins.str:
        '''(experimental) Get the ZooKeeper Connection string.

        Uses a Custom Resource to make an API call to ``describeCluster`` using the Javascript SDK

        :return: - The connection string to use to connect to the Apache ZooKeeper cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "zookeeperConnectionString"))

    @builtins.property
    @jsii.member(jsii_name="zookeeperConnectionStringTls")
    def zookeeper_connection_string_tls(self) -> builtins.str:
        '''(experimental) Get the ZooKeeper Connection string for a TLS enabled cluster.

        Uses a Custom Resource to make an API call to ``describeCluster`` using the Javascript SDK

        :return: - The connection string to use to connect to zookeeper cluster on TLS port.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "zookeeperConnectionStringTls"))

    @builtins.property
    @jsii.member(jsii_name="saslScramAuthenticationKey")
    def sasl_scram_authentication_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(experimental) Key used to encrypt SASL/SCRAM users.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], jsii.get(self, "saslScramAuthenticationKey"))


__all__ = [
    "BrokerLogging",
    "CfnBatchScramSecret",
    "CfnBatchScramSecretProps",
    "CfnCluster",
    "CfnClusterProps",
    "CfnConfiguration",
    "CfnConfigurationProps",
    "CfnServerlessCluster",
    "CfnServerlessClusterProps",
    "ClientAuthentication",
    "ClientBrokerEncryption",
    "Cluster",
    "ClusterConfigurationInfo",
    "ClusterMonitoringLevel",
    "ClusterProps",
    "EbsStorageInfo",
    "EncryptionInTransitConfig",
    "ICluster",
    "KafkaVersion",
    "MonitoringConfiguration",
    "S3LoggingConfiguration",
    "SaslAuthProps",
    "TlsAuthProps",
]

publication.publish()
