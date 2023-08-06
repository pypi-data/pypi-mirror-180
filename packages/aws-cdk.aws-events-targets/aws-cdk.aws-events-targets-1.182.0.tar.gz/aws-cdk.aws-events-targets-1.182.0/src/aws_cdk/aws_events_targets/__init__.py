'''
# Event Targets for Amazon EventBridge

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library contains integration classes to send Amazon EventBridge to any
number of supported AWS Services. Instances of these classes should be passed
to the `rule.addTarget()` method.

Currently supported are:

* [Start a CodeBuild build](#start-a-codebuild-build)
* [Start a CodePipeline pipeline](#start-a-codepipeline-pipeline)
* Run an ECS task
* [Invoke a Lambda function](#invoke-a-lambda-function)
* [Invoke a API Gateway REST API](#invoke-an-api-gateway-rest-api)
* Publish a message to an SNS topic
* Send a message to an SQS queue
* [Start a StepFunctions state machine](#start-a-stepfunctions-state-machine)
* [Queue a Batch job](#queue-a-batch-job)
* Make an AWS API call
* Put a record to a Kinesis stream
* [Log an event into a LogGroup](#log-an-event-into-a-loggroup)
* Put a record to a Kinesis Data Firehose stream
* [Put an event on an EventBridge bus](#put-an-event-on-an-eventbridge-bus)
* [Send an event to EventBridge API Destination](#invoke-an-api-destination)

See the README of the `@aws-cdk/aws-events` library for more information on
EventBridge.

## Event retry policy and using dead-letter queues

The Codebuild, CodePipeline, Lambda, StepFunctions, LogGroup and SQSQueue targets support attaching a [dead letter queue and setting retry policies](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html). See the [lambda example](#invoke-a-lambda-function).
Use [escape hatches](https://docs.aws.amazon.com/cdk/latest/guide/cfn_layer.html) for the other target types.

## Invoke a Lambda function

Use the `LambdaFunction` target to invoke a lambda function.

The code snippet below creates an event rule with a Lambda function as a target
triggered for every events from `aws.ec2` source. You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html).

```python
import aws_cdk.aws_lambda as lambda_


fn = lambda_.Function(self, "MyFunc",
    runtime=lambda_.Runtime.NODEJS_14_X,
    handler="index.handler",
    code=lambda_.Code.from_inline("exports.handler = handler.toString()")
)

rule = events.Rule(self, "rule",
    event_pattern=events.EventPattern(
        source=["aws.ec2"]
    )
)

queue = sqs.Queue(self, "Queue")

rule.add_target(targets.LambdaFunction(fn,
    dead_letter_queue=queue,  # Optional: add a dead letter queue
    max_event_age=cdk.Duration.hours(2),  # Optional: set the maxEventAge retry policy
    retry_attempts=2
))
```

## Log an event into a LogGroup

Use the `LogGroup` target to log your events in a CloudWatch LogGroup.

For example, the following code snippet creates an event rule with a CloudWatch LogGroup as a target.
Every events sent from the `aws.ec2` source will be sent to the CloudWatch LogGroup.

```python
import aws_cdk.aws_logs as logs


log_group = logs.LogGroup(self, "MyLogGroup",
    log_group_name="MyLogGroup"
)

rule = events.Rule(self, "rule",
    event_pattern=events.EventPattern(
        source=["aws.ec2"]
    )
)

rule.add_target(targets.CloudWatchLogGroup(log_group))
```

## Start a CodeBuild build

Use the `CodeBuildProject` target to trigger a CodeBuild project.

The code snippet below creates a CodeCommit repository that triggers a CodeBuild project
on commit to the master branch. You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html).

```python
import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_codecommit as codecommit


repo = codecommit.Repository(self, "MyRepo",
    repository_name="aws-cdk-codebuild-events"
)

project = codebuild.Project(self, "MyProject",
    source=codebuild.Source.code_commit(repository=repo)
)

dead_letter_queue = sqs.Queue(self, "DeadLetterQueue")

# trigger a build when a commit is pushed to the repo
on_commit_rule = repo.on_commit("OnCommit",
    target=targets.CodeBuildProject(project,
        dead_letter_queue=dead_letter_queue
    ),
    branches=["master"]
)
```

## Start a CodePipeline pipeline

Use the `CodePipeline` target to trigger a CodePipeline pipeline.

The code snippet below creates a CodePipeline pipeline that is triggered every hour

```python
import aws_cdk.aws_codepipeline as codepipeline


pipeline = codepipeline.Pipeline(self, "Pipeline")

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.expression("rate(1 hour)")
)

rule.add_target(targets.CodePipeline(pipeline))
```

## Start a StepFunctions state machine

Use the `SfnStateMachine` target to trigger a State Machine.

The code snippet below creates a Simple StateMachine that is triggered every minute with a
dummy object as input.
You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html)
to the target.

```python
import aws_cdk.aws_iam as iam
import aws_cdk.aws_stepfunctions as sfn


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.minutes(1))
)

dlq = sqs.Queue(self, "DeadLetterQueue")

role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("events.amazonaws.com")
)
state_machine = sfn.StateMachine(self, "SM",
    definition=sfn.Wait(self, "Hello", time=sfn.WaitTime.duration(cdk.Duration.seconds(10)))
)

rule.add_target(targets.SfnStateMachine(state_machine,
    input=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
    dead_letter_queue=dlq,
    role=role
))
```

## Queue a Batch job

Use the `BatchJob` target to queue a Batch job.

The code snippet below creates a Simple JobQueue that is triggered every hour with a
dummy object as input.
You can optionally attach a
[dead letter queue](https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html)
to the target.

```python
import aws_cdk.aws_batch as batch
from aws_cdk.aws_ecs import ContainerImage


job_queue = batch.JobQueue(self, "MyQueue",
    compute_environments=[batch.JobQueueComputeEnvironment(
        compute_environment=batch.ComputeEnvironment(self, "ComputeEnvironment",
            managed=False
        ),
        order=1
    )
    ]
)

job_definition = batch.JobDefinition(self, "MyJob",
    container=batch.JobDefinitionContainer(
        image=ContainerImage.from_registry("test-repo")
    )
)

queue = sqs.Queue(self, "Queue")

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.hours(1))
)

rule.add_target(targets.BatchJob(job_queue.job_queue_arn, job_queue, job_definition.job_definition_arn, job_definition,
    dead_letter_queue=queue,
    event=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
    retry_attempts=2,
    max_event_age=cdk.Duration.hours(2)
))
```

## Invoke an API Gateway REST API

Use the `ApiGateway` target to trigger a REST API.

The code snippet below creates a Api Gateway REST API that is invoked every hour.

```python
import aws_cdk.aws_apigateway as api
import aws_cdk.aws_lambda as lambda_


rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.minutes(1))
)

fn = lambda_.Function(self, "MyFunc",
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_14_X,
    code=lambda_.Code.from_inline("exports.handler = e => {}")
)

rest_api = api.LambdaRestApi(self, "MyRestAPI", handler=fn)

dlq = sqs.Queue(self, "DeadLetterQueue")

rule.add_target(
    targets.ApiGateway(rest_api,
        path="/*/test",
        method="GET",
        stage="prod",
        path_parameter_values=["path-value"],
        header_parameters={
            "Header1": "header1"
        },
        query_string_parameters={
            "QueryParam1": "query-param-1"
        },
        dead_letter_queue=dlq
    ))
```

## Invoke an API Destination

Use the `targets.ApiDestination` target to trigger an external API. You need to
create an `events.Connection` and `events.ApiDestination` as well.

The code snippet below creates an external destination that is invoked every hour.

```python
connection = events.Connection(self, "Connection",
    authorization=events.Authorization.api_key("x-api-key", SecretValue.secrets_manager("ApiSecretName")),
    description="Connection with API Key x-api-key"
)

destination = events.ApiDestination(self, "Destination",
    connection=connection,
    endpoint="https://example.com",
    description="Calling example.com with API key x-api-key"
)

rule = events.Rule(self, "Rule",
    schedule=events.Schedule.rate(cdk.Duration.minutes(1)),
    targets=[targets.ApiDestination(destination)]
)
```

## Put an event on an EventBridge bus

Use the `EventBus` target to route event to a different EventBus.

The code snippet below creates the scheduled event rule that route events to an imported event bus.

```python
rule = events.Rule(self, "Rule",
    schedule=events.Schedule.expression("rate(1 minute)")
)

rule.add_target(targets.EventBus(
    events.EventBus.from_event_bus_arn(self, "External", "arn:aws:events:eu-west-1:999999999999:event-bus/test-bus")))
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

import aws_cdk.aws_apigateway
import aws_cdk.aws_codebuild
import aws_cdk.aws_codepipeline
import aws_cdk.aws_ec2
import aws_cdk.aws_ecs
import aws_cdk.aws_events
import aws_cdk.aws_iam
import aws_cdk.aws_kinesis
import aws_cdk.aws_kinesisfirehose
import aws_cdk.aws_lambda
import aws_cdk.aws_logs
import aws_cdk.aws_sns
import aws_cdk.aws_sqs
import aws_cdk.aws_stepfunctions
import aws_cdk.core


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class ApiDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.ApiDestination",
):
    '''Use an API Destination rule target.

    :exampleMetadata: infused

    Example::

        connection = events.Connection(self, "Connection",
            authorization=events.Authorization.api_key("x-api-key", SecretValue.secrets_manager("ApiSecretName")),
            description="Connection with API Key x-api-key"
        )
        
        destination = events.ApiDestination(self, "Destination",
            connection=connection,
            endpoint="https://example.com",
            description="Calling example.com with API key x-api-key"
        )
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(cdk.Duration.minutes(1)),
            targets=[targets.ApiDestination(destination)]
        )
    '''

    def __init__(
        self,
        api_destination: aws_cdk.aws_events.IApiDestination,
        *,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param api_destination: -
        :param event: The event to send. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target. Default: - a new role will be created
        :param header_parameters: Additional headers sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none
        :param path_parameter_values: Path parameters to insert in place of path wildcards (``*``). If the API destination has a wilcard in the path, these path parts will be inserted in that place. Default: - none
        :param query_string_parameters: Additional query string parameters sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                api_destination: aws_cdk.aws_events.IApiDestination,
                *,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
                query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument api_destination", value=api_destination, expected_type=type_hints["api_destination"])
        props = ApiDestinationProps(
            event=event,
            event_role=event_role,
            header_parameters=header_parameters,
            path_parameter_values=path_parameter_values,
            query_string_parameters=query_string_parameters,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [api_destination, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger API destinations from an EventBridge event.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class ApiGateway(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.ApiGateway",
):
    '''Use an API Gateway REST APIs as a target for Amazon EventBridge rules.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_apigateway as api
        import aws_cdk.aws_lambda as lambda_
        
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(cdk.Duration.minutes(1))
        )
        
        fn = lambda_.Function(self, "MyFunc",
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_14_X,
            code=lambda_.Code.from_inline("exports.handler = e => {}")
        )
        
        rest_api = api.LambdaRestApi(self, "MyRestAPI", handler=fn)
        
        dlq = sqs.Queue(self, "DeadLetterQueue")
        
        rule.add_target(
            targets.ApiGateway(rest_api,
                path="/*/test",
                method="GET",
                stage="prod",
                path_parameter_values=["path-value"],
                header_parameters={
                    "Header1": "header1"
                },
                query_string_parameters={
                    "QueryParam1": "query-param-1"
                },
                dead_letter_queue=dlq
            ))
    '''

    def __init__(
        self,
        rest_api: aws_cdk.aws_apigateway.RestApi,
        *,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        method: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        post_body: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        stage: typing.Optional[builtins.str] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param rest_api: -
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created
        :param header_parameters: The headers to be set when requesting API. Default: no header parameters
        :param method: The method for api resource invoked by the rule. Default: '*' that treated as ANY
        :param path: The api resource invoked by the rule. We can use wildcards('*') to specify the path. In that case, an equal number of real values must be specified for pathParameterValues. Default: '/'
        :param path_parameter_values: The path parameter values to be used to populate to wildcards("*") of requesting api path. Default: no path parameters
        :param post_body: This will be the post request body send to the API. Default: the entire EventBridge event
        :param query_string_parameters: The query parameters to be set when requesting API. Default: no querystring parameters
        :param stage: The deploy stage of api gateway invoked by the rule. Default: the value of deploymentStage.stageName of target api gateway.
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                rest_api: aws_cdk.aws_apigateway.RestApi,
                *,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                method: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
                path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
                post_body: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                stage: typing.Optional[builtins.str] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        props = ApiGatewayProps(
            event_role=event_role,
            header_parameters=header_parameters,
            method=method,
            path=path,
            path_parameter_values=path_parameter_values,
            post_body=post_body,
            query_string_parameters=query_string_parameters,
            stage=stage,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [rest_api, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this API Gateway REST APIs as a result from an EventBridge event.

        :param rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sqs-permissions
        '''
        if __debug__:
            def stub(
                rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="restApi")
    def rest_api(self) -> aws_cdk.aws_apigateway.RestApi:
        return typing.cast(aws_cdk.aws_apigateway.RestApi, jsii.get(self, "restApi"))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class AwsApi(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.AwsApi"):
    '''Use an AWS Lambda function that makes API calls as an event rule target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_events_targets as events_targets
        import aws_cdk.aws_iam as iam
        
        # parameters: Any
        # policy_statement: iam.PolicyStatement
        
        aws_api = events_targets.AwsApi(
            action="action",
            service="service",
        
            # the properties below are optional
            api_version="apiVersion",
            catch_error_pattern="catchErrorPattern",
            parameters=parameters,
            policy_statement=policy_statement
        )
    '''

    def __init__(
        self,
        *,
        policy_statement: typing.Optional[aws_cdk.aws_iam.PolicyStatement] = None,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        catch_error_pattern: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
    ) -> None:
        '''
        :param policy_statement: The IAM policy statement to allow the API call. Use only if resource restriction is needed. Default: - extract the permission from the API call
        :param action: The service action to call.
        :param service: The service to call.
        :param api_version: API version to use for the service. Default: - use latest available API version
        :param catch_error_pattern: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param parameters: The parameters for the service action. Default: - no parameters
        '''
        props = AwsApiProps(
            policy_statement=policy_statement,
            action=action,
            service=service,
            api_version=api_version,
            catch_error_pattern=catch_error_pattern,
            parameters=parameters,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: aws_cdk.aws_events.IRule,
        id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this AwsApi as a result from an EventBridge event.

        :param rule: -
        :param id: -
        '''
        if __debug__:
            def stub(
                rule: aws_cdk.aws_events.IRule,
                id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [rule, id]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.AwsApiInput",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "service": "service",
        "api_version": "apiVersion",
        "catch_error_pattern": "catchErrorPattern",
        "parameters": "parameters",
    },
)
class AwsApiInput:
    def __init__(
        self,
        *,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        catch_error_pattern: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
    ) -> None:
        '''Rule target input for an AwsApi target.

        :param action: The service action to call.
        :param service: The service to call.
        :param api_version: API version to use for the service. Default: - use latest available API version
        :param catch_error_pattern: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param parameters: The parameters for the service action. Default: - no parameters

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            
            # parameters: Any
            
            aws_api_input = events_targets.AwsApiInput(
                action="action",
                service="service",
            
                # the properties below are optional
                api_version="apiVersion",
                catch_error_pattern="catchErrorPattern",
                parameters=parameters
            )
        '''
        if __debug__:
            def stub(
                *,
                action: builtins.str,
                service: builtins.str,
                api_version: typing.Optional[builtins.str] = None,
                catch_error_pattern: typing.Optional[builtins.str] = None,
                parameters: typing.Any = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument catch_error_pattern", value=catch_error_pattern, expected_type=type_hints["catch_error_pattern"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "service": service,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if catch_error_pattern is not None:
            self._values["catch_error_pattern"] = catch_error_pattern
        if parameters is not None:
            self._values["parameters"] = parameters

    @builtins.property
    def action(self) -> builtins.str:
        '''The service action to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The service to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version to use for the service.

        :default: - use latest available API version

        :see: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/locking-api-versions.html
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catch_error_pattern(self) -> typing.Optional[builtins.str]:
        '''The regex pattern to use to catch API errors.

        The ``code`` property of the
        ``Error`` object will be tested against this pattern. If there is a match an
        error will not be thrown.

        :default: - do not catch errors
        '''
        result = self._values.get("catch_error_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters for the service action.

        :default: - no parameters

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsApiInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.AwsApiProps",
    jsii_struct_bases=[AwsApiInput],
    name_mapping={
        "action": "action",
        "service": "service",
        "api_version": "apiVersion",
        "catch_error_pattern": "catchErrorPattern",
        "parameters": "parameters",
        "policy_statement": "policyStatement",
    },
)
class AwsApiProps(AwsApiInput):
    def __init__(
        self,
        *,
        action: builtins.str,
        service: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
        catch_error_pattern: typing.Optional[builtins.str] = None,
        parameters: typing.Any = None,
        policy_statement: typing.Optional[aws_cdk.aws_iam.PolicyStatement] = None,
    ) -> None:
        '''Properties for an AwsApi target.

        :param action: The service action to call.
        :param service: The service to call.
        :param api_version: API version to use for the service. Default: - use latest available API version
        :param catch_error_pattern: The regex pattern to use to catch API errors. The ``code`` property of the ``Error`` object will be tested against this pattern. If there is a match an error will not be thrown. Default: - do not catch errors
        :param parameters: The parameters for the service action. Default: - no parameters
        :param policy_statement: The IAM policy statement to allow the API call. Use only if resource restriction is needed. Default: - extract the permission from the API call

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_iam as iam
            
            # parameters: Any
            # policy_statement: iam.PolicyStatement
            
            aws_api_props = events_targets.AwsApiProps(
                action="action",
                service="service",
            
                # the properties below are optional
                api_version="apiVersion",
                catch_error_pattern="catchErrorPattern",
                parameters=parameters,
                policy_statement=policy_statement
            )
        '''
        if __debug__:
            def stub(
                *,
                action: builtins.str,
                service: builtins.str,
                api_version: typing.Optional[builtins.str] = None,
                catch_error_pattern: typing.Optional[builtins.str] = None,
                parameters: typing.Any = None,
                policy_statement: typing.Optional[aws_cdk.aws_iam.PolicyStatement] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument catch_error_pattern", value=catch_error_pattern, expected_type=type_hints["catch_error_pattern"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument policy_statement", value=policy_statement, expected_type=type_hints["policy_statement"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "service": service,
        }
        if api_version is not None:
            self._values["api_version"] = api_version
        if catch_error_pattern is not None:
            self._values["catch_error_pattern"] = catch_error_pattern
        if parameters is not None:
            self._values["parameters"] = parameters
        if policy_statement is not None:
            self._values["policy_statement"] = policy_statement

    @builtins.property
    def action(self) -> builtins.str:
        '''The service action to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The service to call.

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version to use for the service.

        :default: - use latest available API version

        :see: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/locking-api-versions.html
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catch_error_pattern(self) -> typing.Optional[builtins.str]:
        '''The regex pattern to use to catch API errors.

        The ``code`` property of the
        ``Error`` object will be tested against this pattern. If there is a match an
        error will not be thrown.

        :default: - do not catch errors
        '''
        result = self._values.get("catch_error_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''The parameters for the service action.

        :default: - no parameters

        :see: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def policy_statement(self) -> typing.Optional[aws_cdk.aws_iam.PolicyStatement]:
        '''The IAM policy statement to allow the API call.

        Use only if
        resource restriction is needed.

        :default: - extract the permission from the API call
        '''
        result = self._values.get("policy_statement")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.PolicyStatement], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class BatchJob(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.BatchJob",
):
    '''Use an AWS Batch Job / Queue as an event rule target.

    Most likely the code will look something like this:
    ``new BatchJob(jobQueue.jobQueueArn, jobQueue, jobDefinition.jobDefinitionArn, jobDefinition)``

    In the future this API will be improved to be fully typed

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_batch as batch
        from aws_cdk.aws_ecs import ContainerImage
        
        
        job_queue = batch.JobQueue(self, "MyQueue",
            compute_environments=[batch.JobQueueComputeEnvironment(
                compute_environment=batch.ComputeEnvironment(self, "ComputeEnvironment",
                    managed=False
                ),
                order=1
            )
            ]
        )
        
        job_definition = batch.JobDefinition(self, "MyJob",
            container=batch.JobDefinitionContainer(
                image=ContainerImage.from_registry("test-repo")
            )
        )
        
        queue = sqs.Queue(self, "Queue")
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(cdk.Duration.hours(1))
        )
        
        rule.add_target(targets.BatchJob(job_queue.job_queue_arn, job_queue, job_definition.job_definition_arn, job_definition,
            dead_letter_queue=queue,
            event=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
            retry_attempts=2,
            max_event_age=cdk.Duration.hours(2)
        ))
    '''

    def __init__(
        self,
        job_queue_arn: builtins.str,
        job_queue_scope: aws_cdk.core.IConstruct,
        job_definition_arn: builtins.str,
        job_definition_scope: aws_cdk.core.IConstruct,
        *,
        attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        job_name: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param job_queue_arn: The JobQueue arn.
        :param job_queue_scope: The JobQueue Resource.
        :param job_definition_arn: The jobDefinition arn.
        :param job_definition_scope: The JobQueue Resource.
        :param attempts: The number of times to attempt to retry, if the job fails. Valid values are 1–10. Default: no retryStrategy is set
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event
        :param job_name: The name of the submitted job. Default: - Automatically generated
        :param size: The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000. Default: no arrayProperties are set
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                job_queue_arn: builtins.str,
                job_queue_scope: aws_cdk.core.IConstruct,
                job_definition_arn: builtins.str,
                job_definition_scope: aws_cdk.core.IConstruct,
                *,
                attempts: typing.Optional[jsii.Number] = None,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                job_name: typing.Optional[builtins.str] = None,
                size: typing.Optional[jsii.Number] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument job_queue_arn", value=job_queue_arn, expected_type=type_hints["job_queue_arn"])
            check_type(argname="argument job_queue_scope", value=job_queue_scope, expected_type=type_hints["job_queue_scope"])
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
            check_type(argname="argument job_definition_scope", value=job_definition_scope, expected_type=type_hints["job_definition_scope"])
        props = BatchJobProps(
            attempts=attempts,
            event=event,
            job_name=job_name,
            size=size,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [job_queue_arn, job_queue_scope, job_definition_arn, job_definition_scope, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger queue this batch job as a result from an EventBridge event.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [rule, _id]))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class CloudWatchLogGroup(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.CloudWatchLogGroup",
):
    '''Use an AWS CloudWatch LogGroup as an event rule target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs as logs
        
        
        log_group = logs.LogGroup(self, "MyLogGroup",
            log_group_name="MyLogGroup"
        )
        
        rule = events.Rule(self, "rule",
            event_pattern=events.EventPattern(
                source=["aws.ec2"]
            )
        )
        
        rule.add_target(targets.CloudWatchLogGroup(log_group))
    '''

    def __init__(
        self,
        log_group: aws_cdk.aws_logs.ILogGroup,
        *,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param log_group: -
        :param event: The event to send to the CloudWatch LogGroup. This will be the event logged into the CloudWatch LogGroup Default: - the entire EventBridge event
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                log_group: aws_cdk.aws_logs.ILogGroup,
                *,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        props = LogGroupProps(
            event=event,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [log_group, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to log an event into a CloudWatch LogGroup.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class CodeBuildProject(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.CodeBuildProject",
):
    '''Start a CodeBuild build when an Amazon EventBridge rule is triggered.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_sns as sns
        import aws_cdk.aws_events_targets as targets
        
        # repo: codecommit.Repository
        # project: codebuild.PipelineProject
        # my_topic: sns.Topic
        
        
        # starts a CodeBuild project when a commit is pushed to the "master" branch of the repo
        repo.on_commit("CommitToMaster",
            target=targets.CodeBuildProject(project),
            branches=["master"]
        )
        
        # publishes a message to an Amazon SNS topic when a comment is made on a pull request
        rule = repo.on_comment_on_pull_request("CommentOnPullRequest",
            target=targets.SnsTopic(my_topic)
        )
    '''

    def __init__(
        self,
        project: aws_cdk.aws_codebuild.IProject,
        *,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param project: -
        :param event: The event to send to CodeBuild. This will be the payload for the StartBuild API. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target (i.e., the codebuild) when the given rule is triggered. Default: - a new role will be created
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                project: aws_cdk.aws_codebuild.IProject,
                *,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        props = CodeBuildProjectProps(
            event=event,
            event_role=event_role,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [project, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Allows using build projects as event rule targets.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class CodePipeline(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.CodePipeline",
):
    '''Allows the pipeline to be used as an EventBridge rule target.

    :exampleMetadata: infused

    Example::

        # A pipeline being used as a target for a CloudWatch event rule.
        import aws_cdk.aws_events_targets as targets
        import aws_cdk.aws_events as events
        
        # pipeline: codepipeline.Pipeline
        
        
        # kick off the pipeline every day
        rule = events.Rule(self, "Daily",
            schedule=events.Schedule.rate(Duration.days(1))
        )
        rule.add_target(targets.CodePipeline(pipeline))
    '''

    def __init__(
        self,
        pipeline: aws_cdk.aws_codepipeline.IPipeline,
        *,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param pipeline: -
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                pipeline: aws_cdk.aws_codepipeline.IPipeline,
                *,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument pipeline", value=pipeline, expected_type=type_hints["pipeline"])
        options = CodePipelineTargetOptions(
            event_role=event_role,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [pipeline, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns the rule target specification.

        NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.ContainerOverride",
    jsii_struct_bases=[],
    name_mapping={
        "container_name": "containerName",
        "command": "command",
        "cpu": "cpu",
        "environment": "environment",
        "memory_limit": "memoryLimit",
        "memory_reservation": "memoryReservation",
    },
)
class ContainerOverride:
    def __init__(
        self,
        *,
        container_name: builtins.str,
        command: typing.Optional[typing.Sequence[builtins.str]] = None,
        cpu: typing.Optional[jsii.Number] = None,
        environment: typing.Optional[typing.Sequence[typing.Union["TaskEnvironmentVariable", typing.Dict[str, typing.Any]]]] = None,
        memory_limit: typing.Optional[jsii.Number] = None,
        memory_reservation: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param container_name: Name of the container inside the task definition.
        :param command: Command to run inside the container. Default: Default command
        :param cpu: The number of cpu units reserved for the container. Default: The default value from the task definition.
        :param environment: Variables to set in the container's environment.
        :param memory_limit: Hard memory limit on the container. Default: The default value from the task definition.
        :param memory_reservation: Soft memory limit on the container. Default: The default value from the task definition.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            
            container_override = events_targets.ContainerOverride(
                container_name="containerName",
            
                # the properties below are optional
                command=["command"],
                cpu=123,
                environment=[events_targets.TaskEnvironmentVariable(
                    name="name",
                    value="value"
                )],
                memory_limit=123,
                memory_reservation=123
            )
        '''
        if __debug__:
            def stub(
                *,
                container_name: builtins.str,
                command: typing.Optional[typing.Sequence[builtins.str]] = None,
                cpu: typing.Optional[jsii.Number] = None,
                environment: typing.Optional[typing.Sequence[typing.Union[TaskEnvironmentVariable, typing.Dict[str, typing.Any]]]] = None,
                memory_limit: typing.Optional[jsii.Number] = None,
                memory_reservation: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument command", value=command, expected_type=type_hints["command"])
            check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument memory_limit", value=memory_limit, expected_type=type_hints["memory_limit"])
            check_type(argname="argument memory_reservation", value=memory_reservation, expected_type=type_hints["memory_reservation"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_name": container_name,
        }
        if command is not None:
            self._values["command"] = command
        if cpu is not None:
            self._values["cpu"] = cpu
        if environment is not None:
            self._values["environment"] = environment
        if memory_limit is not None:
            self._values["memory_limit"] = memory_limit
        if memory_reservation is not None:
            self._values["memory_reservation"] = memory_reservation

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Name of the container inside the task definition.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Command to run inside the container.

        :default: Default command
        '''
        result = self._values.get("command")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cpu(self) -> typing.Optional[jsii.Number]:
        '''The number of cpu units reserved for the container.

        :default: The default value from the task definition.
        '''
        result = self._values.get("cpu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def environment(self) -> typing.Optional[typing.List["TaskEnvironmentVariable"]]:
        '''Variables to set in the container's environment.'''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.List["TaskEnvironmentVariable"]], result)

    @builtins.property
    def memory_limit(self) -> typing.Optional[jsii.Number]:
        '''Hard memory limit on the container.

        :default: The default value from the task definition.
        '''
        result = self._values.get("memory_limit")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def memory_reservation(self) -> typing.Optional[jsii.Number]:
        '''Soft memory limit on the container.

        :default: The default value from the task definition.
        '''
        result = self._values.get("memory_reservation")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerOverride(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class EcsTask(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-events-targets.EcsTask"):
    '''Start a task on an ECS cluster.

    :exampleMetadata: fixture=basic infused

    Example::

        from aws_cdk.aws_events import Rule, Schedule
        from aws_cdk.aws_events_targets import EcsTask
        from aws_cdk.aws_ecs import Cluster, TaskDefinition
        from aws_cdk.aws_iam import Role
        
        # cluster: Cluster
        # task_definition: TaskDefinition
        # role: Role
        
        
        ecs_task_target = EcsTask(cluster=cluster, task_definition=task_definition, role=role)
        
        Rule(self, "ScheduleRule",
            schedule=Schedule.cron(minute="0", hour="4"),
            targets=[ecs_task_target]
        )
    '''

    def __init__(
        self,
        *,
        cluster: aws_cdk.aws_ecs.ICluster,
        task_definition: aws_cdk.aws_ecs.ITaskDefinition,
        container_overrides: typing.Optional[typing.Sequence[typing.Union[ContainerOverride, typing.Dict[str, typing.Any]]]] = None,
        platform_version: typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cluster: Cluster where service will be deployed.
        :param task_definition: Task Definition of the task that should be started.
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param platform_version: The platform version on which to run your task. Unless you have specific compatibility requirements, you don't need to specify this. Default: - ECS will set the Fargate platform version to 'LATEST'
        :param role: Existing IAM role to run the ECS task. Default: A new IAM role is created
        :param security_group: (deprecated) Existing security group to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param security_groups: Existing security groups to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnet_selection: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param task_count: How many tasks should be started when this event is triggered. Default: 1
        '''
        props = EcsTaskProps(
            cluster=cluster,
            task_definition=task_definition,
            container_overrides=container_overrides,
            platform_version=platform_version,
            role=role,
            security_group=security_group,
            security_groups=security_groups,
            subnet_selection=subnet_selection,
            task_count=task_count,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Allows using tasks as target of EventBridge events.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="securityGroup")
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) The security group associated with the task.

        Only applicable with awsvpc network mode.

        :default: - A new security group is created.

        :deprecated: use securityGroups instead.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], jsii.get(self, "securityGroup"))

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''The security groups associated with the task.

        Only applicable with awsvpc network mode.

        :default: - A new security group is created.
        '''
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], jsii.get(self, "securityGroups"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.EcsTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "task_definition": "taskDefinition",
        "container_overrides": "containerOverrides",
        "platform_version": "platformVersion",
        "role": "role",
        "security_group": "securityGroup",
        "security_groups": "securityGroups",
        "subnet_selection": "subnetSelection",
        "task_count": "taskCount",
    },
)
class EcsTaskProps:
    def __init__(
        self,
        *,
        cluster: aws_cdk.aws_ecs.ICluster,
        task_definition: aws_cdk.aws_ecs.ITaskDefinition,
        container_overrides: typing.Optional[typing.Sequence[typing.Union[ContainerOverride, typing.Dict[str, typing.Any]]]] = None,
        platform_version: typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
        security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
        subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
        task_count: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties to define an ECS Event Task.

        :param cluster: Cluster where service will be deployed.
        :param task_definition: Task Definition of the task that should be started.
        :param container_overrides: Container setting overrides. Key is the name of the container to override, value is the values you want to override.
        :param platform_version: The platform version on which to run your task. Unless you have specific compatibility requirements, you don't need to specify this. Default: - ECS will set the Fargate platform version to 'LATEST'
        :param role: Existing IAM role to run the ECS task. Default: A new IAM role is created
        :param security_group: (deprecated) Existing security group to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param security_groups: Existing security groups to use for the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: A new security group is created
        :param subnet_selection: In what subnets to place the task's ENIs. (Only applicable in case the TaskDefinition is configured for AwsVpc networking) Default: Private subnets
        :param task_count: How many tasks should be started when this event is triggered. Default: 1

        :exampleMetadata: fixture=basic infused

        Example::

            from aws_cdk.aws_events import Rule, Schedule
            from aws_cdk.aws_events_targets import EcsTask
            from aws_cdk.aws_ecs import Cluster, TaskDefinition
            from aws_cdk.aws_iam import Role
            
            # cluster: Cluster
            # task_definition: TaskDefinition
            # role: Role
            
            
            ecs_task_target = EcsTask(cluster=cluster, task_definition=task_definition, role=role)
            
            Rule(self, "ScheduleRule",
                schedule=Schedule.cron(minute="0", hour="4"),
                targets=[ecs_task_target]
            )
        '''
        if isinstance(subnet_selection, dict):
            subnet_selection = aws_cdk.aws_ec2.SubnetSelection(**subnet_selection)
        if __debug__:
            def stub(
                *,
                cluster: aws_cdk.aws_ecs.ICluster,
                task_definition: aws_cdk.aws_ecs.ITaskDefinition,
                container_overrides: typing.Optional[typing.Sequence[typing.Union[ContainerOverride, typing.Dict[str, typing.Any]]]] = None,
                platform_version: typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                security_group: typing.Optional[aws_cdk.aws_ec2.ISecurityGroup] = None,
                security_groups: typing.Optional[typing.Sequence[aws_cdk.aws_ec2.ISecurityGroup]] = None,
                subnet_selection: typing.Optional[typing.Union[aws_cdk.aws_ec2.SubnetSelection, typing.Dict[str, typing.Any]]] = None,
                task_count: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument task_definition", value=task_definition, expected_type=type_hints["task_definition"])
            check_type(argname="argument container_overrides", value=container_overrides, expected_type=type_hints["container_overrides"])
            check_type(argname="argument platform_version", value=platform_version, expected_type=type_hints["platform_version"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument security_group", value=security_group, expected_type=type_hints["security_group"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument subnet_selection", value=subnet_selection, expected_type=type_hints["subnet_selection"])
            check_type(argname="argument task_count", value=task_count, expected_type=type_hints["task_count"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster": cluster,
            "task_definition": task_definition,
        }
        if container_overrides is not None:
            self._values["container_overrides"] = container_overrides
        if platform_version is not None:
            self._values["platform_version"] = platform_version
        if role is not None:
            self._values["role"] = role
        if security_group is not None:
            self._values["security_group"] = security_group
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if subnet_selection is not None:
            self._values["subnet_selection"] = subnet_selection
        if task_count is not None:
            self._values["task_count"] = task_count

    @builtins.property
    def cluster(self) -> aws_cdk.aws_ecs.ICluster:
        '''Cluster where service will be deployed.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(aws_cdk.aws_ecs.ICluster, result)

    @builtins.property
    def task_definition(self) -> aws_cdk.aws_ecs.ITaskDefinition:
        '''Task Definition of the task that should be started.'''
        result = self._values.get("task_definition")
        assert result is not None, "Required property 'task_definition' is missing"
        return typing.cast(aws_cdk.aws_ecs.ITaskDefinition, result)

    @builtins.property
    def container_overrides(self) -> typing.Optional[typing.List[ContainerOverride]]:
        '''Container setting overrides.

        Key is the name of the container to override, value is the
        values you want to override.
        '''
        result = self._values.get("container_overrides")
        return typing.cast(typing.Optional[typing.List[ContainerOverride]], result)

    @builtins.property
    def platform_version(
        self,
    ) -> typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion]:
        '''The platform version on which to run your task.

        Unless you have specific compatibility requirements, you don't need to specify this.

        :default: - ECS will set the Fargate platform version to 'LATEST'

        :see: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/platform_versions.html
        '''
        result = self._values.get("platform_version")
        return typing.cast(typing.Optional[aws_cdk.aws_ecs.FargatePlatformVersion], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''Existing IAM role to run the ECS task.

        :default: A new IAM role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def security_group(self) -> typing.Optional[aws_cdk.aws_ec2.ISecurityGroup]:
        '''(deprecated) Existing security group to use for the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        :default: A new security group is created

        :deprecated: use securityGroups instead

        :stability: deprecated
        '''
        result = self._values.get("security_group")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.ISecurityGroup], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]]:
        '''Existing security groups to use for the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        :default: A new security group is created
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[aws_cdk.aws_ec2.ISecurityGroup]], result)

    @builtins.property
    def subnet_selection(self) -> typing.Optional[aws_cdk.aws_ec2.SubnetSelection]:
        '''In what subnets to place the task's ENIs.

        (Only applicable in case the TaskDefinition is configured for AwsVpc networking)

        :default: Private subnets
        '''
        result = self._values.get("subnet_selection")
        return typing.cast(typing.Optional[aws_cdk.aws_ec2.SubnetSelection], result)

    @builtins.property
    def task_count(self) -> typing.Optional[jsii.Number]:
        '''How many tasks should be started when this event is triggered.

        :default: 1
        '''
        result = self._values.get("task_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class EventBus(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.EventBus",
):
    '''Notify an existing Event Bus of an event.

    :exampleMetadata: infused

    Example::

        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.expression("rate(1 minute)")
        )
        
        rule.add_target(targets.EventBus(
            events.EventBus.from_event_bus_arn(self, "External", "arn:aws:events:eu-west-1:999999999999:event-bus/test-bus")))
    '''

    def __init__(
        self,
        event_bus: aws_cdk.aws_events.IEventBus,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''
        :param event_bus: -
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param role: Role to be used to publish the event. Default: a new role is created.
        '''
        if __debug__:
            def stub(
                event_bus: aws_cdk.aws_events.IEventBus,
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument event_bus", value=event_bus, expected_type=type_hints["event_bus"])
        props = EventBusProps(dead_letter_queue=dead_letter_queue, role=role)

        jsii.create(self.__class__, self, [event_bus, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns the rule target specification.

        NOTE: Do not use the various ``inputXxx`` options. They can be set in a call to ``addTarget``.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [rule, _id]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.EventBusProps",
    jsii_struct_bases=[],
    name_mapping={"dead_letter_queue": "deadLetterQueue", "role": "role"},
)
class EventBusProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''Configuration properties of an Event Bus event.

        Cannot extend TargetBaseProps. Retry policy is not supported for Event bus targets.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param role: Role to be used to publish the event. Default: a new role is created.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_iam as iam
            import aws_cdk.aws_sqs as sqs
            
            # queue: sqs.Queue
            # role: iam.Role
            
            event_bus_props = events_targets.EventBusProps(
                dead_letter_queue=queue,
                role=role
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''Role to be used to publish the event.

        :default: a new role is created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBusProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class KinesisFirehoseStream(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.KinesisFirehoseStream",
):
    '''Customize the Firehose Stream Event Target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_events as events
        import aws_cdk.aws_events_targets as events_targets
        import aws_cdk.aws_kinesisfirehose as kinesisfirehose
        
        # cfn_delivery_stream: kinesisfirehose.CfnDeliveryStream
        # rule_target_input: events.RuleTargetInput
        
        kinesis_firehose_stream = events_targets.KinesisFirehoseStream(cfn_delivery_stream,
            message=rule_target_input
        )
    '''

    def __init__(
        self,
        stream: aws_cdk.aws_kinesisfirehose.CfnDeliveryStream,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
    ) -> None:
        '''
        :param stream: -
        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire Event Bridge event
        '''
        if __debug__:
            def stub(
                stream: aws_cdk.aws_kinesisfirehose.CfnDeliveryStream,
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisFirehoseStreamProps(message=message)

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this Firehose Stream as a result from a Event Bridge event.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.KinesisFirehoseStreamProps",
    jsii_struct_bases=[],
    name_mapping={"message": "message"},
)
class KinesisFirehoseStreamProps:
    def __init__(
        self,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
    ) -> None:
        '''Customize the Firehose Stream Event Target.

        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire Event Bridge event

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events as events
            import aws_cdk.aws_events_targets as events_targets
            
            # rule_target_input: events.RuleTargetInput
            
            kinesis_firehose_stream_props = events_targets.KinesisFirehoseStreamProps(
                message=rule_target_input
            )
        '''
        if __debug__:
            def stub(
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def message(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The message to send to the stream.

        Must be a valid JSON text passed to the target stream.

        :default: - the entire Event Bridge event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class KinesisStream(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.KinesisStream",
):
    '''Use a Kinesis Stream as a target for AWS CloudWatch event rules.

    Example::

        # put to a Kinesis stream every time code is committed
        # to a CodeCommit repository
        repository.on_commit("onCommit", target=targets.KinesisStream(stream))
    '''

    def __init__(
        self,
        stream: aws_cdk.aws_kinesis.IStream,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param stream: -
        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire CloudWatch event
        :param partition_key_path: Partition Key Path for records sent to this stream. Default: - eventId as the partition key
        '''
        if __debug__:
            def stub(
                stream: aws_cdk.aws_kinesis.IStream,
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                partition_key_path: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisStreamProps(
            message=message, partition_key_path=partition_key_path
        )

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this Kinesis Stream as a result from a CloudWatch event.

        :param _rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.KinesisStreamProps",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "partition_key_path": "partitionKeyPath"},
)
class KinesisStreamProps:
    def __init__(
        self,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        partition_key_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Customize the Kinesis Stream Event Target.

        :param message: The message to send to the stream. Must be a valid JSON text passed to the target stream. Default: - the entire CloudWatch event
        :param partition_key_path: Partition Key Path for records sent to this stream. Default: - eventId as the partition key

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events as events
            import aws_cdk.aws_events_targets as events_targets
            
            # rule_target_input: events.RuleTargetInput
            
            kinesis_stream_props = events_targets.KinesisStreamProps(
                message=rule_target_input,
                partition_key_path="partitionKeyPath"
            )
        '''
        if __debug__:
            def stub(
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                partition_key_path: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument partition_key_path", value=partition_key_path, expected_type=type_hints["partition_key_path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message
        if partition_key_path is not None:
            self._values["partition_key_path"] = partition_key_path

    @builtins.property
    def message(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The message to send to the stream.

        Must be a valid JSON text passed to the target stream.

        :default: - the entire CloudWatch event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def partition_key_path(self) -> typing.Optional[builtins.str]:
        '''Partition Key Path for records sent to this stream.

        :default: - eventId as the partition key
        '''
        result = self._values.get("partition_key_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class LambdaFunction(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.LambdaFunction",
):
    '''Use an AWS Lambda function as an event rule target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        
        
        fn = lambda_.Function(self, "MyFunc",
            runtime=lambda_.Runtime.NODEJS_14_X,
            handler="index.handler",
            code=lambda_.Code.from_inline("exports.handler = handler.toString()")
        )
        
        rule = events.Rule(self, "rule",
            event_pattern=events.EventPattern(
                source=["aws.ec2"]
            )
        )
        
        queue = sqs.Queue(self, "Queue")
        
        rule.add_target(targets.LambdaFunction(fn,
            dead_letter_queue=queue,  # Optional: add a dead letter queue
            max_event_age=cdk.Duration.hours(2),  # Optional: set the maxEventAge retry policy
            retry_attempts=2
        ))
    '''

    def __init__(
        self,
        handler: aws_cdk.aws_lambda.IFunction,
        *,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param handler: -
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                handler: aws_cdk.aws_lambda.IFunction,
                *,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = LambdaFunctionProps(
            event=event,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [handler, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this Lambda as a result from an EventBridge event.

        :param rule: -
        :param _id: -
        '''
        if __debug__:
            def stub(
                rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [rule, _id]))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class SfnStateMachine(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.SfnStateMachine",
):
    '''Use a StepFunctions state machine as a target for Amazon EventBridge rules.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_iam as iam
        import aws_cdk.aws_stepfunctions as sfn
        
        
        rule = events.Rule(self, "Rule",
            schedule=events.Schedule.rate(cdk.Duration.minutes(1))
        )
        
        dlq = sqs.Queue(self, "DeadLetterQueue")
        
        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("events.amazonaws.com")
        )
        state_machine = sfn.StateMachine(self, "SM",
            definition=sfn.Wait(self, "Hello", time=sfn.WaitTime.duration(cdk.Duration.seconds(10)))
        )
        
        rule.add_target(targets.SfnStateMachine(state_machine,
            input=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
            dead_letter_queue=dlq,
            role=role
        ))
    '''

    def __init__(
        self,
        machine: aws_cdk.aws_stepfunctions.IStateMachine,
        *,
        input: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param machine: -
        :param input: The input to the state machine execution. Default: the entire EventBridge event
        :param role: The IAM role to be assumed to execute the State Machine. Default: - a new role will be created
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                machine: aws_cdk.aws_stepfunctions.IStateMachine,
                *,
                input: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument machine", value=machine, expected_type=type_hints["machine"])
        props = SfnStateMachineProps(
            input=input,
            role=role,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [machine, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a properties that are used in an Rule to trigger this State Machine.

        :param _rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sns-permissions
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="machine")
    def machine(self) -> aws_cdk.aws_stepfunctions.IStateMachine:
        return typing.cast(aws_cdk.aws_stepfunctions.IStateMachine, jsii.get(self, "machine"))


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class SnsTopic(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.SnsTopic",
):
    '''Use an SNS topic as a target for Amazon EventBridge rules.

    Example::

        # publish to an SNS topic every time code is committed
        # to a CodeCommit repository
        repository.on_commit("onCommit", target=targets.SnsTopic(topic))
    '''

    def __init__(
        self,
        topic: aws_cdk.aws_sns.ITopic,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
    ) -> None:
        '''
        :param topic: -
        :param message: The message to send to the topic. Default: the entire EventBridge event
        '''
        if __debug__:
            def stub(
                topic: aws_cdk.aws_sns.ITopic,
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        props = SnsTopicProps(message=message)

        jsii.create(self.__class__, self, [topic, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this SNS topic as a result from an EventBridge event.

        :param _rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sns-permissions
        '''
        if __debug__:
            def stub(
                _rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [_rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> aws_cdk.aws_sns.ITopic:
        return typing.cast(aws_cdk.aws_sns.ITopic, jsii.get(self, "topic"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.SnsTopicProps",
    jsii_struct_bases=[],
    name_mapping={"message": "message"},
)
class SnsTopicProps:
    def __init__(
        self,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
    ) -> None:
        '''Customize the SNS Topic Event Target.

        :param message: The message to send to the topic. Default: the entire EventBridge event

        :exampleMetadata: infused

        Example::

            # on_commit_rule: events.Rule
            # topic: sns.Topic
            
            
            on_commit_rule.add_target(targets.SnsTopic(topic,
                message=events.RuleTargetInput.from_text(f"A commit was pushed to the repository {codecommit.ReferenceEvent.repositoryName} on branch {codecommit.ReferenceEvent.referenceName}")
            ))
        '''
        if __debug__:
            def stub(
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
        self._values: typing.Dict[str, typing.Any] = {}
        if message is not None:
            self._values["message"] = message

    @builtins.property
    def message(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The message to send to the topic.

        :default: the entire EventBridge event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsTopicProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(aws_cdk.aws_events.IRuleTarget)
class SqsQueue(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-events-targets.SqsQueue",
):
    '''Use an SQS Queue as a target for Amazon EventBridge rules.

    Example::

        # publish to an SQS queue every time code is committed
        # to a CodeCommit repository
        repository.on_commit("onCommit", target=targets.SqsQueue(queue))
    '''

    def __init__(
        self,
        queue: aws_cdk.aws_sqs.IQueue,
        *,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        message_group_id: typing.Optional[builtins.str] = None,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param queue: -
        :param message: The message to send to the queue. Must be a valid JSON text passed to the target queue. Default: the entire EventBridge event
        :param message_group_id: Message Group ID for messages sent to this queue. Required for FIFO queues, leave empty for regular queues. Default: - no message group ID (regular queue)
        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        '''
        if __debug__:
            def stub(
                queue: aws_cdk.aws_sqs.IQueue,
                *,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                message_group_id: typing.Optional[builtins.str] = None,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        props = SqsQueueProps(
            message=message,
            message_group_id=message_group_id,
            dead_letter_queue=dead_letter_queue,
            max_event_age=max_event_age,
            retry_attempts=retry_attempts,
        )

        jsii.create(self.__class__, self, [queue, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        rule: aws_cdk.aws_events.IRule,
        _id: typing.Optional[builtins.str] = None,
    ) -> aws_cdk.aws_events.RuleTargetConfig:
        '''Returns a RuleTarget that can be used to trigger this SQS queue as a result from an EventBridge event.

        :param rule: -
        :param _id: -

        :see: https://docs.aws.amazon.com/eventbridge/latest/userguide/resource-based-policies-eventbridge.html#sqs-permissions
        '''
        if __debug__:
            def stub(
                rule: aws_cdk.aws_events.IRule,
                _id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        return typing.cast(aws_cdk.aws_events.RuleTargetConfig, jsii.invoke(self, "bind", [rule, _id]))

    @builtins.property
    @jsii.member(jsii_name="queue")
    def queue(self) -> aws_cdk.aws_sqs.IQueue:
        return typing.cast(aws_cdk.aws_sqs.IQueue, jsii.get(self, "queue"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.TargetBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
    },
)
class TargetBaseProps:
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''The generic properties for an RuleTarget.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_sqs as sqs
            import aws_cdk.core as cdk
            
            # queue: sqs.Queue
            
            target_base_props = events_targets.TargetBaseProps(
                dead_letter_queue=queue,
                max_event_age=cdk.Duration.minutes(30),
                retry_attempts=123
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.TaskEnvironmentVariable",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class TaskEnvironmentVariable:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''An environment variable to be set in the container run as a task.

        :param name: Name for the environment variable. Exactly one of ``name`` and ``namePath`` must be specified.
        :param value: Value of the environment variable. Exactly one of ``value`` and ``valuePath`` must be specified.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            
            task_environment_variable = events_targets.TaskEnvironmentVariable(
                name="name",
                value="value"
            )
        '''
        if __debug__:
            def stub(*, name: builtins.str, value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''Name for the environment variable.

        Exactly one of ``name`` and ``namePath`` must be specified.
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''Value of the environment variable.

        Exactly one of ``value`` and ``valuePath`` must be specified.
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskEnvironmentVariable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.ApiDestinationProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
        "event_role": "eventRole",
        "header_parameters": "headerParameters",
        "path_parameter_values": "pathParameterValues",
        "query_string_parameters": "queryStringParameters",
    },
)
class ApiDestinationProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Customize the EventBridge Api Destinations Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target. Default: - a new role will be created
        :param header_parameters: Additional headers sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none
        :param path_parameter_values: Path parameters to insert in place of path wildcards (``*``). If the API destination has a wilcard in the path, these path parts will be inserted in that place. Default: - none
        :param query_string_parameters: Additional query string parameters sent to the API Destination. These are merged with headers specified on the Connection, with the headers on the Connection taking precedence. You can only specify secret values on the Connection. Default: - none

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events as events
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_iam as iam
            import aws_cdk.aws_sqs as sqs
            import aws_cdk.core as cdk
            
            # queue: sqs.Queue
            # role: iam.Role
            # rule_target_input: events.RuleTargetInput
            
            api_destination_props = events_targets.ApiDestinationProps(
                dead_letter_queue=queue,
                event=rule_target_input,
                event_role=role,
                header_parameters={
                    "header_parameters_key": "headerParameters"
                },
                max_event_age=cdk.Duration.minutes(30),
                path_parameter_values=["pathParameterValues"],
                query_string_parameters={
                    "query_string_parameters_key": "queryStringParameters"
                },
                retry_attempts=123
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
                query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
            check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
            check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event
        if event_role is not None:
            self._values["event_role"] = event_role
        if header_parameters is not None:
            self._values["header_parameters"] = header_parameters
        if path_parameter_values is not None:
            self._values["path_parameter_values"] = path_parameter_values
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The event to send.

        :default: - the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def event_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The role to assume before invoking the target.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def header_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional headers sent to the API Destination.

        These are merged with headers specified on the Connection, with
        the headers on the Connection taking precedence.

        You can only specify secret values on the Connection.

        :default: - none
        '''
        result = self._values.get("header_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Path parameters to insert in place of path wildcards (``*``).

        If the API destination has a wilcard in the path, these path parts
        will be inserted in that place.

        :default: - none
        '''
        result = self._values.get("path_parameter_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def query_string_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional query string parameters sent to the API Destination.

        These are merged with headers specified on the Connection, with
        the headers on the Connection taking precedence.

        You can only specify secret values on the Connection.

        :default: - none
        '''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.ApiGatewayProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event_role": "eventRole",
        "header_parameters": "headerParameters",
        "method": "method",
        "path": "path",
        "path_parameter_values": "pathParameterValues",
        "post_body": "postBody",
        "query_string_parameters": "queryStringParameters",
        "stage": "stage",
    },
)
class ApiGatewayProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
        header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        method: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        post_body: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        stage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Customize the API Gateway Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created
        :param header_parameters: The headers to be set when requesting API. Default: no header parameters
        :param method: The method for api resource invoked by the rule. Default: '*' that treated as ANY
        :param path: The api resource invoked by the rule. We can use wildcards('*') to specify the path. In that case, an equal number of real values must be specified for pathParameterValues. Default: '/'
        :param path_parameter_values: The path parameter values to be used to populate to wildcards("*") of requesting api path. Default: no path parameters
        :param post_body: This will be the post request body send to the API. Default: the entire EventBridge event
        :param query_string_parameters: The query parameters to be set when requesting API. Default: no querystring parameters
        :param stage: The deploy stage of api gateway invoked by the rule. Default: the value of deploymentStage.stageName of target api gateway.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_apigateway as api
            import aws_cdk.aws_lambda as lambda_
            
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(cdk.Duration.minutes(1))
            )
            
            fn = lambda_.Function(self, "MyFunc",
                handler="index.handler",
                runtime=lambda_.Runtime.NODEJS_14_X,
                code=lambda_.Code.from_inline("exports.handler = e => {}")
            )
            
            rest_api = api.LambdaRestApi(self, "MyRestAPI", handler=fn)
            
            dlq = sqs.Queue(self, "DeadLetterQueue")
            
            rule.add_target(
                targets.ApiGateway(rest_api,
                    path="/*/test",
                    method="GET",
                    stage="prod",
                    path_parameter_values=["path-value"],
                    header_parameters={
                        "Header1": "header1"
                    },
                    query_string_parameters={
                        "QueryParam1": "query-param-1"
                    },
                    dead_letter_queue=dlq
                ))
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
                header_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                method: typing.Optional[builtins.str] = None,
                path: typing.Optional[builtins.str] = None,
                path_parameter_values: typing.Optional[typing.Sequence[builtins.str]] = None,
                post_body: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                query_string_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                stage: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
            check_type(argname="argument header_parameters", value=header_parameters, expected_type=type_hints["header_parameters"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument path_parameter_values", value=path_parameter_values, expected_type=type_hints["path_parameter_values"])
            check_type(argname="argument post_body", value=post_body, expected_type=type_hints["post_body"])
            check_type(argname="argument query_string_parameters", value=query_string_parameters, expected_type=type_hints["query_string_parameters"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event_role is not None:
            self._values["event_role"] = event_role
        if header_parameters is not None:
            self._values["header_parameters"] = header_parameters
        if method is not None:
            self._values["method"] = method
        if path is not None:
            self._values["path"] = path
        if path_parameter_values is not None:
            self._values["path_parameter_values"] = path_parameter_values
        if post_body is not None:
            self._values["post_body"] = post_body
        if query_string_parameters is not None:
            self._values["query_string_parameters"] = query_string_parameters
        if stage is not None:
            self._values["stage"] = stage

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    @builtins.property
    def header_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The headers to be set when requesting API.

        :default: no header parameters
        '''
        result = self._values.get("header_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''The method for api resource invoked by the rule.

        :default: '*' that treated as ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The api resource invoked by the rule.

        We can use wildcards('*') to specify the path. In that case,
        an equal number of real values must be specified for pathParameterValues.

        :default: '/'
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path_parameter_values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The path parameter values to be used to populate to wildcards("*") of requesting api path.

        :default: no path parameters
        '''
        result = self._values.get("path_parameter_values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def post_body(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''This will be the post request body send to the API.

        :default: the entire EventBridge event
        '''
        result = self._values.get("post_body")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def query_string_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The query parameters to be set when requesting API.

        :default: no querystring parameters
        '''
        result = self._values.get("query_string_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def stage(self) -> typing.Optional[builtins.str]:
        '''The deploy stage of api gateway invoked by the rule.

        :default: the value of deploymentStage.stageName of target api gateway.
        '''
        result = self._values.get("stage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.BatchJobProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "attempts": "attempts",
        "event": "event",
        "job_name": "jobName",
        "size": "size",
    },
)
class BatchJobProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        job_name: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Customize the Batch Job Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param attempts: The number of times to attempt to retry, if the job fails. Valid values are 1–10. Default: no retryStrategy is set
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event
        :param job_name: The name of the submitted job. Default: - Automatically generated
        :param size: The size of the array, if this is an array batch job. Valid values are integers between 2 and 10,000. Default: no arrayProperties are set

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_batch as batch
            from aws_cdk.aws_ecs import ContainerImage
            
            
            job_queue = batch.JobQueue(self, "MyQueue",
                compute_environments=[batch.JobQueueComputeEnvironment(
                    compute_environment=batch.ComputeEnvironment(self, "ComputeEnvironment",
                        managed=False
                    ),
                    order=1
                )
                ]
            )
            
            job_definition = batch.JobDefinition(self, "MyJob",
                container=batch.JobDefinitionContainer(
                    image=ContainerImage.from_registry("test-repo")
                )
            )
            
            queue = sqs.Queue(self, "Queue")
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(cdk.Duration.hours(1))
            )
            
            rule.add_target(targets.BatchJob(job_queue.job_queue_arn, job_queue, job_definition.job_definition_arn, job_definition,
                dead_letter_queue=queue,
                event=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
                retry_attempts=2,
                max_event_age=cdk.Duration.hours(2)
            ))
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                attempts: typing.Optional[jsii.Number] = None,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                job_name: typing.Optional[builtins.str] = None,
                size: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument attempts", value=attempts, expected_type=type_hints["attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if attempts is not None:
            self._values["attempts"] = attempts
        if event is not None:
            self._values["event"] = event
        if job_name is not None:
            self._values["job_name"] = job_name
        if size is not None:
            self._values["size"] = size

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times to attempt to retry, if the job fails.

        Valid values are 1–10.

        :default: no retryStrategy is set
        '''
        result = self._values.get("attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The event to send to the Lambda.

        This will be the payload sent to the Lambda Function.

        :default: the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def job_name(self) -> typing.Optional[builtins.str]:
        '''The name of the submitted job.

        :default: - Automatically generated
        '''
        result = self._values.get("job_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''The size of the array, if this is an array batch job.

        Valid values are integers between 2 and 10,000.

        :default: no arrayProperties are set
        '''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchJobProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.CodeBuildProjectProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
        "event_role": "eventRole",
    },
)
class CodeBuildProjectProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''Customize the CodeBuild Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send to CodeBuild. This will be the payload for the StartBuild API. Default: - the entire EventBridge event
        :param event_role: The role to assume before invoking the target (i.e., the codebuild) when the given rule is triggered. Default: - a new role will be created

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_codebuild as codebuild
            import aws_cdk.aws_codecommit as codecommit
            
            
            repo = codecommit.Repository(self, "MyRepo",
                repository_name="aws-cdk-codebuild-events"
            )
            
            project = codebuild.Project(self, "MyProject",
                source=codebuild.Source.code_commit(repository=repo)
            )
            
            dead_letter_queue = sqs.Queue(self, "DeadLetterQueue")
            
            # trigger a build when a commit is pushed to the repo
            on_commit_rule = repo.on_commit("OnCommit",
                target=targets.CodeBuildProject(project,
                    dead_letter_queue=dead_letter_queue
                ),
                branches=["master"]
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event
        if event_role is not None:
            self._values["event_role"] = event_role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The event to send to CodeBuild.

        This will be the payload for the StartBuild API.

        :default: - the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def event_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The role to assume before invoking the target (i.e., the codebuild) when the given rule is triggered.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeBuildProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.CodePipelineTargetOptions",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event_role": "eventRole",
    },
)
class CodePipelineTargetOptions(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''Customization options when creating a {@link CodePipeline} event target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event_role: The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered. Default: - a new role will be created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_iam as iam
            import aws_cdk.aws_sqs as sqs
            import aws_cdk.core as cdk
            
            # queue: sqs.Queue
            # role: iam.Role
            
            code_pipeline_target_options = events_targets.CodePipelineTargetOptions(
                dead_letter_queue=queue,
                event_role=role,
                max_event_age=cdk.Duration.minutes(30),
                retry_attempts=123
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                event_role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event_role", value=event_role, expected_type=type_hints["event_role"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event_role is not None:
            self._values["event_role"] = event_role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event_role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The role to assume before invoking the target (i.e., the pipeline) when the given rule is triggered.

        :default: - a new role will be created
        '''
        result = self._values.get("event_role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodePipelineTargetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.LambdaFunctionProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
    },
)
class LambdaFunctionProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
    ) -> None:
        '''Customize the Lambda Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send to the Lambda. This will be the payload sent to the Lambda Function. Default: the entire EventBridge event

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            
            
            fn = lambda_.Function(self, "MyFunc",
                runtime=lambda_.Runtime.NODEJS_14_X,
                handler="index.handler",
                code=lambda_.Code.from_inline("exports.handler = handler.toString()")
            )
            
            rule = events.Rule(self, "rule",
                event_pattern=events.EventPattern(
                    source=["aws.ec2"]
                )
            )
            
            queue = sqs.Queue(self, "Queue")
            
            rule.add_target(targets.LambdaFunction(fn,
                dead_letter_queue=queue,  # Optional: add a dead letter queue
                max_event_age=cdk.Duration.hours(2),  # Optional: set the maxEventAge retry policy
                retry_attempts=2
            ))
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The event to send to the Lambda.

        This will be the payload sent to the Lambda Function.

        :default: the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.LogGroupProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "event": "event",
    },
)
class LogGroupProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
    ) -> None:
        '''Customize the CloudWatch LogGroup Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param event: The event to send to the CloudWatch LogGroup. This will be the event logged into the CloudWatch LogGroup Default: - the entire EventBridge event

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events as events
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_sqs as sqs
            import aws_cdk.core as cdk
            
            # queue: sqs.Queue
            # rule_target_input: events.RuleTargetInput
            
            log_group_props = events_targets.LogGroupProps(
                dead_letter_queue=queue,
                event=rule_target_input,
                max_event_age=cdk.Duration.minutes(30),
                retry_attempts=123
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                event: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument event", value=event, expected_type=type_hints["event"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if event is not None:
            self._values["event"] = event

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def event(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The event to send to the CloudWatch LogGroup.

        This will be the event logged into the CloudWatch LogGroup

        :default: - the entire EventBridge event
        '''
        result = self._values.get("event")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.SfnStateMachineProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "input": "input",
        "role": "role",
    },
)
class SfnStateMachineProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        input: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
    ) -> None:
        '''Customize the Step Functions State Machine target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param input: The input to the state machine execution. Default: the entire EventBridge event
        :param role: The IAM role to be assumed to execute the State Machine. Default: - a new role will be created

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_iam as iam
            import aws_cdk.aws_stepfunctions as sfn
            
            
            rule = events.Rule(self, "Rule",
                schedule=events.Schedule.rate(cdk.Duration.minutes(1))
            )
            
            dlq = sqs.Queue(self, "DeadLetterQueue")
            
            role = iam.Role(self, "Role",
                assumed_by=iam.ServicePrincipal("events.amazonaws.com")
            )
            state_machine = sfn.StateMachine(self, "SM",
                definition=sfn.Wait(self, "Hello", time=sfn.WaitTime.duration(cdk.Duration.seconds(10)))
            )
            
            rule.add_target(targets.SfnStateMachine(state_machine,
                input=events.RuleTargetInput.from_object({"SomeParam": "SomeValue"}),
                dead_letter_queue=dlq,
                role=role
            ))
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                input: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                role: typing.Optional[aws_cdk.aws_iam.IRole] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if input is not None:
            self._values["input"] = input
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def input(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The input to the state machine execution.

        :default: the entire EventBridge event
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def role(self) -> typing.Optional[aws_cdk.aws_iam.IRole]:
        '''The IAM role to be assumed to execute the State Machine.

        :default: - a new role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[aws_cdk.aws_iam.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SfnStateMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-events-targets.SqsQueueProps",
    jsii_struct_bases=[TargetBaseProps],
    name_mapping={
        "dead_letter_queue": "deadLetterQueue",
        "max_event_age": "maxEventAge",
        "retry_attempts": "retryAttempts",
        "message": "message",
        "message_group_id": "messageGroupId",
    },
)
class SqsQueueProps(TargetBaseProps):
    def __init__(
        self,
        *,
        dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
        max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
        retry_attempts: typing.Optional[jsii.Number] = None,
        message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
        message_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Customize the SQS Queue Event Target.

        :param dead_letter_queue: The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_. The events not successfully delivered are automatically retried for a specified period of time, depending on the retry policy of the target. If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue. Default: - no dead-letter queue
        :param max_event_age: The maximum age of a request that Lambda sends to a function for processing. Minimum value of 60. Maximum value of 86400. Default: Duration.hours(24)
        :param retry_attempts: The maximum number of times to retry when the function returns an error. Minimum value of 0. Maximum value of 185. Default: 185
        :param message: The message to send to the queue. Must be a valid JSON text passed to the target queue. Default: the entire EventBridge event
        :param message_group_id: Message Group ID for messages sent to this queue. Required for FIFO queues, leave empty for regular queues. Default: - no message group ID (regular queue)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_events as events
            import aws_cdk.aws_events_targets as events_targets
            import aws_cdk.aws_sqs as sqs
            import aws_cdk.core as cdk
            
            # queue: sqs.Queue
            # rule_target_input: events.RuleTargetInput
            
            sqs_queue_props = events_targets.SqsQueueProps(
                dead_letter_queue=queue,
                max_event_age=cdk.Duration.minutes(30),
                message=rule_target_input,
                message_group_id="messageGroupId",
                retry_attempts=123
            )
        '''
        if __debug__:
            def stub(
                *,
                dead_letter_queue: typing.Optional[aws_cdk.aws_sqs.IQueue] = None,
                max_event_age: typing.Optional[aws_cdk.core.Duration] = None,
                retry_attempts: typing.Optional[jsii.Number] = None,
                message: typing.Optional[aws_cdk.aws_events.RuleTargetInput] = None,
                message_group_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument max_event_age", value=max_event_age, expected_type=type_hints["max_event_age"])
            check_type(argname="argument retry_attempts", value=retry_attempts, expected_type=type_hints["retry_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument message_group_id", value=message_group_id, expected_type=type_hints["message_group_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if max_event_age is not None:
            self._values["max_event_age"] = max_event_age
        if retry_attempts is not None:
            self._values["retry_attempts"] = retry_attempts
        if message is not None:
            self._values["message"] = message
        if message_group_id is not None:
            self._values["message_group_id"] = message_group_id

    @builtins.property
    def dead_letter_queue(self) -> typing.Optional[aws_cdk.aws_sqs.IQueue]:
        '''The SQS queue to be used as deadLetterQueue. Check out the `considerations for using a dead-letter queue <https://docs.aws.amazon.com/eventbridge/latest/userguide/rule-dlq.html#dlq-considerations>`_.

        The events not successfully delivered are automatically retried for a specified period of time,
        depending on the retry policy of the target.
        If an event is not delivered before all retry attempts are exhausted, it will be sent to the dead letter queue.

        :default: - no dead-letter queue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[aws_cdk.aws_sqs.IQueue], result)

    @builtins.property
    def max_event_age(self) -> typing.Optional[aws_cdk.core.Duration]:
        '''The maximum age of a request that Lambda sends to a function for processing.

        Minimum value of 60.
        Maximum value of 86400.

        :default: Duration.hours(24)
        '''
        result = self._values.get("max_event_age")
        return typing.cast(typing.Optional[aws_cdk.core.Duration], result)

    @builtins.property
    def retry_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times to retry when the function returns an error.

        Minimum value of 0.
        Maximum value of 185.

        :default: 185
        '''
        result = self._values.get("retry_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[aws_cdk.aws_events.RuleTargetInput]:
        '''The message to send to the queue.

        Must be a valid JSON text passed to the target queue.

        :default: the entire EventBridge event
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[aws_cdk.aws_events.RuleTargetInput], result)

    @builtins.property
    def message_group_id(self) -> typing.Optional[builtins.str]:
        '''Message Group ID for messages sent to this queue.

        Required for FIFO queues, leave empty for regular queues.

        :default: - no message group ID (regular queue)
        '''
        result = self._values.get("message_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqsQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiDestination",
    "ApiDestinationProps",
    "ApiGateway",
    "ApiGatewayProps",
    "AwsApi",
    "AwsApiInput",
    "AwsApiProps",
    "BatchJob",
    "BatchJobProps",
    "CloudWatchLogGroup",
    "CodeBuildProject",
    "CodeBuildProjectProps",
    "CodePipeline",
    "CodePipelineTargetOptions",
    "ContainerOverride",
    "EcsTask",
    "EcsTaskProps",
    "EventBus",
    "EventBusProps",
    "KinesisFirehoseStream",
    "KinesisFirehoseStreamProps",
    "KinesisStream",
    "KinesisStreamProps",
    "LambdaFunction",
    "LambdaFunctionProps",
    "LogGroupProps",
    "SfnStateMachine",
    "SfnStateMachineProps",
    "SnsTopic",
    "SnsTopicProps",
    "SqsQueue",
    "SqsQueueProps",
    "TargetBaseProps",
    "TaskEnvironmentVariable",
]

publication.publish()
