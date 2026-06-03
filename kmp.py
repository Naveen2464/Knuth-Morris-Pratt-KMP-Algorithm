def compute_lps(pattern):
    """
    Computes the Longest Proper Prefix which is also a Suffix (LPS) array.
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # length of the previous longest proper prefix suffix
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def search(text, pattern):
    """
    Searches for pattern in text using Knuth-Morris-Pratt algorithm.
    """
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    
    results = []
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            results.append(i - j)
            j = lps[j - 1]
        
        elif i < n and pattern[j] != text[i]:
            if j != 0:  # mismatch after j matches
                j = lps[j - 1] #Uses LPS to avoid rechecking.
            else:
                i += 1
    return results

if __name__ == "__main__":
    print("--- KMP String Matching ---")
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
