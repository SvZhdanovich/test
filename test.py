import requests
import pytest


def test():
    r = requests.get('https://www.google.com/')
    assert r.status_code == 200
