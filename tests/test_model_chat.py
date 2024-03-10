"""Test Snap SAAS Base."""

from unittest import TestCase

from snap_saas_base.models.chat import Chat, ChatMessage


class ChatModelTest(TestCase):
    """Test class for Chat model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = Chat()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None


class ChatMessageModelTest(TestCase):
    """Test class for ChatMessage model."""

    def setUp(self) -> None:
        """Create instance of class to test."""
        print("Setting up model testcase")
        self.model_data = ChatMessage()

    def test_creation(self) -> None:
        print("Test model object creation")
        assert isinstance(self.model_data.as_dict, dict)
        assert self.model_data.id is not None
