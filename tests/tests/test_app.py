from app import calculate_transfer_fee, validate_transfer
import pytest


def test_transfer_fee():
    assert calculate_transfer_fee(100) == 1.00


def test_zero_transfer_is_invalid():
    assert validate_transfer(0) is False


def test_positive_transfer_is_valid():
    assert validate_transfer(100) is True


def test_negative_amount():
    with pytest.raises(ValueError):
        calculate_transfer_fee(-1)
