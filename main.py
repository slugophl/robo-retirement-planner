# TODO - Math stuff

investment_portfolio = {
    25: {"stocks": 100, "bonds": 0},
    30: {"stocks": 95, "bonds": 0},
    35: {"stocks": 85, "bonds": 10},
    40: {"stocks": 75, "bonds": 20},
    45: {"stocks": 65, "bonds": 30},
    50: {"stocks": 55, "bonds": 40},
    55: {"stocks": 45, "bonds": 50},
    60: {"stocks": 35, "bonds": 60},
    65: {"stocks": 25, "bonds": 70},
    70: {"stocks": 15, "bonds": 80},
    75: {"stocks": 5, "bonds": 90},
}

life_expectancy_table_male = {
    0: 73.54,
    1: 72.97,
    2: 72.00,
    3: 71.02,
    4: 70.04,
    5: 69.05,
    6: 68.06,
    7: 67.07,
    8: 66.08,
    9: 65.09,
    10: 64.10,
    11: 63.10,
    12: 62.11,
    13: 61.12,
    14: 60.14,
    15: 59.16,
    16: 58.18,
    17: 57.22,
    18: 56.27,
    19: 55.33,
    20: 54.40,
    21: 53.47,
    22: 52.55,
    23: 51.64,
    24: 50.72,
    25: 49.82,
    26: 48.91,
    27: 48.01,
    28: 47.12,
    29: 46.23,
    30: 45.34,
    31: 44.46,
    32: 43.57,
    33: 42.69,
    34: 41.82,
    35: 40.94,
    36: 40.06,
    37: 39.19,
    38: 38.32,
    39: 37.45,
    40: 36.58,
    41: 35.72,
    42: 34.86,
    43: 34.00,
    44: 33.15,
    45: 32.30,
    46: 31.45,
    47: 30.61,
    48: 29.77,
    49: 28.94,
    50: 28.12,
    51: 27.30,
    52: 26.50,
    53: 25.70,
    54: 24.91,
    55: 24.14,
    56: 23.37,
    57: 22.61,
    58: 21.87,
    59: 21.13,
    60: 20.41,
    61: 19.70,
    62: 19.00,
    63: 18.31,
    64: 17.63,
    65: 16.95,
    66: 16.29,
    67: 15.63,
    68: 14.98,
    69: 14.33,
    70: 13.69,
    71: 13.06,
    72: 12.43,
    73: 11.82,
    74: 11.21,
    75: 10.62,
    76: 10.05,
    77: 9.49,
    78: 8.95,
    79: 8.42,
    80: 7.92,
    81: 7.43,
    82: 6.96,
    83: 6.50,
    84: 6.07,
    85: 5.65,
    86: 5.26,
    87: 4.88,
    88: 4.53,
    89: 4.21,
    90: 3.90,
    91: 3.62,
    92: 3.36,
    93: 3.14,
    94: 2.94,
    95: 2.76,
    96: 2.60,
    97: 2.45,
    98: 2.32,
    99: 2.20,
    100: 2.09,
    101: 1.98,
    102: 1.87,
    103: 1.77,
    104: 1.67,
    105: 1.58,
    106: 1.49,
    107: 1.40,
    108: 1.32,
    109: 1.24,
    110: 1.16,
    111: 1.09,
    112: 1.01,
    113: 0.95,
    114: 0.88,
    115: 0.82,
    116: 0.76,
    117: 0.70,
    118: 0.65,
    119: 0.60,
}

life_expectancy_table_female = {
    0: 79.30,
    1: 78.70,
    2: 77.74,
    3: 76.75,
    4: 75.77,
    5: 74.78,
    6: 73.79,
    7: 72.79,
    8: 71.80,
    9: 70.81,
    10: 69.82,
    11: 68.82,
    12: 67.83,
    13: 66.84,
    14: 65.85,
    15: 64.86,
    16: 63.88,
    17: 62.90,
    18: 61.92,
    19: 60.94,
    20: 59.97,
    21: 59.00,
    22: 58.03,
    23: 57.07,
    24: 56.11,
    25: 55.15,
    26: 54.19,
    27: 53.23,
    28: 52.28,
    29: 51.33,
    30: 50.38,
    31: 49.44,
    32: 48.50,
    33: 47.56,
    34: 46.62,
    35: 45.69,
    36: 44.76,
    37: 43.83,
    38: 42.91,
    39: 41.98,
    40: 41.07,
    41: 40.15,
    42: 39.24,
    43: 38.33,
    44: 37.42,
    45: 36.52,
    46: 35.62,
    47: 34.73,
    48: 33.84,
    49: 32.95,
    50: 32.07,
    51: 31.20,
    52: 30.33,
    53: 29.47,
    54: 28.62,
    55: 27.77,
    56: 26.93,
    57: 26.10,
    58: 25.27,
    59: 24.46,
    60: 23.65,
    61: 22.86,
    62: 22.07,
    63: 21.29,
    64: 20.52,
    65: 19.75,
    66: 18.99,
    67: 18.23,
    68: 17.48,
    69: 16.74,
    70: 16.00,
    71: 15.27,
    72: 14.56,
    73: 13.85,
    74: 13.16,
    75: 12.49,
    76: 11.83,
    77: 11.19,
    78: 10.57,
    79: 9.96,
    80: 9.38,
    81: 8.81,
    82: 8.26,
    83: 7.73,
    84: 7.21,
    85: 6.72,
    86: 6.26,
    87: 5.82,
    88: 5.41,
    89: 5.02,
    90: 4.65,
    91: 4.31,
    92: 3.99,
    93: 3.71,
    94: 3.45,
    95: 3.22,
    96: 3.01,
    97: 2.82,
    98: 2.66,
    99: 2.50,
    100: 2.35,
    101: 2.21,
    102: 2.08,
    103: 1.95,
    104: 1.82,
    105: 1.71,
    106: 1.59,
    107: 1.49,
    108: 1.39,
    109: 1.29,
    110: 1.20,
    111: 1.11,
    112: 1.03,
    113: 0.95,
    114: 0.88,
    115: 0.82,
    116: 0.76,
    117: 0.70,
    118: 0.65,
    119: 0.60,
}

