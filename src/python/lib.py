"""Module that contains the implemented algorithms and utility functions."""


def dfs_naif(seq: list[str], alphabet: list[str]) -> list[list[str]]:
    """Generates all possible sequences using DFS.

    Args:
        seq: base sequence
        alphabet: the alphabet whose elements will be used to generate the
          sequences
    """
    results = []
    for item in alphabet:
        new_sequence = seq + [item]
        print("".join(new_sequence) + "\n")
        results.append(new_sequence)
        results.extend(dfs_naif(new_sequence, alphabet))
    return results


def dfs_borne(
        seq: list[str], alphabet: list[str], d_max: int, depth: int=0,
        results: list[list[str]]|None=None
    ) -> list[list[str]]:
    """Generates all possible sequences using DFS with a depth limit.

    Args:
        seq: base sequence
        alphabet: the alphabet whose elements will be used to generate the
          sequences
        d_max: maximum recursion depth
        depth: current recursion depth
        results: a list containing all the generated sequences
    """
    if results is None:
        results = []
    if depth > d_max:
        return results
    for item in alphabet:
        new_sequence = seq + [item]
        print("".join(new_sequence) + "\n")
        results.append(new_sequence)
        dfs_borne(new_sequence, alphabet, d_max, depth + 1, results)
    return results


def count_sequences(alphabet_size: int, max_depth: int) -> int:
    """Counts the number of non-empty sequences of length at most max_depth."""
    result = 0
    for value in range(1, max_depth + 1):
        result += alphabet_size**value
    return result


def compter(
        m: int,
        d: int,
        seq: list[int]|None=None,
        current_depth: int=1
    ) -> int:
    """Counts the sequences without storing them."""
    if seq is None:
        seq = []
    count = 0
    if current_depth > d:
        return 0
    for item in range(1, m + 1):
        new_sequence = seq + [item]
        count += compter(m, d, new_sequence, current_depth + 1)
        count += 1
    return count


def generer(
        m: int,
        d: int,
        seq: list[int]|None=None,
        current_depth: int=1,
        results: list[list[int]]|None=None
    ) -> list[list[int]]:
    """Generates the sequences and stores them in a list."""
    if seq is None:
        seq = []
    if results is None:
        results = []
    if current_depth > d:
        return results
    for item in range(1, m + 1):
        new_sequence = seq + [item]
        results.append(new_sequence)
        generer(m, d, new_sequence, current_depth + 1, results)
    return results
