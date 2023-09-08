#!/usr/bin/env python3
import os

import aws_cdk as cdk

from my_ecs_cicd.my_ecs_cicd_stack import MyEcsCicdStack
from assets.ec2.cdk_ec2.cdk_ec2_stack import CdkEC2Stack
from assets.vpc.cdk_cluster_vpc_stack import CdkClusterVpcStack

from pipeline.codepipeline_build_deploy_stack import CodepipelineBuildDeployStack

env_AU_TEST = cdk.Environment(account="172582138886", region="ap-southeast-2")  #711219499793

app = cdk.App()
#MyEcsCicdStack(app, "MyEcsCicdStack", env=env_AU_TEST)


#CDK via static VPC to EC2 stack


#MyEcsCicdStack(app, "MyEcsCicdStack", env=env_AU_TEST)

vpcStack = CdkClusterVpcStack(app, "CdkClusterVpcStack", env=env_AU_TEST)

CdkEC2Stack(app, "CdkEC2Stack", vpcStack.vpc, env=env_AU_TEST)

CodepipelineBuildDeployStack(app, "CodepipelineBuildDeployStack", vpcStack.vpc, env=env_AU_TEST)


app.synth()
