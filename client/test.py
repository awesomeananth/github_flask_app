from .client import get_user_input
import sys, pytest

def test_success(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', 'Olshansk/interview')
        assert get_user_input() == 200

def test_success_two_inputs(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', 'Olshansk/interview', 'vlang/v')
        assert get_user_input() == 200
