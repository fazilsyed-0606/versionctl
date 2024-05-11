import pandas as pd
import sys

file_path = sys.argv[0]

# if len(sys.argv) <= 2:



#  read source file data to source_df dataframe


# read destination file data to dest_df dataframe or if no file given

# you can create a dataframe with defined column headers.
# print(source_df)
# create a dataframe with above headers
dest_df = pd.DataFrame(columns = sys.argv[1])

header_sequence = dest_df.columns.tolist()
print("Header sequence:", header_sequence)
for column_name in header_sequence:
    print(column_name)


column_data_types = dest_df.dtypes
print(column_data_types)

for column_name, data_type in column_data_types.items():
    print(f"{column_name}: {data_type}")

headers = dest_df.columns.tolist()
print("Headers:", headers)

print("Headers:")
for header in headers:
    print(header)

# # Define actions list
# cmd_actions = [
#     'add',
#     'sub',
#     'mul'
# ]

# Define command dictionary
cmd_dict = [
    {
        'action': "add",
        'source_col_1': 'Distributor Price',
        'source_col_2': 'Vet Price',
        'dest_col': 'Addition'  # if the column in destination not exits then create one
    },
    {
        'action': "sub",
        'source_col_1': 'SRP',
        'source_col_2': 'Vet Price',
        'dest_col': 'Subtraction'
    },
    {
        'action': "mul",
        'source_col_1': 'Distributor Price',
        'source_col_2': 'Vet Price',
        'dest_col': 'Multiplication'
    },
    {
        'action': "div",
        'source_col_1': 'Distributor Price',
        'source_col_2': 'SRP',
        'dest_col': 'Division'
    },
    {
        'action': "mod",
        'source_col_1': 'MAP',
        'source_col_2': 'SRP',
        'dest_col': 'Modulus'
    },
    {
        'action': "Change data type",
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': "Replace",
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': "Duplicate column",
        'source_col_1': 'Fund',
        'dest_col': 'Duplicate_column'
    },
    {
        'action': 'Filter',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Split',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Merge',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Trim spaces',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Truncate',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Add prefix or suffix',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Extract',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Fill empty cells',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Count',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Select columns',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Add formula',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Window functions',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Cluster and Merge',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Change case',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Create buckets',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Language detection',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Keyword extraction',
        'source_col_1': '1',
        'dest_col': 1
    },
    {
        'action': 'Sentiment analysis',
        'source_col_1': '1',
        'dest_col': 1
    }
]
# parse command dict
cmd_actions = {
    'add': 'add',
    'sub': 'sub',
    'mul': 'mul',
    'div': 'div',
    'mod': 'mod',
    'Change_data_type': 'Change data type',
    # 'Replace': 'Replace',
    'Duplicate_column': 'Duplicate column',
    'Filter': 'Filter',
    'Split': 'Split',
    'Merge': 'Merge',
    'Trim_spaces': 'Trim spaces',
    'Truncate': 'Truncate',
    'Add_prefix_or_suffix': 'Add prefix or suffix',
    'Extract': 'Extract',
    'Fill empty cells': 'Fill empty cells',
    'Count': 'Count',
    'Select_columns': 'Select columns',
    'Add_formula': 'Add formula',
    'Window_functions': 'Window functions',
    'Cluster_and_merge': 'Cluster_and_merge',
    'Create_buckets': 'Create buckets',
    'Language_detection': 'Language detection',
    'Keyword_extraction': 'Keyword extraction',
    'Sentiment_analysis': 'Sentiment analysis'
}


# # Convert cmd_dict to JSON string
# cmd_dic_json = json.dumps(cmd_dict)
# print(cmd_dic_json)
#
# cmd_dict_list = json.loads(cmd_dic_json)
# print(cmd_dict_list)
# exit(0)
# check if command exists in the action list
def add(cmd, dest_df, source_df):
    destcolumn = cmd['dest_col']
    sourceCol1 = cmd['source_col_1']
    sourceCol2 = cmd['source_col_2']

    # prepare the pandas instruction for the particular command and execute
    dest_df[destcolumn] = source_df[sourceCol1] + source_df[sourceCol2]

    return dest_df


def sub(cmd, dest_df, source_df):
    destcolumn = cmd['dest_col']
    sourceCol1 = cmd['source_col_1']
    sourceCol2 = cmd['source_col_2']

    # prepare the pandas instruction for the particular command and execute
    try:
        dest_df[destcolumn] = source_df[sourceCol1] - source_df[sourceCol2]
    except TypeError:
        print("Error: cannot subtract a string from string")


def mul(cmd, dest_df, source_df):
    destcolumn = cmd['dest_col']
    sourceCol1 = cmd['source_col_1']
    sourceCol2 = cmd['source_col_2']

    # prepare the pandas instruction for the particular command and execute
    try:
        dest_df[destcolumn] = source_df[sourceCol1] * source_df[sourceCol2]
    except TypeError:
        print("Error: cannot multiply a string into string")


def div(cmd, dest_df, source_df):
    destcolumn = cmd['dest_col']
    sourceCol1 = cmd['source_col_1']
    sourceCol2 = cmd['source_col_2']

    # prepare the pandas instruction for the particular command and execute
    try:
        dest_df[destcolumn] = source_df[sourceCol1] / source_df[sourceCol2]
    except TypeError:
        print("Error: cannot  divide a string by stirng")


def mod(cmd, dest_df, source_df):
    destcolumn = cmd['dest_col']
    sourceCol1 = cmd['source_col_1']
    sourceCol2 = cmd['source_col_2']

    # prepare the pandas instruction for the particular command and execute
    try:
        dest_df[destcolumn] = source_df[sourceCol1] % source_df[sourceCol2]
    except TypeError:
        print("Error: cannot mod a string by string")


def Duplicate_column(cmd, dest_df, source_df):
    destcolumn = cmd['dest_col']
    sourceCol1 = cmd['source_col_1']

    dest_df[destcolumn] = source_df['source_col_1']
    return destcolumn


for cmd in cmd_dict:
    a = (cmd['action'])
    if a in cmd_actions:
        print(a)
        action_method_to_call = globals()[a]
        result = action_method_to_call(cmd, dest_df, source_df)
        print(result)
    else:
        print("a : not in command list")


