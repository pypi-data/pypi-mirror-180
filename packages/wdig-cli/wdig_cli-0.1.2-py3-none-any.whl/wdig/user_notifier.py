"""
simple pub/sub in memory to allow code to publish user messages
"""

# singleton for state


from dataclasses import dataclass

_subscriber_methods_to_call = []


@dataclass
class NotificationMessage:
    message: str


class UserNotifier:
    def __init__(self) -> None:
        # consumer_name = who is sending or receiving
        pass

    def subscribe(self, method_to_invoke: callable) -> None:
        _subscriber_methods_to_call.append(method_to_invoke)

    def send(self, msg: NotificationMessage) -> None:
        for sub in _subscriber_methods_to_call:
            sub(msg)
