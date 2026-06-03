# String Matching using Finite Automata

## Overview
This algorithm treats pattern matching as a state machine. The machine transitions between states (0 to $m$, where $m$ is pattern length) based on the input character from the text.

## How it Works
1.  **Preprocessing:** Build a Transition Function (TF) table.
    *   Rows represent states (0 to $m$).
    *   Columns represent possible characters (alphabet).
    *   `TF[state][char]` tells the machine which state to move to next.
2.  **Searching:** 
    *   Start at `state 0`.
    *   For each character in the text, look up the next state in the TF table.
    *   If the state reaches $m$, a match is found.

## Complexity
*   **Preprocessing:** $O(m^3 \cdot |\Sigma|)$ for the naive approach, where $m$ is pattern length and $|\Sigma|$ is alphabet size.
*   **Matching:** $O(n)$, where $n$ is text length.

## Key Logic
The core challenge is finding the longest prefix of the pattern that is also a suffix of `pattern[0...state-1] + char`. This ensures that even if we fail to match the full pattern, we "save" as much of the partial match as possible.
