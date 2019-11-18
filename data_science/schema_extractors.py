import pandas as pd
import tabula


def get_asserts_and_liabilities():
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


extractors = [
    get_asserts_and_liabilities,
    get_other_info_schema,
    get_price_schema,
    get_id_no_schema,
    get_asset_country_schema,
    get_market_type_schema,
    get_currency_schema,
    get_rating_agency_schema,
    get_financial_institution_schemas,
    get_anchor_interest_schema,
    get_anchor_interest_duration,
    get_country_origin_schema,
]
