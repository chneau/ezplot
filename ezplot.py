#!/usr/bin/env python


import os
import time
from functools import partial

import click
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

click.option = partial(click.option, show_default=True)

# TODO
# - Add argument for output directory

output_format = None
binsize = None


@click.command()
@click.argument(
    "files", nargs=-1, required=True,
)
@click.option(
    "--format",
    "-f",
    default="png",
    help="The output plots format ('png', 'pdf', 'svg', ...)",
)
@click.option("--size", "-s", default=(6.4, 4.8), help="The output plots size")
@click.option(
    "--context",
    "-c",
    default="talk",
    help="The output plot context (paper, notebook, talk, poster)",
)
def main(files, format, size, context):
    """Process all FILES."""
    start = time.process_time()
    sns.set_style(
        "darkgrid",
        {"axes.edgecolor": "black", "xtick.bottom": True, "ytick.left": True,},
    )
    sns.set_context(context)
    global output_format
    global binsize
    output_format = format
    plt.rcParams["figure.figsize"] = size
    print(f"Plot size: {size}, format: {format}, context: {context}",)
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

    min_mean_max(df=df, title="all")
    if len(csvs) == 1:
        print(f"1 plot generated in {time.process_time() - start}s.")
        return
    for csv in csvs:
        min_mean_max(df=csv["df"], title=csv["name"])
    all(csvs=csvs, title="min", fn=lambda x: x.min(axis=1))
    all(csvs=csvs, title="mean", fn=lambda x: x.mean(axis=1))
    all(csvs=csvs, title="max", fn=lambda x: x.max(axis=1))
    print(f"{1+3+len(csvs)} plots generated in {time.process_time() - start}s.")


def all(csvs, title, fn):
    data = {}
    for csv in csvs:
        data[csv["name"]] = fn(csv["df"])
    m = pd.DataFrame(data)
    plt.figure()
    p = sns.lineplot(data=m.groupby(m.index // binsize).mean())
    p.set_title(f"{title}").get_figure().savefig(f"all_{title}.{output_format}")


def min_mean_max(df, title):
    mmm = pd.DataFrame(
        {"min": df.min(axis=1), "mean": df.mean(axis=1), "max": df.max(axis=1)}
    )
    plt.figure()
    p = sns.lineplot(data=mmm.groupby(mmm.index // binsize).mean())
    p.set_title(f"{title}").get_figure().savefig(
        f"{title}_min_mean_max.{output_format}"
    )


if __name__ == "__main__":
    main()
