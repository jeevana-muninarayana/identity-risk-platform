# aws_iam.py
import boto3
def fetch_aws_iam_events(since_timestamp):
    """
    Query CloudTrail or IAM logs for console sign-in events.
    """
    ct = boto3.client("cloudtrail")
    events = ct.lookup_events(
        LookupAttributes=[{"AttributeKey":"EventName","AttributeValue":"ConsoleLogin"}],
        StartTime=since_timestamp
    )
    return events.get("Events", [])
