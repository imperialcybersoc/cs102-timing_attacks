from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class PassObject:

    passwords: list[str] = field(default_factory=lambda: [
        "password123",
        "correct-horse-battery-staple",
        "myV3rYv£Ry$3cUreP@55w0rd",
        "=yEH(4z*Y20_8}DJvxN",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris volutpat accumsan dui, id interdum purus finibus ac. Mauris scelerisque efficitur nulla, sit amet imperdiet erat gravida sit amet. Donec aliquam mauris tristique augue pulvinar, non auctor ipsum laoreet. Maecenas vehicula diam id augue mollis interdum. Ut suscipit lectus sit amet lectus hendrerit interdum. Maecenas in purus vel orci pulvinar venenatis in eget ipsum. Aenean finibus purus nec turpis posuere, a pretium lectus bibendum. Aliquam erat volutpat. Proin tincidunt mauris aliquam ex ullamcorper, non pretium libero semper."
    ])

    def get_password(self, index: int) -> str:
        return self.passwords[index]

phred = PassObject()