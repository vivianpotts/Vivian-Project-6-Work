"""Automatically generate data used for benchmarking."""

# implement all of the generation functions so that your program can
# generate data according to the requirements in the README.md file. Please
# note that you should be able to generate:
# - strings that contain characters
# - strings that contain numbers
# The strings must always be of the same size. The size of the strings must
# follow the rules associated with running a doubling experiment. You should
# generate the strings and then confirm that it works through test cases.

import random
import string

from .approach import DataType


def generate_data(size, data_type):
    """Generate input data of the specified size and type (int or char)."""
    print(
        f"Generating data with size={size}, data_type={data_type}"
    )  # Debugging log

    # Ensure data_type is handled as an enum or string
    if isinstance(data_type, DataType):
        data_type = data_type.value  # Convert enum to its string value
    elif isinstance(data_type, str):
        data_type = data_type.lower()  # Normalize string input to lowercase

    print(
        f"Processed data_type: {data_type}"
    )  # Debugging log after conversion

    # Generate data based on the type
    if data_type == "ints":
        return [random.randint(0, 9) for _ in range(size)], [
            random.randint(0, 9) for _ in range(size)
        ]
    elif data_type == "chars":
        return "".join(random.choices(string.ascii_letters, k=size)), "".join(
            random.choices(string.ascii_letters, k=size)
        )
