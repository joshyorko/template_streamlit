import os
from io import BytesIO

from pandas import ExcelWriter, concat, read_csv, to_datetime
from streamlit import cache, write


@cache
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


def to_excel(df):
    output = BytesIO()
    writer = ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Building_Occupancy')
    workbook = writer.book
    worksheet = writer.sheets['Building_Occupancy']
    format1 = workbook.add_format({'num_format': '0.00'})
    worksheet.set_column('A:A', None, format1)
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def get_files(file):
    dfdata = []
    for uploaded_file in file:
        write("Input Filename: ", uploaded_file.name.upper())
        df = read_csv(uploaded_file)
        dfdata.append(df)
    for df in range(len(dfdata)):
        if df > 0:
            continue
    zoneIds = concat(dfdata)

    return zoneIds


def get_files2(file_path):

    xl_files = os.listdir(file_path)
    xl_files = [x for x in xl_files if x. endswith('csv')]
    dfdata = []
    for xl_file in xl_files:
        xl_path = os.path.join(file_path, xl_file)
        df = read_csv(xl_path)
        dfdata.append(df)

    df = concat(dfdata)

    return df



