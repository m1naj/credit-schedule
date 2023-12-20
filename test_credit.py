import pytest

from credit import calculate_loan

@pytest.mark.parametrize("amount, percent, period, expected_overpayment", [
    (10000, 5, 12, 270.83),
    (5000, 3, 6, 43.75),
    (20000, 8, 24, 1666.67)
])
def test_calculate_loan(amount, percent, period, expected_overpayment):
    payment_schedule, overpayment = calculate_loan(amount, percent, period)

    assert len(payment_schedule) == period
    assert isinstance(overpayment, float)
    assert overpayment == pytest.approx(expected_overpayment, abs=0.01)

def test_calculate_loan_zero_amount():
    amount = 0
    percent = 5
    period = 12

    with pytest.raises(ValueError) as e:
        calculate_loan(amount, percent, period)
    
    assert str(e.value) == "Amount must be a positive number"
    

def test_calculate_loan_negative_amount():
    amount = -10000
    percent = 5
    period = 12

    with pytest.raises(ValueError) as e:
        calculate_loan(amount, percent, period)
    
    assert str(e.value) == "Amount must be a positive number"