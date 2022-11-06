from time import sleep


def main():
    quit = ("q", "quit", "Q", "QUIT", "exit")
    while True:
        ui = input("Please enter your equation. Enter 'q' to quit." + 
                   "\nUse exp(x) for any equations involving e = 2.718..." + 
                   "\nUse log for any equations involving loge(x), where e = 2.718...\n\n")
        if ui in quit:
            print("Exiting...")
            sleep(1)
            break
        print(calc(ui))

valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
valid_ops = ["+", "-", "*", "/", "^"]
valid_chars = ["(", ")", "."]
order = [["+", "-"], ["*", "/"], ["^"]]


def isNum(a):
    return a >= '0' and a <= '9'


def check_op(num):
    """Get the precedence order of a specific operator"""
    return order[num-1]


def prec(op):
    """Get the precedence order of a specific operator"""
    match op:
        case "+" | "-":
            return 1
        case "*" | "/":
            return 2
        case "^":
            return 3


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


def validate(eq: str):
    """Checks and returns a value based on whether or not the given expression is valid or not. 
    If is it valid, it returns the equation with '!' prefixed to it to indicate it passed.
    Otherwise, it returns an error message."""

    valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    valid_ops = ["+", "-", "*", "/", "^"]
    valid_chars = ["(", ")", "."]
    # check entire equation at first

    # check first character of expression
    if eq[0] in valid_ops and eq[0] != "-":
        return "Invalid: Can only have number or \"-\" at beginning of expression"

    # check last character of expression
    if eq[-1] in valid_ops or eq[-1] in valid_chars:
        return "Invalid: Cannot end expression with an operator"

    # check for too many adjacent instances of operators
    for i in range(len(eq)):
        # check every character invidually now
        if eq[i] not in valid_nums and eq[i] not in valid_ops and eq[i] not in valid_chars:
            return "Invalid: Contains invalid character: \"" + eq[i] + "\""
        if eq[i] == ".":
            if (i == 0 or i == len(eq) - 1) or (isNum(eq[i-1]) and not isNum(eq[i+1])):
                return "Invalid: invalid position for decimal point (.)"
        # "++++++..." should be "++", else invalid (a + (+b)) = a + b
        # "------..." should be "--", else invalid (a - (-b)) = a + b
        if eq[i] in valid_ops and eq[i+1] in valid_ops:
            if not eq[i+1] in ('+', '-'):
                return "Invalid: consecutive operator not '+' or '-'"
            if eq[i+2] in valid_ops:
                return "Invalid: can't have more than three operators in a row"

    return "!" + eq


def calc(equation: str):
    """Calculates the expression and returns the result."""

    nums = []
    ops = []
    neg_pos = []  # positions to negate characters

    eq = equation.replace(" ", "")  # remove whitespace
    eq = validate(eq)
    if eq[0] != "!":
        return eq
    eq = eq[0:]

    teq = ""
    i = 0
    while i < len(eq):
        c = eq[i]
        p = ""
        if i != 0:
            if c == "-" and eq[i+1].isalnum() and eq[i-1].isalnum():
                # given an equation x - y * z, the program will assume y to be positive when multplying.
                # this loop takes any negative value and, as long as it isn't at the beginning, changes it from
                # - to +-
                # to make the program recognise that the value should be assumed to be negative rather than positive.
                # e.g., a - b = a + (-b) = a+-b
                # additionally, the order of precedence must be accounted for, so the value will NOT be negated if
                # the operator in front of it is the exponent
                # e.g., a-b^c = a - (b^c).
                q = i+1
                while q < len(eq) and (eq[q].isalnum() or eq[q] == "."):
                    q += 1
                if q != len(eq) and eq[q] != "^":
                    p = "+-"
                else:
                    p += c
            elif eq[i] == "+" and eq[i+1] == "+":
                # a ++ b == a + b, but a +++ b = invalid
                # it technically still counts when entered into an actual calculator,
                # but it is prohibited here based on the rules in `validate()`
                # w = i
                # while eq[w+1] == c:
                #     w += 1
                # i = w
                p = c
                i += 1
            else:
                # else just add it like a regular character
                p = c
        teq += p
        i += 1

    eq = teq

    # eq is now the equation to be worked from to avoid side effects
    for i in range(len(eq)):
        c = eq[i]
        if not c.isalnum():
            # if the current char is an operator (not a number)
            if i == 0:
                if c == "-":
                    neg_pos.append(0)
                    # print(c)
                    continue
            if not eq[i-1].isalnum():
                # if the current and prev chars are negative, then this one must be negated
                neg_pos.append(i)
            else:
                # otherwise this is an operator
                ops.append(c)

    # remove all operators
    nums = eq.replace("+", ",").replace("-", ",").replace("*", ",").replace("/",
                                                                            ",").replace("^", ",").replace("(", ",").replace(")", ",")

    # for each value to be negated, replace the character at that position with '-'
    for i in range(len(nums)):
        if i in neg_pos:
            nums = nums[:i] + "-" + nums[i+1:]

    # split string by comma delimiter, leaving negative values in
    nums = nums.split(",")
    p_o = len(order)  # precedence orderer

    # actual calculation
    # calculate all adjacent values left to right, write result in left position, and remove right value
    # follows order of precedence as defined by the order of operators in ops
    while len(nums) > 1:
        while p_o > 0:
            # if the set of operators in the equation has at least one of the operators at the current precedence
            while not set(ops).isdisjoint(check_op(p_o)):
                i = 0
                while i < len(ops):
                    if ops[i] in check_op(p_o):
                        a = float(nums[i]) if "." in nums[i] else int(nums[i])
                        b = float(nums[i+1]) if "." in nums[i+1] else int(nums[i+1])
                        nums[i+1] = None
                        c = sub_calc(a, b, ops[i])
                        if c == None:
                            return "Invalid: Division by zero"
                        nums[i] = str(c)
                        break
                    i += 1
                [nums.remove(p) for p in nums if p == None]
                del ops[i]
            p_o -= 1

    if '.' in nums[0]:
        return '{:.3f}'.format(float(nums[0])) # format to 3 decimal places
    else:
        return nums[0]


if __name__ == '__main__':
    main()
