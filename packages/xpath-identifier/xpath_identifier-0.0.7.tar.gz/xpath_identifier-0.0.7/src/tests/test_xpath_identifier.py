import pytest
from xpath_identifier import search_email
from xpath_identifier import search_html
from xpath_identifier import find_closest_tag

@pytest.fixture
def email_fixture():
    return open("src/tests/fixtures/test_email.eml").read()

@pytest.fixture
def html_fixture():
    return open("src/tests/fixtures/test_html.html").read()

def test_search_in_email(email_fixture):
    response = search_email(email_fixture, "9300120111409082698691")
    assert len(response) == 1
    assert [x[1] for x in response] == [
        "/html/body/div/table/tr/td/table/tr/td/div[5]/div/table/tr/td/p[2]/a/span"
    ]
    response = search_email(email_fixture, "9405511202508597717093")
    assert [x[1] for x in response] == [
        "/html/body/div/table/tr/td/table/tr/td/div[6]/div/table/tr/td/p[2]/a/span"
    ]


def test_search_in_html(html_fixture):
    response = search_html(html_fixture, "Send them a gift tracking link")
    assert [x[1] for x in response] == [
        "/html/head/script[2]"
    ]

def test_closest_tag(email_fixture):
    response = search_html(email_fixture, "9405511202508597717093")
    closest_result = find_closest_tag(response[0][0], "a")
    assert [x[1] for x in closest_result] == [
        "/html/body/p/aaaaaaaaaaaaaaaaaaaa/uspsinformeddelivery/div/table/tr/td/table/tr/td/div[6]/div/table/tr/td/p[2]/a",
        "/html/body/p/aaaaaaaaaaaaaaaaaaaa/uspsinformeddelivery/div/table/tr/td/table/tr/td/div[7]/table[1]/tbody/tr/td/p[1]/a",
    ]
