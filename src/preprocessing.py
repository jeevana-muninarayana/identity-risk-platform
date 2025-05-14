import pandas as pd

def to_dataframe(events: list) -> pd.DataFrame:
    """
    Normalize raw events into a DataFrame with features:
    user, ip, timestamp, device_info, success/failure, etc.
    """
    df = pd.json_normalize(events)
    # select & rename columns
    return df[[
      "actor.alternateId","client.ipAddress","published",
      "outcome.result","client.userAgent"
    ]].rename(columns={
      "actor.alternateId":"user",
      "client.ipAddress":"ip",
      "published":"timestamp",
      "outcome.result":"result",
      "client.userAgent":"user_agent"
    })
