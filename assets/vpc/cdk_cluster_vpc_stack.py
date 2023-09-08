from aws_cdk import CfnOutput, Stack, Tags
import aws_cdk.aws_ec2 as ec2
from constructs import Construct

vpc_id = "vpc-0a09686505f2c4051"  # aws-usyd-staging-mocklegacy 172582138886 


class CdkClusterVpcStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id=vpc_id)
        ecr_dkr = vpc.add_interface_endpoint("ecrEndpoint", service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER, private_dns_enabled=True)
        ecr_api = vpc.add_interface_endpoint("ecrApiEndpoint", service=ec2.InterfaceVpcEndpointAwsService.ECR, private_dns_enabled=True)
        self.vpc = vpc
        #Tags.of(ecr_api).add('name','ecrApiEndpoint')
    
        # self.cluster_vpc = ec2.Vpc(
        #     self, "ClusterVpc",
        #     ip_addresses=ec2.IpAddresses.cidr(cidr_block="10.75.0.0/16"),
        #     #create_internet_gateway=False,
        #     max_azs=2,
        #     subnet_configuration=[ec2.SubnetConfiguration(
        #         # 'subnetType' controls Internet access, as described above.
        #         subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,

        #         # 'name' is used to name this particular subnet group. You will have to
        #         # use the name for subnet selection if you have more than one subnet
        #         # group of the same type.
        #         name="PriEgr",

        #         # 'cidrMask' specifies the IP addresses in the range of of individual
        #         # subnets in the group. Each of the subnets in this group will contain
        #         # `2^(32 address bits - 24 subnet bits) - 2 reserved addresses = 254`
        #         # usable IP addresses.
        #         #
        #         # If 'cidrMask' is left out the available address space is evenly
        #         # divided across the remaining subnet groups.
        #         cidr_mask=18
                
        #         # 'reserved' can be used to reserve IP address space. No resources will
        #         # be created for this subnet, but the IP range will be kept available for
        #         # future creation of this subnet, or even for future subdivision.
        #         #reserved=True
        #     ), ec2.SubnetConfiguration(
        #         cidr_mask=26,
        #         name="PubIng",
        #         subnet_type=ec2.SubnetType.PUBLIC
        #     )
        #     ]
        # )      
        

        # CfnOutput(self, "Output",
        #                value=host.instance_private_ip)
