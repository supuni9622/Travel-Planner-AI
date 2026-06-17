import json
from pathlib import Path


MEMORY_DIR = (
    Path(__file__).parent / "users"
)

MEMORY_DIR.mkdir(
    exist_ok=True
)


def load_user_profile(
    user_id: str,
) -> dict:

    file_path = (
        MEMORY_DIR /
        f"{user_id}.json"
    )

    if not file_path.exists():
        return {}

    with open(
        file_path,
        "r",
    ) as f:
        return json.load(f)


def save_user_profile(
    user_id: str,
    profile: dict,
):

    file_path = (
        MEMORY_DIR /
        f"{user_id}.json"
    )

    with open(
        file_path,
        "w",
    ) as f:
        json.dump(
            profile,
            f,
            indent=2,
        )