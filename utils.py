import threading
import zoneinfo
from datetime import datetime

def set_interval(func, seconds, app):
    def func_wrapper():
        try:
            with app.app_context():
                func()
                set_interval(func, seconds, app)
        except Exception as e:
            print(f"Func cannot run. {e}", flush=True)
        finally:
            print(f'Finished Scan at: {datetime.now(zoneinfo.ZoneInfo("America/New_York")).strftime("%-I:%M %p")}',
                  flush=True)

    t = threading.Timer(seconds, func_wrapper)

    t.start()

    return t


# deprecated, for reference later
        # count = Video.query.count()
        # min_plays = db.session.query(func.min(VideoStatus.selection_count)).scalar()
        # videos = (db.session.query(Video)
        #           .join(VideoStatus)
        #           .filter(VideoStatus.selection_count == min_plays)
        #           .all())
        # if "played" in filter_args:
        #     random_video = random.choice(videos)
        #     if "lte" in filter_args:
        #         random_videos = (
        #             (db.session.query(Video)
        #              .join(VideoStatus)
        #              .filter(VideoStatus.selection_count == min_plays,
        #                      Video.duration <= int(filter_args["lte"]) * 60)).all()
        #         )
        #         random_video = random.choice(random_videos)
        #     if "gte" in filter_args:
        #         random_videos = (
        #             Video.query.join(VideoStatus)
        #             .filter(
        #                     VideoStatus.selection_count == min_plays,
        #                     Video.duration >= int(filter_args["gte"]) * 60,
        #             ).all()
        #         )
        #         random_video = random.choice(random_videos)
        # elif "lte" in filter_args:
        #     random_videos = (
        #         Video.query.filter(Video.duration <= int(filter_args["lte"] * 60)).all()
        #     )
        #     random_video = random.choice(random_videos)
        # elif "gte" in filter_args:
        #     random_videos = (
        #         Video.query.filter(Video.duration >= int(filter_args["gte"] * 60)).all()
        #     )
        #     random_video = random.choice(random_videos)
        # else:
        #     # random_video = Video.query.offset(random.randrange(count)).first()
        #     random_video = random.choice(videos)
        #
