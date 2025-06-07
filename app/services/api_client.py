import requests
from flask import current_app

def fetch_competition_matches(competition="PL", date_from=None, date_to=None):
    cfg = current_app.config
    url = f"{cfg['SOCCER_API_URL']}/competitions/{competition}/matches"
    headers = {"X-Auth-Token": cfg["SOCCER_API_TOKEN"]}
    params = {}
    if date_from: params["dateFrom"] = date_from
    if date_to:   params["dateTo"]   = date_to

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()["matches"]


def fetch_competitions():
    """
    Returns a list of competitions your account is subscribed to.
    """
    cfg = current_app.config
    url = f"{cfg['SOCCER_API_URL']}/competitions"
    headers = {"X-Auth-Token": cfg["SOCCER_API_TOKEN"]}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()  # contains "competitions" key


def fetch_live_matches_for_comps(comps, date_from=None, date_to=None):
    cfg   = current_app.config
    url   = f"{cfg['SOCCER_API_URL']}/matches"
    headers = {"X-Auth-Token": cfg["SOCCER_API_TOKEN"]}
    params  = {"competitions": comps}
    if date_from: params["dateFrom"] = date_from
    if date_to:   params["dateTo"]   = date_to

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()["matches"]


from app.services.api_client import fetch_competition_matches

def fetch_multiple_competition_matches(comps, date_from=None, date_to=None):
    """
    Fetch and combine matches for multiple competitions by calling
    the single‐competition endpoint in a loop.
    """
    all_matches = []
    for comp in comps.split(","):
        ms = fetch_competition_matches(
            competition=comp.strip(),
            date_from=date_from,
            date_to=date_to,
        )
        all_matches.extend(ms)
    return all_matches
