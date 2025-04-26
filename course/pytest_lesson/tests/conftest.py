import pytest


@pytest.fixture()
def set_up():
    print('вход в систему')
    yield
    print('выход из системы!')

@pytest.fixture(scope='module') # возпроизводиться в каждом модуле/файле
def some():
    print('Начало модуля')
    yield
    print('Конец модуля!')

@pytest.fixture(scope='function') # вопсроизводится в каждом методе
def body():
    print('Начало метода ')
    yield
    print('Конец метода!')