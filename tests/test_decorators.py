# test_decorators.py

import pytest
import os
import logging
from src.decorators import log

@pytest.fixture
def clear_log_file():
    """Фикстура для очистки лог-файла перед тестами."""
    log_file = "test_log.txt"
    if os.path.exists(log_file):
        os.remove(log_file)
    yield
    if os.path.exists(log_file):
        os.remove(log_file)

@log(filename="test_log.txt")
def add(x, y):
    return x + y

@log(filename="test_log.txt")
def divide(x, y):
    return x / y

def test_add_logging(clear_log_file):
    add(1, 2)
    with open("test_log.txt", "r") as f:
        logs = f.read()
    assert "add ok" in logs

def test_divide_logging(clear_log_file):
    divide(4, 2)
    with open("test_log.txt", "r") as f:
        logs = f.read()
    assert "divide ok" in logs

def test_divide_logging_error(clear_log_file):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    with open("test_log.txt", "r") as f:
        logs = f.read()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in logs

def test_add_logging_console(capsys):
    @log()
    def multiply(x, y):
        return x * y

    multiply(3, 4)
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out