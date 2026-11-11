"""Main module that executes the implemented functions."""
import lib
import pandas as pd


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


def run_compter() -> None:
    m = 4
    d = 8
    n_m_d = lib.compter(m, d)
    print(f"N({m}, {d}) = {n_m_d}")


def run_generer() -> None:
    m = 3
    d = 11
    results_m_d = lib.generer(m, d)
    # print(results_m_d)
    # for item in results_m_d:
    #     print(item)
    n_m_d = len(results_m_d)
    print(f"N({m}, {d}) = {n_m_d}")


def run_comparison_compter_vs_generer() -> None:
    m_d_values = {
        2: 20,
        3: 14,
        4: 11
    }
    comparison_list = lib.performance_compter_vs_generer(
        m_d_values,
        repetition_count=3
    )
    comparison_df = pd.DataFrame(comparison_list)
    comparison_df.to_csv(
        "outputs/compter_vs_generer.csv",
        index=False
    )
    lib.show_perf_compter_vs_generer(
        "execution_time",
        comparison_list=comparison_list
    )
    lib.show_perf_compter_vs_generer(
        "sequence_count",
        comparison_list=comparison_list
    )


def run_find_embedding() -> None:
    s = ["a", "b", "c", "a", "c"]

    print(lib.find_embedding(["a", "c"], s))
    print(lib.find_embedding(["a", "b", "c"], s))
    print(lib.find_embedding(["c", "b"], s))


def run_support() -> None:
    patterns = [
        ["a"],
        ["b"],
        ["d"],
        ["a", "b"],
        ["b", "a"],
        ["c", "a"],
        ["a", "b", "c"],
        ["a", "a"]
    ]
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]

    for pattern in patterns:
        print(f"support( {pattern} ) = {lib.support(pattern, db)}")


def run_prefixes() -> None:
    s = ["a", "b", "c", "a", "c"]

    prefixes = lib.prefixes(s)
    for prefixe in prefixes:
        print(prefixe)


def run_suffixes() -> None:
    s = ["a", "b", "c", "a", "c"]

    suffixes = lib.suffixes(s)
    for suffixe in suffixes:
        print(suffixe)


def run_project_seq() -> None:
    s = ["a", "b", "c", "a", "c"]

    print(lib.project_seq(s, ["a"]))
    print(lib.project_seq(s, ["a", "b"]))
    print(lib.project_seq(s, ["a", "c"]))
    print(lib.project_seq(s, ["c", "a"]))


if __name__ == "__main__":
    # run_dfs_naif()
    # print_longest_sequence_with_dfs_naif()
    # run_dfs_borne()
    # run_count_sequences()
    # run_compter()
    # run_generer()
    # run_comparison_compter_vs_generer()
    # run_find_embedding()
    # run_support()
    # run_prefixes()
    # run_suffixes()
    run_project_seq()
