#!/usr/bin/env python3
import os

import aws_cdk as cdk

from iplocation.iplocation_download import IpLocationDownload
from iplocation.iplocation_lookupuse1 import IpLocationLookupUse1
from iplocation.iplocation_lookupusw2 import IpLocationLookupUsw2
from iplocation.iplocation_stack import IpLocationStack

app = cdk.App()

IpLocationDownload(
    app, 'IpLocationDownload',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

IpLocationLookupUse1(
    app, 'IpLocationLookupUse1',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-1'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

IpLocationLookupUsw2(
    app, 'IpLocationLookupUsw2',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-west-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

IpLocationStack(
    app, 'IpLocationStack',
    env = cdk.Environment(
        account = os.getenv('CDK_DEFAULT_ACCOUNT'),
        region = 'us-east-2'
    ),
    synthesizer = cdk.DefaultStackSynthesizer(
        qualifier = 'lukach'
    )
)

cdk.Tags.of(app).add('Alias','iplocation')
cdk.Tags.of(app).add('GitHub','https://github.com/jblukach/iplocation')
cdk.Tags.of(app).add('Org','lukach.io')

app.synth()