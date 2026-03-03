def add(a, b):
    """Add two numbeers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b

    """
    return a + b


def sub(a, b):
    """Sub two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: subtraction of b from a

    """
    return a - b


def square(a):
    """Return the square of a.

    Args:
        a (int): First number

    Returns:
        int: square of a

    """
    return a**2


def print_data(df):
    """Print a DataFrame and return its number of rows.

    Args:
        df (pd.DataFrame): DataFrame to print

    Returns:
        int: number of rows in the DataFrame

    """
    print(df)
    return df.shape[0]
