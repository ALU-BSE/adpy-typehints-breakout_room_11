from typing import TypedDict
class UserData(TypedDict):
    id: int
    name: str

def process_user_data(user_data: UserData, include_history=False):
    user_id = user_data["id"]
    name = user_data["name"]
    
    result = {
        "display_name": f"User {name}",
        "normalized_id": str(user_id).zfill(8)
    }
    
    if include_history:
        result["history"] = get_user_history(user_id)
    
    return result

def get_user_history(user_id: int):
    
    # Simulate database call
    return [
        {"action": "login", "timestamp": "2023-10-01T10:30:00"},
        {"action": "purchase", "timestamp": "2023-10-02T14:20:00"}
    ]

# Sample usage
sample_user: UserData = {"id": 42, "name": "Alice"}
processed = process_user_data(sample_user, True)
print(processed)
