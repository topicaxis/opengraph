import json
from unittest import TestCase, main
from unittest.mock import patch, MagicMock

from opengraph.opengraph import OpenGraph

HTML = """
<html>
    <head>
        <title>The Rock (1996)</title>
        <meta property="og:title" content="The Rock" />
        <meta property="og:type" content="movie" />
        <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
        <meta property="og:image" content="http://ia.media-imdb.com/images/rock.jpg" />
        <meta property="og:description" content="movie description" />
    </head>
    <body>
        <p>hello world</p>
    </body>
</html>
"""


HTML_WITH_MISSING_REQUIRED_ATTRS = """
<html>
    <head>
        <title>The Rock (1996)</title>
        <meta property="og:title" content="The Rock" />
        <meta property="og:type" content="movie" />
        <meta property="og:url" content="http://www.imdb.com/title/tt0117500/" />
    </head>
    <body>
        <p>hello world</p>
    </body>
</html>
"""


class OpenGraphTests(TestCase):
    def test_parser(self):
        og = OpenGraph()
        og.parser(HTML)

        self.assertTrue(og.is_valid())
        self.assertDictEqual(
            og,
            {
                "_url": None,
                "description": "movie description",
                "image": "http://ia.media-imdb.com/images/rock.jpg",
                "scrape": False,
                "title": "The Rock",
                "type": "movie",
                "url": "http://www.imdb.com/title/tt0117500/"
            }
        )

    def test_parser_with_missing_required_attrs(self):
        og = OpenGraph()
        og.parser(HTML_WITH_MISSING_REQUIRED_ATTRS)

        self.assertFalse(og.is_valid())
        self.assertDictEqual(
            og,
            {
                "_url": None,
                "scrape": False,
                "title": "The Rock",
                "type": "movie",
                "url": "http://www.imdb.com/title/tt0117500/"
            }
        )

    def test_convert_to_json(self):
        og = OpenGraph()
        og.parser(HTML)

        json_encoded = og.to_json()

        self.assertIsInstance(json_encoded, str)

        decoded = json.loads(json_encoded)

        self.assertDictEqual(
            decoded,
            {
                "_url": None,
                "description": "movie description",
                "image": "http://ia.media-imdb.com/images/rock.jpg",
                "scrape": False,
                "title": "The Rock",
                "type": "movie",
                "url": "http://www.imdb.com/title/tt0117500/"
            }
        )

    def test_is_valid(self):
        og = OpenGraph()
        og.parser(HTML)

        self.assertTrue(og.is_valid())

    def test_is_valid_with_missing_required_attrs(self):
        og = OpenGraph()
        og.parser(HTML_WITH_MISSING_REQUIRED_ATTRS)

        self.assertFalse(og.is_valid())

    @patch("opengraph.opengraph.urlopen")
    def test_open_url(self, urlopen_mock):
        read_mock = MagicMock()
        read_mock.read.return_value = HTML
        urlopen_mock.side_effect = lambda url: read_mock

        og = OpenGraph(url="http://www.example.com")

        self.assertTrue(og.is_valid())
        self.assertDictEqual(
            og,
            {
                "_url": "http://www.example.com",
                "description": "movie description",
                "image": "http://ia.media-imdb.com/images/rock.jpg",
                "scrape": False,
                "title": "The Rock",
                "type": "movie",
                "url": "http://www.imdb.com/title/tt0117500/"
            }
        )


if __name__ == "__main__":
    main()
