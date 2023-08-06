# Zerodha Login Automated; Supported by Lambda function that processes the redirect rul and stores accessk key to DynamoDB AND GCP function that automates login through headless chrome

## Context
This code is for a python package for automated login to Zerodha. The redirect URL is not handled here - Separate Repo with a container that runs as a lambda function saves the access token to dynamoDB

## How to productionalize
- Get Zerodha (kite.trade) account for API based access to the platform.
- Create a '.zerodha' file in your home directory (Sample provided - check .zerodha.sample file)
    - Needed Variables in File are Zerodha API keys/secret


- Checkout zlogin-puppeteer repository that automates login process (using headless chrome)
- Check out the zerodha-dynamodb-save-accesstoken repository to set up a lambda function to handle Zerodha redirect url (it saves the access token in the save_access table in dynamodb)
- Install zlogin package from pypi, "pip install zlogin"

```python
import zlogin
access_token = zlogin.fetch_access_token()
```

## This repo is a sister repo with zerodha-dynamodb-save-accesstoken & zlogin-puppeteer tools which has a container code for lambda function that handles storage of access token to dynamodb; 
