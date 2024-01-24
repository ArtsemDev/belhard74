from dataclasses import dataclass


def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]


@dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    email: str
