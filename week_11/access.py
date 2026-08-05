def check_access(registered, lab_open, computer_available):
    if registered and lab_open and computer_available:
        return "Access Granted"
    else:
        return "Access Denied"


def get_reason(registered, lab_open, computer_available):
    if not registered:
        return "Student is not registered."
    elif not lab_open:
        return "Computer lab is closed."
    elif not computer_available:
        return "No available computer."
    else:
        return "Welcome to the lab."