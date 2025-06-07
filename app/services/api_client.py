import requests
from flask import current_app

def fetch_live_matches(date_from=None, date_to=None):
    """
    Returns the JSON payload of matches from Football-Data.org.
    Optional date_from/to in YYYY-MM-DD format filters the results.
    """
    cfg = current_app.config
    url = f"{cfg['SOCCER_API_URL']}/matches"
    headers = {"X-Auth-Token": cfg["SOCCER_API_TOKEN"]}
    params = {}
    if date_from: params["dateFrom"] = date_from
    if date_to:   params["dateTo"]   = date_to

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()  # dict with "matches" key
