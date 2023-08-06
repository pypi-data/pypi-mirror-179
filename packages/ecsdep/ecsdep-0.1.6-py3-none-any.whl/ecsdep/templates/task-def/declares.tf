terraform {
  required_version = ">= 1.1.2"
  backend "s3" {
    bucket  = "states-data"
    key     = "terraform/ecs-cluster/skitai-cluster/task-def/ecsdep-worker/terraform.tfstate"
    region  = "ap-northeast-2"
    encrypt = true
    acl     = "bucket-owner-full-control"
  }
}

provider "aws" {
  region  = "ap-northeast-1"
}

variable "template_version" {
  default = "1"
}

variable "cluster_name" {
  default = "skitai-cluster"
}

# variables -----------------------------------------------
variable "awslog_region" {
  default = "ap-northeast-1"
}

variable "stages" {
  default = {
    default = {
        env_service_stage = "production"
        service_name = "ecsdep-worker"
        task_definition_name = "ecsdep-worker"
    }
  }
}

variable "service_auto_scaling" {
  default = {
    desired = 1
    min = 1
    max = 1
    cpu = 0
    memory = 0
  }
}

variable "exposed_container" {
  default = []
}

variable "target_group" {
  default = {
    protocol = "HTTP"
    healthcheck = {
        path = "/"
        timeout = 10
        interval = 60
        healthy_threshold = 2
        unhealthy_threshold = 10
        matcher = "200,301,302,404"
    }
  }
}

variable "loggings" {
  default = ["skitai-worker"]
}

variable "loadbalancing_pathes" {
  default = ["/*"]
}

variable "requires_compatibilities" {
  default = ["EC2"]
}

variable "service_resources" {
  default = {
    memory = 24
    cpu = 128
  }
}
