"""Conduct experiments to evaluate performance of LCS computation."""

# Add all of the required source code to implement a benchmark
# that runs a doubling experiment to evaluate the performance of the
# three algorithms that compute the longest common subsequence (LCS)
# of two strings that contain either characters or numbers.

# Please refer to the README.md file for more details about the
# requirements that this program must fulfill. If you have questions about
# how to implement the functions in this file or in any other files, then
# please schedule a meeting with the course instructor well in advance
# of the deadline for this algorithm engineering project.

import argparse

from .approach import DataType, Strategy
from .benchmark import run_benchmark
from .lcs import lcs_calculate, lcs_dynamic, lcs_recursive


def cli():
    """Command-line interface entry point."""
    main()


def parse_arguments():
    """Parse command-line arguments for the LCS benchmark."""
    parser = argparse.ArgumentParser(
        description="Benchmarking Tool for Finding the LCS"
    )
    parser.add_argument(
        "--algorithmtype",
        choices=["recursive", "dynamic", "calculate"],
        required=True,
        help="Type of LCS algorithm to use",
    )
    parser.add_argument(
        "--datatype",
        choices=["ints", "chars"],
        required=True,
        help="Type of data to use (ints or chars)",
    )
    parser.add_argument(
        "--startsize",
        type=int,
        required=True,
        help="Starting size of the input data",
    )
    parser.add_argument(
        "--runs",
        type=int,
        required=True,
        help="Number of runs for the benchmark",
    )
    parser.add_argument(
        "--strategy",
        choices=["double", "magnitude"],
        default="double",
        help="Strategy for increasing input size",
    )
    return parser.parse_args()


def main():
    """Main function to run the LCS benchmark."""
    args = parse_arguments()

    # Map algorithm type to function
    algorithm_map = {
        "recursive": lcs_recursive,
        "dynamic": lcs_dynamic,
        "calculate": lcs_calculate,
    }

    # Run the benchmark
    run_benchmark(
        algorithm_map[args.algorithmtype],
        DataType[args.datatype.upper()],
        args.startsize,
        args.runs,
        Strategy[args.strategy.upper()],
    )


if __name__ == "__main__":
    main()
