import pandas as pd
import schema_extractors


def main():
    with pd.ExcelWriter("tmp/schemas.xlsx") as writer:  # doctest: +SKIP
        for i, extractor in enumerate(schema_extractors.extractors):
            extractor().to_excel(writer, sheet_name=extractor, index=False)


if __name__ == "__main__":
    main()
