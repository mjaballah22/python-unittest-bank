import pytest
from bank_account.bank_account import BankAccount

def test_init_negative_balance_raises():
    with pytest.raises(ValueError):
        BankAccount(-100)

def test_deposit_negative_or_zero_raises():
    acct = BankAccount(50)
    with pytest.raises(ValueError):
        acct.deposit(0)
    with pytest.raises(ValueError):
        acct.deposit(-10)

def test_withdraw_negative_or_zero_raises():
    acct = BankAccount(50)
    with pytest.raises(ValueError):
        acct.withdraw(0)
    with pytest.raises(ValueError):
        acct.withdraw(-5)

def test_withdraw_more_than_balance_raises():
    acct = BankAccount(50)
    with pytest.raises(ValueError):
        acct.withdraw(100)

def test_transfer_valid():
    acct1 = BankAccount(100)
    acct2 = BankAccount(50)
    acct1.transfer_to(acct2, 40)
    assert acct1.balance == 60
    assert acct2.balance == 90

def test_transfer_invalid_target_raises():
    acct1 = BankAccount(100)
    with pytest.raises(ValueError):
        acct1.transfer_to("not-an-account", 10)
