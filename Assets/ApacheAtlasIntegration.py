import requests, json, os 

from pyapacheatlas.auth import ServicePrincipalAuthentication
from pyapacheatlas.core import PurviewClient, AtlasEntity
from pyapacheatlas.readers import ExcelConfiguration, ExcelReader
from pyapacheatlas.core.client import PurviewClient

tenant_id = '<enter your tenant id>'
client_id = '<enter your client id>'
client_secret = '<enter your secret>'
account_name= '<enter your purview account name>'
data_catalog_name = '<enter your purview account name>'
resource_url = 'https://purview.azure.net'

def azuread_auth(tenant_id: str, client_id: str, client_secret: str, resource_url: str):
    """
    Authenticates Service Principal to the provided Resource URL, and returns the OAuth Access Token
    """
    url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
    payload= f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&resource={resource_url}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = json.loads(response.text)['access_token']
    return access_token


#Get the Purview Authorization
def purview_auth(tenant_id: str, client_id: str, client_secret: str, data_catalog_name: str):
    """
    Authenticates to Atlas Endpoint and returns a client object
    """
    oauth = ServicePrincipalAuthentication(
        tenant_id = tenant_id,
        client_id = client_id,
        client_secret = client_secret
    )
    client = PurviewClient(
        account_name = data_catalog_name,
        authentication = oauth
    )
    return client

oauth = ServicePrincipalAuthentication(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

client = PurviewClient(
    account_name=data_catalog_name,
    authentication=oauth
)
results = client.get_all_typedefs()
print(json.dumps(results, indent=2))