from typing import Dict

import pytest

from solution import parse_address


@pytest.mark.parametrize(
    argnames=["address_string", "expected"],
    argvalues=(
            ("Winterallee 3", {"street": "Winterallee", "housenumber": "3"}),
            ("Musterstrasse 45", {"street": "Musterstrasse", "housenumber": "45"}),
            ("Blaufeldweg 123B", {"street": "Blaufeldweg", "housenumber": "123B"}),
            ("Am Bächle 23", {"street": "Am Bächle", "housenumber": "23"}),
            ("Auf der Vogelwiese 23 b", {"street": "Auf der Vogelwiese", "housenumber": "23 b"}),
            ("4, rue de la revolution", {"street": "rue de la revolution", "housenumber": "4"}),
            ("200 Broadway Av", {"street": "Broadway Av", "housenumber": "200"}),
            ("Calle Aduana, 29", {"street": "Calle Aduana", "housenumber": "29"}),
            ("Calle 39 No 1540", {"street": "Calle 39", "housenumber": "No 1540"}),
    )
)
def test_parse_address(address_string: str, expected: Dict[str, str]):
    assert parse_address(address_string) == expected
