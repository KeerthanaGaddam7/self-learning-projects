import hashlib
import json


def generate_sha256(data: dict) -> str:

    json_string = json.dumps(
        data,
        sort_keys=True
    )

    sha = hashlib.sha256(
        json_string.encode("utf-8")
    )

    return sha.hexdigest()