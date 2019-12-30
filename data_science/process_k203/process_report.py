import xlrd
import pandas as pd
import dask.dataframe as dd


def get_schemas(path):
    schemas = {}
    wb = xlrd.open_workbook(path)
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
    df.DateCode = dd.to_datetime(df.DateCode, format="%d%m%Y")
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
