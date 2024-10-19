import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    filtered_df = animals[animals['weight'] > 100]
    sorted_df = filtered_df.sort_values(by='weight', ascending=False)
    result = sorted_df[['name']]
    return result