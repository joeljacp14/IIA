def sleep_in(weekday, vacation):
    if vacation:
        return True
    else:
        if not weekday:
            return True
        return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
