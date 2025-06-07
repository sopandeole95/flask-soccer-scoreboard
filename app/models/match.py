from app import db

class Match(db.Model):
    __tablename__ = "matches"

    id         = db.Column(db.Integer, primary_key=True)
    api_id     = db.Column(db.Integer, unique=True, index=True, nullable=False)
    utc_date   = db.Column(db.DateTime, nullable=False)
    home_team  = db.Column(db.String(128), nullable=False)
    away_team  = db.Column(db.String(128), nullable=False)
    home_score = db.Column(db.Integer, nullable=True)
    away_score = db.Column(db.Integer, nullable=True)
    competition= db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return f"<Match {self.api_id} {self.home_team} vs {self.away_team}>"
