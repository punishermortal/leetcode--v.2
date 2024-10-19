import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    # solution : 1
    # return list(players.shape)    #players.shape :- return tuple (no of rows,no of columns)

    # solution :2
    return [len(players),players.shape[1]]
    # Number of rows:-
                    # print(len(df))      # or df.shape[0]
    # Number of columns
                    #print(df.shape[1])
    