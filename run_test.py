import pytest


def run_tests():
    pytest.main(["-v", "-s", "test", "-W", "ignore::DeprecationWarning"])


if __name__ == "__main__":
    run_tests()
