
def sub_calc(a, b, op):
    match op:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b if b != 0 else None
        case "^":
            return a**b
        case _:
            return None


def calc(string: str):
    # return eval("1 * - 2")
    return sep(string)


def sep(eq: str):
    nums = []
    ops = []
    neg_pos = []  # positions to negate characters
    ops_in_a_row = 0
    for i in range(len(eq)):
        c = eq[i]
        if not c.isalnum():
            # if the current char is an operator (not a number)
            ops_in_a_row += 1
            if i == 0:
                if c == "-":
                    neg_pos.append(i)
                    continue
                else:
                    return "Cannot have '+' or '*' operator at beginning of expression"
            if not eq[i-1].isalnum():
                # if the current and prev chars are operators, then this one must be '-' and should be skipped
                if ops_in_a_row == 3:
                    return "Cannot have more than 2 operators in a row"
                neg_pos.append(i)
                continue
            ops.append(c)
        else:
            ops_in_a_row = 0

    nums = eq.replace("+", ",").replace("-", ",").replace("*", ",").replace("/", ",").replace("^", ",")
    # [nums.remove(c) for c in nums if c == '']
    for i in range(len(nums)):
        if i in neg_pos:
            nums = nums[:i] + "-" + nums[i+1:]

    nums = nums.split(",")
    return nums

print(calc("1/2/3"))