import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset='email', keep='first')
    return customers

# this will keep the last occurrence and remove left duplicates
            # customers = customers.drop_duplicates(subset='email', keep='last')

# for removing all duplicates rows
            # customers = customers[~customers['email'].duplicated(keep=False)]