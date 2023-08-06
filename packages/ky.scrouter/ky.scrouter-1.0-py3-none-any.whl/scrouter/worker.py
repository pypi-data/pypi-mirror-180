from . import scratch_api as api


def explore_worker(username) -> tuple[tuple, str]:
    """Scratch Router's worker.

    Searches for related users (followers and following) by username using Scratch API."""

    followers = api.get_followers(username)
    following = api.get_following(username)
    friends = []

    if following > followers:
        for f in followers:
            if f in following:
                friends.append(f)
    else:
        for f in following:
            if f in followers:
                friends.append(f)

    found = following + followers

    return found, username


def check_worker(username) -> bool:
    """Scratch Router's worker.

    Checks if certain user really exists."""

    return api.check_user(username)
