# =============================================================================
# Abundant and Deficient numbers
# =====================================================================@020143=
# 1. podnaloga
# Write a function `divisors(x)` that will return the list of all proper
# divisiors of a given number `x`. These are all divisiors that are smaller
# than `x`.
#
# Example:
#
#     divisiors(12)
#
# should return:
#
#     [1, 2, 3, 4, 6]
# =============================================================================


def divisors(x, n):
    for i in range(x+1):
        if x % n == 0:
            n += 1
            print(f"{n}")



divisors(20, 1)