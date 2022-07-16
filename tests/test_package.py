"""test_package"""
from package import hello_world


def test_hello_world() -> None:
    """Test hello_world returns."""
    assert hello_world() == "Hello World."
