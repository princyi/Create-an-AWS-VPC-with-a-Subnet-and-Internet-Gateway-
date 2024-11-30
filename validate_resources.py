import boto3
import json

# AWS Configuration
region = "us-east-1"

# Load Terraform Outputs
with open("terraform_outputs.json", "r") as file:
    outputs = json.load(file)

vpc_id = outputs["vpc_id"]["value"]
subnet_id = outputs["subnet_id"]["value"]
igw_id = outputs["internet_gateway_id"]["value"]

# Initialize AWS Clients
ec2 = boto3.client("ec2", region_name=region)

# Validate VPC
print(f"Validating VPC: {vpc_id}")
vpcs = ec2.describe_vpcs(VpcIds=[vpc_id])
if vpcs["Vpcs"]:
    print(f"VPC {vpc_id} exists!")
else:
    print(f"VPC {vpc_id} not found!")

# Validate Subnet
print(f"\nValidating Subnet: {subnet_id}")
subnets = ec2.describe_subnets(SubnetIds=[subnet_id])
if subnets["Subnets"]:
    print(f"Subnet {subnet_id} exists!")
else:
    print(f"Subnet {subnet_id} not found!")

# Validate Internet Gateway
print(f"\nValidating Internet Gateway: {igw_id}")
igws = ec2.describe_internet_gateways(InternetGatewayIds=[igw_id])
if igws["InternetGateways"]:
    print(f"Internet Gateway {igw_id} exists!")
else:
    print(f"Internet Gateway {igw_id} not found!")
