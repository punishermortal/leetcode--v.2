import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df_melted = pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')
    return df_melted