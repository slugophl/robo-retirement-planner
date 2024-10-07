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


def life_expectancy(age: int) -> float | None:
    pass


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
        return f"You fall into this investment bracket Age: {age}. Stocks: {stocks}%, Bonds: {bonds}%"
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

    retirement_target: float = get_float_value(
        "What is the target amount you would like for your retirement account?: "
    )
    your_investment: str = allocation(customer_age, investment_portfolio)  # type: ignore

    print(
        f"""
        Your gender is {gender}
        Your age is {customer_age}
        Your annual income is ${income:.2f}
        The age you'd like to retire at is {retirement_age}
        The amount of years until you retire is {retirement_countdown}
        Your target for your retirement account is ${retirement_target:.2f}
        Your allocation should be {your_investment}
        """
    )


main()
