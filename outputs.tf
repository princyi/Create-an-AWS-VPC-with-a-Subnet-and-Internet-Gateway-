# Output the VPC ID
output "vpc_id" {
  value = aws_vpc.example_vpc.id
  description = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

# Output the Subnet ID
output "subnet_id" {
  value = aws_subnet.xxxxxxxxxxx.xxxxxxxxxxx
  description = "The ID of the created Subnet"
}

# Output the Internet Gateway ID
output "internet_gateway_id" {
  value = aws_internet_gateway.example_igw.id
  description = "The ID of the created Internet Gateway"
}
