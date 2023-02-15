from typing import Dict

import pytest

from solution import parse_address


@pytest.mark.parametrize(
    argnames=["address_string", "expected"],
    argvalues=(
        # Simple cases
        ("Winterallee 3", {"street": "Winterallee", "housenumber": "3"}),
        ("Musterstrasse 45", {"street": "Musterstrasse", "housenumber": "45"}),
        ("Blaufeldweg 123B", {"street": "Blaufeldweg", "housenumber": "123B"}),

        # More complicated ones
        ("Am Bächle 23", {"street": "Am Bächle", "housenumber": "23"}),
        ("Auf der Vogelwiese 23 b", {"street": "Auf der Vogelwiese", "housenumber": "23 b"}),

        # Complex cases, incl. other countries
        ("4, rue de la revolution", {"street": "rue de la revolution", "housenumber": "4"}),
        ("200 Broadway Av", {"street": "Broadway Av", "housenumber": "200"}),
        ("Calle Aduana, 29", {"street": "Calle Aduana", "housenumber": "29"}),
        ("Calle 39 No 1540", {"street": "Calle 39", "housenumber": "No 1540"}),

        # Edge cases
        ## No space in "No13"
        ("No13 Paulsternstr.", {"street": "Paulsternstr.", "housenumber": "No13"}),
        ## More than a single character after the number
        ("12Unter den Linden", None),
        ## But it works if there is only 1 character after a number
        ("12A Unter den Linden", {"street": "Unter den Linden", "housenumber": "12A"}),

        # What if there is only a street? Now we return nothing but is it correct?
        ("Unter den Linden", None),

        # If "No." is provided with a dot
        ("Friedrichstr. No. 90", {"street": "Friedrichstr.", "housenumber": "No. 90"})
    ),
)
def test_parse_address(address_string: str, expected: Dict[str, str]):
    assert parse_address(address_string) == expected
