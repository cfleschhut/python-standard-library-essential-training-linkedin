import secrets
import string


def generateTempPass(numChars=8):
    potentialChars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    result = "".join(secrets.choice(potentialChars) for i in range(numChars))
    return result


print(generateTempPass(10))


def generateBetterPass(numChars=8):
    potentialChars = string.ascii_letters + string.digits + "+=?/!@#$%*"
    while True:
        result = "".join(secrets.choice(potentialChars)
                         for i in range(numChars))

        if (any(c.isupper() for c in result) and any(c.isdigit() for c in result)):
            break

    return result


print(generateBetterPass(10))


resultUrl = "https://my.example.com?reset="
resultUrl += secrets.token_urlsafe(15)

print(resultUrl)
