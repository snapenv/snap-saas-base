"""Test Snap SAAS Base."""

from snap_saas_base.models.user import User


def test_model() -> None:
    """Test that the model can be used."""
    model_data = User()
    assert isinstance(model_data.as_dict, dict)
    # assert isinstance(snap_saas_base.__name__, str)
