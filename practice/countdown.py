def countdown(n):

    if n <= 0:
        done = print("Done!")
        return done

    print(f"This is number: {n}")
    return countdown(n - 1)

countdown(10)