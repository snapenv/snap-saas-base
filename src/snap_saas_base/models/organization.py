import sqlalchemy as sa
import sqlalchemy.orm as so
import uuid6

from snap_saas_base.models.base_model import AbstractModel
from snap_saas_base.models.user import User

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class Organization(AbstractModel):
    """A class used to represent an Organization in the database.

    This class is a subclass of the AbstractModel class and represents the structure of the 'organizations' table in the database.

    Attributes
    ----------
    __tablename__ : str
        The name of the table in the database.
    name : so.Mapped[str]
        The name of the organization. This field cannot be null.
    slug : so.Mapped[str]
        The slug of the organization. This field cannot be null and must be unique.
    bucket : so.Mapped[str]
        The bucket of the organization. This field cannot be null.
    created_by : so.Mapped[str]
        The user who created the organization. This field cannot be null and is a foreign key referencing the 'users' table.
    created_by_member: so.Mapped[User]
        And object referencing the user that created the Organization
    revoke_link : so.Mapped[bool]
        A boolean indicating whether the link to the organization has been revoked. The default value is False.
    org_member : so.WriteOnlyMapped["OrgMember"]
        A relationship to the OrgMember class, back_populates to 'org', with cascade options set to 'all, delete-orphan'.

    Methods
    -------
    as_dict:
        Returns a dictionary representation of the Organization instance.
    __init__(*args, **kwargs):
        Initializes the workspace. If no id is provided, a unique id is generated.
    """

    __tablename__ = "organizations"

    name: so.Mapped[str] = so.mapped_column(nullable=False)
    slug: so.Mapped[str] = so.mapped_column(nullable=False, unique=True)
    bucket: so.Mapped[str] = so.mapped_column(nullable=False)
    created_by: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    created_by_member: so.Mapped[User] = so.relationship("User", uselist=False, lazy="raise")
    revoke_link: so.Mapped[bool] = so.mapped_column(default=False, server_default=sa.text("false"))
    org_member: so.WriteOnlyMapped["OrgMember"] = so.relationship(
        back_populates="org", cascade="all, delete-orphan", passive_deletes=True
    )

    __mapper_args__ = {"eager_defaults": True}

    @property
    def as_dict(self):
        """Returns a dictionary representation of the Organization instance.

        This method iterates over the columns of the 'organizations' table and gets the corresponding attribute value from the Organization instance.

        Returns
        -------
        dict
            A dictionary where the keys are the column names and the values are the corresponding attribute values of the Organization instance.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super().__init__(*args, **kwargs)


class OrgMember(AbstractModel):
    """A class used to represent an Organization Member in a database.

    This class is a mapping to the "organizations_members" table in the database. It contains
    the organization id, member id and role of the member in the organization. It also has a
    relationship with the Organization class.

    ...

    Attributes
    ----------
    __tablename__ : str
        a string representing the name of the table in the database
    org_id : so.Mapped[str]
        a string representing the id of the organization the member belongs to
    member_id : so.Mapped[str]
        a string representing the id of the member
    role : so.Mapped[str]
        a string representing the role of the member in the organization
    org : so.Mapped["Organization"]
        an object representing the organization the member belongs to
    member : so.Mapped["User"]
        an object representing the member of the organization

    Methods
    -------
    as_dict:
        Returns the object as a dictionary
    __init__(*args, **kwargs):
        Initializes the workspace. If no id is provided, a unique id is generated.
    """

    __tablename__ = "organizations_members"

    org_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False
    )
    member_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role: so.Mapped[str] = so.mapped_column(nullable=False)
    org = so.relationship("Organization", back_populates="org_member", uselist=False, lazy="raise")
    member = so.relationship("User", uselist=False, lazy="raise")

    __mapper_args__ = {"eager_defaults": True}

    __table_args__ = (
        sa.Index("ix_organizations_members_org_id_member_id_role", "org_id", "member_id", "role"),
    )

    @property
    def as_dict(self):
        """Returns the object as a dictionary.

        This method is used to convert the object into a dictionary, where the keys are the column names
        and the values are the corresponding attributes of the object.

        Returns
        -------
        dict
            a dictionary representing the object
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super().__init__(*args, **kwargs)
