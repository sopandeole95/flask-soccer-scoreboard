import datetime

def make_match_payload(api_id=42):
    return {
        "api_id": api_id,
        "utc_date": datetime.datetime.utcnow().isoformat(),
        "home_team": "Team A",
        "away_team": "Team B",
        "competition": "PL"
    }

def test_list_empty(client):
    resp = client.get("/matches/")
    assert resp.status_code == 200
    assert resp.get_json() == []

def test_create_and_get_match(client):
    payload = make_match_payload()
    # Create
    resp = client.post("/matches/", json=payload)
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["api_id"] == payload["api_id"]

    # Get by id
    match_id = data["id"]
    resp = client.get(f"/matches/{match_id}")
    assert resp.status_code == 200
    got = resp.get_json()
    assert got["home_team"] == "Team A"

def test_update_and_delete(client):
    payload = make_match_payload(api_id=100)
    # create
    r = client.post("/matches/", json=payload)
    mid = r.get_json()["id"]

    # update
    resp = client.put(f"/matches/{mid}", json={"home_score": 2, "away_score": 1})
    assert resp.status_code == 200
    assert resp.get_json()["home_score"] == 2

    # delete
    resp = client.delete(f"/matches/{mid}")
    assert resp.status_code == 204

    # now 404 on get
    resp = client.get(f"/matches/{mid}")
    assert resp.status_code == 404