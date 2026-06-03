def get_next_state(pattern, m, state, x):
    """
    Computes the next state for the Finite Automaton.
    """
    # If the character c is same as next character in pattern,
    # then next state is simply state + 1
    if state < m and x == ord(pattern[state]):
        return state + 1

    # ns stores the result which is next state
    # ns finally contains the longest prefix which is also a suffix in pattern[0..state-1] + c
    for ns in range(state, 0, -1):
        if ord(pattern[ns-1]) == x:
            i = 0
            while i < ns - 1:
                if pattern[i] != pattern[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0

def compute_tf(pattern, m, alphabet_size=256):
    """
    This function builds the Transition Function table.
    """
    tf = [[0 for _ in range(alphabet_size)] for _ in range(m + 1)]

    for state in range(m + 1):
        for x in range(alphabet_size):
            tf[state][x] = get_next_state(pattern, m, state, x)
    return tf

def search(text, pattern):
    """
    Searches for pattern in text using Finite Automata.
    """
    m = len(pattern)
    n = len(text)
    tf = compute_tf(pattern, m)

    # Process text over FA
    state = 0
    results = []
    for i in range(n):
        state = tf[state][ord(text[i])]
        if state == m:
            results.append(i - m + 1)
    
    return results

if __name__ == "__main__":
    print("--- Finite Automata String Matching ---")
    text = input("Enter the text to search in: ")
    pattern = input("Enter the pattern to search for: ")
    
    if not pattern:
        print("Pattern cannot be empty.")
    else:
        matches = search(text, pattern)
        if matches:
            print(f"Pattern '{pattern}' found at indices: {matches}")
        else:
            print(f"Pattern '{pattern}' not found in the text.")
