from flask import Blueprint, request, jsonify, abort
from app import db
from app.models import Match
import datetime

bp = Blueprint("matches", __name__, url_prefix="/matches")

@bp.route("/", methods=["GET"])
def list_matches():
    matches = Match.query.all()
    return jsonify([m.to_dict() for m in matches]), 200

@bp.route("/<int:id>", methods=["GET"])
def get_match(id):
    m = Match.query.get(id)
    if not m:
        abort(404, description="Match not found")
    return jsonify(m.to_dict()), 200

@bp.route("/", methods=["POST"])
def create_match():
    data = request.get_json() or {}
    # basic validation
    for field in ("api_id","utc_date","home_team","away_team","competition"):
        if field not in data:
            abort(400, description=f"Missing field: {field}")
    m = Match(
        api_id      = data["api_id"],
        utc_date    = datetime.datetime.fromisoformat(data["utc_date"]),
        home_team   = data["home_team"],
        away_team   = data["away_team"],
        home_score  = data.get("home_score"),
        away_score  = data.get("away_score"),
        competition = data["competition"],
    )
    db.session.add(m)
    db.session.commit()
    return jsonify(m.to_dict()), 201

@bp.route("/<int:id>", methods=["PUT"])
def update_match(id):
    m = Match.query.get(id)
    if not m:
        abort(404, description="Match not found")
    data = request.get_json() or {}
    # update allowed fields
    for field in ("home_score","away_score"):
        if field in data:
            setattr(m, field, data[field])
    db.session.commit()
    return jsonify(m.to_dict()), 200

@bp.route("/<int:id>", methods=["DELETE"])
def delete_match(id):
    m = Match.query.get(id)
    if not m:
        abort(404, description="Match not found")
    db.session.delete(m)
    db.session.commit()
    return "", 204
