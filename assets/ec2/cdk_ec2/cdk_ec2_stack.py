from aws_cdk import CfnOutput, Stack
import aws_cdk.aws_ec2 as ec2
from constructs import Construct

#vpc_id = "vpc-0a09686505f2c4051"  # aws-usyd-staging-mocklegacy 172582138886 
ec2_type = "t2.micro"
key_name = "ICT-TEST-Staging"
linux_ami = ec2.GenericLinuxImage({
    "ap-southeast-2": "ami-0a709bebf4fa9246f"
})
with open("./assets/ec2/cdk_ec2/user_data/user_data.sh") as f:
    user_data = f.read()


class CdkEC2Stack(Stack):

    def __init__(self, scope: Construct, id: str, props: ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        #vpc = ec2.Vpc.from_lookup(self, "VPC", vpc_id=vpc_id)
    

        host = ec2.Instance(self, "SVEC2",
                            instance_type=ec2.InstanceType(
                                instance_type_identifier=ec2_type),
                            instance_name="pocNetprefix",
                            machine_image=linux_ami,
                            vpc=props,
                            key_name=key_name,
                            vpc_subnets=ec2.SubnetSelection(
                                availability_zones=["ap-southeast-2b"]),
                            user_data=ec2.UserData.custom(user_data)
                            )
        # ec2.Instance has no property of BlockDeviceMappings, add via lower layer cdk api:
        host.instance.add_property_override("BlockDeviceMappings", [{
            "DeviceName": "/dev/xvda",
            "Ebs": {
                "VolumeSize": "10",
                "VolumeType": "io1",
                "Iops": "150",
                "DeleteOnTermination": "true"
            }
        }, {
            "DeviceName": "/dev/sdb",
            "Ebs": {"VolumeSize": "30"}
        }
        ])  # by default VolumeType is gp2, VolumeSize 8GB
        host.connections.allow_from_any_ipv4(
            ec2.Port.tcp(22), "Allow ssh from internet")
        host.connections.allow_from_any_ipv4(
            ec2.Port.tcp(80), "Allow http from internet")

        CfnOutput(self, "Output",
                       value=host.instance_private_ip)
