import pytest

import schema_extractors
import pandas as pd


@pytest.mark.parametrize("extractor", schema_extractors.extractors)
def test_all_extractors(extractor):
    df = extractor()
    assert isinstance(df, pd.DataFrame)
