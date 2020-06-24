#!/usr/bin/env python


import os

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
    csvs = []
    for file in files:
        result = pd.read_csv(file, header=None)
        csvs += [{"name": os.path.basename(file), "df": result}]
        if df is None:  # init df
            df = result
            continue
        df = pd.concat([df, result], axis=1)  # add on the right
    df.columns = range(df.shape[1])

    binsize = 1
    if df.shape[0] > 100:
        binsize = int(df.shape[0] / 100)

    min_mean_max(df=df, binsize=binsize, title="all")
    for csv in csvs:
        min_mean_max(df=csv["df"], binsize=binsize, title=csv["name"])
    all(csvs=csvs, binsize=binsize, title="min", fn=lambda x: x.min(axis=1))
    all(csvs=csvs, binsize=binsize, title="mean", fn=lambda x: x.mean(axis=1))
    all(csvs=csvs, binsize=binsize, title="max", fn=lambda x: x.max(axis=1))


def all(csvs, binsize, title, fn):
    data = {}
    for csv in csvs:
        data[csv["name"]] = fn(csv["df"])
    m = pd.DataFrame(data)
    plt.figure()
    p = sns.lineplot(data=m.groupby(m.index // binsize).mean())
    p.set_title(f"{title}").get_figure().savefig(f"all_{title}.png")


def min_mean_max(df, binsize, title):
    mmm = pd.DataFrame(
        {"min": df.min(axis=1), "mean": df.mean(axis=1), "max": df.max(axis=1)}
    )
    plt.figure()
    p = sns.lineplot(data=mmm.groupby(mmm.index // binsize).mean())
    p.set_title(f"{title}").get_figure().savefig(f"{title}_min_mean_max.png")


if __name__ == "__main__":
    main()
