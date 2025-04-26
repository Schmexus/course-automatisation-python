import pytest

@pytest.fixture()
def set_up(): #эта штука приоритетнее сетапа в конфтесте
    print('вход в систему')
    yield
    print('выход из системы')

def test_sending_mail_0(set_up, some):
    print('mail is sended')

def test_sending_mail_1(set_up, some):
    print('mail is sended')
