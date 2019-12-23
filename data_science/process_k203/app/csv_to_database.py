import logging
import os
import sys
import pandas as pd
from sqlalchemy import create_engine

from . import process_report
from . import constants

log = logging.getLogger(__name__)


def main(in_, storage):
    engine = create_engine(storage)
    log.info("loading file")
    df = pd.read_excel(in_)
    log.info("dump to sql")
    processed = process_report.apply_schemas(schemas, constants.SCHEMA_POSITIONS, df)
    if os.environ["ENV"] == "LOCAL" and not os.path.exists(os.environ["OUT_DIRECTORY"]):
        os.makedirs(os.environ["OUT_DIRECTORY"])
    processed.to_csv(out)


if __name__ == "__main__":
    in_, out = sys.argv[1:3]
    main(in_, storage)
