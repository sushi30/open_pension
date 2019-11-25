import joblib
import pandas as pd
import tabula


def get_schema_description():
    p678 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[6, 7, 8],
        relative_area=True,
        area=[0, 50, 100, 100],
    )
    p9 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[9],
        relative_area=True,
        area=[11, 50, 30, 100],
    )
    p9.columns = p678.columns
    p9 = p9.dropna()
    p678 = p678[p678["מיקום"].str.isnumeric()]
    return pd.concat([p678, p9])


def get_asset_type_schema():
    df = pd.concat(
        [
            tabula.read_pdf(
                "docs/Monthly_reporting_structure.pdf",
                pages=[9],
                relative_area=True,
                area=[30, 0, 100, 100],
            ),
            tabula.read_pdf(
                "docs/Monthly_reporting_structure.pdf",
                pages=[10, 11],
                relative_area=True,
                area=[0, 0, 100, 100],
            ),
        ]
    )
    return df[df[df.columns[-1]].astype(str).str.isnumeric()]


def get_other_info_schema():
    return tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[12],
        relative_area=True,
        area=[0, 0, 80, 100],
    )


def get_price_schema():
    return tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[13],
        relative_area=True,
        area=[25, 0, 50, 100],
    )


def get_id_no_schema():
    page12 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[12],
        relative_area=True,
        area=[80, 0, 100, 100],
    )
    page13 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[13],
        relative_area=True,
        area=[0, 0, 30, 100],
    )
    return pd.concat([page12, page13])


def get_asset_country_schema():
    p13 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[13],
        relative_area=True,
        area=[50, 0, 100, 100],
    )
    p14 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[14],
        relative_area=True,
        area=[0, 0, 40, 100],
    )
    return pd.concat([p13, p14])


def get_market_type_schema():
    return tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[14],
        relative_area=True,
        area=[35, 0, 50, 100],
    )


def get_currency_schema():
    p15 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[15],
        relative_area=True,
        area=[0, 0, 60, 100],
    )

    p14 = tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[14],
        relative_area=True,
        area=[50, 0, 100, 100],
    )
    return pd.concat([p14, p15])


def get_rating_agency_schema():
    return tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[15],
        relative_area=True,
        area=[65, 0, 100, 100],
    )


def get_financial_institution_schemas():
    return tabula.read_pdf("docs/Monthly_reporting_structure.pdf", pages=[16])


def get_anchor_interest_schema():
    return tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[17],
        relative_area=True,
        area=[10, 0, 40, 100],
    )


def get_anchor_interest_duration():
    return tabula.read_pdf(
        "docs/Monthly_reporting_structure.pdf",
        pages=[17],
        relative_area=True,
        area=[45, 0, 70, 100],
    )


def get_country_origin_schema():
    return pd.concat(
        [
            tabula.read_pdf(
                "docs/Monthly_reporting_structure.pdf",
                pages=[17],
                relative_area=True,
                area=[78, 0, 100, 100],
            ),
            tabula.read_pdf(
                "docs/Monthly_reporting_structure.pdf",
                pages=[18],
                relative_area=True,
                area=[0, 0, 60, 100],
            ),
        ]
    )


extractors = {
    "schema_description": get_schema_description,
    "assets": get_asset_type_schema,
    "info": get_other_info_schema,
    "price": get_price_schema,
    "id": get_id_no_schema,
    "asset_country": get_asset_country_schema,
    "market_type": get_market_type_schema,
    "currency": get_currency_schema,
    "rating_agency": get_rating_agency_schema,
    "financial_institution": get_financial_institution_schemas,
    "anchor_interest": get_anchor_interest_schema,
    "anchor_interest_duration": get_anchor_interest_duration,
    "origin_country": get_country_origin_schema,
}

memory = joblib.Memory("tmp", verbose=0)
cached_extractors = {
    name: memory.cache(extractor) for name, extractor in extractors.items()
}
