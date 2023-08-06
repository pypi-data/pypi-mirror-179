# B.NodeCdkLayer

![Pipeline](https://github.com/Biomapas/B.NodeCdkLayer/workflows/Pipeline/badge.svg?branch=master)

### Description

This is a simple Lambda layer AWS CDK resource that contains `node` and `aws cdk cli` within. 
This package is useful for lambda functions that want to run `aws cdk` commands within themselves.
Imagine a scenario where you run `cdk deploy --all` command not within you local pc or a build environment
but through a lambda function. This library would greatly help you.

### Remarks

[Biomapas](https://www.biomapas.com/) aims to modernise life-science industry by sharing its IT knowledge with other companies and the community. 
This is an open source library intended to be used by anyone. 
Improvements and pull requests are welcome. 

### Related technology

- Python3
- Docker
- AWS CDK

### Assumptions

This project assumes you have:

- Good knowledge in AWS. 
- Good knowledge in AWS CDK. 
- Good Python skills and basis of OOP.

### Useful sources

- Read more about how Docker is ued when building custom lambda layers:<br>
  https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_lambda/Code.html#aws_cdk.aws_lambda.Code.from_docker_build

### Install

Before installing this library, ensure you have these tools setup:

- Python / Pip

To install this project from source run:

```
pip install .
```

Or you can install it from a PyPi repository:

```
pip install b-node-cdk-layer
```

### Usage & Examples

Simply create a lambda function with this layer:

```python
from aws_cdk.aws_lambda import Function
from b_node_cdk_layer.node_cdk_layer import NodeCdkLayer

Function(
    scope=Stack(...),
    id='Function',
    
    ...,
  
    layers=[NodeCdkLayer(Stack(...))],
  
    # Running node process requires more RAM and longer runtime.
    timeout=Duration.minutes(1),
    memory_size=512
)
```

To run some node or cdk command, follow this example:

```python
import subprocess

# This is the path to AWS CDK CLI. It comes from a NodeCDK layer, that is a custom-built layer using docker.
CDK_CLI_PATH = '/opt/bin/node_modules/aws-cdk/bin/cdk'


def handler(*args, **kwargs):
    output = subprocess.check_output([
        CDK_CLI_PATH,
        '--version',
    ])

    print(output)
```

### Testing

This package has unit tests based on **pytest**.
To run tests simply run:

```
pytest b_node_cdk_layer_test/integration
```

### Contribution

Found a bug? Want to add or suggest a new feature? 
Contributions of any kind are gladly welcome. 
You may contact us directly, create a pull-request or an issue in github platform. 
Lets modernize the world together.
