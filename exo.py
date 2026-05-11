from typing import TypedDict, Literal


class UserData(TypedDict):
    id: int
    name: str


class HistoryItem(TypedDict):
    action: Literal["login", "purchase", "logout"]
    timestamp: str


class Result(TypedDict):
    display_name: str
    normalized_id: str
    history: list[HistoryItem] | None


def process_user_data(
    user_data: UserData,
    include_history: bool = False
) -> Result:

    user_id = user_data["id"]
    name = user_data["name"]

    result: Result = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8),
        "history": None
    }

    if include_history:
        result["history"] = get_user_history(user_id)

    return result


def get_user_history(user_id: int) -> list[HistoryItem]:

    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]


sample_user: UserData = {
    "id": 42,
    "name": "Alice"
}

processed = process_user_data(sample_user, True)

print(processed)