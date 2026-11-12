"""Module that contains the implemented algorithms and utility functions."""
import time
from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd


PAUSE_BETWEEN_MEASUREMENTS = 5


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


def get_performance(
        m: int,
        d: int,
        type: Literal["compter", "generer"],
        repetition_count: int=3
    ) -> dict[str, int|float]:
    total_duration = 0
    result = 0

    for count in range(repetition_count):
        time.sleep(PAUSE_BETWEEN_MEASUREMENTS)

        start_time = time.perf_counter()

        if type == "compter":
            result = compter(m, d)
        else:
            result = len(generer(m, d))

        end_time = time.perf_counter()
        total_duration += end_time - start_time

    mean_duration = total_duration / repetition_count

    return {
        "m": m,
        "d": d,
        "sequence_count": result,
        "execution_time": mean_duration
    }


def performance_compter_vs_generer(
        m_d_values: dict[int, int],
        repetition_count: int=3
    ) -> list[dict[str, int|float]]:
    result = []

    for m, max_d in m_d_values.items():
        print(f"\nMesures pour m = {m}")

        for d in range(1, max_d + 1):
            print(f"  Mesures pour d = {d}/{max_d}")

            print("    Exécution de compter...")
            compter_performance = get_performance(
                m,
                d,
                "compter",
                repetition_count
            )

            print("    Exécution de generer...")
            generer_performance = get_performance(
                m,
                d,
                "generer",
                repetition_count
            )

            comparison_line = {
                "m": m,
                "d": d,
                "compter_sequence_count": compter_performance["sequence_count"],
                "compter_execution_time": compter_performance["execution_time"],
                "generer_sequence_count": generer_performance["sequence_count"],
                "generer_execution_time": generer_performance["execution_time"]
            }

            result.append(comparison_line)

            print(
                f"    Terminé : "
                f"compter = {compter_performance['execution_time']:.6f}s, "
                f"generer = {generer_performance['execution_time']:.6f}s"
            )

    print("\nToutes les mesures sont terminées.")

    return result


def show_perf_compter_vs_generer(
        parameter: Literal["sequence_count", "execution_time"],
        comparison_list: list[dict[str, int|float]]|None=None,
        comparison_csv_path: str|None=None
    ) -> None:
    if comparison_list is None and comparison_csv_path is None:
        raise ValueError(
            "At least one of the parameters 'comparison_list' and "
            "'comparison_csv_path' must be specified."
        )

    if comparison_csv_path is not None:
        comparison_df = pd.read_csv(comparison_csv_path)
    else:
        comparison_df = pd.DataFrame(comparison_list)

    plt.figure(figsize=(8, 6), dpi=300)
    plt.semilogy()

    for m in sorted(comparison_df["m"].unique()):
        m_df = comparison_df[comparison_df["m"] == m]

        xdata = m_df["d"]

        y1data = m_df[f"compter_{parameter}"]
        y2data = m_df[f"generer_{parameter}"]

        plt.plot(
            xdata,
            y1data,
            marker="o",
            label=f"Compter (m={m})"
        )

        plt.plot(
            xdata,
            y2data,
            marker="s",
            linestyle="--",
            label=f"Generer (m={m})"
        )

    xlabel = "Maximum sequence depth (d)"
    plt.xlabel(xlabel)

    ylabel = ("Number of sequences"
              if parameter == "sequence_count"
              else "Execution time")
    plt.ylabel(ylabel)

    plt.title(f"Compter vs Generer - {ylabel}")
    plt.legend()
    plt.grid()

    plt.savefig(f"outputs/compter_vs_generer_{parameter}.png")
    plt.show()


def find_embedding(t: list[str], s: list[str]) -> list[int]|None:
    """Returns the leftmost occurrence (list of indices) of t in s, or None."""
    embedding = []
    start_index = 0

    for item in t:
        found = False
        for index in range(start_index, len(s)):
            if s[index] == item:
                embedding.append(index)
                start_index = index + 1
                found = True
                break

        if not found:
            return None

    return embedding


def support(t: list[str], db: list[list[str]]) -> int:
    """Calculates the support of t in db."""
    count = 0
    for sequence in db:
        if find_embedding(t, sequence) is not None:
            count += 1
    return count


def prefixes(s: list[str]) -> list[list[str]]:
    """Generates all possible prefixes of a sequence."""
    return [s[:ind] for ind in range(len(s) + 1)]


def suffixes(s: list[str]) -> list[list[str]]:
    """Generates all possible suffixes of a sequence."""
    return [s[ind:] for ind in range(len(s) + 1)]


def project_seq(s: list[str], alpha: list[str]) -> list[str]|None:
    """Determines the projection of s relative to alpha."""
    embedding = find_embedding(alpha, s)
    if embedding is None:
        return None
    last_index = embedding[-1]
    return s[last_index + 1:]


def project(db: list[list[str]], alpha: list[str]) -> list[list[str]]:
    """Returns the projected base DB|alpha."""
    result = []
    for sequence in db:
        suffix = project_seq(sequence, alpha)
        if suffix is not None:
            result.append(suffix)
    return result
