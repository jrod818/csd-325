# Jose Rodriguez
# 7/13/2026
# CSD 325 Module 7.2 Test Cases


# Formats city and country information.
# Population and language are optional.


def city_country(city, country, population=None, language=None):
    """Return formatted city information with optional details."""

    location = f"{city.title()}, {country.title()}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language.title()}"

    return location


if __name__ == "__main__":
    print(city_country("santiago", "chile"))

    print(
        city_country(
            "napa",
            "united states",
            79000
        )
    )

    print(
        city_country(
            "anchorage",
            "united states",
            286000,
            "english"
        )
    )