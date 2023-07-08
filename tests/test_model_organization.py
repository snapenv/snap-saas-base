"""Test Snap SAAS Base."""
from unittest import TestCase

from snap_saas_base.models.organization import Organization, OrgMember


class OrganizationModelTest(TestCase):
    """Test class for Organization model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = Organization()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None


class OrgMemberModelTest(TestCase):
    """Test class for OrgMember model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = OrgMember()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None
