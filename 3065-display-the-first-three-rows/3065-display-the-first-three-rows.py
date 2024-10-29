import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # return employees.head(3)
    # return employees[:3]
    return employees.iloc[:3]