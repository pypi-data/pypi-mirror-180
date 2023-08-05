#!/bin/bash

%{ for key, value in envs }
export ${key}=${value}
%{ endfor ~}

# install packages
sudo yum update -y
sudo yum install unzip -y
sudo yum install git -y
sudo yum install python3 -y

# install aws cli
if [ "$PLATFORM" == "arm64" ] ; then
    # install amazon cli
    sudo curl "https://awscli.amazonaws.com/awscli-exe-linux-aarch64.zip" -o "awscliv2.zip"
    sudo unzip awscliv2.zip
    sudo rm awscliv2.zip
    sudo ./aws/install
fi

# install ssm agent
if [ "$PLATFORM" == "arm64" ] ; then
    sudo yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_arm64/amazon-ssm-agent.rpm
    sudo systemctl start amazon-ssm-agent
fi

# install docker
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chkconfig docker on

# install docker compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# this is a work around for a bug with the terraform spot instance resource
# https://github.com/hashicorp/terraform/issues/3263
INSTANCE_ID=$(curl -s http://169.254.169.254/latest/meta-data/instance-id)
SPOT_REQ_ID=$(aws --region $AWS_REGION ec2 describe-instances --instance-ids "$INSTANCE_ID"  --query 'Reservations[0].Instances[0].SpotInstanceRequestId' --output text)
TAGS=$(aws --region $AWS_REGION ec2 describe-spot-instance-requests --spot-instance-request-ids "$SPOT_REQ_ID" --query 'SpotInstanceRequests[0].Tags')
aws --region $AWS_REGION ec2 create-tags --resources "$INSTANCE_ID" --tags "$TAGS"

%{ for key, value in envs }
unset ${key}
%{ endfor ~}