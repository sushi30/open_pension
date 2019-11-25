import os

import xlrd
import pandas as pd


def get_schemas():
    schemas = {}
    wb = xlrd.open_workbook(os.environ["SCHEMAS_FILE"])
    for sheet in wb.sheets():
        schemas[sheet.name] = pd.read_excel(wb, sheet.name)
    for key in [
        "assets",
        "origin_country",
        "rating_agency",
        "financial_institution",
        "id",
    ]:
        schemas[key] = schemas[key].set_index(schemas[key].columns[-1]).squeeze()
    return schemas


def apply_schema(schema, pos, df):
    return df[df.columns[pos]].apply(
        lambda x: null_on_error(x)(lambda: schema.loc[x])()
    )


def apply_schemas(schemas, schema_positions, df):
    df = df.copy()
    for key, pos in schema_positions.items():
        schema = schemas[key]
        df[df.columns[pos]] = apply_schema(schema, pos, df)

    return df


def null_on_error(null_value):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return null_value

        return inner

    return wrapper
