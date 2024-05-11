import pandas as pd
import sys

file_imported = sys.argv[1]
df = pd.read_excel(file_imported)
# print(df.columns)
# print(df.shape[0])
# print(df.shape[1])

 # find every column datatype

structure_of_the_incoming_sheet = {
    'row_count': df.shape[0],
    'col_count': df.shape[1],
    'header_list': df.columns,
    'col_dt': {
        'col_1' :{
            'num': 20,
            'text': 10
        },
        'col_2' :{
            'num': 20,
            'text': 10
        }
    }
}
print(structure_of_the_incoming_sheet)
