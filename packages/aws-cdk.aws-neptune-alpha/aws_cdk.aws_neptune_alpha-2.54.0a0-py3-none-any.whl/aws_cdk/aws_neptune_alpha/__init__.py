'''
# Amazon Neptune Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

Amazon Neptune is a fast, reliable, fully managed graph database service that makes it easy to build and run applications that work with highly connected datasets. The core of Neptune is a purpose-built, high-performance graph database engine. This engine is optimized for storing billions of relationships and querying the graph with milliseconds latency. Neptune supports the popular graph query languages Apache TinkerPop Gremlin and W3C’s SPARQL, enabling you to build queries that efficiently navigate highly connected datasets.

The `@aws-cdk/aws-neptune` package contains primitives for setting up Neptune database clusters and instances.

```python
import aws_cdk.aws_neptune_alpha as neptune
```

## Starting a Neptune Database

To set up a Neptune database, define a `DatabaseCluster`. You must always launch a database in a VPC.

```python
cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE
)
```

By default only writer instance is provisioned with this construct.

## Connecting

To control who can access the cluster, use the `.connections` attribute. Neptune databases have a default port, so
you don't need to specify the port:

```python
cluster.connections.allow_default_port_from_any_ipv4("Open to the world")
```

The endpoints to access your database cluster will be available as the `.clusterEndpoint` and `.clusterReadEndpoint`
attributes:

```python
write_address = cluster.cluster_endpoint.socket_address
```

## IAM Authentication

You can also authenticate to a database cluster using AWS Identity and Access Management (IAM) database authentication;
See [https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html) for more information and a list of supported
versions and limitations.

The following example shows enabling IAM authentication for a database cluster and granting connection access to an IAM role.

```python
cluster = neptune.DatabaseCluster(self, "Cluster",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    iam_authentication=True
)
role = iam.Role(self, "DBRole", assumed_by=iam.AccountPrincipal(self.account))
# Use one of the following statements to grant the role the necessary permissions
cluster.grant_connect(role) # Grant the role neptune-db:* access to the DB
cluster.grant(role, "neptune-db:ReadDataViaQuery", "neptune-db:WriteDataViaQuery")
```

## Customizing parameters

Neptune allows configuring database behavior by supplying custom parameter groups.  For more details, refer to the
following link: [https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html)

```python
cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
    description="Cluster parameter group",
    parameters={
        "neptune_enable_audit_log": "1"
    }
)

db_params = neptune.ParameterGroup(self, "DbParams",
    description="Db parameter group",
    parameters={
        "neptune_query_timeout": "120000"
    }
)

cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    cluster_parameter_group=cluster_params,
    parameter_group=db_params
)
```

Note: if you want to use Neptune engine `1.2.0.0` or later, you need to specify the corresponding `engineVersion` prop to `neptune.DatabaseCluster` and `family` prop of `ParameterGroupFamily.NEPTUNE_1_2` to `neptune.ClusterParameterGroup` and `neptune.ParameterGroup`.

## Adding replicas

`DatabaseCluster` allows launching replicas along with the writer instance. This can be specified using the `instanceCount`
attribute.

```python
cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    instances=2
)
```

Additionally, it is also possible to add replicas using `DatabaseInstance` for an existing cluster.

```python
replica1 = neptune.DatabaseInstance(self, "Instance",
    cluster=cluster,
    instance_type=neptune.InstanceType.R5_LARGE
)
```

## Automatic minor version upgrades

By setting `autoMinorVersionUpgrade` to true, Neptune will automatically update
the engine of the entire cluster to the latest minor version after a stabilization
window of 2 to 3 weeks.

```python
neptune.DatabaseCluster(self, "Cluster",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    auto_minor_version_upgrade=True
)
```

## Logging

Neptune supports various methods for monitoring performance and usage. One of those methods is logging

1. Neptune provides logs e.g. audit logs which can be viewed or downloaded via the AWS Console. Audit logs can be enabled using the `neptune_enable_audit_log` parameter in `ClusterParameterGroup` or `ParameterGroup`
2. Neptune provides the ability to export those logs to CloudWatch Logs

```python
# Cluster parameter group with the neptune_enable_audit_log param set to 1
cluster_parameter_group = neptune.ClusterParameterGroup(self, "ClusterParams",
    description="Cluster parameter group",
    parameters={
        "neptune_enable_audit_log": "1"
    }
)

cluster = neptune.DatabaseCluster(self, "Database",
    vpc=vpc,
    instance_type=neptune.InstanceType.R5_LARGE,
    # Audit logs are enabled via the clusterParameterGroup
    cluster_parameter_group=cluster_parameter_group,
    # Optionally configuring audit logs to be exported to CloudWatch Logs
    cloudwatch_logs_exports=[neptune.LogType.AUDIT],
    # Optionally set a retention period on exported CloudWatch Logs
    cloudwatch_logs_retention=logs.RetentionDays.ONE_MONTH
)
```

For more information on monitoring, refer to https://docs.aws.amazon.com/neptune/latest/userguide/monitoring.html.
For more information on audit logs, refer to https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html.
For more information on exporting logs to CloudWatch Logs, refer to https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html.

## Metrics

Both `DatabaseCluster` and `DatabaseInstance` provide a `metric()` method to help with cluster-level and instance-level monitoring.

```python
# cluster: neptune.DatabaseCluster
# instance: neptune.DatabaseInstance


cluster.metric("SparqlRequestsPerSec") # cluster-level SparqlErrors metric
instance.metric("SparqlRequestsPerSec")
```

For more details on the available metrics, refer to https://docs.aws.amazon.com/neptune/latest/userguide/cw-metrics.html
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
import aws_cdk.aws_cloudwatch
import aws_cdk.aws_ec2
import aws_cdk.aws_iam
import aws_cdk.aws_kms
import aws_cdk.aws_logs
import constructs


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.ClusterParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameters": "parameters",
        "cluster_parameter_group_name": "clusterParameterGroupName",
        "description": "description",
        "family": "family",
    },
)
class ClusterParameterGroupProps:
    def __init__(
        self,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        family: typing.Optional["ParameterGroupFamily"] = None,
    ) -> None:
        '''(experimental) Marker class for cluster parameter group.

        :param parameters: (experimental) The parameters in this parameter group.
        :param cluster_parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description
        :param family: (experimental) Parameter group family. Default: - NEPTUNE_1

        :stability: experimental
        :exampleMetadata: infused

        Example::

            cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
                description="Cluster parameter group",
                parameters={
                    "neptune_enable_audit_log": "1"
                }
            )
            
            db_params = neptune.ParameterGroup(self, "DbParams",
                description="Db parameter group",
                parameters={
                    "neptune_query_timeout": "120000"
                }
            )
            
            cluster = neptune.DatabaseCluster(self, "Database",
                vpc=vpc,
                instance_type=neptune.InstanceType.R5_LARGE,
                cluster_parameter_group=cluster_params,
                parameter_group=db_params
            )
        '''
        if __debug__:
            def stub(
                *,
                parameters: typing.Mapping[builtins.str, builtins.str],
                cluster_parameter_group_name: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                family: typing.Optional[ParameterGroupFamily] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument cluster_parameter_group_name", value=cluster_parameter_group_name, expected_type=type_hints["cluster_parameter_group_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameters": parameters,
        }
        if cluster_parameter_group_name is not None:
            self._values["cluster_parameter_group_name"] = cluster_parameter_group_name
        if description is not None:
            self._values["description"] = description
        if family is not None:
            self._values["family"] = family

    @builtins.property
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The parameters in this parameter group.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def cluster_parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter group.

        :default: A CDK generated name for the parameter group

        :stability: experimental
        '''
        result = self._values.get("cluster_parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for this parameter group.

        :default: a CDK generated description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def family(self) -> typing.Optional["ParameterGroupFamily"]:
        '''(experimental) Parameter group family.

        :default: - NEPTUNE_1

        :stability: experimental
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional["ParameterGroupFamily"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseClusterAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_endpoint_address": "clusterEndpointAddress",
        "cluster_identifier": "clusterIdentifier",
        "cluster_resource_identifier": "clusterResourceIdentifier",
        "port": "port",
        "reader_endpoint_address": "readerEndpointAddress",
        "security_group": "securityGroup",
    },
)
class DatabaseClusterAttributes:
    def __init__(
        self,
        *,
        cluster_endpoint_address: builtins.str,
        cluster_identifier: builtins.str,
        cluster_resource_identifier: builtins.str,
        port: jsii.Number,
        reader_endpoint_address: builtins.str,
        security_group: aws_cdk.aws_ec2.ISecurityGroup,
    ) -> None:
        '''(experimental) Properties that describe an existing cluster instance.

        :param cluster_endpoint_address: (experimental) Cluster endpoint address.
        :param cluster_identifier: (experimental) Identifier for the cluster.
        :param cluster_resource_identifier: (experimental) Resource Identifier for the cluster.
        :param port: (experimental) The database port.
        :param reader_endpoint_address: (experimental) Reader endpoint address.
        :param security_group: (experimental) The security group of the database cluster.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_neptune_alpha as neptune_alpha
            from aws_cdk import aws_ec2 as ec2
            
            # security_group: ec2.SecurityGroup
            
            database_cluster_attributes = neptune_alpha.DatabaseClusterAttributes(
                cluster_endpoint_address="clusterEndpointAddress",
                cluster_identifier="clusterIdentifier",
                cluster_resource_identifier="clusterResourceIdentifier",
                port=123,
                reader_endpoint_address="readerEndpointAddress",
                security_group=security_group
            )
        '''
        if __debug__:
            def stub(
                *,
                cluster_endpoint_address: builtins.str,
                cluster_identifier: builtins.str,
                cluster_resource_identifier: builtins.str,
                port: jsii.Number,
                reader_endpoint_address: builtins.str,
                security_group: aws_cdk.aws_ec2.ISecurityGroup,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster_endpoint_address", value=cluster_endpoint_address, expected_type=type_hints["cluster_endpoint_address"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
            check_type(argname="argument cluster_resource_identifier", value=cluster_resource_identifier, expected_type=type_hints["cluster_resource_identifier"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument reader_endpoint_address", value=reader_endpoint_address, expected_type=type_hints["reader_endpoint_address"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_endpoint_address": cluster_endpoint_address,
            "cluster_identifier": cluster_identifier,
            "cluster_resource_identifier": cluster_resource_identifier,
            "port": port,
            "reader_endpoint_address": reader_endpoint_address,
            "security_group": security_group,
        }

    @builtins.property
    def cluster_endpoint_address(self) -> builtins.str:
        '''(experimental) Cluster endpoint address.

        :stability: experimental
        '''
        result = self._values.get("cluster_endpoint_address")
        assert result is not None, "Required property 'cluster_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier for the cluster.

        :stability: experimental
        '''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource Identifier for the cluster.

        :stability: experimental
        '''
        result = self._values.get("cluster_resource_identifier")
        assert result is not None, "Required property 'cluster_resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''(experimental) The database port.

        :stability: experimental
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def reader_endpoint_address(self) -> builtins.str:
        '''(experimental) Reader endpoint address.

        :stability: experimental
        '''
        result = self._values.get("reader_endpoint_address")
        assert result is not None, "Required property 'reader_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group(self) -> aws_cdk.aws_ec2.ISecurityGroup:
        '''(experimental) The security group of the database cluster.

        :stability: experimental
        '''
        result = self._values.get("security_group")
        assert result is not None, "Required property 'security_group' is missing"
        return typing.cast(aws_cdk.aws_ec2.ISecurityGroup, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "vpc": "vpc",
        "associated_roles": "associatedRoles",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "backup_retention": "backupRetention",
        "cloudwatch_logs_exports": "cloudwatchLogsExports",
        "cloudwatch_logs_retention": "cloudwatchLogsRetention",
        "cloudwatch_logs_retention_role": "cloudwatchLogsRetentionRole",
        "cluster_parameter_group": "clusterParameterGroup",
        "db_cluster_name": "dbClusterName",
        "deletion_protection": "deletionProtection",
        "engine_version": "engineVersion",
        "iam_authentication": "iamAuthentication",
        "instance_identifier_base": "instanceIdentifierBase",
        "instances": "instances",
        "kms_key": "kmsKey",
        "parameter_group": "parameterGroup",
        "port": "port",
        "preferred_backup_window": "preferredBackupWindow",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "removal_policy": "removalPolicy",
        "security_groups": "securityGroups",
        "storage_encrypted": "storageEncrypted",
        "subnet_group": "subnetGroup",
        "vpc_subnets": "vpcSubnets",
    },
)
class DatabaseClusterProps:
    def __init__(
        self,
        *,
        instance_type: "InstanceType",
        vpc: aws_cdk.aws_ec2.IVpc,
        associated_roles: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IRole]] = None,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        backup_retention: typing.Optional[aws_cdk.Duration] = None,
        cloudwatch_logs_exports: typing.Optional[typing.Sequence["LogType"]] = None,
        cloudwatch_logs_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        cloudwatch_logs_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        cluster_parameter_group: typing.Optional["IClusterParameterGroup"] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        engine_version: typing.Optional["EngineVersion"] = None,
        iam_authentication: typing.Optional[builtins.bool] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        parameter_group: typing.Optional["IParameterGroup"] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
        subnet_group: typing.Optional["ISubnetGroup"] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for a new database cluster.

        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param vpc: (experimental) What subnets to run the Neptune instances in. Must be at least 2 subnets in two different AZs.
        :param associated_roles: (experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services. Default: - No role is attached to the cluster.
        :param auto_minor_version_upgrade: (experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks. Default: - false
        :param backup_retention: (experimental) How many days to retain the backup. Default: - cdk.Duration.days(1)
        :param cloudwatch_logs_exports: (experimental) The list of log types that need to be enabled for exporting to CloudWatch Logs. Default: - no log exports
        :param cloudwatch_logs_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``Infinity``. Default: - logs never expire
        :param cloudwatch_logs_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - a new role is created.
        :param cluster_parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
        :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
        :param deletion_protection: (experimental) Indicates whether the DB cluster should have deletion protection enabled. Default: - true if ``removalPolicy`` is RETAIN, false otherwise
        :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
        :param iam_authentication: (experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts. Default: - ``false``
        :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: (experimental) Number of Neptune compute instances. Default: 1
        :param kms_key: (experimental) The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param port: (experimental) The port the Neptune cluster will listen on. Default: - The default engine port
        :param preferred_backup_window: (experimental) A daily time range in 24-hours UTC format in which backups preferably execute. Must be at least 30 minutes long. Example: '01:00-02:00' Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see
        :param preferred_maintenance_window: (experimental) A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: (experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param security_groups: (experimental) Security group. Default: a new security group is created.
        :param storage_encrypted: (experimental) Whether to enable storage encryption. Default: true
        :param subnet_group: (experimental) Existing subnet group for the cluster. Default: - a new subnet group will be created.
        :param vpc_subnets: (experimental) Where to place the instances within the VPC. Default: private subnets

        :stability: experimental
        :exampleMetadata: infused

        Example::

            cluster = neptune.DatabaseCluster(self, "Database",
                vpc=vpc,
                instance_type=neptune.InstanceType.R5_LARGE,
                instances=2
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                instance_type: InstanceType,
                vpc: aws_cdk.aws_ec2.IVpc,
                associated_roles: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IRole]] = None,
                auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
                backup_retention: typing.Optional[aws_cdk.Duration] = None,
                cloudwatch_logs_exports: typing.Optional[typing.Sequence[LogType]] = None,
                cloudwatch_logs_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                cloudwatch_logs_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
                db_cluster_name: typing.Optional[builtins.str] = None,
                deletion_protection: typing.Optional[builtins.bool] = None,
                engine_version: typing.Optional[EngineVersion] = None,
                iam_authentication: typing.Optional[builtins.bool] = None,
                instance_identifier_base: typing.Optional[builtins.str] = None,
                instances: typing.Optional[jsii.Number] = None,
                kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                parameter_group: typing.Optional[IParameterGroup] = None,
                port: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                storage_encrypted: typing.Optional[builtins.bool] = None,
                subnet_group: typing.Optional[ISubnetGroup] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument associated_roles", value=associated_roles, expected_type=type_hints["associated_roles"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument backup_retention", value=backup_retention, expected_type=type_hints["backup_retention"])
            check_type(argname="argument cloudwatch_logs_exports", value=cloudwatch_logs_exports, expected_type=type_hints["cloudwatch_logs_exports"])
            check_type(argname="argument cloudwatch_logs_retention", value=cloudwatch_logs_retention, expected_type=type_hints["cloudwatch_logs_retention"])
            check_type(argname="argument cloudwatch_logs_retention_role", value=cloudwatch_logs_retention_role, expected_type=type_hints["cloudwatch_logs_retention_role"])
            check_type(argname="argument cluster_parameter_group", value=cluster_parameter_group, expected_type=type_hints["cluster_parameter_group"])
            check_type(argname="argument db_cluster_name", value=db_cluster_name, expected_type=type_hints["db_cluster_name"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument iam_authentication", value=iam_authentication, expected_type=type_hints["iam_authentication"])
            check_type(argname="argument instance_identifier_base", value=instance_identifier_base, expected_type=type_hints["instance_identifier_base"])
            check_type(argname="argument instances", value=instances, expected_type=type_hints["instances"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument parameter_group", value=parameter_group, expected_type=type_hints["parameter_group"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument preferred_backup_window", value=preferred_backup_window, expected_type=type_hints["preferred_backup_window"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument storage_encrypted", value=storage_encrypted, expected_type=type_hints["storage_encrypted"])
            check_type(argname="argument subnet_group", value=subnet_group, expected_type=type_hints["subnet_group"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_type": instance_type,
            "vpc": vpc,
        }
        if associated_roles is not None:
            self._values["associated_roles"] = associated_roles
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if backup_retention is not None:
            self._values["backup_retention"] = backup_retention
        if cloudwatch_logs_exports is not None:
            self._values["cloudwatch_logs_exports"] = cloudwatch_logs_exports
        if cloudwatch_logs_retention is not None:
            self._values["cloudwatch_logs_retention"] = cloudwatch_logs_retention
        if cloudwatch_logs_retention_role is not None:
            self._values["cloudwatch_logs_retention_role"] = cloudwatch_logs_retention_role
        if cluster_parameter_group is not None:
            self._values["cluster_parameter_group"] = cluster_parameter_group
        if db_cluster_name is not None:
            self._values["db_cluster_name"] = db_cluster_name
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if iam_authentication is not None:
            self._values["iam_authentication"] = iam_authentication
        if instance_identifier_base is not None:
            self._values["instance_identifier_base"] = instance_identifier_base
        if instances is not None:
            self._values["instances"] = instances
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if port is not None:
            self._values["port"] = port
        if preferred_backup_window is not None:
            self._values["preferred_backup_window"] = preferred_backup_window
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if storage_encrypted is not None:
            self._values["storage_encrypted"] = storage_encrypted
        if subnet_group is not None:
            self._values["subnet_group"] = subnet_group
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def instance_type(self) -> "InstanceType":
        '''(experimental) What type of instance to start for the replicas.

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast("InstanceType", result)

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) What subnets to run the Neptune instances in.

        Must be at least 2 subnets in two different AZs.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    @builtins.property
    def associated_roles(self) -> typing.Optional[typing.List[aws_cdk.aws_iam.IRole]]:
        '''(experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services.

        :default: - No role is attached to the cluster.

        :stability: experimental
        '''
        result = self._values.get("associated_roles")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_iam.IRole]], result)

    @builtins.property
    def auto_minor_version_upgrade(self) -> typing.Optional[builtins.bool]:
        '''(experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks.

        :default: - false

        :stability: experimental
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def backup_retention(self) -> typing.Optional[aws_cdk.Duration]:
        '''(experimental) How many days to retain the backup.

        :default: - cdk.Duration.days(1)

        :stability: experimental
        '''
        result = self._values.get("backup_retention")
        return typing.cast(typing.Optional[aws_cdk.Duration], result)

    @builtins.property
    def cloudwatch_logs_exports(self) -> typing.Optional[typing.List["LogType"]]:
        '''(experimental) The list of log types that need to be enabled for exporting to CloudWatch Logs.

        :default: - no log exports

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html#auditing-enable
        :stability: experimental
        '''
        result = self._values.get("cloudwatch_logs_exports")
        return typing.cast(typing.Optional[typing.List["LogType"]], result)

    @builtins.property
    def cloudwatch_logs_retention(
        self,
    ) -> typing.Optional[aws_cdk.aws_logs.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``Infinity``.

        :default: - logs never expire

        :stability: experimental
        '''
        result = self._values.get("cloudwatch_logs_retention")
        return typing.cast(typing.Optional[aws_cdk.aws_logs.RetentionDays], result)

    @builtins.property
    def cloudwatch_logs_retention_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''(experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - a new role is created.

        :stability: experimental
        '''
        result = self._values.get("cloudwatch_logs_retention_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def cluster_parameter_group(self) -> typing.Optional["IClusterParameterGroup"]:
        '''(experimental) Additional parameters to pass to the database engine.

        :default: - No parameter group.

        :stability: experimental
        '''
        result = self._values.get("cluster_parameter_group")
        return typing.cast(typing.Optional["IClusterParameterGroup"], result)

    @builtins.property
    def db_cluster_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) An optional identifier for the cluster.

        :default: - A name is automatically generated.

        :stability: experimental
        '''
        result = self._values.get("db_cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deletion_protection(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates whether the DB cluster should have deletion protection enabled.

        :default: - true if ``removalPolicy`` is RETAIN, false otherwise

        :stability: experimental
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def engine_version(self) -> typing.Optional["EngineVersion"]:
        '''(experimental) What version of the database to start.

        :default: - The default engine version.

        :stability: experimental
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional["EngineVersion"], result)

    @builtins.property
    def iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts.

        :default: - ``false``

        :stability: experimental
        '''
        result = self._values.get("iam_authentication")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def instance_identifier_base(self) -> typing.Optional[builtins.str]:
        '''(experimental) Base identifier for instances.

        Every replica is named by appending the replica number to this string, 1-based.

        :default:

        - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the
        identifier is automatically generated.

        :stability: experimental
        '''
        result = self._values.get("instance_identifier_base")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instances(self) -> typing.Optional[jsii.Number]:
        '''(experimental) Number of Neptune compute instances.

        :default: 1

        :stability: experimental
        '''
        result = self._values.get("instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def kms_key(self) -> typing.Optional[aws_cdk.aws_kms.IKey]:
        '''(experimental) The KMS key for storage encryption.

        :default: - default master key.

        :stability: experimental
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[aws_cdk.aws_kms.IKey], result)

    @builtins.property
    def parameter_group(self) -> typing.Optional["IParameterGroup"]:
        '''(experimental) The DB parameter group to associate with the instance.

        :default: no parameter group

        :stability: experimental
        '''
        result = self._values.get("parameter_group")
        return typing.cast(typing.Optional["IParameterGroup"], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The port the Neptune cluster will listen on.

        :default: - The default engine port

        :stability: experimental
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preferred_backup_window(self) -> typing.Optional[builtins.str]:
        '''(experimental) A daily time range in 24-hours UTC format in which backups preferably execute.

        Must be at least 30 minutes long.

        Example: '01:00-02:00'

        :default:

        - a 30-minute window selected at random from an 8-hour block of
        time for each AWS Region. To see the time blocks available, see

        :stability: experimental
        '''
        result = self._values.get("preferred_backup_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''(experimental) A weekly time range in which maintenance should preferably execute.

        Must be at least 30 minutes long.

        Example: 'tue:04:17-tue:04:47'

        :default:

        - 30-minute window selected at random from an 8-hour block of time for
        each AWS Region, occurring on a random day of the week.

        :stability: experimental
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted.

        This
        removal policy also applies to the implicit security group created for the
        cluster if one is not supplied as a parameter.

        :default: - Retain cluster.

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''(experimental) Security group.

        :default: a new security group is created.

        :stability: experimental
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def storage_encrypted(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Whether to enable storage encryption.

        :default: true

        :stability: experimental
        '''
        result = self._values.get("storage_encrypted")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def subnet_group(self) -> typing.Optional["ISubnetGroup"]:
        '''(experimental) Existing subnet group for the cluster.

        :default: - a new subnet group will be created.

        :stability: experimental
        '''
        result = self._values.get("subnet_group")
        return typing.cast(typing.Optional["ISubnetGroup"], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Where to place the instances within the VPC.

        :default: private subnets

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseInstanceAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "instance_endpoint_address": "instanceEndpointAddress",
        "instance_identifier": "instanceIdentifier",
        "port": "port",
    },
)
class DatabaseInstanceAttributes:
    def __init__(
        self,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> None:
        '''(experimental) Properties that describe an existing instance.

        :param instance_endpoint_address: (experimental) The endpoint address.
        :param instance_identifier: (experimental) The instance identifier.
        :param port: (experimental) The database port.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_neptune_alpha as neptune_alpha
            
            database_instance_attributes = neptune_alpha.DatabaseInstanceAttributes(
                instance_endpoint_address="instanceEndpointAddress",
                instance_identifier="instanceIdentifier",
                port=123
            )
        '''
        if __debug__:
            def stub(
                *,
                instance_endpoint_address: builtins.str,
                instance_identifier: builtins.str,
                port: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_endpoint_address", value=instance_endpoint_address, expected_type=type_hints["instance_endpoint_address"])
            check_type(argname="argument instance_identifier", value=instance_identifier, expected_type=type_hints["instance_identifier"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        self._values: typing.Dict[str, typing.Any] = {
            "instance_endpoint_address": instance_endpoint_address,
            "instance_identifier": instance_identifier,
            "port": port,
        }

    @builtins.property
    def instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The endpoint address.

        :stability: experimental
        '''
        result = self._values.get("instance_endpoint_address")
        assert result is not None, "Required property 'instance_endpoint_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        '''
        result = self._values.get("instance_identifier")
        assert result is not None, "Required property 'instance_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''(experimental) The database port.

        :stability: experimental
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "instance_type": "instanceType",
        "availability_zone": "availabilityZone",
        "db_instance_name": "dbInstanceName",
        "parameter_group": "parameterGroup",
        "removal_policy": "removalPolicy",
    },
)
class DatabaseInstanceProps:
    def __init__(
        self,
        *,
        cluster: "IDatabaseCluster",
        instance_type: "InstanceType",
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        parameter_group: typing.Optional["IParameterGroup"] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
    ) -> None:
        '''(experimental) Construction properties for a DatabaseInstanceNew.

        :param cluster: (experimental) The Neptune database cluster the instance should launch into.
        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param availability_zone: (experimental) The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: (experimental) A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param removal_policy: (experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :stability: experimental
        :exampleMetadata: fixture=with-cluster infused

        Example::

            replica1 = neptune.DatabaseInstance(self, "Instance",
                cluster=cluster,
                instance_type=neptune.InstanceType.R5_LARGE
            )
        '''
        if __debug__:
            def stub(
                *,
                cluster: IDatabaseCluster,
                instance_type: InstanceType,
                availability_zone: typing.Optional[builtins.str] = None,
                db_instance_name: typing.Optional[builtins.str] = None,
                parameter_group: typing.Optional[IParameterGroup] = None,
                removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument db_instance_name", value=db_instance_name, expected_type=type_hints["db_instance_name"])
            check_type(argname="argument parameter_group", value=parameter_group, expected_type=type_hints["parameter_group"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
            "instance_type": instance_type,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if db_instance_name is not None:
            self._values["db_instance_name"] = db_instance_name
        if parameter_group is not None:
            self._values["parameter_group"] = parameter_group
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy

    @builtins.property
    def cluster(self) -> "IDatabaseCluster":
        '''(experimental) The Neptune database cluster the instance should launch into.

        :stability: experimental
        '''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast("IDatabaseCluster", result)

    @builtins.property
    def instance_type(self) -> "InstanceType":
        '''(experimental) What type of instance to start for the replicas.

        :stability: experimental
        '''
        result = self._values.get("instance_type")
        assert result is not None, "Required property 'instance_type' is missing"
        return typing.cast("InstanceType", result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the Availability Zone where the DB instance will be located.

        :default: - no preference

        :stability: experimental
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_instance_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) A name for the DB instance.

        If you specify a name, AWS CloudFormation
        converts it to lowercase.

        :default: - a CloudFormation generated name

        :stability: experimental
        '''
        result = self._values.get("db_instance_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_group(self) -> typing.Optional["IParameterGroup"]:
        '''(experimental) The DB parameter group to associate with the instance.

        :default: no parameter group

        :stability: experimental
        '''
        result = self._values.get("parameter_group")
        return typing.cast(typing.Optional["IParameterGroup"], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update.

        :default: RemovalPolicy.Retain

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Endpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.Endpoint",
):
    '''(experimental) Connection endpoint of a neptune cluster or instance.

    Consists of a combination of hostname and port.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_neptune_alpha as neptune_alpha
        
        endpoint = neptune_alpha.Endpoint("address", 123)
    '''

    def __init__(self, address: builtins.str, port: jsii.Number) -> None:
        '''
        :param address: -
        :param port: -

        :stability: experimental
        '''
        if __debug__:
            def stub(address: builtins.str, port: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument address", value=address, expected_type=type_hints["address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [address, port])

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        '''(experimental) The hostname of the endpoint.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        '''(experimental) The port of the endpoint.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="socketAddress")
    def socket_address(self) -> builtins.str:
        '''(experimental) The combination of "HOSTNAME:PORT" for this endpoint.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "socketAddress"))


class EngineVersion(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.EngineVersion",
):
    '''(experimental) Possible Instances Types to use in Neptune cluster used for defining {@link DatabaseClusterProps.engineVersion}.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_neptune_alpha as neptune_alpha
        
        engine_version = neptune_alpha.EngineVersion.V1_0_1_0
    '''

    def __init__(self, version: builtins.str) -> None:
        '''(experimental) Constructor for specifying a custom engine version.

        :param version: the engine version of Neptune.

        :stability: experimental
        '''
        if __debug__:
            def stub(version: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        jsii.create(self.__class__, self, [version])

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_1_0")
    def V1_0_1_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.1.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_1_1")
    def V1_0_1_1(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.1.1.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_1_2")
    def V1_0_1_2(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.1.2.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_1_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_2_1")
    def V1_0_2_1(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.2.1.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_2_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_2_2")
    def V1_0_2_2(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.2.2.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_2_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_3_0")
    def V1_0_3_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.3.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_3_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_4_0")
    def V1_0_4_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.4.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_4_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_4_1")
    def V1_0_4_1(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.4.1.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_4_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_0_5_0")
    def V1_0_5_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.0.5.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_0_5_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_1_0_0")
    def V1_1_0_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.1.0.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_1_0_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_1_1_0")
    def V1_1_1_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.1.1.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_1_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="V1_2_0_0")
    def V1_2_0_0(cls) -> "EngineVersion":
        '''(experimental) Neptune engine version 1.2.0.0.

        :stability: experimental
        '''
        return typing.cast("EngineVersion", jsii.sget(cls, "V1_2_0_0"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) the engine version of Neptune.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))


@jsii.interface(jsii_type="@aws-cdk/aws-neptune-alpha.IClusterParameterGroup")
class IClusterParameterGroup(aws_cdk.IResource, typing_extensions.Protocol):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        ...


class _IClusterParameterGroupProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-neptune-alpha.IClusterParameterGroup"

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterParameterGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterParameterGroup).__jsii_proxy_class__ = lambda : _IClusterParameterGroupProxy


@jsii.interface(jsii_type="@aws-cdk/aws-neptune-alpha.IDatabaseCluster")
class IDatabaseCluster(
    aws_cdk.IResource,
    aws_cdk.aws_ec2.IConnectable,
    typing_extensions.Protocol,
):
    '''(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        :attribute: Endpoint,Port
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        :attribute: ReadEndpoint
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        :attribute: ClusterResourceId
        '''
        ...

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the given identity the specified actions.

        :param grantee: the identity to be granted the actions.
        :param actions: the data-access actions.

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html
        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="grantConnect")
    def grant_connect(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the given identity connection access to the database.

        :param grantee: -

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric associated with this DatabaseCluster instance.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/cw-dimensions.html
        :stability: experimental
        '''
        ...


class _IDatabaseClusterProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
    jsii.proxy_for(aws_cdk.aws_ec2.IConnectable), # type: ignore[misc]
):
    '''(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-neptune-alpha.IDatabaseCluster"

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        :attribute: Endpoint,Port
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        :attribute: ReadEndpoint
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        :attribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the given identity the specified actions.

        :param grantee: the identity to be granted the actions.
        :param actions: the data-access actions.

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html
        :stability: experimental
        '''
        if __debug__:
            def stub(
                grantee: aws_cdk.aws_iam.IGrantable,
                *actions: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantConnect")
    def grant_connect(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the given identity connection access to the database.

        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            def stub(grantee: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantConnect", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric associated with this DatabaseCluster instance.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/cw-dimensions.html
        :stability: experimental
        '''
        if __debug__:
            def stub(
                metric_name: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                label: typing.Optional[builtins.str] = None,
                period: typing.Optional[aws_cdk.Duration] = None,
                region: typing.Optional[builtins.str] = None,
                statistic: typing.Optional[builtins.str] = None,
                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseCluster).__jsii_proxy_class__ = lambda : _IDatabaseClusterProxy


@jsii.interface(jsii_type="@aws-cdk/aws-neptune-alpha.IDatabaseInstance")
class IDatabaseInstance(aws_cdk.IResource, typing_extensions.Protocol):
    '''(experimental) A database instance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :attribute: Endpoint
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :attribute: Port
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric associated with this database instance.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/cw-dimensions.html
        :stability: experimental
        '''
        ...


class _IDatabaseInstanceProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
):
    '''(experimental) A database instance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-neptune-alpha.IDatabaseInstance"

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :attribute: Endpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :attribute: Port
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric associated with this database instance.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/cw-dimensions.html
        :stability: experimental
        '''
        if __debug__:
            def stub(
                metric_name: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                label: typing.Optional[builtins.str] = None,
                period: typing.Optional[aws_cdk.Duration] = None,
                region: typing.Optional[builtins.str] = None,
                statistic: typing.Optional[builtins.str] = None,
                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseInstance).__jsii_proxy_class__ = lambda : _IDatabaseInstanceProxy


@jsii.interface(jsii_type="@aws-cdk/aws-neptune-alpha.IParameterGroup")
class IParameterGroup(aws_cdk.IResource, typing_extensions.Protocol):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        ...


class _IParameterGroupProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
):
    '''(experimental) A parameter group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-neptune-alpha.IParameterGroup"

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of this parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterGroup).__jsii_proxy_class__ = lambda : _IParameterGroupProxy


@jsii.interface(jsii_type="@aws-cdk/aws-neptune-alpha.ISubnetGroup")
class ISubnetGroup(aws_cdk.IResource, typing_extensions.Protocol):
    '''(experimental) Interface for a subnet group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''(experimental) The name of the subnet group.

        :stability: experimental
        :attribute: true
        '''
        ...


class _ISubnetGroupProxy(
    jsii.proxy_for(aws_cdk.IResource), # type: ignore[misc]
):
    '''(experimental) Interface for a subnet group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-neptune-alpha.ISubnetGroup"

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''(experimental) The name of the subnet group.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetGroup).__jsii_proxy_class__ = lambda : _ISubnetGroupProxy


class InstanceType(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.InstanceType",
):
    '''(experimental) Possible Instances Types to use in Neptune cluster used for defining {@link DatabaseInstanceProps.instanceType}.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            instances=2
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, instance_type: builtins.str) -> "InstanceType":
        '''(experimental) Build an InstanceType from given string or token, such as CfnParameter.

        :param instance_type: -

        :stability: experimental
        '''
        if __debug__:
            def stub(instance_type: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
        return typing.cast("InstanceType", jsii.sinvoke(cls, "of", [instance_type]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_2XLARGE")
    def R4_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_4XLARGE")
    def R4_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_8XLARGE")
    def R4_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_LARGE")
    def R4_LARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R4_XLARGE")
    def R4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r4.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R4_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_12XLARGE")
    def R5_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_24XLARGE")
    def R5_24_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.24xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_24XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_2XLARGE")
    def R5_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_4XLARGE")
    def R5_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_8XLARGE")
    def R5_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_LARGE")
    def R5_LARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R5_XLARGE")
    def R5_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r5.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R5_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_12XLARGE")
    def R6_G_12_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.12xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_12XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_16XLARGE")
    def R6_G_16_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.16xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_16XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_2XLARGE")
    def R6_G_2_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.2xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_2XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_4XLARGE")
    def R6_G_4_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.4xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_4XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_8XLARGE")
    def R6_G_8_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.8xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_8XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_LARGE")
    def R6_G_LARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.large.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="R6G_XLARGE")
    def R6_G_XLARGE(cls) -> "InstanceType":
        '''(experimental) db.r6g.xlarge.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "R6G_XLARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T3_MEDIUM")
    def T3_MEDIUM(cls) -> "InstanceType":
        '''(experimental) db.t3.medium.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T3_MEDIUM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="T4G_MEDIUM")
    def T4_G_MEDIUM(cls) -> "InstanceType":
        '''(experimental) db.t4g.medium.

        :stability: experimental
        '''
        return typing.cast("InstanceType", jsii.sget(cls, "T4G_MEDIUM"))


class LogType(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-neptune-alpha.LogType"):
    '''(experimental) Neptune log types that can be exported to CloudWatch logs.

    :see: https://docs.aws.amazon.com/neptune/latest/userguide/cloudwatch-logs.html
    :stability: experimental
    :exampleMetadata: infused

    Example::

        # Cluster parameter group with the neptune_enable_audit_log param set to 1
        cluster_parameter_group = neptune.ClusterParameterGroup(self, "ClusterParams",
            description="Cluster parameter group",
            parameters={
                "neptune_enable_audit_log": "1"
            }
        )
        
        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            # Audit logs are enabled via the clusterParameterGroup
            cluster_parameter_group=cluster_parameter_group,
            # Optionally configuring audit logs to be exported to CloudWatch Logs
            cloudwatch_logs_exports=[neptune.LogType.AUDIT],
            # Optionally set a retention period on exported CloudWatch Logs
            cloudwatch_logs_retention=logs.RetentionDays.ONE_MONTH
        )
    '''

    def __init__(self, value: builtins.str) -> None:
        '''(experimental) Constructor for specifying a custom log type.

        :param value: the log type.

        :stability: experimental
        '''
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.create(self.__class__, self, [value])

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUDIT")
    def AUDIT(cls) -> "LogType":
        '''(experimental) Audit logs.

        :see: https://docs.aws.amazon.com/neptune/latest/userguide/auditing.html
        :stability: experimental
        '''
        return typing.cast("LogType", jsii.sget(cls, "AUDIT"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''(experimental) the log type.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "value"))


@jsii.implements(IParameterGroup)
class ParameterGroup(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.ParameterGroup",
):
    '''(experimental) DB parameter group.

    :stability: experimental
    :resource: AWS::Neptune::DBParameterGroup
    :exampleMetadata: infused

    Example::

        cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
            description="Cluster parameter group",
            parameters={
                "neptune_enable_audit_log": "1"
            }
        )
        
        db_params = neptune.ParameterGroup(self, "DbParams",
            description="Db parameter group",
            parameters={
                "neptune_query_timeout": "120000"
            }
        )
        
        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            cluster_parameter_group=cluster_params,
            parameter_group=db_params
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        description: typing.Optional[builtins.str] = None,
        family: typing.Optional["ParameterGroupFamily"] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param parameters: (experimental) The parameters in this parameter group.
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description
        :param family: (experimental) Parameter group family. Default: - NEPTUNE_1
        :param parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                parameters: typing.Mapping[builtins.str, builtins.str],
                description: typing.Optional[builtins.str] = None,
                family: typing.Optional[ParameterGroupFamily] = None,
                parameter_group_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ParameterGroupProps(
            parameters=parameters,
            description=description,
            family=family,
            parameter_group_name=parameter_group_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromParameterGroupName")
    @builtins.classmethod
    def from_parameter_group_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        parameter_group_name: builtins.str,
    ) -> IParameterGroup:
        '''(experimental) Imports a parameter group.

        :param scope: -
        :param id: -
        :param parameter_group_name: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                parameter_group_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        return typing.cast(IParameterGroup, jsii.sinvoke(cls, "fromParameterGroupName", [scope, id, parameter_group_name]))

    @builtins.property
    @jsii.member(jsii_name="parameterGroupName")
    def parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of the parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "parameterGroupName"))


class ParameterGroupFamily(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.ParameterGroupFamily",
):
    '''(experimental) The DB parameter group family that a DB parameter group is compatible with.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_neptune_alpha as neptune_alpha
        
        parameter_group_family = neptune_alpha.ParameterGroupFamily("family")
    '''

    def __init__(self, family: builtins.str) -> None:
        '''(experimental) Constructor for specifying a custom parameter group famil.

        :param family: the family of the parameter group Neptune.

        :stability: experimental
        '''
        if __debug__:
            def stub(family: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        jsii.create(self.__class__, self, [family])

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_1")
    def NEPTUNE_1(cls) -> "ParameterGroupFamily":
        '''(experimental) Family used by Neptune engine versions before 1.2.0.0.

        :stability: experimental
        '''
        return typing.cast("ParameterGroupFamily", jsii.sget(cls, "NEPTUNE_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NEPTUNE_1_2")
    def NEPTUNE_1_2(cls) -> "ParameterGroupFamily":
        '''(experimental) Family used by Neptune engine versions 1.2.0.0 and later.

        :stability: experimental
        '''
        return typing.cast("ParameterGroupFamily", jsii.sget(cls, "NEPTUNE_1_2"))

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> builtins.str:
        '''(experimental) the family of the parameter group Neptune.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "family"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.ParameterGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameters": "parameters",
        "description": "description",
        "family": "family",
        "parameter_group_name": "parameterGroupName",
    },
)
class ParameterGroupProps:
    def __init__(
        self,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        description: typing.Optional[builtins.str] = None,
        family: typing.Optional[ParameterGroupFamily] = None,
        parameter_group_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Marker class for cluster parameter group.

        :param parameters: (experimental) The parameters in this parameter group.
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description
        :param family: (experimental) Parameter group family. Default: - NEPTUNE_1
        :param parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group

        :stability: experimental
        :exampleMetadata: infused

        Example::

            cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
                description="Cluster parameter group",
                parameters={
                    "neptune_enable_audit_log": "1"
                }
            )
            
            db_params = neptune.ParameterGroup(self, "DbParams",
                description="Db parameter group",
                parameters={
                    "neptune_query_timeout": "120000"
                }
            )
            
            cluster = neptune.DatabaseCluster(self, "Database",
                vpc=vpc,
                instance_type=neptune.InstanceType.R5_LARGE,
                cluster_parameter_group=cluster_params,
                parameter_group=db_params
            )
        '''
        if __debug__:
            def stub(
                *,
                parameters: typing.Mapping[builtins.str, builtins.str],
                description: typing.Optional[builtins.str] = None,
                family: typing.Optional[ParameterGroupFamily] = None,
                parameter_group_name: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "parameters": parameters,
        }
        if description is not None:
            self._values["description"] = description
        if family is not None:
            self._values["family"] = family
        if parameter_group_name is not None:
            self._values["parameter_group_name"] = parameter_group_name

    @builtins.property
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''(experimental) The parameters in this parameter group.

        :stability: experimental
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description for this parameter group.

        :default: a CDK generated description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def family(self) -> typing.Optional[ParameterGroupFamily]:
        '''(experimental) Parameter group family.

        :default: - NEPTUNE_1

        :stability: experimental
        '''
        result = self._values.get("family")
        return typing.cast(typing.Optional[ParameterGroupFamily], result)

    @builtins.property
    def parameter_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the parameter group.

        :default: A CDK generated name for the parameter group

        :stability: experimental
        '''
        result = self._values.get("parameter_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISubnetGroup)
class SubnetGroup(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.SubnetGroup",
):
    '''(experimental) Class for creating a RDS DB subnet group.

    :stability: experimental
    :resource: AWS::Neptune::DBSubnetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_neptune_alpha as neptune_alpha
        import aws_cdk as cdk
        from aws_cdk import aws_ec2 as ec2
        
        # subnet: ec2.Subnet
        # subnet_filter: ec2.SubnetFilter
        # vpc: ec2.Vpc
        
        subnet_group = neptune_alpha.SubnetGroup(self, "MySubnetGroup",
            vpc=vpc,
        
            # the properties below are optional
            description="description",
            removal_policy=cdk.RemovalPolicy.DESTROY,
            subnet_group_name="subnetGroupName",
            vpc_subnets=ec2.SubnetSelection(
                availability_zones=["availabilityZones"],
                one_per_az=False,
                subnet_filters=[subnet_filter],
                subnet_group_name="subnetGroupName",
                subnets=[subnet],
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            )
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        description: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: (experimental) The VPC to place the subnet group in.
        :param description: (experimental) Description of the subnet group. Default: - a name is generated
        :param removal_policy: (experimental) The removal policy to apply when the subnet group are removed from the stack or replaced during an update. Default: RemovalPolicy.DESTROY
        :param subnet_group_name: (experimental) The name of the subnet group. Default: - a name is generated
        :param vpc_subnets: (experimental) Which subnets within the VPC to associate with this group. Default: - private subnets

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                vpc: aws_cdk.aws_ec2.IVpc,
                description: typing.Optional[builtins.str] = None,
                removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                subnet_group_name: typing.Optional[builtins.str] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SubnetGroupProps(
            vpc=vpc,
            description=description,
            removal_policy=removal_policy,
            subnet_group_name=subnet_group_name,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSubnetGroupName")
    @builtins.classmethod
    def from_subnet_group_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        subnet_group_name: builtins.str,
    ) -> ISubnetGroup:
        '''(experimental) Imports an existing subnet group by name.

        :param scope: -
        :param id: -
        :param subnet_group_name: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                subnet_group_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
        return typing.cast(ISubnetGroup, jsii.sinvoke(cls, "fromSubnetGroupName", [scope, id, subnet_group_name]))

    @builtins.property
    @jsii.member(jsii_name="subnetGroupName")
    def subnet_group_name(self) -> builtins.str:
        '''(experimental) The name of the subnet group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "subnetGroupName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-neptune-alpha.SubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "vpc": "vpc",
        "description": "description",
        "removal_policy": "removalPolicy",
        "subnet_group_name": "subnetGroupName",
        "vpc_subnets": "vpcSubnets",
    },
)
class SubnetGroupProps:
    def __init__(
        self,
        *,
        vpc: aws_cdk.aws_ec2.IVpc,
        description: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        subnet_group_name: typing.Optional[builtins.str] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for creating a SubnetGroup.

        :param vpc: (experimental) The VPC to place the subnet group in.
        :param description: (experimental) Description of the subnet group. Default: - a name is generated
        :param removal_policy: (experimental) The removal policy to apply when the subnet group are removed from the stack or replaced during an update. Default: RemovalPolicy.DESTROY
        :param subnet_group_name: (experimental) The name of the subnet group. Default: - a name is generated
        :param vpc_subnets: (experimental) Which subnets within the VPC to associate with this group. Default: - private subnets

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_neptune_alpha as neptune_alpha
            import aws_cdk as cdk
            from aws_cdk import aws_ec2 as ec2
            
            # subnet: ec2.Subnet
            # subnet_filter: ec2.SubnetFilter
            # vpc: ec2.Vpc
            
            subnet_group_props = neptune_alpha.SubnetGroupProps(
                vpc=vpc,
            
                # the properties below are optional
                description="description",
                removal_policy=cdk.RemovalPolicy.DESTROY,
                subnet_group_name="subnetGroupName",
                vpc_subnets=ec2.SubnetSelection(
                    availability_zones=["availabilityZones"],
                    one_per_az=False,
                    subnet_filters=[subnet_filter],
                    subnet_group_name="subnetGroupName",
                    subnets=[subnet],
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                )
            )
        '''
        if isinstance(vpc_subnets, dict):
            vpc_subnets = aws_cdk.aws_ec2.SubnetSelection(**vpc_subnets)
        if __debug__:
            def stub(
                *,
                vpc: aws_cdk.aws_ec2.IVpc,
                description: typing.Optional[builtins.str] = None,
                removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                subnet_group_name: typing.Optional[builtins.str] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[str, typing.Any] = {
            "vpc": vpc,
        }
        if description is not None:
            self._values["description"] = description
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if subnet_group_name is not None:
            self._values["subnet_group_name"] = subnet_group_name
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) The VPC to place the subnet group in.

        :stability: experimental
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(aws_cdk.aws_ec2.IVpc, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description of the subnet group.

        :default: - a name is generated

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[aws_cdk.RemovalPolicy]:
        '''(experimental) The removal policy to apply when the subnet group are removed from the stack or replaced during an update.

        :default: RemovalPolicy.DESTROY

        :stability: experimental
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[aws_cdk.RemovalPolicy], result)

    @builtins.property
    def subnet_group_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the subnet group.

        :default: - a name is generated

        :stability: experimental
        '''
        result = self._values.get("subnet_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''(experimental) Which subnets within the VPC to associate with this group.

        :default: - private subnets

        :stability: experimental
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IClusterParameterGroup)
class ClusterParameterGroup(
    aws_cdk.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.ClusterParameterGroup",
):
    '''(experimental) A cluster parameter group.

    :stability: experimental
    :resource: AWS::Neptune::DBClusterParameterGroup
    :exampleMetadata: infused

    Example::

        cluster_params = neptune.ClusterParameterGroup(self, "ClusterParams",
            description="Cluster parameter group",
            parameters={
                "neptune_enable_audit_log": "1"
            }
        )
        
        db_params = neptune.ParameterGroup(self, "DbParams",
            description="Db parameter group",
            parameters={
                "neptune_query_timeout": "120000"
            }
        )
        
        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            cluster_parameter_group=cluster_params,
            parameter_group=db_params
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        parameters: typing.Mapping[builtins.str, builtins.str],
        cluster_parameter_group_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        family: typing.Optional[ParameterGroupFamily] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param parameters: (experimental) The parameters in this parameter group.
        :param cluster_parameter_group_name: (experimental) The name of the parameter group. Default: A CDK generated name for the parameter group
        :param description: (experimental) Description for this parameter group. Default: a CDK generated description
        :param family: (experimental) Parameter group family. Default: - NEPTUNE_1

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                parameters: typing.Mapping[builtins.str, builtins.str],
                cluster_parameter_group_name: typing.Optional[builtins.str] = None,
                description: typing.Optional[builtins.str] = None,
                family: typing.Optional[ParameterGroupFamily] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ClusterParameterGroupProps(
            parameters=parameters,
            cluster_parameter_group_name=cluster_parameter_group_name,
            description=description,
            family=family,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromClusterParameterGroupName")
    @builtins.classmethod
    def from_cluster_parameter_group_name(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        cluster_parameter_group_name: builtins.str,
    ) -> IClusterParameterGroup:
        '''(experimental) Imports a parameter group.

        :param scope: -
        :param id: -
        :param cluster_parameter_group_name: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                cluster_parameter_group_name: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument cluster_parameter_group_name", value=cluster_parameter_group_name, expected_type=type_hints["cluster_parameter_group_name"])
        return typing.cast(IClusterParameterGroup, jsii.sinvoke(cls, "fromClusterParameterGroupName", [scope, id, cluster_parameter_group_name]))

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupName")
    def cluster_parameter_group_name(self) -> builtins.str:
        '''(experimental) The name of the parameter group.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterParameterGroupName"))


@jsii.implements(IDatabaseCluster)
class DatabaseClusterBase(
    aws_cdk.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseClusterBase",
):
    '''(experimental) A new or imported database cluster.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_neptune_alpha as neptune_alpha
        from aws_cdk import aws_ec2 as ec2
        
        # security_group: ec2.SecurityGroup
        
        database_cluster_base = neptune_alpha.DatabaseClusterBase.from_database_cluster_attributes(self, "MyDatabaseClusterBase",
            cluster_endpoint_address="clusterEndpointAddress",
            cluster_identifier="clusterIdentifier",
            cluster_resource_identifier="clusterResourceIdentifier",
            port=123,
            reader_endpoint_address="readerEndpointAddress",
            security_group=security_group
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                environment_from_arn: typing.Optional[builtins.str] = None,
                physical_name: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = aws_cdk.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseClusterAttributes")
    @builtins.classmethod
    def from_database_cluster_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster_endpoint_address: builtins.str,
        cluster_identifier: builtins.str,
        cluster_resource_identifier: builtins.str,
        port: jsii.Number,
        reader_endpoint_address: builtins.str,
        security_group: aws_cdk.aws_ec2.ISecurityGroup,
    ) -> IDatabaseCluster:
        '''(experimental) Import an existing DatabaseCluster from properties.

        :param scope: -
        :param id: -
        :param cluster_endpoint_address: (experimental) Cluster endpoint address.
        :param cluster_identifier: (experimental) Identifier for the cluster.
        :param cluster_resource_identifier: (experimental) Resource Identifier for the cluster.
        :param port: (experimental) The database port.
        :param reader_endpoint_address: (experimental) Reader endpoint address.
        :param security_group: (experimental) The security group of the database cluster.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                cluster_endpoint_address: builtins.str,
                cluster_identifier: builtins.str,
                cluster_resource_identifier: builtins.str,
                port: jsii.Number,
                reader_endpoint_address: builtins.str,
                security_group: aws_cdk.aws_ec2.ISecurityGroup,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DatabaseClusterAttributes(
            cluster_endpoint_address=cluster_endpoint_address,
            cluster_identifier=cluster_identifier,
            cluster_resource_identifier=cluster_resource_identifier,
            port=port,
            reader_endpoint_address=reader_endpoint_address,
            security_group=security_group,
        )

        return typing.cast(IDatabaseCluster, jsii.sinvoke(cls, "fromDatabaseClusterAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
        *actions: builtins.str,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the given identity the specified actions.

        :param grantee: -
        :param actions: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                grantee: aws_cdk.aws_iam.IGrantable,
                *actions: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grant", [grantee, *actions]))

    @jsii.member(jsii_name="grantConnect")
    def grant_connect(
        self,
        grantee: aws_cdk.aws_iam.IGrantable,
    ) -> aws_cdk.aws_iam.Grant:
        '''(experimental) Grant the given identity connection access to the database.

        :param grantee: -

        :stability: experimental
        '''
        if __debug__:
            def stub(grantee: aws_cdk.aws_iam.IGrantable) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(aws_cdk.aws_iam.Grant, jsii.invoke(self, "grantConnect", [grantee]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric associated with this DatabaseCluster instance.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        '''
        if __debug__:
            def stub(
                metric_name: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                label: typing.Optional[builtins.str] = None,
                period: typing.Optional[aws_cdk.Duration] = None,
                region: typing.Optional[builtins.str] = None,
                statistic: typing.Optional[builtins.str] = None,
                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    @abc.abstractmethod
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    @abc.abstractmethod
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    @abc.abstractmethod
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    @abc.abstractmethod
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="connections")
    @abc.abstractmethod
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The connections object to implement IConnectable.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="enableIamAuthentication")
    @abc.abstractmethod
    def _enable_iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        ...

    @_enable_iam_authentication.setter
    @abc.abstractmethod
    def _enable_iam_authentication(self, value: typing.Optional[builtins.bool]) -> None:
        ...


class _DatabaseClusterBaseProxy(
    DatabaseClusterBase,
    jsii.proxy_for(aws_cdk.Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) Resource identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The connections object to implement IConnectable.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="enableIamAuthentication")
    def _enable_iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableIamAuthentication"))

    @_enable_iam_authentication.setter
    def _enable_iam_authentication(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIamAuthentication", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DatabaseClusterBase).__jsii_proxy_class__ = lambda : _DatabaseClusterBaseProxy


@jsii.implements(IDatabaseInstance)
class DatabaseInstanceBase(
    aws_cdk.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseInstanceBase",
):
    '''(experimental) A new or imported database instance.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_neptune_alpha as neptune_alpha
        
        database_instance_base = neptune_alpha.DatabaseInstanceBase.from_database_instance_attributes(self, "MyDatabaseInstanceBase",
            instance_endpoint_address="instanceEndpointAddress",
            instance_identifier="instanceIdentifier",
            port=123
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                environment_from_arn: typing.Optional[builtins.str] = None,
                physical_name: typing.Optional[builtins.str] = None,
                region: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = aws_cdk.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDatabaseInstanceAttributes")
    @builtins.classmethod
    def from_database_instance_attributes(
        cls,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_endpoint_address: builtins.str,
        instance_identifier: builtins.str,
        port: jsii.Number,
    ) -> IDatabaseInstance:
        '''(experimental) Import an existing database instance.

        :param scope: -
        :param id: -
        :param instance_endpoint_address: (experimental) The endpoint address.
        :param instance_identifier: (experimental) The instance identifier.
        :param port: (experimental) The database port.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                instance_endpoint_address: builtins.str,
                instance_identifier: builtins.str,
                port: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = DatabaseInstanceAttributes(
            instance_endpoint_address=instance_endpoint_address,
            instance_identifier=instance_identifier,
            port=port,
        )

        return typing.cast(IDatabaseInstance, jsii.sinvoke(cls, "fromDatabaseInstanceAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[aws_cdk.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
    ) -> aws_cdk.aws_cloudwatch.Metric:
        '''(experimental) Return the given named metric associated with this database instance.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Use the factory functions on the ``Stats`` object to construct valid input strings. Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: experimental
        :inheritdoc: true
        '''
        if __debug__:
            def stub(
                metric_name: builtins.str,
                *,
                account: typing.Optional[builtins.str] = None,
                color: typing.Optional[builtins.str] = None,
                dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                label: typing.Optional[builtins.str] = None,
                period: typing.Optional[aws_cdk.Duration] = None,
                region: typing.Optional[builtins.str] = None,
                statistic: typing.Optional[builtins.str] = None,
                unit: typing.Optional[aws_cdk.aws_cloudwatch.Unit] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = aws_cdk.aws_cloudwatch.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(aws_cdk.aws_cloudwatch.Metric, jsii.invoke(self, "metric", [metric_name, props]))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    @abc.abstractmethod
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :inheritdoc: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    @abc.abstractmethod
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :inheritdoc: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    @abc.abstractmethod
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        :inheritdoc: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    @abc.abstractmethod
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        :inheritdoc: true
        '''
        ...


class _DatabaseInstanceBaseProxy(
    DatabaseInstanceBase,
    jsii.proxy_for(aws_cdk.Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DatabaseInstanceBase).__jsii_proxy_class__ = lambda : _DatabaseInstanceBaseProxy


@jsii.implements(IDatabaseCluster)
class DatabaseCluster(
    DatabaseClusterBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseCluster",
):
    '''(experimental) Create a clustered database with a given number of instances.

    :stability: experimental
    :resource: AWS::Neptune::DBCluster
    :exampleMetadata: infused

    Example::

        cluster = neptune.DatabaseCluster(self, "Database",
            vpc=vpc,
            instance_type=neptune.InstanceType.R5_LARGE,
            instances=2
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        instance_type: InstanceType,
        vpc: aws_cdk.aws_ec2.IVpc,
        associated_roles: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IRole]] = None,
        auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
        backup_retention: typing.Optional[aws_cdk.Duration] = None,
        cloudwatch_logs_exports: typing.Optional[typing.Sequence[LogType]] = None,
        cloudwatch_logs_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
        cloudwatch_logs_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
        db_cluster_name: typing.Optional[builtins.str] = None,
        deletion_protection: typing.Optional[builtins.bool] = None,
        engine_version: typing.Optional[EngineVersion] = None,
        iam_authentication: typing.Optional[builtins.bool] = None,
        instance_identifier_base: typing.Optional[builtins.str] = None,
        instances: typing.Optional[jsii.Number] = None,
        kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
        parameter_group: typing.Optional[IParameterGroup] = None,
        port: typing.Optional[jsii.Number] = None,
        preferred_backup_window: typing.Optional[builtins.str] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        storage_encrypted: typing.Optional[builtins.bool] = None,
        subnet_group: typing.Optional[ISubnetGroup] = None,
        vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param vpc: (experimental) What subnets to run the Neptune instances in. Must be at least 2 subnets in two different AZs.
        :param associated_roles: (experimental) A list of AWS Identity and Access Management (IAM) role that can be used by the cluster to access other AWS services. Default: - No role is attached to the cluster.
        :param auto_minor_version_upgrade: (experimental) If set to true, Neptune will automatically update the engine of the entire cluster to the latest minor version after a stabilization window of 2 to 3 weeks. Default: - false
        :param backup_retention: (experimental) How many days to retain the backup. Default: - cdk.Duration.days(1)
        :param cloudwatch_logs_exports: (experimental) The list of log types that need to be enabled for exporting to CloudWatch Logs. Default: - no log exports
        :param cloudwatch_logs_retention: (experimental) The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``Infinity``. Default: - logs never expire
        :param cloudwatch_logs_retention_role: (experimental) The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - a new role is created.
        :param cluster_parameter_group: (experimental) Additional parameters to pass to the database engine. Default: - No parameter group.
        :param db_cluster_name: (experimental) An optional identifier for the cluster. Default: - A name is automatically generated.
        :param deletion_protection: (experimental) Indicates whether the DB cluster should have deletion protection enabled. Default: - true if ``removalPolicy`` is RETAIN, false otherwise
        :param engine_version: (experimental) What version of the database to start. Default: - The default engine version.
        :param iam_authentication: (experimental) Map AWS Identity and Access Management (IAM) accounts to database accounts. Default: - ``false``
        :param instance_identifier_base: (experimental) Base identifier for instances. Every replica is named by appending the replica number to this string, 1-based. Default: - ``dbClusterName`` is used with the word "Instance" appended. If ``dbClusterName`` is not provided, the identifier is automatically generated.
        :param instances: (experimental) Number of Neptune compute instances. Default: 1
        :param kms_key: (experimental) The KMS key for storage encryption. Default: - default master key.
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param port: (experimental) The port the Neptune cluster will listen on. Default: - The default engine port
        :param preferred_backup_window: (experimental) A daily time range in 24-hours UTC format in which backups preferably execute. Must be at least 30 minutes long. Example: '01:00-02:00' Default: - a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see
        :param preferred_maintenance_window: (experimental) A weekly time range in which maintenance should preferably execute. Must be at least 30 minutes long. Example: 'tue:04:17-tue:04:47' Default: - 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week.
        :param removal_policy: (experimental) The removal policy to apply when the cluster and its instances are removed or replaced during a stack update, or when the stack is deleted. This removal policy also applies to the implicit security group created for the cluster if one is not supplied as a parameter. Default: - Retain cluster.
        :param security_groups: (experimental) Security group. Default: a new security group is created.
        :param storage_encrypted: (experimental) Whether to enable storage encryption. Default: true
        :param subnet_group: (experimental) Existing subnet group for the cluster. Default: - a new subnet group will be created.
        :param vpc_subnets: (experimental) Where to place the instances within the VPC. Default: private subnets

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                instance_type: InstanceType,
                vpc: aws_cdk.aws_ec2.IVpc,
                associated_roles: typing.Optional[typing.Sequence[aws_cdk.aws_iam.IRole]] = None,
                auto_minor_version_upgrade: typing.Optional[builtins.bool] = None,
                backup_retention: typing.Optional[aws_cdk.Duration] = None,
                cloudwatch_logs_exports: typing.Optional[typing.Sequence[LogType]] = None,
                cloudwatch_logs_retention: typing.Optional[aws_cdk.aws_logs.RetentionDays] = None,
                cloudwatch_logs_retention_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                cluster_parameter_group: typing.Optional[IClusterParameterGroup] = None,
                db_cluster_name: typing.Optional[builtins.str] = None,
                deletion_protection: typing.Optional[builtins.bool] = None,
                engine_version: typing.Optional[EngineVersion] = None,
                iam_authentication: typing.Optional[builtins.bool] = None,
                instance_identifier_base: typing.Optional[builtins.str] = None,
                instances: typing.Optional[jsii.Number] = None,
                kms_key: typing.Optional[aws_cdk.aws_kms.IKey] = None,
                parameter_group: typing.Optional[IParameterGroup] = None,
                port: typing.Optional[jsii.Number] = None,
                preferred_backup_window: typing.Optional[builtins.str] = None,
                preferred_maintenance_window: typing.Optional[builtins.str] = None,
                removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                storage_encrypted: typing.Optional[builtins.bool] = None,
                subnet_group: typing.Optional[ISubnetGroup] = None,
                vpc_subnets: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseClusterProps(
            instance_type=instance_type,
            vpc=vpc,
            associated_roles=associated_roles,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            backup_retention=backup_retention,
            cloudwatch_logs_exports=cloudwatch_logs_exports,
            cloudwatch_logs_retention=cloudwatch_logs_retention,
            cloudwatch_logs_retention_role=cloudwatch_logs_retention_role,
            cluster_parameter_group=cluster_parameter_group,
            db_cluster_name=db_cluster_name,
            deletion_protection=deletion_protection,
            engine_version=engine_version,
            iam_authentication=iam_authentication,
            instance_identifier_base=instance_identifier_base,
            instances=instances,
            kms_key=kms_key,
            parameter_group=parameter_group,
            port=port,
            preferred_backup_window=preferred_backup_window,
            preferred_maintenance_window=preferred_maintenance_window,
            removal_policy=removal_policy,
            security_groups=security_groups,
            storage_encrypted=storage_encrypted,
            subnet_group=subnet_group,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="DEFAULT_NUM_INSTANCES")
    def DEFAULT_NUM_INSTANCES(cls) -> jsii.Number:
        '''(experimental) The default number of instances in the Neptune cluster if none are specified.

        :stability: experimental
        '''
        return typing.cast(jsii.Number, jsii.sget(cls, "DEFAULT_NUM_INSTANCES"))

    @builtins.property
    @jsii.member(jsii_name="clusterEndpoint")
    def cluster_endpoint(self) -> Endpoint:
        '''(experimental) The endpoint to use for read/write operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdentifier")
    def cluster_identifier(self) -> builtins.str:
        '''(experimental) Identifier of the cluster.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="clusterReadEndpoint")
    def cluster_read_endpoint(self) -> Endpoint:
        '''(experimental) Endpoint to use for load-balanced read-only operations.

        :stability: experimental
        '''
        return typing.cast(Endpoint, jsii.get(self, "clusterReadEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="clusterResourceIdentifier")
    def cluster_resource_identifier(self) -> builtins.str:
        '''(experimental) The resource id for the cluster;

        for example: cluster-ABCD1234EFGH5678IJKL90MNOP. The cluster ID uniquely
        identifies the cluster and is used in things like IAM authentication policies.

        :stability: experimental
        :attribute: ClusterResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "clusterResourceIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> aws_cdk.aws_ec2.Connections:
        '''(experimental) The connections object to implement IConnectable.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoints")
    def instance_endpoints(self) -> typing.List[Endpoint]:
        '''(experimental) Endpoints which address each individual instance.

        :stability: experimental
        '''
        return typing.cast(typing.List[Endpoint], jsii.get(self, "instanceEndpoints"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifiers")
    def instance_identifiers(self) -> typing.List[builtins.str]:
        '''(experimental) Identifiers of the instance.

        :stability: experimental
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "instanceIdentifiers"))

    @builtins.property
    @jsii.member(jsii_name="subnetGroup")
    def subnet_group(self) -> ISubnetGroup:
        '''(experimental) Subnet group used by the DB.

        :stability: experimental
        '''
        return typing.cast(ISubnetGroup, jsii.get(self, "subnetGroup"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> aws_cdk.aws_ec2.IVpc:
        '''(experimental) The VPC where the DB subnet group is created.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.IVpc, jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="vpcSubnets")
    def vpc_subnets(self) -> aws_cdk.aws_ec2.SubnetSelection:
        '''(experimental) The subnets used by the DB subnet group.

        :stability: experimental
        '''
        return typing.cast(aws_cdk.aws_ec2.SubnetSelection, jsii.get(self, "vpcSubnets"))

    @builtins.property
    @jsii.member(jsii_name="enableIamAuthentication")
    def _enable_iam_authentication(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "enableIamAuthentication"))

    @_enable_iam_authentication.setter
    def _enable_iam_authentication(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            def stub(value: typing.Optional[builtins.bool]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableIamAuthentication", value)


@jsii.implements(IDatabaseInstance)
class DatabaseInstance(
    DatabaseInstanceBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-neptune-alpha.DatabaseInstance",
):
    '''(experimental) A database instance.

    :stability: experimental
    :resource: AWS::Neptune::DBInstance
    :exampleMetadata: fixture=with-cluster infused

    Example::

        replica1 = neptune.DatabaseInstance(self, "Instance",
            cluster=cluster,
            instance_type=neptune.InstanceType.R5_LARGE
        )
    '''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        cluster: IDatabaseCluster,
        instance_type: InstanceType,
        availability_zone: typing.Optional[builtins.str] = None,
        db_instance_name: typing.Optional[builtins.str] = None,
        parameter_group: typing.Optional[IParameterGroup] = None,
        removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param cluster: (experimental) The Neptune database cluster the instance should launch into.
        :param instance_type: (experimental) What type of instance to start for the replicas.
        :param availability_zone: (experimental) The name of the Availability Zone where the DB instance will be located. Default: - no preference
        :param db_instance_name: (experimental) A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. Default: - a CloudFormation generated name
        :param parameter_group: (experimental) The DB parameter group to associate with the instance. Default: no parameter group
        :param removal_policy: (experimental) The CloudFormation policy to apply when the instance is removed from the stack or replaced during an update. Default: RemovalPolicy.Retain

        :stability: experimental
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id: builtins.str,
                *,
                cluster: IDatabaseCluster,
                instance_type: InstanceType,
                availability_zone: typing.Optional[builtins.str] = None,
                db_instance_name: typing.Optional[builtins.str] = None,
                parameter_group: typing.Optional[IParameterGroup] = None,
                removal_policy: typing.Optional[aws_cdk.RemovalPolicy] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DatabaseInstanceProps(
            cluster=cluster,
            instance_type=instance_type,
            availability_zone=availability_zone,
            db_instance_name=db_instance_name,
            parameter_group=parameter_group,
            removal_policy=removal_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> IDatabaseCluster:
        '''(experimental) The instance's database cluster.

        :stability: experimental
        '''
        return typing.cast(IDatabaseCluster, jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointAddress")
    def db_instance_endpoint_address(self) -> builtins.str:
        '''(experimental) The instance endpoint address.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointAddress"))

    @builtins.property
    @jsii.member(jsii_name="dbInstanceEndpointPort")
    def db_instance_endpoint_port(self) -> builtins.str:
        '''(experimental) The instance endpoint port.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dbInstanceEndpointPort"))

    @builtins.property
    @jsii.member(jsii_name="instanceEndpoint")
    def instance_endpoint(self) -> Endpoint:
        '''(experimental) The instance endpoint.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(Endpoint, jsii.get(self, "instanceEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdentifier")
    def instance_identifier(self) -> builtins.str:
        '''(experimental) The instance identifier.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "instanceIdentifier"))


__all__ = [
    "ClusterParameterGroup",
    "ClusterParameterGroupProps",
    "DatabaseCluster",
    "DatabaseClusterAttributes",
    "DatabaseClusterBase",
    "DatabaseClusterProps",
    "DatabaseInstance",
    "DatabaseInstanceAttributes",
    "DatabaseInstanceBase",
    "DatabaseInstanceProps",
    "Endpoint",
    "EngineVersion",
    "IClusterParameterGroup",
    "IDatabaseCluster",
    "IDatabaseInstance",
    "IParameterGroup",
    "ISubnetGroup",
    "InstanceType",
    "LogType",
    "ParameterGroup",
    "ParameterGroupFamily",
    "ParameterGroupProps",
    "SubnetGroup",
    "SubnetGroupProps",
]

publication.publish()
