import aws_cdk as core
import aws_cdk.assertions as assertions

from my_ecs_cicd.my_ecs_cicd_stack import MyEcsCicdStack

# example tests. To run these tests, uncomment this file along with the example
# resource in my_ecs_cicd/my_ecs_cicd_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MyEcsCicdStack(app, "my-ecs-cicd")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
