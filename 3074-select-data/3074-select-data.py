import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    # return students.loc[students["student_id"]== 101 ,["name","age"]]
    return students.query("student_id == 101")[["name", "age"]]
    