"""Test Snap SAAS Base."""

import snap_saas_base


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(snap_saas_base.__name__, str)
