"""Run a benchmark on a function that can automatically find the LCS."""

# implement all of the functions needed to conduct a benchmark that runs a
# doubling experiment to evaluate the performance of the LCS algorithms

import time

from .generate import generate_data


def run_benchmark(algorithm, data_type, start_size, runs, strategy):
    """Run a benchmark for the given LCS algorithm."""
    print("Benchmarking Tool for Finding the LCS\n")
    print(f"Type of list: {algorithm.__name__}")
    print(f"Data stored in list: {data_type.value}")
    print(f"Benchmarking strategy: {strategy.name.lower()}")
    print(f"Number of runs: {runs}\n")

    times = []
    size = start_size

    for run in range(1, runs + 1):
        # Generate data
        X, Y = generate_data(size, data_type)

        # Measure execution time
        start_time = time.perf_counter()
        algorithm(X, Y)
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        print(
            f"Run {run} of {runs} for {algorithm.__name__} algorithm using size {size:2} took {elapsed_time:.10f} seconds"
        )

        # Adjust size for the next run
        if strategy.name.lower() == "double":
            size *= 2
        elif strategy.name.lower() == "magnitude":
            size += 10

    # Calculate statistics
    min_time = min(times)
    max_time = max(times)
    avg_time = sum(times) / len(times)

    print(
        "\nMinimum execution time: ",
        f"{min_time:.10f} seconds for run {times.index(min_time) + 1} with size {start_size}",
    )
    print(
        "Maximum execution time: ",
        f"{max_time:.10f} seconds for run {times.index(max_time) + 1} with size {start_size * (2 ** (times.index(max_time)))}",
    )
    print(
        "\nAverage execution time: ",
        f"{avg_time:.10f} seconds across runs 1 through {runs}",
    )
