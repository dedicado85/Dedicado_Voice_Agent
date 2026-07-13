import webbrowser
from urllib.parse import quote_plus


class Browser:

    def open(self, url):

        webbrowser.open(url)

    def google_search(self, query):

        url = (
            "https://www.google.com/search?q="
            + quote_plus(query)
        )

        webbrowser.open(url)