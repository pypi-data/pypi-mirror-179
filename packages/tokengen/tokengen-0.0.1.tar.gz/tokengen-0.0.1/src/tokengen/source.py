
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import secrets
import docker
from docker.errors import APIError, ContainerError
import logging
import sys
import os


"""Configure logger to stream to stdout"""
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("tokengen")


credential = DefaultAzureCredential()

def generate_30_hex_secret():
    """hex(16) -- 32 characters"""
    AIFI_API_TOKEN = secrets.token_hex(16)

    return AIFI_API_TOKEN


def generate_80_hex_secret():
    """hex(40) -- 80 characters"""
    PEPPER = secrets.token_hex(40)

    return PEPPER


def generate_secret_value_and_push_to_azkeyvault(secret_name, vault_url):
    """
    Authentication procedure -- Azure CLI login
    Target -- Environment variables
    """
    secret_client = SecretClient(vault_url=vault_url, credential=credential)

    hex_30_secret = generate_30_hex_secret()
    hex_80_secret = generate_80_hex_secret()

    try:
        """Send AIFI_API_TOKEN and PEPPER tokens to the secret in the Azurekeyvault"""
        secret = secret_client.set_secret(
            secret_name, 
            "AIFI_API_TOKEN: {0}\nPEPPER: {1}".format(hex_30_secret, hex_80_secret)
            )

        os.environ['AIFI_API_TOKEN'] = hex_30_secret
        os.environ['PEPPER'] = hex_80_secret

    except Exception as e:
        logger.error(e)

    # return hex_30_secret, hex_80_secret
    # Uncomment if we no longer want to export variables to stdout but return then to another function


    # print(secret.name)
    # print(secret.value)         # Gives the key:value pair
    # print(secret.properties.version)



def get_secret_value(vault_url, secret_name):

    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret = secret_client.get_secret(secret_name)

    logger.info(secret.name)
    logger.info(secret.value)


def generate_oasis_api_token(username=None, password=None, email=None, registry=None, retailer=None):
    client = docker.from_env()
    try:
        client.login(
            username=username, 
            password=password, 
            email=email,
            registry='registry.gitlab.com')

        logger.info("Successfully Logged in to registry!")
    except APIError as e:
        print(e)

    try:
        """ auto_remove=True removes container after it exits """
        image_name = "registry.gitlab.com/aifi-ml/production/cloud-api/utils:2.112.0"
        command_args = "'node' './build/src/scripts/generateAdminToken.js'"
        environment_variables = ["PEPPER={0}".format(os.getenv("PEPPER")), "RETAILER=retailer".format(retailer)]

        container = client.containers.run(image_name, command_args, environment=environment_variables, detach=True)

        for log in container.logs(stream=True):
           logger.info(str(log.strip(), encoding="utf-8"))

    except ContainerError as e:
        logger.error(e)