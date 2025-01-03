from collections import deque

sentences = [
    'A rosa upala na lapu Asora',
    'AbcDeFfedCba',
    'Kayak',
    'Deified',
    'Rotator',
    'Repaper',
    'Deed',
    'Peep',
    'Wow',
    'Noon',
    'Engage le jeu que je le gagne',
    'I topi non avevano nipoti',
    'Alli trota la tortilla',
    'Нажал кабан на баклажан',
    'Кіт утік',
    'Це кінець'
]

def is_palindrome(string: str) -> bool:
    prepared = string.lower().replace(' ', '')

    q = deque(prepared)
    iterations = len(prepared) / 2 if len(prepared) % 2 == 0 else len(prepared) // 2

    for _ in range(int(iterations)):
        if q.popleft() == q.pop():
            continue
        else:
            return False

    return True

if __name__ == '__main__':
    for sentence in sentences:
        print(f"'{sentence}' is PALINDROME") \
            if is_palindrome(sentence) \
            else print(f"'{sentence}' is NOT palindrome")
