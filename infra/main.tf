# e.g. AWS MSK for Kafka, ECS for API, S3 for data, IAM roles
terraform {
  required_providers {
    # no providers yet—this block exists so init won’t complain
  }
}

# A dummy null_resource so we can plan/apply later
resource "null_resource" "placeholder" {}
