def validate_input(user_input):
    parts = user_input.strip().split()

    if len(parts) != 3:
        return False, "Input must be: number operator number"

    a, op, b = parts

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return False, "Operands must be valid numbers"

    valid_ops = ['+', '-', '*', '/', '%', '**']

    if op not in valid_ops:
        return False, f"Unsupported operator: {op}"

    if op == '/' and b == 0:
        return False, "Division by zero is not allowed"

    return True, (a, op, b)
