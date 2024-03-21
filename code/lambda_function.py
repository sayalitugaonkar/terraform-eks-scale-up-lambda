import boto3


def lambda_handler(event, context):

    eks = boto3.client('eks')

    cluster_name = "CLUSTER_NAME"

    nodegroup_sizes = {
        'node-pool-1': 7,(INTEGER)
        't4a-medium-pool': 7,
    }

    nodegroup_minsizes = {
        'NODE_GROUP_1': 5,(INTEGER)
        'NODE_GROUP_2': 5,
    }

    nodegroup_maxsizes = {
        'NODE_GROUP_1': 10,(INTEGER)
        'NODE_GROUP_2': 10,
    }

    for nodegroup_name, max_size in nodegroup_maxsizes.items():
        response = eks.describe_nodegroup(
            clusterName=cluster_name,
            nodegroupName=nodegroup_name
        )
        current_size = response['nodegroup']['scalingConfig']['maxSize']

        if max_size != current_size:
            response = eks.update_nodegroup_config(
                clusterName=cluster_name,
                nodegroupName=nodegroup_name,
                scalingConfig={
                    'maxSize': max_size
                }
            )
            print(
                f"Updated maximum size for node group {nodegroup_name} to {max_size}")
        else:
            print(
                f"Maximum size is already {max_size} for node group {nodegroup_name}")

    for nodegroup_name, desired_size in nodegroup_sizes.items():
        response = eks.describe_nodegroup(
            clusterName=cluster_name,
            nodegroupName=nodegroup_name
        )
        current_size = response['nodegroup']['scalingConfig']['desiredSize']

        if desired_size != current_size:
            response = eks.update_nodegroup_config(
                clusterName=cluster_name,
                nodegroupName=nodegroup_name,
                scalingConfig={
                    'desiredSize': desired_size
                }
            )
            print(
                f"Updated desired size for node group {nodegroup_name} to {desired_size}")
        else:
            print(
                f"Desired size is already {desired_size} for node group {nodegroup_name}")

    for nodegroup_name, min_size in nodegroup_minsizes.items():
        response = eks.describe_nodegroup(
            clusterName=cluster_name,
            nodegroupName=nodegroup_name
        )
        current_size = response['nodegroup']['scalingConfig']['minSize']

        if min_size != current_size:
            response = eks.update_nodegroup_config(
                clusterName=cluster_name,
                nodegroupName=nodegroup_name,
                scalingConfig={
                    'minSize': min_size
                }
            )
            print(
                f"Updated minimal size for node group {nodegroup_name} to {min_size}")
        else:
            print(
                f"Minimal size is already {min_size} for node group {nodegroup_name}")