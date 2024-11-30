## How to Run the Python Script
Install Dependencies:

bash
Copy code
pip install boto3
Export Terraform Outputs to JSON: Run this command after applying the Terraform code:

bash
Copy code
terraform output -json > terraform_outputs.json
Run the Script:

bash
Copy code
python validate_resources.py
Steps Summary
Deploy infrastructure with Terraform:
bash
Copy code
terraform init
terraform apply
Export Terraform outputs to a JSON file:
bash
Copy code
terraform output -json > terraform_outputs.json
Validate the created resources with Python:
bash
Copy code
python validate_resources.py
