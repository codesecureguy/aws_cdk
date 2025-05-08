from aws_cdk import (
    App, Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
)
from constructs import Construct

class EksVpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # VPC with public and private subnets
        vpc = ec2.Vpc(self, "EksVpc",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
                ec2.SubnetConfiguration(name="private", subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS, cidr_mask=24),
            ]
        )

        # EKS cluster
        cluster = eks.Cluster(self, "EksCluster",
            version=eks.KubernetesVersion.V1_27,
            vpc=vpc,
            default_capacity=1,
            default_capacity_instance=ec2.InstanceType("t3.medium"),
        )

app = App()
EksVpcStack(app, "EksVpcStack")
app.synth()
