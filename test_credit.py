from credit import amount, period, percent
import pytest

# Сумма кредита
def test_amount1():
    assert amount > 0

def test_amount2():
    assert (amount < 0) == False

# Процентная ставка
def test_percent1():
    assert percent > 0

def test_percent2():
    assert (percent < 0) == False

# Период кредиторования
def test_period1():
    assert period > 0

def test_period2():
    assert (period < 0) == False

pytest.main()