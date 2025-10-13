def my_steps(steps):
    if not 1 <= steps <= 25:
        raise ValueError("Number of steps must be between 1 and 25, try again.")
    # if number steps = 1, return 1
    if steps == 1:
        return 1
    # fibonacci like sequence, where ways(n) = ways(n-1) + ways(n-2)
    prev = 1 # 1 step
    current = 2 # 2 steps, _ is a throaway variable. We return b if we only get 2 as input
    # loop to implement sequence
    for _ in range(3, steps+1):
        temp = prev
        prev = current
        current = temp+ current
    return current


    