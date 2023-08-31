"""Test Snap SAAS Base."""
from unittest import TestCase

from snap_saas_base.schemas.user import UserBaseSchema


class UserBaseSchemaTest(TestCase):
    """Test class for User bae schema."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up schema testcase")
        self.schema_data = {
            "username": "John Doe",
            "provider": "local",
            "email": "john.doe@domain.com",
            "cell_phone": "55279998812345",
            "avatar": "",
            "is_verified": True,
            "is_active": True,
            "is_superuser": False,
            "password": "SomeGoodPassword"
        }

    def test_creation(self) -> None:
        print("Test model object creation")
        new_obj = UserBaseSchema(**self.schema_data, full_name="John Doe")
        assert isinstance(new_obj, UserBaseSchema)
        assert new_obj.full_name is not None
