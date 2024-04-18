import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    """
    Функция, которая создаёт и разрушает фикстуру
    :param request: специальный параметр
    :return: фикстура (объект класса Application)
    """
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

