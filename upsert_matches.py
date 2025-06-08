# upsert_matches.py
from app import create_app, db
from app.services.api_client import fetch_multiple_competition_matches
from app.models import Match
import datetime

app = create_app()
with app.app_context():
    # 1) purge old data
    db.session.query(Match).delete()
    db.session.commit()

    # 2) fetch fresh matches
    matches = fetch_multiple_competition_matches(
        "PL,PD", date_from="2025-01-01", date_to="2025-06-07"
    )

    # 3) insert all
    for m in matches:
        rec = Match(
            api_id=m["id"],
            utc_date=datetime.datetime.fromisoformat(m["utcDate"].replace("Z", "")),
            home_team=m["homeTeam"]["name"],
            away_team=m["awayTeam"]["name"],
            home_score=m["score"]["fullTime"]["home"],
            away_score=m["score"]["fullTime"]["away"],
            competition=m["competition"]["code"],
        )
        db.session.add(rec)

    db.session.commit()
    print(f"Loaded {len(matches)} matches")
