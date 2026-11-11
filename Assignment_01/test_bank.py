
import pytest
from bank import BankAccount
@pytest.fixture
def account():
    return BankAccount("Ali", 1000)
def test_deposit(account):
    account.deposit(500)
    assert account.balance == 1500
def test_withdraw(account):
    account.withdraw(300)
    assert account.balance == 700
def test_history(account):
    account.deposit(200)
    account.withdraw(100)
    assert len(account.history) == 2
def test_negative_deposit(account):
    with pytest.raises(ValueError):
        account.deposit(-100)
def test_negative_withdraw(account):
    with pytest.raises(ValueError):
        account.withdraw(-100)
def test_insufficient_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)
