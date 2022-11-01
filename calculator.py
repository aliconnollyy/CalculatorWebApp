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