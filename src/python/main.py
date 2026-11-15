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


def run_project() -> None:
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]
    alphabet = ["a", "b", "c", "d"]
    for item in alphabet:
        print(f"{item} : ", end="")
        proj = lib.project(db, [item])
        for sequence in proj:
            print(f"({"".join(sequence)})", end=" ")
        print()


def run_project_item() -> None:
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]
    db_a = lib.project(db, ["a"])

    print(lib.project_item(db_a, "b"))
    print(lib.project_item(db_a, "c"))


def run_count_items() -> None:
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]
    db_a = lib.project(db, ["a"])
    db_ab = lib.project(db_a, ["b"])

    print(lib.count_items(db_a))
    print(lib.count_items(db_ab))


def run_prefixspan() -> None:
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]
    resultats = lib.prefixspan(db, 2)

    for pattern, support_value in sorted(resultats.items()):
        print(pattern, support_value)


def run_prefixspan_2() -> None:
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]

    for minsup in range(1, 5):
        print(f"Minsup = {minsup}:")
        resultats = lib.prefixspan(db, minsup)
        max_pattern_length = 0

        for pattern, support_value in sorted(resultats.items()):
            print(f"  - {"".join(pattern)} {support_value}")

            current_pattern_length = len(pattern)
            if current_pattern_length > max_pattern_length:
                max_pattern_length = current_pattern_length

        print()
        print(f"  * nombre de motifs : {len(resultats)}")
        print(f"  * longueur maximale d'un motif : {max_pattern_length}")
        print()


def run_prefixspan_bruteforce_validation() -> None:
    db = [list("abcac"), list("acbc"), list("babc"), list("abd"), list("cba")]
    bruteforce_depth = 5

    for minsup in range(1, 5):
        result = lib.prefixspan_bruteforce_validation(
            db, minsup, bruteforce_depth
        )
        print(f"for minsup = {minsup}: {result["equals"]}")


def run_read_spmf() -> None:
    toy_db = lib.read_spmf("data/toy.txt")

    for sequence in toy_db:
        print(sequence)


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
    # run_project_seq()
    # run_project()
    # run_project_item()
    # run_count_items()
    # run_prefixspan()
    # run_prefixspan_2()
    # run_prefixspan_bruteforce_validation()
    run_read_spmf()
