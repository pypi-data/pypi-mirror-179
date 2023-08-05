

# Configure Azure CLI from CLI
```sh
# Authenticate with Azure CLI Creds from Terminal -- Temporal
az login 

# Creating an Azure Active Directory Registered Application
az ad sp create-for-rbac --name aifi-tokengen --role Contributor --scopes /subscriptions/<subscription-id>

az ad sp create-for-rbac --name aifi-tokengen --role Contributor --scopes /subscriptions/46081af3-7258-44cd-899c-db7516f0a121

# Set Environment Variables with the Values
AZURE_CLIENT_ID	appId value from the generated JSON
AZURE_TENANT_ID	tenant value from the generated JSON
AZURE_CLIENT_SECRET	password value from the generated JSON
```

# Environment Setup
```sh
# create venv
python3 -m venv venv

# Activate the venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Switch to developer mode
python3 setup.py develop

# Run for helper commands
tokengen -h
```

## Why Python Secrets?
```sh
# From Python Docs
The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.
```
# Issues
## Performance Time Too High For Initial Pull

1. Take a look at the `registry.gitlab.com/aifi-ml/production/cloud-api/utils` image

- See if that can be changed to an alpine image for node


# Logging Improvement
```sh
- Exception if the secret doesnt exist
- Exception if the secret name is invalid
- Azure Authenticate with Env variables or kubernetes (hmm..!)

```