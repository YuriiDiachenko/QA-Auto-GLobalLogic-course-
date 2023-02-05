import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print(f'Respone is {r.text}')


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/YuriiDiachenko')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Yurii Diachenko'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404
