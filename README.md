# SPM Tutorials

This repository contains the work I completed for the Data Mining (M2) course’s [tutorials on Sequential Pattern Mining](https://johnaoga.github.io/gl-dm/part4/td_prefixspan.html).


## Usage

#### Install the dependencies

Make sure Python 3.14+ is installed on your computer, then install the dependencies with this command:

```
pip install -r requirements.txt
```

#### Run most of the implemented functions

To answer the questions in the tutorial, I implemented several functions that I then ran (with test data) from the `main.py` file. In this file, you can uncomment or comment out the functions you want to test or skip. Then run the file with this command:

```
python src/python/main.py
```

#### Compare the performance of my PrefixSpan implementation with that of SPMF

The `perf_comparison.py` file is the script used to compare the performance of the PrefixSpan implementations. To run it, enter the following command:

```
python src/python/perf_comparison.py
```


## References

- The `SIGN` and `LEVIATHAN` datasets were downloaded from the SPMF website [here](https://www.philippe-fournier-viger.com/spmf/datasets.php).
- The `spmf.jar` file was downloaded from the SPMF website [here](https://www.philippe-fournier-viger.com/spmf/index.php?link=download.php).
