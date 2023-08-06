from functools import reduce
from pandas.core.frame import DataFrame

import pandas as pd
from typing import Union


def series_to_dataframe(
    df: Union[pd.Series, pd.DataFrame]
) -> (Union[pd.Series, pd.DataFrame], bool):
    dataf = df.copy()
    isseries = False
    if isinstance(dataf, pd.Series):
        columnname = dataf.name
        dataf = dataf.to_frame()

        try:
            dataf.columns = [columnname]
        except Exception:
            dataf.index = [columnname]
            dataf = dataf.T
        isseries = True

    return dataf, isseries


def pivot_to_list(
    df: pd.DataFrame,
    columns: Union[list, str],
    new_name_of_cols: str = "old_columns",
    stack: bool = False,
) -> pd.DataFrame:

    dfga = unmelt(df, columns=columns, explode=True)

    if not stack:
        return dfga.groupby(new_name_of_cols).agg(
            ({k: lambda x: [y for y in x] for k in dfga.columns}).copy()
        )
    else:
        return (
            dfga.groupby(new_name_of_cols)
            .agg(({k: lambda x: [y for y in x] for k in dfga.columns}).copy())
            .stack()
        )


def pivot_to_list_no_old_index_column(
    df: pd.DataFrame, columns: Union[list, str], stack: bool = False
) -> pd.DataFrame:
    dfga = unmelt(df, columns=columns, explode=False, new_name_of_cols="old_columns")
    dfga.index = dfga["old_columns"].__array__().copy()
    dfga = dfga.drop(columns=["old_columns"])
    if not stack:
        return dfga
    else:
        return dfga.stack()


def pivot_to_list_no_old_index_column_transposed(
    df: pd.DataFrame, columns: Union[list, str], stack: bool = False
) -> pd.DataFrame:
    d6 = pivot_to_list_no_old_index_column(df, columns=columns, stack=False).T
    if not stack:
        return reduce(lambda a, b: a.explode(b), d6.columns, d6,)
    else:
        return reduce(lambda a, b: a.explode(b), d6.columns, d6,).stack()


def unmelt(
    dframe: pd.DataFrame,
    columns: Union[list, str],
    explode: bool = False,
    new_name_of_cols: str = "old_columns",
) -> pd.DataFrame:
    if not isinstance(columns, list):
        columns = [columns]

    groupbycol = columns

    df, isseries = series_to_dataframe(dframe)
    groupbydf = (
        df.groupby(groupbycol)
        .agg({k: lambda x: [y for y in x] for k in df.columns})
        .copy()
    )
    groupbydf[groupbycol] = groupbydf[groupbycol].apply(lambda x: x)

    groupy = groupbydf.apply(lambda x: x.to_frame(), axis=1)

    grous = pd.concat(groupy.to_list(), axis=1).drop(index=groupbycol)

    dfga = grous.copy()
    if explode:
        dfgax4 = dfga.apply(
            lambda x: pd.Series(
                [
                    (k + max([len(y) for y in x]) * [None])[: max([len(y) for y in x])]
                    for k in x
                ]
            ),
            axis=1,
        )
    else:
        dfgax4 = dfga.copy()
    dfgax4.columns = dfga.columns
    if explode:
        dfgax4 = dfgax4.explode(dfgax4.columns.to_list())
    dfgax4[new_name_of_cols] = dfgax4.index.__array__().copy()
    dfgax4 = dfgax4.reset_index(drop=True)
    return dfgax4


def pd_add_stack_melt_tools():
    DataFrame.ds_pivot_to_list_no_old_index_column_transposed = (
        pivot_to_list_no_old_index_column_transposed
    )
    DataFrame.ds_pivot_to_list_no_old_index_column = pivot_to_list_no_old_index_column
    DataFrame.ds_pivot_to_list = pivot_to_list
    DataFrame.ds_pivot = unmelt
