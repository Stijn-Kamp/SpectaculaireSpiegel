import requests
import simplejson


class ApiReader:
    """class used to communicate to web apis"""
    def __init__(self, base, **parameters):
        """"
        :param base: Base of the url
        :param parameters: list of keys and values
        """
        self.url = self.url_builder(base, **parameters)

    def get(self):
        """
        :return: None if failed, else the content of the request
        """
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            response = response.json()
        except requests.HTTPError:
            response = None
        except requests.exceptions.ConnectionError:
            response = None
        except simplejson.errors.JSONDecodeError:
            response = None
        return response

    @staticmethod
    def url_builder(base, **parameters):
        """
        Builds an url using the base url and the parameters
        :param base: Base of the url
        :param parameters: url parameters
        :return: modified url
        """
        base += '?'
        for par in parameters.items():
            base += "%s=%s&" % par
        base = base[:-1]
        print(base)
        return base
