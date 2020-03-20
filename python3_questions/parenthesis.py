# Python3 balanced parenthesis.
# Method to tell if there is parenthesis
def control(brackets_series):

    s = []
    for b in brackets_series:
        if b == "{" or b == "[" or b == "(":
            s.append(b)

        elif b == "}" and s:
            pop_item = s.pop()
            if pop_item != "{":
                return 0

        elif b == "]" and s:
            pop_item = s.pop()
            if pop_item != "[":
                return 0

        elif b == ")" and s:
            pop_item = s.pop()
            if pop_item != "(":
                return 0
        else:
            return 0


    if not s:
        return True

    return False


if __name__ == "__main__":
    print(control("{[()()]}"))