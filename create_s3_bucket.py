# app.py
from aws_cdk import (
    App, Stack,
    aws_s3 as s3,
)
from constructs import Construct

class MyS3Stack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, "ExampleBucket",
            bucket_name="my-cdk-example-bucket",
            versioned=False,
            removal_policy=None
        )

app = App()
MyS3Stack(app, "MyS3Stack", env={'region': 'us-east-1'})
app.synth()
