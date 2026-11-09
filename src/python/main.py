"""Main module that executes the implemented functions."""
import lib


def run_dfs_naif() -> None:
    alphabet = ["a", "b", "c"]
    initial_sequence = []
    sequences = lib.dfs_naif(initial_sequence, alphabet)
    print(sequences)


def print_longest_sequence_with_dfs_naif() -> None:
    sequence = ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                "aaaaaaaaaaaaaaaaaaaaaa")
    print(len(sequence))


def run_dfs_borne() -> None:
    alphabet = ["a", "b", "c"]
    initial_sequence = []
    sequences = lib.dfs_borne(initial_sequence, alphabet, 2)
    print(sequences)
    print(len(sequences))


def run_count_sequences() -> None:
    m = 3
    d = 10
    n_m_d = lib.count_sequences(m, d)
    n_m_d_1 = lib.count_sequences(m, d + 1)
    print(f"N({m}, {d}) = {n_m_d}")
    print(f"N({m}, {d + 1}) = {n_m_d_1}")
    print(f"{n_m_d_1} / {n_m_d} = {n_m_d_1 / n_m_d}")


if __name__ == "__main__":
    # run_dfs_naif()
    # print_longest_sequence_with_dfs_naif()
    # run_dfs_borne()
    run_count_sequences()
