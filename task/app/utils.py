import json
from json import JSONDecodeError

from task.models.model_name import ModelName


def get_model_name_from_input() -> ModelName:
    print(f"Input a model to use: {[model.value for model in ModelName]}")
    model = input("> ").strip()

    try:
        return ModelName(model)
    except ValueError:
        print(f"Invalid model name: {model}")
        raise


def get_choices_from_input() -> int:
    print("Input a number of choices (n parameter) between 1 to 5:")
    n = input("> ").strip()

    try:
        n = int(n)

        if not (1 <= n <= 5):
            raise ValueError("Input must be an integer between 1 and 5.")

        return n
    except ValueError:
        print(f"Invalid number: {n}")
        raise

def get_temperature_from_input() -> float:
    print("Input a temperature (between 0.0 to 2.0):")
    temperature = input("> ").strip()

    try:
        temperature = round(float(temperature), 1)

        if not (0.0 <= temperature <= 2.0):
            raise ValueError("Input must be a float between 0.0 and 2.0.")

        return temperature
    except ValueError:
        print(f"Invalid float: {temperature}")
        raise

def get_seed_from_input() -> int | None:
    print("Input an integer for seed or press Enter to skip seed usage:")
    n = input("> ").strip()

    try:
        return None if n == "" else int(n)
    except ValueError:
        print(f"Invalid integer: {n}")
        raise

def get_max_tokens_from_input() -> int:
    print("Input an integer for max tokens:")
    n = input("> ").strip()

    try:
        return int(n)
    except ValueError:
        print(f"Invalid integer: {n}")
        raise


def get_penalty_from_input() -> float:
    print("Input a penalty (between -2.0 to 2.0):")
    temperature = input("> ").strip()

    try:
        temperature = round(float(temperature), 1)

        if not (-2.0 <= temperature <= 2.0):
            raise ValueError("Input must be a float between -2.0 and 2.0.")

        return temperature
    except ValueError:
        print(f"Invalid float: {temperature}")
        raise

def get_stop_from_input() -> list[str] | str:
    print("Input string or json array for stop tokens:")
    stop_str = input("> ").strip()

    if not stop_str:
        raise ValueError("Stop cannot be empty")

    try:
        stop = json.loads(stop_str)
        if not isinstance(stop, list) or len(stop) == 0 or any(not (isinstance(_, str) and  _) for _ in stop):
            raise ValueError("Stop must be an array of non-empty strings")

        return stop
    except JSONDecodeError:
        return stop_str.replace("\\n", "\n") # special case to input linebreak
    except ValueError:
        print(f"Invalid stop value: {stop_str}")
        raise