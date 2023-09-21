from utils.myconfigparser import getPetAPIURL

BASE_URL_PETSTORE = getPetAPIURL()


def test_a1():
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1


def test_a2():
    assert 9 / 5 == 1.5, "faild test intentionally"


def test_a3():
    assert 9 // 5 == 1  # integer truncating division


def test_a4():
    url = BASE_URL_PETSTORE + '123'
    print(url)
    assert 'petstore' in url