def get_float_value(text: str) -> float:
    while True:
        try:
            user_input: float = float(input(text))
            if user_input > 0:
                return user_input
            else:
                print("Enter a value greater than 0.")
        except ValueError:
            print("Please enter a valid number.")


def get_retirement_value(text: str) -> float:
    while True:
        try:
            user_input: float = float(input(text))
            if user_input >= 0:
                return user_input
            else:
                print("Enter a non negative value.")
        except ValueError:
            print("Please enter a valid number It must be greater than or equal to 0.")


def get_gender(text: str) -> str:
    while True:
        try:
            user_input: str = input(text)
            match user_input.lower():
                case "m":
                    return "male"
                case "f":
                    return "female"
                case _:
                    print("Please enter 'm' for male or 'f' for female.")
        except ValueError:
            print("Please enter 'm' for male or 'f' for female.")


def years_to_retire(current_age: int, retirement_age: int) -> int:
    while True:
        try:
            years_left: int = retirement_age - current_age
            if retirement_age >= years_left:
                return years_left
        except ValueError:
            print(
                f"Please enter valid integer values. age: {current_age} or retirement_age: {retirement_age} should be integers."
            )


def get_age(text: str) -> int:
    while True:
        try:
            user_input: int = int(input(text))
            if user_input >= 0 and user_input <= 130:
                return user_input
            else:
                print("Please enter an age less than 130.")
        except ValueError:
            print("Please enter a valid age. Age must be less than 130.")


def get_retirement_age(text: str, age: int) -> int:
    while True:
        try:
            user_input: int = int(input(text))
            if user_input > age:
                return user_input
            else:
                print(
                    f"Please enter an age greater than or equal to your current age - {age}: "
                )
        except ValueError:
            print(
                f"Please enter a valid age. Age must be greater than your current age - {age}."
            )


def investment_per_paycheck(
    retirement_target: float, years_to_retire: int, principal: float = 0
) -> float:
    r: float = 0.07  # This is guestimating an average 7% return
    n: int = 26  # Bi-weekly paychecks
    t: int = years_to_retire  # Years to retirement target
    p: float = principal  # Starting with input, would default to 0.
    fv: float = retirement_target  # This is what we want in our 401k. (future value)

    numerator: float = fv - p * (1 + r / n) ** (n * t)
    denominator: float = ((1 + r / n) ** (n * t) - 1) / (r / n)

    contribution: float = numerator / denominator
    return round(contribution, 2)

def life_expectancy(age: int, gender: str) -> float | None:
    if gender == 'male':
        print(life_expectancy_table_male)
        return life_expectancy_table_male[age] + age
    else:
        print(life_expectancy_table_female)
        return life_expectancy_table_female[age] + age

def allocation(age: int, investment: dict) -> str | None:
    try:
        if age <= 25:
            age = 25
        elif age >= 75:
            age = 75
        else:
            round_to_nearest_five: int = lambda n: int(5 * round(n / 5))  # type: ignore
            age = round_to_nearest_five(age)  # type: ignore
        stocks = investment[age]["stocks"]
        bonds = investment[age]["bonds"]
        return (
            f"You fall into this Age Bracket: {age}. Stocks: {stocks}%, Bonds: {bonds}%"
        )
    except ValueError as e:
        print(f"Your value is incorrect {e}")


def main():
    gender: str = get_gender(
        "Please enter your gender. The value must be m for male or f for female: "
    )
    customer_age: int = get_age("Please enter your current age:  ")
    income: float = get_float_value(
        "Please enter your annual income. This value must be greater than or equal to 0: "
    )
    retirement_age: int = get_retirement_age(
        "Please enter the age you would like to retire: ", customer_age
    )
    retirement_countdown: int = years_to_retire(customer_age, retirement_age)
    saved_amount: float = get_retirement_value(
        "Please enter the amount of your current 401k you will be transferring. This can also be 0: "
    )

    retirement_target: float = get_float_value(
        "What is the target amount you would like for your retirement account?: "
    )
    your_investment: str = allocation(customer_age, investment_portfolio)  # type: ignore
    contribution: float = investment_per_paycheck(
        retirement_target, retirement_countdown, saved_amount
    )
    your_life_expectancy: float = life_expectancy(customer_age, gender)

    print(
        f"""
        Your gender is {gender}
        Your age is {customer_age}
        Your life expectancy is {your_life_expectancy}
        Your annual income is ${income:.2f}
        The age you'd like to retire at is {retirement_age}
        The amount of years until you retire is {retirement_countdown}
        Your target for your retirement account is ${retirement_target:.2f}
        {your_investment}
        You would need to contribute ${contribution:.2f} per pay period until retirement.
        """
    )


main()