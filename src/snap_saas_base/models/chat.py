from datetime import datetime
from typing import Any

import sqlalchemy as sa
import sqlalchemy.orm as so
import uuid6
from sqlalchemy.dialects.postgresql import JSONB

from snap_saas_base.models.base_model import AbstractModel
from snap_saas_base.models.workspace import Workspace

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class Chat(AbstractModel):
    # Chats Table.
    __tablename__ = "chats"

    workspace_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
    )
    workspace: so.Mapped["Workspace"] = so.relationship("Workspace", uselist=False, lazy="raise")
    channel: so.Mapped[str] = so.mapped_column(nullable=False)
    channel_plugin: so.Mapped[str] = so.mapped_column(nullable=False)
    channel_id: so.Mapped[str] = so.mapped_column(nullable=False)
    channel_session_id: so.Mapped[str] = so.mapped_column(nullable=False)
    channel_contact_uid: so.Mapped[str] = so.mapped_column(nullable=False, index=True)
    subject: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    agi_id: so.Mapped[str] = so.mapped_column(nullable=False, index=True)
    status: so.Mapped[int] = so.mapped_column(nullable=False)
    state: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    # contact_id = Column(
    #     String(25), ForeignKey("contact.id", ondelete="RESTRICT", onupdate="CASCADE"), nullable=False
    # )
    contact_id: so.Mapped[str] = so.mapped_column(nullable=False)
    handsoff: so.Mapped[str] = so.mapped_column(nullable=True)
    handsoff_config: so.Mapped[str] = so.mapped_column(nullable=True, index=True)
    handsoff_cid: so.Mapped[str] = so.mapped_column(nullable=True)
    handsoff_data: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    slots: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    # session_data: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    session_metadata: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    history: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    deleted_at: so.Mapped[datetime] = so.mapped_column(nullable=True)

    # messages: so.WriteOnlyMapped["ChatMessage"] = so.relationship(
    #     back_populates="chat", cascade="all, delete-orphan"
    # )
    messages: so.Mapped[list["ChatMessage"]] = so.relationship(
        lazy="selectin", back_populates="chat"
    )
    # messages = so.relationship(
    #     "ChatMessage", back_populates="chat", lazy="raise", passive_deletes=True
    # )

    __table_args__ = (
        sa.UniqueConstraint("workspace_id", "id"),
        sa.UniqueConstraint("workspace_id", "handsoff_config", "handsoff_cid"),
        sa.UniqueConstraint("workspace_id", "channel", "channel_session_id"),
        sa.Index(
            "ix_chats_workspace_id_channel_channel_id",
            "workspace_id",
            "channel",
            "channel_session_id",
        ),
        sa.Index(
            "ix_chats_workspace_id_channel_contact_uid_created_at",
            "workspace_id",
            "channel_contact_uid",
            "created_at",
        ),
        sa.Index("ix_chats_workspace_id_id", "workspace_id", "id"),
        sa.Index(
            "ix_chats_by_channel_plugin",
            "workspace_id",
            "channel",
            "channel_plugin",
            "channel_session_id",
            "channel_contact_uid",
            "status",
        ),
        sa.Index(
            "ix_chats_session",
            "workspace_id",
            "channel",
            "channel_session_id",
            "channel_contact_uid",
            "status",
        ),
        sa.Index(
            "ix_chats_by_date_created",
            "workspace_id",
            "created_at",
            "id",
        ),
    )
    __mapper_args__ = {"eager_defaults": True}

    @property
    def as_dict(self):
        """Returns the chat as a dictionary.

        This method iterates over the columns of the table and gets the value of each column for the chat.

        Returns
        -------
        dict
            A dictionary representation of the chat.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super(Chat, self).__init__(*args, **kwargs)


class ChatMessage(AbstractModel):
    # Chats Table.
    __tablename__ = "chats_messages"

    chat_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("chats.id", ondelete="CASCADE"), nullable=False
    )
    channel_message_id: so.Mapped[str] = so.mapped_column(nullable=True)
    role: so.Mapped[str] = so.mapped_column(nullable=False)
    content_type: so.Mapped[str] = so.mapped_column(nullable=False)
    content: so.Mapped[str] = so.mapped_column(nullable=False)
    # origin: so.Mapped[str] = so.mapped_column(nullable=True)
    message_metadata: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)
    rating: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=True)
    deleted_at: so.Mapped[datetime] = so.mapped_column(nullable=True)

    chat: so.Mapped["Chat"] = so.relationship(
        back_populates="messages", uselist=False, lazy="raise"
    )
    # chat = so.relationship("Chat", back_populates="messages", uselist=False, lazy="raise")

    __table_args__ = (
        sa.UniqueConstraint("chat_id", "id"),
        sa.UniqueConstraint("chat_id", "channel_message_id"),
        sa.Index(
            "ix_chatsmessage_chat_id_id_created_at",
            "chat_id",
            "id",
            "created_at",
        ),
    )
    __mapper_args__ = {"eager_defaults": True}

    @property
    def as_dict(self):
        """Returns the chat as a dictionary.

        This method iterates over the columns of the table and gets the value of each column for the chat.

        Returns
        -------
        dict
            A dictionary representation of the chat.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super(ChatMessage, self).__init__(*args, **kwargs)
