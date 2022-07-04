from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    for i in range(len(longer)):
        buf = longer[i]
        if buf in shorter:
            shorter = shorter.replace(buf, '', 1)
        else:
            return buf
            break

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
