from datetime import datetime
from typing import Any

import sqlalchemy as sa
import sqlalchemy.orm as so
import uuid6
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from snap_saas_base.models.base_model import AbstractModel
from snap_saas_base.models.user import User

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class Workspace(AbstractModel):
    """A class used to represent a Workspace.

    This class inherits from the AbstractModel class and represents a workspace in a database.
    It includes information about the workspace such as its name, slug, bucket and  organization id.

    Attributes
    ----------
    __tablename__ : str
        The name of the table in the database.
    name : so.Mapped[str]
        The name of the workspace. This field is not nullable.
    slug : so.Mapped[str]
        The slug of the workspace. This field is not nullable.
    bucket : so.Mapped[str]
        The bucket of the workspace. This field is nullable.
    org_id : so.Mapped[str]
        The organization id of the workspace. This field is not nullable and is a foreign key referencing the id of the organization.
    org : so.Mapped["Organization"]
        an object representing the organization the workspace belongs to.
    __table_args__ : tuple
        A tuple containing a unique constraint for the combination of org_id and slug.

    Methods
    -------
    as_dict:
        Returns the workspace as a dictionary.
    __init__(*args, **kwargs):
        Initializes the workspace. If no id is provided, a unique id is generated.
    """

    __tablename__ = "workspaces"
    name: so.Mapped[str] = so.mapped_column(nullable=False)
    slug: so.Mapped[str] = so.mapped_column(nullable=False)
    bucket: so.Mapped[str] = so.mapped_column(nullable=True)
    org_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("organizations.id", ondelete="RESTRICT"), nullable=False
    )
    org = so.relationship("Organization", uselist=False, lazy="raise")

    __table_args__ = (sa.UniqueConstraint("org_id", "slug"),)

    @property
    def as_dict(self):
        """Returns the workspace as a dictionary.

        This method iterates over the columns of the table and gets the value of each column for the workspace.

        Returns
        -------
        dict
            A dictionary representation of the workspace.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super().__init__(*args, **kwargs)


class WorkspaceMember(AbstractModel):
    """A class used to represent a member in a workspace.

    This class is a model for the table "workspaces_members" in the database. It contains the workspace_id, member_id and role
    of a member in a workspace. It also includes a method to return the object as a dictionary.

    Attributes
    ----------
    __tablename__ : str
        The name of the table in the database.
    workspace_id : so.Mapped[str]
        The ID of the workspace the member belongs to. This is a foreign key linked to the "workspaces" table.
    member_id : so.Mapped[str]
        The ID of the member. This is a foreign key linked to the "users" table.
    role : so.Mapped[str]
        The role of the member in the workspace.
    workspace : so.Mapped["Workspace"]
        an object representing the workspace the member belongs to
    member : so.Mapped["User"]
        an object representing the member of the workspace
    __table_args__ : tuple
        Additional arguments for the table, such as indexes.

    Methods
    -------
    as_dict:
        Returns the object as a dictionary.
    __init__(*args, **kwargs):
        Initializes the workspace. If no id is provided, a unique id is generated.
    """

    __tablename__ = "workspaces_members"
    workspace_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
    )
    member_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role: so.Mapped[str] = so.mapped_column(nullable=False)
    workspace: so.Mapped[Workspace] = so.relationship("Workspace", uselist=False, lazy="raise")
    member: so.Mapped[User] = so.relationship("User", uselist=False, lazy="raise")

    __table_args__ = (
        sa.Index(
            "ix_workspaces_members_workspace_id_member_id_role", "workspace_id", "member_id", "role"
        ),
    )

    @property
    def as_dict(self):
        """Returns the object as a dictionary.

        This method uses a dictionary comprehension to iterate over the columns of the table and get the corresponding
        attribute from the object.

        Returns
        -------
        dict
            A dictionary where the keys are the column names and the values are the corresponding attributes of the object.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super().__init__(*args, **kwargs)


