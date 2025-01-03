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

def is_palindrome(original_string: str) -> str:
    prepared = original_string.lower().replace(' ', '')

    return 'palindrome' if prepared == prepared[::-1] else 'NOT palindrome'


if __name__ == '__main__':
    for sentence in sentences:
        print(f"'{sentence}' is {is_palindrome(sentence)}")
