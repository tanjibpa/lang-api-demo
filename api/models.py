from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    playback = db.relationship("Playback", backref="track", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }


class Playback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_listened_date = db.Column(db.Date)
    listen_reps = db.Column(db.Integer, default=0)
    track_id = db.Column(db.Integer, db.ForeignKey("track.id"), nullable=False)
