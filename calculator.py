def calc(string: str):
    return sep(string)

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
    

    
def validate(eq:str):
    """Checks and returns a value based on whether or not the given expression is valid or not. 
    If is it valid, it returns the equation with '!' prefixed to it to indicate it passed.
    Otherwise, it returns an error message."""
    
    valid_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    valid_ops = ["+", "-", "*", "/", "^", "(", ")"]
    # check entire equation at first
    if "." in eq:
        return "Invalid: Can only have integers" # TODO implement functionality for floats
    

    # check first character of expression
    if not eq[0].isalnum() and eq[0] != "-":
        return "Invalid: Can only have number or \"-\" at beginning of expression"
    
    # check last character of expression
    if eq[-1] in valid_ops and not eq[-1] == ")":
        return "Invalid: Cannot end expression with an operator"

    # check for too many adjacent instances of operators
    for i in range(len(eq)):
        # check every character invidually now
        if eq[i] not in valid_nums and eq[i] not in valid_ops:
            return "Invalid: Contains invalid character: \"" + eq[i] + "\""
        # "+-++-" is invalid
        if eq[i] in valid_ops and eq[i+1] in valid_ops and eq[i+2] in valid_ops:
            return "Invalid: can't have more than three operators in a row"
        # "***..." should be "*", else invalid
        if eq[i] == "*":
            if eq[i+1] == "*":
                return "Invalid: can't have duplicate \"*\" operators in a row"
        # "++++++..." should be "++", else invalid (a + (+b)) = a + b
        # "------..." should be "--", else invalid (a - (-b)) = a + b
        if (eq[i] == "-" and eq[i+1] == "-") or (eq[i] == "+" and eq[i+1] == "+"):
            if eq[i+2] in valid_ops:
                return "Invalid: can't have more than three \"" + eq[i] + "\" operators in a row"

    return "!" + eq


def sep(equation: str):
    """Calculates the expression and returns the result."""
    
    nums = []
    ops = []
    neg_pos = [] # positions to negate characters
    oper = ["^", "/", "*", "+", "-"]
    
    eq = validate(equation)
    if eq[0] != "!": return eq
    eq = eq[0:]
    
    # given an equation x - y * z, the program will assume y to be positive when multplying.
    # this loop takes any negative value and, as long as it isn't at the beginning, changes it from
    # - to +-
    # to make the program recognise that the value should be assumed to be negative rather than positive.
    teq = ""
    for i in range(len(eq)):
        c = eq[i]
        p = ""
        if i != 0:
            if c == "-" and eq[i+1].isalnum() and eq[i-1].isalnum():
                p = "+-"
            else:
                p = c
        teq += p
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
    nums = eq.replace("+", ",").replace("-", ",").replace("*", ",").replace("/", ",").replace("^", ",")
    
    # for each value to be negated, replace the character at that position with '-'    
    for i in range(len(nums)):
        if i in neg_pos:
            nums = nums[:i] + "-" + nums[i+1:]
            
    nums = nums.split(",") # split string by comma delimiter, leaving negative values in
    
    # actual calculation
    # calculate all adjacent values left to right, write result in left position, and remove right value
    # follows order of precedence as defined by the order of operators in ops
    while len(nums) > 1:
        for op in oper:
            while op in ops:
                i = 0
                while i < len(ops):
                    if ops[i] == op:
                        a = nums[i]
                        b = nums[i+1]
                        nums[i+1] = None
                        c = sub_calc(int(a), int(b), op)
                        if c == None:
                            return "Invalid: Division by zero"
                        nums[i] = c
                        break
                    i += 1
                [nums.remove(p) for p in nums if p == None]
                del ops[i]
                
    return nums[0]

# if __name__ == '__main__':
    # main()
