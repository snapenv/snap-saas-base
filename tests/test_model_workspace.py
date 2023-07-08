"""Test Snap SAAS Base."""
from unittest import TestCase
from snap_saas_base.models.workspace import Workspace, WorkspaceMember, WorkspaceKv


class WorkspaceModelTest(TestCase):
    """Test class for Workspace model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = Workspace()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None


class WorkspaceMemberModelTest(TestCase):
    """Test class for WorkspaceMember model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = WorkspaceMember()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None


class WorkspaceKvModelTest(TestCase):
    """Test class for WorkspaceKv model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = WorkspaceKv()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None
