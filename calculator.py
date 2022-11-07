from math import e, log
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
        print(solve(ui))

valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
valid_ops = ["+", "-", "*", "/", "^"]
valid_chars = ["(", ")", "."]
order = [["+", "-"], ["*", "/"], ["^"]]
euler = str(e)  # euler = e = 2.718281828...

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

    if eq == "":
        return "Invalid: Expressions cannot be empty"

    # check first character of expression
    if eq[0] in valid_ops and eq[0] != "-":
        return "Invalid: Can only have number or \"-\" (negative) at beginning of expression"
    

    if "(" in eq and ")" not in eq:
        return "Invalid: Unclosed expression" 
    if ")" in eq and "(" not in eq:
        return "Invalid: Parenthesis closed before opening"

    if eq[-1] in valid_ops and not eq[-1] == ")":
        return "Invalid: Cannot end expression with an operator"

    # check for too many adjacent instances of operators
    # for i in range(len(eq)):
    i = 0
    while i < len(eq):
        # check every character invidually now
        # "+-*-+" is invalid, but also "+++" or "---"
        if eq[i] in valid_ops and eq[i+1] in valid_ops:
            if not eq[i+1] in ('+', '-'):
                return "Invalid: Consecutive operator not '+' or '-'"
            if eq[i+2] in valid_ops:
                return "Invalid: Can't have more than three \"" + eq[i] + "\" operators in a row"
        if eq[i] == ".":
            if (i == 0 or i == len(eq) - 1) or (isNum(eq[i-1]) and not isNum(eq[i+1])):
                return "Invalid: Illegal position for decimal point (.)"
        if i < len(eq) - 1 and eq[i] == ")" and isNum(eq[i+1]):
            return "Invalid: Number after parenthesis has no preceeding operator"
        if i < len(eq) - 1 and eq[i] == "(" and eq[i+1] in valid_ops:
            return "Invalid: Parenthesis cannot start with an operator"
        if i > 0 and eq[i] == ")" and eq[i-1] in valid_ops:
            return "Invalid: Parenthesis cannot end with an operator"
        if i < len(eq) - 1 and eq[i] == "(" and eq[i+1] == ")":
            return "Invalid: Empty parenthesis"
        if i < len(eq) - 3:
            if eq[i:i+3] in ("exp", "log"):
                t_op = eq[i:i+3]
                if not eq[i+3] == "(":
                    return "Invalid: Unary operator " + t_op + " must enclose its parameter in brackets (e.g. " + t_op + "(4))"
                i += 3  # continue past "exp(" or "log("
                if eq[i+1] == ")":
                    return "Invalid: Empty parenthesis"
        if eq[i] not in valid_nums and eq[i] not in valid_ops and eq[i] not in valid_chars:
            return "Invalid: Contains invalid character: \"" + eq[i] + "\""

        i += 1

    return "!" + eq


def solve(eq: str, dp=3) -> str:
    """
    Solves the equation `eq`.
    `dp` refers to how many decimal points are to be shown, defaulting to 3.
    """
    
    eq = eq.replace(" ", "")  # remove whitespace
    eq = validate(eq)
    if eq[0] != "!":
        return eq

    eq = eq[1:]
    i = 0
    p = i
    while i < len(eq) and "(" in eq and ")" in eq:
        while i < len(eq) and eq[i] != ")":
            i += 1
        p = i
        while i >= 0 and eq[p] != "(":
            p -= 1

        # to parse x(y)
        if p > 0 and isNum(eq[p-1]):
            eq = eq[:p] + "*" + eq[p:]
            p += 1
            i += 1
        
        small_eq = eq[p+1:i]
        
        ans = calc(small_eq)
        ahead = eq[i+1:]
        i = p + len(ans)
        eq = eq[:p] + ans + ahead

    # Recurse through the equation if there are still parenthesis in it
    if "(" in eq and ")" in eq:
        eq = solve(eq, dp=dp)

    # format output based on whether or not it is a decimal number
    final = calc(eq)
    if "." in final:
        return "{:.{prec}f}".format(float(final), prec=dp)
    else:
        return final


def normalise(eq: str) -> str:
    """Takes in a valid equation and normalises it, allowing it to work with calc()"""
    
    for i in range(len(eq)):
        if i < len(eq) - 3:
            if "exp" in eq[i:i+3]:
                # exp must use a minimum of 6 characters (e.g. len("exp(a)") == 6)
                eq = eq[:i] + euler + "^" + eq[i+3:]
                i += len(euler)
            if "log" in eq[i:i+3]:
                # log must use a minimum of 6 characters (e.g. len("log(a)") == 6)
                # replace the calculation of the current log(x) and put it back in this string
                p = i
                while p < len(eq) and eq[p] not in valid_ops:
                    p += 1
                eq = eq[:i] + str(log(float(calc(eq[i+3:p])))) + eq[p:]  # horrible, but necessary
                # return (True, str(log(float(eq[i+3:]))))

    teq = eq[0]
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

    return teq

def calc(equation: str) -> str:
    """Calculates the expression and returns the result."""

    nums = []
    ops = []
    neg_pos = []  # positions to negate characters

    eq = normalise(equation)

    # eq is now the equation to be worked from to avoid side effects
    for i in range(len(eq)):
        c = eq[i]
        if c in valid_ops:
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
    nums = eq.replace("+", ",").replace("-", ",").replace("*", ",")
    nums = nums.replace("/",",").replace("^", ",")
    nums = nums.replace("(", "").replace(")", "")

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
    try:
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
    except ValueError:
        return "Invalid: Result too large"

    return nums[0]


if __name__ == '__main__':
    main()
