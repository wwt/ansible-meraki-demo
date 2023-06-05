from datetime import datetime, timezone
from dateutil import parser


def _received_at():
    return f"{datetime.now(timezone.utc).isoformat()}".replace("+00:00", "Z")

def _received_at_epoch(strtime):
    return int(parser.parse(strtime).timestamp())

def main(event):
    if "timestamps" not in event:
        event["timestamps"] = {}

    if "received_at" not in event["timestamps"]:
        event["timestamps"]["received_at"] = _received_at()
        event["timestamps"]["received_at_epoch"] = (
            _received_at_epoch(event["timestamps"]["received_at"])
        )

    if "ts" in event:
        event["timestamps"]["ts_epoch"] = _received_at_epoch(event["ts"])

        if "msg_age" not in event["timestamps"]:
            event["timestamps"]["msg_age"] = (
                event["timestamps"]["received_at_epoch"] - event["timestamps"]["ts_epoch"]
            )

    return event
