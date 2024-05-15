import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle

fixture = None
target = None

@pytest.fixture
def app(request):
    """
    Функция, которая создаёт фикстуру и выполняет логин
    :param request: специальный параметр
    :return: фикстура (объект класса Application)
    """
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.abspath(f'../{request.config.getoption("--target")}')
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    """
    Функция, которая разрушает фикстуру и выполняет логаут
    :param request: специальный параметр
    :return: фикстура (объект класса Application)
    """
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])

def load_from_module(module):
    return importlib.import_module("data.{}".format(module)).test_data

def load_from_json(file):
    with open(os.path.join(os.path.abspath(os.path.abspath(f"../data/{file}.json")))) as f:
        return jsonpickle.decode(f.read())

