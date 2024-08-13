import sympy as sp #use sympy for safe evaluation which is both powerful and secure


def evaluate(expression):
    try:
        result = sp.sympify(expression)
        return result
    except (sp.SympifyError, ValueError):
        return "Invalid expression"