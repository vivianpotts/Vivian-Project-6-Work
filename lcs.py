"""Compute the longest common subsequence of two strings."""

# Add the three algorithms that compute the longest common
# subsequence (LCS) of two strings that contain either characters or
# numbers. Make sure to add the required function signatures and
# documentation to ensure that the code is clear and understandable.
# You must add comments that explain the purpose of each of the key
# statements inside of each of the LCS algorithms.


def lcs_recursive(X, Y):
    """Recursive LCS implementation."""
    if not X or not Y:
        return 0
    elif X[-1] == Y[-1]:
        return 1 + lcs_recursive(X[:-1], Y[:-1])
    else:
        return max(lcs_recursive(X[:-1], Y), lcs_recursive(X, Y[:-1]))


def lcs_dynamic(X, Y):
    """Compute the LCS using dynamic programming."""
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_calculate(X, Y):
    """
    Space-optimized dynamic programming LCS implementation.
    This approach reduces memory usage by only storing two rows of the DP table.
    """
    m, n = len(X), len(Y)
    # Initialize two rows for the DP table
    previous = [0] * (n + 1)
    current = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])
        # Swap rows: current becomes previous for the next iteration
        previous, current = current, [0] * (n + 1)

    # The result is in the last cell of the previous row
    return previous[n]
