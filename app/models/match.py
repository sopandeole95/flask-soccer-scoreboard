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
    
        def to_dict(self):
            return {
                "id":          self.id,
                "api_id":      self.api_id,
                "utc_date":    self.utc_date.isoformat(),
                "home_team":   self.home_team,
                "away_team":   self.away_team,
                "home_score":  self.home_score,
                "away_score":  self.away_score,
                "competition": self.competition,
            }
