def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, other = s.split("@")
        websitename, extension = other.split(".")
    except:
        return False
    
    username = username.replace("-", "").replace("_", "")
    if username.isalnum() == False:
        return False
    elif websitename.isalnum() == False:
        return False
    elif len(extension) > 3:
        return False
    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
