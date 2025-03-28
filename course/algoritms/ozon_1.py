letters = "abcdefghijklmnopqrstuvxyz"
vowels_lower = "euioay"
letters_upper = ''.join(x.upper() for x in letters)
vowels_upper = ''.join(x.upper() for x in vowels_lower)
vowels = vowels_lower + vowels_upper
consonant_lower = ''.join(x for x in letters if x not in vowels_lower)
consonant_upper = ''.join(x.upper() for x in consonant_lower)
consonant = consonant_lower + consonant_upper


def check_password(password):
    if not any(i in consonant for i in password):
        if not any(i in letters_upper for i in password):
            password += consonant_upper[1]
        else:
            password += consonant_lower[1]

    if not any(i in vowels for i in password):
        if not any(i in letters_upper for i in password):
            password += vowels_upper[1]
        else:
            password += vowels_lower[1]

    if not any(i.islower() for i in password):
        password += consonant_lower[1]
    if not any(i.isdigit() for i in password):
        password += '1'
    if not any(i.isupper() for i in password):
        password += consonant_upper[1]

    return password


def main():
    t = int(input())
    passwords = []
    while t > 0:
        passwords.append(input())
        t -= 1
    for i in passwords:
        print(check_password(i))

if __name__ == "__main__":
    main()