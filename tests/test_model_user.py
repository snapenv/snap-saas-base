"""Test Snap SAAS Base."""
from unittest import TestCase

from snap_saas_base.models.user import User


class UserModelTest(TestCase):
    """Test class for User model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = User()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None
