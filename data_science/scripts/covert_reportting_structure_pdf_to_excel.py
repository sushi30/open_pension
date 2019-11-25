import pandas as pd
import schema_extractors


def main():
    schemas = {
        name: extractor()
        for name, extractor in schema_extractors.cached_extractors.items()
    }
    with pd.ExcelWriter("tmp/schemas.xlsx") as writer:  # doctest: +SKIP
        for name, df in schemas.items():
            df = df.rename(columns=lambda x: x.replace("\r", " ").strip())
            df.to_excel(writer, sheet_name=name, index=False)


if __name__ == "__main__":
    main()
