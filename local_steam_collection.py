import json

file = "/home/lettever/.steam/debian-installation/userdata/1047710596/config/cloudstorage/cloud-storage-namespace-1.json"
with open(file) as f:
    data = f.read()


def get_collections(data):
    """Extract all active (non-deleted) user collections with their game IDs."""
    active_collections = []

    for item in data:
        key = item[0]
        metadata = item[1]

        if not key.startswith("user-collections.uc-"):
            continue

        if metadata.get("is_deleted", False):
            continue

        if "value" in metadata:
            try:
                value_data = json.loads(metadata["value"])

                if "added" in value_data:
                    active_collections.append(
                        {
                            "key": key,
                            "name": value_data.get("name", "Unnamed"),
                            "timestamp": metadata.get("timestamp"),
                            "version": metadata.get("version"),
                            "game_ids": value_data.get("added", []),
                            "game_count": len(value_data.get("added", [])),
                            "conflict_method": metadata.get("conflictResolutionMethod"),
                            "str_method_id": metadata.get("strMethodId"),
                        }
                    )
            except json.JSONDecodeError:
                print(f"Could not parse value for {key}")
                continue

    return active_collections


collections = {col["name"]: col for col in get_collections(json.loads(data))}
print(f"{len(collections)=}")
print(f"{len(collections["2.2 - Check Later"]["game_ids"])=}")
