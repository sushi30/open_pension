import logging
import os
import sys
import pandas as pd
from . import process_report
from . import constants

log = logging.getLogger(__name__)


def main(in_, out):
    log.info("loading file")
    df = pd.read_excel(in_)
    log.info("getting schema description file")
    schemas = process_report.get_schemas()
    log.info("applying schema")
    processed = process_report.apply_schemas(schemas, constants.SCHEMA_POSITIONS, df)
    if os.environ["ENV"] == "LOCAL" and not os.path.exists(os.environ["OUT_DIRECTORY"]):
        os.makedirs(os.environ["OUT_DIRECTORY"])
    processed.to_csv(out)


if __name__ == "__main__":
    in_, out = sys.argv[1:3]
    main(in_, out)
