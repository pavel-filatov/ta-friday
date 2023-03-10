import logging
import re
from typing import Dict, Optional

SEPARATOR = r"[\s,]+"
DEFAULT_HOUSE_NUMBER = r"\d+(\s*[a-z]\b)?"
STREET = r"[\w\s\.]+"

extended_house_number = r"\bno\.?\s*{default_house_number}".format(default_house_number=DEFAULT_HOUSE_NUMBER)

street_housenum = r"^(?P<street>{street}){sep}(?P<housenumber>{house_number})$"
housenum_street = r"^(?P<housenumber>{house_number}){sep}(?P<street>{street})$"

patterns_raw = [
    (
        "starts_with_extensive_house",
        housenum_street.format(street=STREET, sep=SEPARATOR, house_number=extended_house_number),
    ),
    (
        "starts_with_extensive_street",
        street_housenum.format(street=STREET, sep=SEPARATOR, house_number=extended_house_number),
    ),
    ("starts_with_house", housenum_street.format(street=STREET, sep=SEPARATOR, house_number=DEFAULT_HOUSE_NUMBER)),
    ("starts_with_street", street_housenum.format(street=STREET, sep=SEPARATOR, house_number=DEFAULT_HOUSE_NUMBER)),
]

compiled_patterns = [(pattern_name, re.compile(pattern, re.IGNORECASE)) for pattern_name, pattern in patterns_raw]


def parse_address(address_string: str) -> Optional[Dict[str, str]]:
    """Extracts street name and house number from a string."""
    for pattern_name, pattern in compiled_patterns:
        m = re.match(pattern, address_string)
        if m:
            logging.debug(f"String{address_string}\tMatched pattern '{pattern_name}'")
            # As we use named groups for capturing, no need to parse them manually
            return m.groupdict()


def main() -> None:
    """The application loop."""
    continue_loop = True
    print("Welcome to Address Parser 3000! This is the right place to parse addresses.")

    try:
        while continue_loop:
            print("Please enter the address or :quit to exit.")
            user_address = input("> ")
            if user_address == ":quit":
                break

            result = parse_address(user_address)
            if result:
                print(f"This is what we parsed: {result}")
            else:
                print(f"Unable to parse: {user_address}")
    except KeyboardInterrupt:
        pass

    print("Thanks for being here. Tsch??ssi!")


if __name__ == "__main__":
    main()
