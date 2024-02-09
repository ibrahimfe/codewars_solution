def flick_switch(lst):
    result = []
    flicked = True

    for item in lst:
        if item == "flick":
            flicked = not flicked

        result.append(flicked)

    return result
