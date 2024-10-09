import string
import time
from typing import Callable
from passwords import phred



def basic_compare(val1: str, val2: str) -> bool:
    # first check the length of the two strings
    # if they're not the same length, they can't be the same
    if len(val1) != len(val2):
        return False

    for x, y in zip(val1, val2):
        time.sleep(0.01)
        if x != y:
            return False
    time.sleep(0.01)

    return True


def guess_length(correct_password: str, comparison_fn: Callable[[str, str], bool]) -> int:
    """this function guesses the length of the password by comparing lengths"""

    number_of_attempts = 50
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
    sorted_times = sorted(list(enumerate(average_times)),key=lambda x: x[1], reverse=True)
    # print top 5 slowest lengths
    print(sorted_times[:5])
    
    # return the slowest length
    return sorted_times[0][0]




# TODO: does this timing attack work against python's built-in equality operator? Nope

def guess_password(correct_password: str, comparison_fn: Callable[[str,str],bool], length_guess:int) -> str:
    """tries to guess the password :D"""
    # set of valid characters
    letters_numbers_symbols = set(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' ')

    # make a random string of same length as guess
    guess = "a"*length_guess
    
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
            timed_guesses.append((c,av_time))
        
        sorted_times = sorted(timed_guesses,key=lambda x: x[1], reverse=True)

        # create new guess based on longest time
        guess=guess[:i] + sorted_times[0][0] + guess[i+1:]
    return guess

if __name__ == "__main__":
    password: str = phred.get_password(1)
    length_guess = guess_length(correct_password=password, comparison_fn=basic_compare)
    password = guess_password(correct_password=password,comparison_fn=basic_compare,length_guess=length_guess)
    print(f"This is the password woooo lets gooooo {password}")
