data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]
    effect  = "Allow"
    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }
  }
}

resource "aws_iam_role_policy_attachment" "assume_role" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role       = "${aws_iam_role.lambda.name}"
}


resource "aws_iam_role" "lambda" {
  assume_role_policy = "${data.aws_iam_policy_document.eks_update_nodes_list_nodes.json}"
  name               = "custom-iam-role-for-lambda"
}

data "aws_iam_policy_document" "eks_update_nodes_list_nodes" {
  statement {
    actions = [
      "eks:ListNodegroups",
      "eks:UpdateNodegroupConfig",
      "eks:DescribeNodegroup"
    ]
    effect    = "Allow"
    resources = ["arn:aws:lambda:*:*:*"]
  }
}

resource "aws_iam_policy_attachment" "logs" {
  name       = "attach-lambda-policy"
  policy_arn = "${aws_iam_policy.eks_scaling.arn}"
  roles      = [aws_iam_role.lambda.name]
}


resource "aws_iam_policy" "eks_scaling" {
  name   = "iam-policy-for-scaling"
  policy = "${data.aws_iam_policy_document.eks_update_nodes_list_nodes.json}"
}
