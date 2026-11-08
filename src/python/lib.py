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
