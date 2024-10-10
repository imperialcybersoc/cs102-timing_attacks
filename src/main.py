import string
import time
from typing import Callable
from passwords import phred
from hashlib import sha256
import sys
from random import choice as randchoice



def basic_compare(val1: str, val2: str) -> bool:
    # first check the length of the two strings
    # if they're not the same length, they can't be the same
    if len(val1) != len(val2):
        return False

    compare_time = 0.02

    for x, y in zip(val1, val2):
        time.sleep(compare_time)
        if x != y:
            return False

    time.sleep(compare_time*2)

    return True


def secure_compare(val1: str, val2: str) -> bool:
    #return hmac.compare_digest(val1, val2)
    hash1 = sha256(val1.encode()).hexdigest()
    hash2 = sha256(val2.encode()).hexdigest()
    return hash1 == hash2



def guess_length(correct_password: str, comparison_fn: Callable[[str, str], bool]) -> int:
    """this function guesses the length of the password by comparing lengths"""

    number_of_attempts = 600
    average_times = []

    for length in range(number_of_attempts):
        attempt = "a"*length
        durations=[]

        # compare strings 10 times and average it
        for _ in range(10):

            tic = time.perf_counter_ns()
            comparison_fn(correct_password, attempt)
            toc = time.perf_counter_ns()

            durations.append((toc - tic) / 1e9)

        av_time = sum(durations) / len(durations)
        average_times.append(av_time)

    # sort the times
    sorted_times = sorted(
        list(enumerate(average_times)),
        key=lambda x: x[1],
        reverse=True
    )

    # print top 5 slowest lengths
    print(sorted_times[:5])

    # return the slowest length
    return sorted_times[0][0]


def guess_password(correct_password: str, comparison_fn: Callable[[str,str],bool], length_guess:int) -> str:
    """tries to guess the password :D"""
    # set of valid characters
    letters_numbers_symbols = set(
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
        + ' '
    )

    lns_ls = list(letters_numbers_symbols)

    # make a random string of same length as guess
    guess = "".join([randchoice(lns_ls) for _ in range(length_guess)])

    # iterate through every character in guess
    for i in range(length_guess):
        timed_guesses: list[tuple[str,float]] = []
        # iterate through all possible characters
        for c in letters_numbers_symbols:
            new_guess = guess[:i] + c + guess[i+1:]
            print(new_guess)

            # compare strings 10 times and average it
            durations = []
            for _ in range(10):

                tic = time.perf_counter_ns()
                comparison_fn(correct_password, new_guess)
                toc = time.perf_counter_ns()

                durations.append((toc - tic) / 1e9)

            av_time = sum(durations) / len(durations)
            timed_guesses.append((c, av_time))

        sorted_times = sorted(timed_guesses, key=lambda x: x[1], reverse=True)

        # create new guess based on longest time
        guess = guess[:i] + sorted_times[0][0] + guess[i+1:]

    return guess


def guess_demo():
    pwd_idx: int = int(sys.argv[1])
    password: str = phred.get_password(pwd_idx)

    print(f"The target password is {password}\n{'-'*30}")
    time.sleep(1)

    length_guess = guess_length(
        correct_password=password,
        comparison_fn=basic_compare
    )

    if length_guess == len(password):
        print(f"The length of the password is {length_guess}\n")
        time.sleep(1)
    else:
        print(f"Failed to guess the length of the password, the length was {len(password)} but we guessed {length_guess} D:")
        return

    password_guess = guess_password(
        correct_password=password,
        comparison_fn=basic_compare,
        length_guess=length_guess
    )


    if password_guess == password:
        print(f"The password is \"{password_guess}\", woooo lets gooooo")
    else:
        print(f"Failed to guess the password, the password was {password} but we guessed {password_guess} :(")


if __name__ == "__main__":
    guess_demo()
    #secure_compare("hello", "hello")
