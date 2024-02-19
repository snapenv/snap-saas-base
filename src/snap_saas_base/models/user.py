import sqlalchemy as sa
import sqlalchemy.orm as so
import uuid6

from snap_saas_base.models.base_model import AbstractModel

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class User(AbstractModel):
    """
    A class used to represent a User in the system.

    ...

    Attributes
    ----------
    __tablename__ : str
        a string representing the name of the table in the database
    username : so.Mapped[str]
        a string representing the username of the user, cannot be null
    provider : so.Mapped[str]
        a string representing the provider of the user, default is "local"
    email : so.Mapped[str]
        a string representing the email of the user
    cell_phone : so.Mapped[str]
        a string representing the cell phone number of the user
    full_name : so.Mapped[str]
        a string representing the full name of the user, cannot be null
    hashed_password : so.Mapped[str]
        a string representing the hashed password of the user
    is_verified : so.Mapped[bool]
        a boolean indicating whether the user is verified, default is False
    is_active : so.Mapped[bool]
        a boolean indicating whether the user is active, default is True
    is_superuser : so.Mapped[bool]
        a boolean indicating whether the user is a superuser, default is False
    phone_verified : so.Mapped[bool]
        a boolean indicating whether the user's phone is verified, default is False

    Methods
    -------
    as_dict:
        Returns the user's attributes as a dictionary
    __init__(*args, **kwargs):
        Initializes the workspace. If no id is provided, a unique id is generated.
    """

    __tablename__ = "users"
    username: so.Mapped[str] = so.mapped_column(nullable=False)
    provider: so.Mapped[str] = so.mapped_column(default="local", nullable=False)
    email: so.Mapped[str] = so.mapped_column(nullable=False)
    cell_phone: so.Mapped[str] = so.mapped_column(nullable=False, index=True)
    full_name: so.Mapped[str] = so.mapped_column(nullable=False)
    avatar: so.Mapped[str] = so.mapped_column(nullable=True)
    password: so.Mapped[str] = so.mapped_column(nullable=True)
    is_verified: so.Mapped[bool] = so.mapped_column(
        nullable=False, default=False, server_default=sa.text("false")
    )
    is_premium: so.Mapped[bool] = so.mapped_column(
        nullable=False, default=False, server_default=sa.text("false")
    )
    is_active: so.Mapped[bool] = so.mapped_column(default=True, server_default=sa.text("true"))
    is_superuser: so.Mapped[bool] = so.mapped_column(default=False, server_default=sa.text("false"))
    phone_verified: so.Mapped[bool] = so.mapped_column(
        default=False, server_default=sa.text("false")
    )

    __table_args__ = (sa.UniqueConstraint("username", "provider"),)

    @property
    def as_dict(self):
        """Returns the user's attributes as a dictionary.

        Returns
        -------
        dict
            a dictionary containing the user's attributes
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __init__(self, *args, **kwargs):
        if "id" not in kwargs:
            kwargs["id"] = str(uuid6.uuid7())
        super().__init__(*args, **kwargs)
