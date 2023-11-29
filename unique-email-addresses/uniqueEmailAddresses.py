def numUniqueEmails(emails: List[str]) -> int:
    unique = set()

    for email in emails:
        cleanedEmail = ""
        ignoreNextChars = False
        i = 0
        while i < len(email):
            if email[i] == '@':
                cleanedEmail += email[i:]
                break
            elif email[i] == '+':
                ignoreNextChars = True
            elif email[i] == '.':
                pass
            else:
                if not ignoreNextChars:
                    cleanedEmail += email[i]
                
            i += 1

        unique.add(cleanedEmail)

    return len(unique)


