from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class PassObject:

    passwords: list[str] = field(default_factory=lambda: ["password", "password123", "password1234", "password12345", "password123456"])

    def get_password(self, index: int) -> str:
        return self.passwords[index]

phred = PassObject()