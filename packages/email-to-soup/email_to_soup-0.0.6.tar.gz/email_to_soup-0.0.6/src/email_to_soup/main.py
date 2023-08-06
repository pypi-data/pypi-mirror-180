import re
from bs4 import BeautifulSoup
from bs4 import Tag
from typing import Optional
from email.parser import Parser
from email.policy import default as default_policy
from dataclasses import dataclass
from lxml import html
import html2text


MULTIPLE_SPACES_REGEX = re.compile(r"[\s\u200c]+")

@dataclass
class EmailSoup:
    html_body: Optional[Tag]
    soup_text: str
    html_soup: BeautifulSoup
    xml_tree: html.HtmlElement
    markdown_text: str = None

def soupify_email(email: str) -> EmailSoup:
    """Convert an email string to a BeautifulSoup object.

    Args:
        email: The email string to convert.

    Returns:
        An EmailSoup object representing the email html-soup, html-body, soup-text.
    """
    email = Parser(policy=default_policy).parsestr(email)
    html_body = email.get_body(preferencelist=('html', 'plain')).get_content()
    html_soup = BeautifulSoup(html_body, features="lxml")
    xml_tree = html.fromstring(html_body)
    email_soup = EmailSoup(
        html_soup = html_soup,
        soup_text = _extract_soup_text(html_soup),
        html_body = html_body,
        xml_tree = xml_tree,
        markdown_text = _markdownify_email(html_body)
    )
    return email_soup


def _markdownify_email(html_body: str) -> Optional[str]:
    try:
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_tables = False
        markdown_text = h.handle(html_body)
        return markdown_text
    except Exception:
        return ""

def _extract_soup_text(html_soup: BeautifulSoup, ignore_links=True) -> str:
    try:
        soup_text = re.sub(
            MULTIPLE_SPACES_REGEX, " ", html_soup.get_text(strip=True, separator=" ")
        ).strip()
    except Exception:  # pylint: disable=broad-except
        return ""

    if not ignore_links:
        # loop over all links and and mention them in the soup text
        for link in html_soup.find_all("a"):
            # get the link text and url
            soup_text += f"{link.text.strip()} url: {link.get('href')}.\n"

    return soup_text
