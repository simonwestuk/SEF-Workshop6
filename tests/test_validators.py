
import pytest
from my_app.validator import validate_name, validate_number

def test_validate_name_valid(monkeypatch):
  monkeypatch.setattr("builtins.input", lambda _: "Simon")
  assert validate_name() == "Simon"

def test_validate_name_invalid_then_valid(monkeypatch, capsys):
  inputs = iter(["123", "Simon"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))

  result = validate_name()
  captured = capsys.readouterr()

  assert result == "Simon"
  assert "Name can only contain letters and spaces." in captured.out

def test_validate_number_valid(monkeypatch):
  monkeypatch.setattr("builtins.input", lambda _: "01234567890")
  assert validate_number() == "01234567890"

def test_validate_number_wrong_length_then_valid(monkeypatch, capsys):
  inputs = iter(["12345", "01234567890"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))

  result = validate_number()
  captured = capsys.readouterr()

  assert result == "01234567890"
  assert "Number must be 11 digits and contain only digits." in captured.out

def test_validate_number_non_digits_then_valid(monkeypatch, capsys):
  inputs = iter(["abcdefghijk", "01234567890"])
  monkeypatch.setattr("builtins.input", lambda _: next(inputs))

  result = validate_number()
  captured = capsys.readouterr()

  assert result == "01234567890"
  assert "Number must be 11 digits and contain only digits." in captured.out