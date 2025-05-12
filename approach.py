"""Configuration of the benchmarking tool and its approaches."""

# All all of the enums that you need to define the configuration
# of the approach through the command-line interface of the tool.

from enum import Enum


class AlgorithmType(Enum):
    """Enum for algorithm types."""

    RECURSIVE = "recursive"
    DYNAMIC = "dynamic"
    CALCULATE = "calculate"


class DataType(Enum):
    """Enum for data types."""

    INTS = "ints"
    CHARS = "chars"


class Strategy(Enum):
    """Enum for strategies."""

    DOUBLE = "double"
    MAGNITUDE = "magnitude"
