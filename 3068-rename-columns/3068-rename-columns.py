import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # it will create a new dataframe 
    # students = students.rename(columns = {"id":"student_id","first":"first_name","last":"last_name","age":"age_in_years"})

    # rename without creating new df

    students.rename(columns = {"id":"student_id","first":"first_name","last":"last_name","age":"age_in_years"},inplace = True)
    return students