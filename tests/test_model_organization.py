"""Test Snap SAAS Base."""

from snap_saas_base.models.organization import Organization, OrgMember


def test_model_organization() -> None:
    """Test that the model can be used."""
    model_data = Organization()
    assert isinstance(model_data.as_dict, dict)


def test_model_organization_members() -> None:
    """Test that the model can be used."""
    model_data = OrgMember()
    assert isinstance(model_data.as_dict, dict)
