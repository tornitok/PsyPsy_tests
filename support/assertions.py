from support.error_messages import AssertionErrors
import urllib.parse

class Assertions:
    @staticmethod
    def assert_equal(expected, actual):
        expected_decoded = urllib.parse.unquote(expected)
        actual_decoded = urllib.parse.unquote(actual)
        assert (expected_decoded == actual_decoded,
                AssertionErrors.URL_NOT_FOUND.format(
                    expected_decoded,
                    actual_decoded
                )
            )
