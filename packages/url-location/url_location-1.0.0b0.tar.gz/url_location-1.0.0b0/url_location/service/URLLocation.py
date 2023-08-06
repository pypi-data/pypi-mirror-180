__author__ = "Eduardo Tuteggito Rosero"
__license__ = "MIT License"
__version__ = "1.0.0-beta"
__maintainer__ = "Eduardo Tuteggito Rosero"
__email__ = "zerhiphop@live.com"
__status__ = "Development"
__date__ = "08/December/2022"

from url_location.utils.Countries import Countries


class URLLocation:
    def __init__(self):
        self.__countries = Countries().getCountries()
        self.__subdomains = ["com", "org", "net", "int", "edu", "gob", "gov", "mil", "blog"]
        self.__updateRegex()
        self.__updateCountries()

    def processUrl(self, url: str) -> str:
        for r in self.__regex:
            if r in url:
                index = url.index(r)
                subDomain = url[index: index + len(r) + 2]
                return self.__myCountries.get(subDomain[-2:], None)

    def addSubdomain(self, subDomain: [str, list]) -> None:
        """
        :param subDomain: Could be a subdomain string or a list of subdomains that will be appended to existing domains
        :return:
        """
        if isinstance(subDomain, str):
            self.__subdomains.append(subDomain)
            self.__updateRegex()
        elif isinstance(subDomain, list):
            self.__subdomains.extend(subDomain)
            self.__subdomains = list(set(self.__subdomains))
            self.__updateRegex()
        else:
            raise ValueError

    def defineSubdomains(self, subDomain: [str, list]) -> None:
        """
        :param subDomain: Could be a subdomain string or a list of subdomains that will replace to existing domains
        :return:
        """
        if isinstance(subDomain, str):
            self.__subdomains = [subDomain]
            self.__updateRegex()
        elif isinstance(subDomain, list):
            self.__subdomains = subDomain
            self.__subdomains = list(set(self.__subdomains))
            self.__updateRegex()
        else:
            raise ValueError

    def addCountry(self, country: dict) -> None:
        if isinstance(country, dict):
            self.__countries.append(country)
            self.__updateCountries()
        else:
            raise ValueError

    def defineCountries(self, country: [dict, list]) -> None:
        if isinstance(country, dict):
            self.__countries = [country]
            self.__updateCountries()
        elif isinstance(country, list):
            self.__countries = country
            self.__updateCountries()
        else:
            raise ValueError

    def __updateRegex(self) -> None:
        self.__regex = [f".{s}." for s in self.__subdomains]

    def __updateCountries(self) -> None:
        self.__myCountries = {c.get('alpha2code').lower(): c.get('alpha3code') for c in self.__countries}

    def getSubDomains(self) -> list:
        return self.__subdomains

    def getCountries(self) -> list:
        return self.__countries
