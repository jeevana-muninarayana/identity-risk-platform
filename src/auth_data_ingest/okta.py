# okta.py
import requests, os
def fetch_okta_events(since_timestamp):
    """
    Call Okta System Log API, return list of sign-in events since `since_timestamp`.
    """
    token = os.getenv("OKTA_API_TOKEN")
    org   = os.getenv("OKTA_ORG_URL")
    params = {"since": since_timestamp}
    resp = requests.get(f"{org}/api/v1/logs", headers={"Authorization": f"SSWS {token}"}, params=params)
    return resp.json()
