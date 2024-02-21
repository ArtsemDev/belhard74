__all__ = [
    "send_email",
]


def send_email(subject: str, message: str, email: str, recipients: list[str]) -> bool:
    print("SEND")


if __name__ == '__main__':
    send_email("", "", "", [])
