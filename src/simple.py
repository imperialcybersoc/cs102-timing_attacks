import time
from passwords import fred
password = fred.get_password(0)


def basic_compare(val1, val2):
    # first check the length of the two strings
    # if they're not the same length, they can't be the same
    if len(val1) != len(val2):
        return False

    for x, y in zip(val1, val2):
        time.sleep(0.01)  # accentuate comparison delay
        if x != y:
            return False

    return True


def guess_demo():
    correct_password = password
    correct = False

    while not correct:
        durations = []

        guess = input("Enter a guess: ")

        # take an average of 10 attempts
        for i in range(10):
            tic = time.perf_counter_ns()
            correct = basic_compare(correct_password, guess)
            toc = time.perf_counter_ns()

            durations.append((tic - toc) / 1e9)

        av_time = sum(durations) / len(durations)

        print(f"Guess took {av_time:.6f}s, and was {'correct' if correct else 'incorrect'}")


def timing_attack_demo():
    correct_password = password
    attempt = ""
    correct = False
    pwd_length = 0

    # guess password length
    while not correct:
        durations = []

        attempt = "a"*pwd_length

        # take an average of 10 attempts
        for i in range(10):
            tic = time.perf_counter_ns()
            correct = basic_compare(correct_password, attempt)
            toc = time.perf_counter_ns()

            durations.append((tic - toc) / 1e9)

        av_time = sum(durations) / len(durations)

        # TODO: write this

        pwd_length += 1


    attempt = "a"*pwd_length

    _ = input("Press enter to continue")

    while not correct:
        durations = []

        # take an average of 10 attempts
        for i in range(10):
            tic = time.perf_counter_ns()
            correct = basic_compare(correct_password, attempt)
            toc = time.perf_counter_ns()

            durations.append((tic - toc) / 1e9)

        av_time = sum(durations) / len(durations)



# TODO: does this timing attack work against python's built-in equality operator?


def demo_example():
    correct_password = password
    attempt = ""

    tic = time.perf_counter_ns()
    correct = basic_compare(correct_password, attempt)
    toc = time.perf_counter_ns()

    duration = (tic - toc) / 1e9

    print(f"Guess took {duration:.6f}s, and was {"correct" if correct else "incorrect"}")



if __name__ == "__main__":
    guess_demo()