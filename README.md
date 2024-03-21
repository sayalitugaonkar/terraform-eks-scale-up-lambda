## Lambda function with terraform to scale up nodes at morning ##


Kubernetes is a powerful orchestration tool for managing containerized applications and is the most popular container-orchestration platform in use today. 

However, while AWS EKS provides a powerful and convenient way to manage containerized applications, it can also be costly.

With the other scale-down project, we are scaling down the nodes, and with this one, we are again upscaling it at morning 6.00am


In `lambda_function.tf`, we are defining a lambda function to be taken as a zip file created in archive.tf

We are adding triggers via Cloudwatch event rules and upscaling the node group mentioned in file to the sizes mentioned



