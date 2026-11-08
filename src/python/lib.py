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
