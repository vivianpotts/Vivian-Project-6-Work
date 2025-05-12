"""Define constants with dataclasses."""

# define any numerical constants used in the listmutator module
# make sure that you use the dataclass decorator to create the constants;
# you can refer to your prior algorithm engineering projects for more details

from dataclasses import dataclass


@dataclass(frozen=True)
class Constants:
    """Constants for the LCS benchmark tool."""

    DEFAULT_START_SIZE: int = 1
    DEFAULT_RUNS: int = 5
    DEFAULT_STRATEGY: str = "double"
