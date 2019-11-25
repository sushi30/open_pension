import logging
import os
import sys
import pandas as pd
from . import process_report
from . import constants

log = logging.getLogger(__name__)


def main(path):
    log.info("loading file")
    df = pd.read_excel(path)
    log.info("getting schema description file")
    schemas = process_report.get_schemas()
    log.info("applying schema")
    processed = process_report.apply_schemas(schemas, constants.SCHEMA_POSITIONS, df)
    file_without_extension = os.path.splitext(os.path.split(path)[-1])[0]
    if os.environ["ENV"] == "LOCAL" and not os.path.exists(os.environ["OUT_DIRECTORY"]):
        os.makedirs(os.environ["OUT_DIRECTORY"])
    out_path = os.environ["OUT_DIRECTORY"] + file_without_extension + ".csv"
    log.info(f"dumping file to {out_path}")
    processed.to_csv(out_path)
    return out_path


if __name__ == "__main__":
    main(sys.argv[0])