class WorkspaceKv(AbstractModel):
    """A class used to represent the Workspace Key-Value pair model.

    This class is a subclass of the AbstractModel and is used to map the
    'workspaces_kv' table in the database. It contains three main attributes:
    workspace_id, key, and value. The workspace_id is a foreign key that
    references the 'id' in the 'workspaces' table. The 'key' and 'value'
    attributes are used to store the key-value pairs.

    Attributes
    ----------
    __tablename__ : str
        The name of the table in the database that this class maps to.
    workspace_id : so.Mapped[str]
        The ID of the workspace that this key-value pair belongs to.
    workspace : so.Mapped["Workspace"]
        an object representing the workspace the key-value pair belongs to.
    key : so.Mapped[str]
        The key in the key-value pair.
    value : so.Mapped[dict[str, str]]
        The value in the key-value pair.

    Methods
    -------
    as_dict:
        Returns a dictionary representation of the WorkspaceKv object.
    __init__(*args, **kwargs):
        Initializes the workspace. If no id is provided, a unique id is generated.
    """

    __tablename__ = "workspaces_kv"
    workspace_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
    )
    workspace: so.Mapped[Workspace] = so.relationship("Workspace", uselist=False, lazy="raise")
    key: so.Mapped[str] = so.mapped_column(nullable=False)
    value: so.Mapped[dict[str, str]] = so.mapped_column(JSONB, nullable=False)

    @property
    def as_dict(self):
        """Returns a dictionary representation of the WorkspaceKv object.

        This method iterates over the columns of the 'workspaces_kv' table
        and gets the corresponding attribute value from the WorkspaceKv object.

        Returns
        -------
        dict
            A dictionary where the keys are the column names and the values
            are the corresponding attribute values from the WorkspaceKv object.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super().__init__(*args, **kwargs)


class WorkspaceApiKey(AbstractModel):
    """
    A class used to represent a Workspace API key.

    This class is a model for the table 'workspaces_apikeys' in the database. It includes
    information about the API key such as the workspace_id, member_id, type, label, key,
    value, role, and active status.

    Attributes
    ----------
    __tablename__ : str
        The name of the table in the database.
    workspace_id : so.Mapped[str]
        The ID of the workspace the API key belongs to. This is a foreign key linked to the "workspaces" table.
    member_id : so.Mapped[str]
        The ID of the member associated with the API key. This is a foreign key linked to the "users" table.
    workspace : so.Mapped["Workspace"]
        an object representing the workspace the member belongs to
    member : so.Mapped["User"]
        an object representing the member of the workspace
    type : so.Mapped[str]
        The type of the API key.
    label : so.Mapped[str]
        The label or name associated with the API key.
    key : so.Mapped[str]
        The key value of the API key.
    value : so.Mapped[dict[str, str]]
        The value associated with the API key.
    role : so.Mapped[str]
        The role assigned to the API key.
    active : so.Mapped[bool]
        The status of the API key, whether it is active or not.

    Methods
    -------
    as_dict:
        Returns the object as a dictionary.
    __init__(*args, **kwargs):
        Initializes the WorkspaceApiKey. If no id is provided, a unique id is generated.
    """

    __tablename__ = "workspaces_apikeys"
    workspace_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
    )
    member_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    workspace: so.Mapped[Workspace] = so.relationship("Workspace", uselist=False, lazy="raise")
    member: so.Mapped[User] = so.relationship("User", uselist=False, lazy="raise")
    type: so.Mapped[str] = so.mapped_column(nullable=False)
    label: so.Mapped[str] = so.mapped_column(nullable=False)
    key: so.Mapped[str] = so.mapped_column(nullable=False)
    value: so.Mapped[dict[str, str]] = so.mapped_column(JSONB, nullable=False)
    role: so.Mapped[str] = so.mapped_column(nullable=False)
    active: so.Mapped[bool] = so.mapped_column(
        nullable=False, default=True, server_default=sa.text("true")
    )

    __table_args__ = (
        sa.UniqueConstraint("member_id", "key"),
        sa.UniqueConstraint("key"),
    )

    @property
    def as_dict(self):
        """Returns the object as a dictionary.

        This method uses a dictionary comprehension to iterate over the columns of the table and get the corresponding
        attribute from the object.

        Returns
        -------
        dict
            A dictionary where the keys are the column names and the values are the corresponding attributes of the object.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        if "key" not in kwargs:
            kwargs["key"] = str(uuid6.uuid7())

        super(WorkspaceApiKey, self).__init__(*args, **kwargs)


class WorkspaceMetric(AbstractModel):
    """
    A class used to represent a metric in a workspace.

    This class is a model for the table 'workspaces_metrics' in the database. It includes
    information about the metric such as the workspace_id, specversion, type, event_id, time,
    source, subject, and data.

    Attributes
    ----------
    __tablename__ : str
        The name of the table in the database.
    workspace_id : so.Mapped[str]
        The ID of the workspace the metric belongs to. This is a foreign key linked to the "workspaces" table.
    workspace : so.Mapped[Workspace]
        an object representing the workspace the metric belongs to
    specversion : so.Mapped[str]
        The specversion of the metric.
    type : so.Mapped[str]
        The type of the metric.
    event_id : so.Mapped[str]
        The event_id associated with the metric.
    time : so.Mapped[datetime]
        The time at which the metric was recorded.
    source : so.Mapped[str]
        The source of the metric.
    subject : so.Mapped[str]
        The subject of the metric.
    data : so.Mapped[dict[str, Any]]
        The data associated with the metric.

    Methods
    -------
    as_dict:
        Returns the workspace metric as a dictionary.
    __init__(*args, **kwargs):
        Initializes the WorkspaceMetric. If no id is provided, a unique id is generated.
    """

    __tablename__ = "workspaces_metrics"

    workspace_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False
    )
    workspace: so.Mapped[Workspace] = so.relationship("Workspace", uselist=False, lazy="raise")
    specversion: so.Mapped[str] = so.mapped_column(nullable=False)
    type: so.Mapped[str] = so.mapped_column(nullable=False)
    event_id: so.Mapped[str] = so.mapped_column(nullable=False)
    time: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )
    source: so.Mapped[str] = so.mapped_column(nullable=False)
    subject: so.Mapped[str] = so.mapped_column(nullable=False)
    data: so.Mapped[dict[str, Any]] = so.mapped_column(JSONB, nullable=False)

    __table_args__ = (
        sa.Index("ix_workspaces_metrics_time_type", "workspace_id", "time", "type"),
        sa.Index(
            "ix_workspaces_metrics_type_time",
            "workspace_id",
            "type",
            "time",
        ),
        sa.UniqueConstraint("workspace_id", "source", "event_id"),
    )
    __mapper_args__ = {"eager_defaults": True}

    @property
    def as_dict(self):
        """Returns the workspace metric as a dictionary.

        This method iterates over the columns of the table and gets the value of each column for the workspace metric.

        Returns
        -------
        dict
            A dictionary representation of the workspace.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super(WorkspaceMetric, self).__init__(*args, **kwargs)
