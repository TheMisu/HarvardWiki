from django.test import TestCase
from .views import convert_md_to_html
from .util import get_entry

# Create your tests here.
class ConvertMdToHtml(TestCase):
    def test_conv(self):
        html_content = convert_md_to_html("CSS")
        print(html_content)
        self.assertIsNotNone(html_content)