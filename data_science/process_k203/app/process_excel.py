import os
import sys
import pandas as pd
from . import process_report
from . import constants


def main(path):
    df = pd.read_excel(path)
    schemas = process_report.get_schemas()
    processed = process_report.apply_schemas(schemas, constants.SCHEMA_POSITIONS, df)
    processed.DateCode = pd.to_datetime(processed.DateCode, format="%d%m%Y")
    file_without_extension = os.path.splitext(os.path.split(path)[-1])[0]
    if os.environ["ENV"] == "LOCAL" and not os.path.exists(os.environ["OUT_DIRECTORY"]):
        os.makedirs(os.environ["OUT_DIRECTORY"])
    processed.to_csv("" + file_without_extension + ".csv")


if __name__ == "__main__":
    main(sys.argv[0])
