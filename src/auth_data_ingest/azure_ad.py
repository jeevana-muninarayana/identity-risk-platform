# azure_ad.py
from msal import ConfidentialClientApplication
def fetch_azure_signins(since_timestamp):
    """
    Authenticate via MSAL and pull Azure AD sign-in logs.
    """
    app = ConfidentialClientApplication(
        os.getenv("AZURE_CLIENT_ID"),
        authority=f"https://login.microsoftonline.com/{os.getenv('AZURE_TENANT_ID')}",
        client_credential=os.getenv("AZURE_CLIENT_SECRET")
    )
    token = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
    # call MS Graph signInReports…
    return []
