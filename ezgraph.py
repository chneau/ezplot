#!/usr/bin/env python


import click
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


@click.command()
@click.argument(
    "files", nargs=-1, required=True,
)
def main(files):
    """Process all FILES."""
    df = None
    for file in files:
        result = pd.read_csv(file, header=None)
        if df is None:  # init df
            df = result
            continue
        df = pd.concat([df, result], axis=1)  # add on the right
    df.columns = range(df.shape[1])
    binsize = 1
    if df.shape[0] > 100:
        binsize = int(df.shape[0] / 100)
    min_mean_max(df=df, binsize=binsize)


def min_mean_max(df, binsize):
    mmm = pd.DataFrame(
        {"min": df.min(axis=1), "mean": df.mean(axis=1), "max": df.max(axis=1)}
    )
    p = sns.lineplot(data=mmm.groupby(mmm.index // binsize).mean())
    p.get_figure().savefig("min_mean_max.png")


if __name__ == "__main__":
    main()
