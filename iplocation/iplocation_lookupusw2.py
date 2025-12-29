from aws_cdk import (
    Duration,
    RemovalPolicy,
    SecretValue,
    Size,
    Stack,
    aws_apigatewayv2 as _api,
    aws_apigatewayv2_integrations as _integrations,
    aws_certificatemanager as _acm,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_logs as _logs,
    aws_route53 as _route53,
    aws_route53_targets as _r53targets,
    aws_s3 as _s3,
    aws_s3_deployment as _deployment,
    aws_secretsmanager as _secrets,
    aws_ssm as _ssm
)

from constructs import Construct

class IpLocationLookupUsw2(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

    ### PARAMETERS ###

        organization = _ssm.StringParameter.from_string_parameter_attributes(
            self, 'organization',
            parameter_name = '/organization/id'
        )

    ### S3 BUCKETS ###

        staged = _s3.Bucket(
            self, 'staged',
            bucket_name = 'iplocation-staged-usw2-lukach-io',
            encryption = _s3.BucketEncryption.S3_MANAGED,
            block_public_access = _s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy = RemovalPolicy.DESTROY,
            auto_delete_objects = True,
            enforce_ssl = True,
            versioned = False
        )

        bucket_policy_one = _iam.PolicyStatement(
            effect = _iam.Effect(
                'ALLOW'
            ),
            principals = [
                _iam.AnyPrincipal()
            ],
            actions = [
                's3:ListBucket'
            ],
            resources = [
                staged.bucket_arn
            ],
            conditions = {"StringEquals": {"aws:PrincipalOrgID": organization.string_value}}
        )

        staged.add_to_resource_policy(bucket_policy_one)

        object_policy_one = _iam.PolicyStatement(
            effect = _iam.Effect(
                'ALLOW'
            ),
            principals = [
                _iam.AnyPrincipal()
            ],
            actions = [
                's3:GetObject'
            ],
            resources = [
                staged.arn_for_objects('*')
            ],
            conditions = {"StringEquals": {"aws:PrincipalOrgID": organization.string_value}}
        )

        staged.add_to_resource_policy(object_policy_one)

