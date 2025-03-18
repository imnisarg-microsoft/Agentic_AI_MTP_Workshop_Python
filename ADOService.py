import requests
from azure.identity import AzureCliCredential

# Set your Azure DevOps details
ADO_ORG = "https://dev.azure.com/microsoft"  # Replace with your org URL
ADO_PROJECT = "SITOPS"  # Replace with your project name
ADO_REPO = "SITOPS-Svc-TenantManagement"  # Replace with your repo name
FILE_PATH = "README.md"  # Replace with the file path in the repo
BRANCH = "main"  # Replace with the branch name

# Authenticate using AzureCLICredential
credential = AzureCliCredential()
access_token = credential.get_token("499b84ac-1321-427f-aa17-267ca6975798/.default").token  # Azure DevOps Scope

# Headers for authentication
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Construct URL to fetch file contents
file_url = f"{ADO_ORG}/{ADO_PROJECT}/_apis/git/repositories/{ADO_REPO}/items?path={FILE_PATH}&versionType=branch&version={BRANCH}&includeContent=True&api-version=7.1-preview.1"

# Send GET request
response = requests.get(file_url, headers=headers)

if response.status_code == 200:
    file_content = response.text  # Directly get the file content
    print(f"Contents of {FILE_PATH}:\n")
    print(file_content)
else:
    print(f"Failed to fetch file: {response.status_code}, {response.text}")
