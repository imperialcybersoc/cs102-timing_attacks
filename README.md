# cs102-timing_attacks
The slides, schedule, and example code for the Timing Attack workshop.

## Planning Progress
So far the workshop has been planned, just some Copilot-generated code in `main.py`, and the slides are a WIP

## Plan

- Intro, what is time? why is it a target? (5 min: 5)
  - example of friend "lemme get my keys", time how long they take to get back, where were the keys
  - little nudge towards Spectre and Meltdown in the PPT
- Introduce the basic password-checker (10 min : 15)
  - interactive: ask them to design fastest string comparison (8 min)
    - first check length
    - check character by character
    - maximises early exits
  - me: show the one that we'll be using (2 min) (simple and possibly the same implementation as built-in?)
- Interactive: get them to try and come up with a design for a password cracker targeting these (24 min: 39-40)
  - at regular intervals (8 min), present hint 1 and then 2 (8 min * 3)
  1. how would you make use of the length checker (can show code)
  2. what information can you get from how long the char-by-char checker takes?
- Have them present their solutions, 2-3 groups (10 min), then present mine (5 min: 55)
  - non-technical submissions can be presented, I'll just be doing common sense checks, I think
- Break (5 min: 60)
- Red vs Blue, iteration:
  - interactive: let them run free and see what they can come up with (25 min: 85)
  - let then let them present some of their solutions, idk how long this will take, maybe let ppl leave at this point? (15min: 100)
- Then can wrap up and see if anyone has any questions


> TODO: Design the running of the workshop itself
> TODO: Write the slides that you'll be using
> TODO: Then write the code that you'll need

