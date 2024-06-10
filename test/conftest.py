import pytest
from fixture.application import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
target = None

def load_config(file):
    """
    Вспомогательная функция, которая выполняет загрузку конфигурации
    :param file: файл
    :return: конфгурация
    """
    global target
    if target is None:
        config_file = os.path.abspath(f'../{file}')
        # config_file = os.path.abspath(f'{file}')
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    """
    Функция, которая создаёт фикстуру и выполняет логин
    :param request: специальный параметр
    :return: фикстура (объект класса Application)
    """
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture(scope="session")
def db(request):
    """
    Функция, которая создаёт соединение с базой данных приложения, а затем закрывает его
    :param request: специальный параметр
    :return: фикстура (объект класса DbFixture)
    """
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture

@pytest.fixture(scope="session")
def orm(request):
    """
    Функция, которая создаёт соединение с базой данных приложения
    :param request: специальный параметр
    :return: фикстура (объект класса ORMFixture)
    """
    orm_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host=orm_config['host'], name=orm_config['name'], user=orm_config['user'],
                          password=orm_config['password'])
    return ormfixture

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

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

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
    with open(os.path.abspath(f"../data/{file}.json")) as f:
    # with open(os.path.abspath(f"data/{file}.json")) as f:
        return jsonpickle.decode(f.read())

