from . import scratch_api as api


def explore_worker(username) -> tuple[tuple, str]:
    """Scratch Router's worker.

    Searches for related users (followers and following) by username using Scratch API."""

    following = api.get_following(username)

    found = following

    return found, username


def check_worker(username) -> bool:
    """Scratch Router's worker.

    Checks if certain user really exists."""

    return api.check_user(username)
