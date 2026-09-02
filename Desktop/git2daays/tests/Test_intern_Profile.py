from src.intern_profile import print_profile
from src.intern_profile import intern_name, role, department, skills


def test_print_profile(capsys):
    print_profile()

    captured = capsys.readouterr()

    assert intern_name in captured.out
    assert role in captured.out
    assert department in captured.out

    for skill in skills:
        assert skill in captured.out
# python3 -m pytest tests/test_intern_profile.py