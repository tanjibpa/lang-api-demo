import random
from datetime import date

from flask import current_app as app
from flask_restplus import Resource, Api, reqparse
from sqlalchemy import and_
from sqlalchemy.sql.operators import ColumnOperators

from .models import db, Track, Playback

api = Api()

listening_args = reqparse.RequestParser()
listening_args.add_argument("size", type=int)
listening_args.add_argument("pulledids", action="append")

listening_put_args = reqparse.RequestParser()
listening_put_args.add_argument("id", type=int)

# generate random user id
user_id = random.randint(1, 6)


@api.route("/listening")
class Listening(Resource):
    def get(self):
        args = listening_args.parse_args()
        size = args.size
        # print(args.pulledids)
        # return "get"
        pulledids = [int(i) for i in args.pulledids[0].split(',')]
        tracks = Track.query.filter(~Track.id.in_(pulledids)).limit(size).all()
        print(tracks)
        if len(tracks) < size:
            print(Track.query.limit(size-len(tracks)).all())
            tracks += Track.query.limit(size-len(tracks)).all()
        return [track.to_dict() for track in tracks]

    def put(self):
        args = listening_put_args.parse_args()
        track = Track.query.filter_by(id=args.id).first()

        if not track:
            return {"error": "Track does not exist"}
        
        today = date.today()
        track_record = Playback.query.filter(
            and_(
                Playback.track_id == track.id,
                Playback.last_listened_date == date.today(),
            )
        ).first()
        
        if track_record:
            track_record.listen_reps += 1
        else:
            track_record = Playback(
                track=track, last_listened_date=today, listen_reps=1
        
            )
        db.session.add(track_record)
        db.session.commit()

        return {
            "message": "Playback updated"
        }
