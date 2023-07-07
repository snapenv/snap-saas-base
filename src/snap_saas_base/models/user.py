import sqlalchemy as sa
import sqlalchemy.orm as so

from snap_saas_base.models.base_model_postgres import AbstractModel

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class User(AbstractModel):
    """A User class that represents the users table in the database.

    Attributes
    ----------
        __tablename__ (str): The name of the table in the database.
        username (so.Mapped[str]): The username of the user. This field is not nullable.
        provider (so.Mapped[str]): The provider of the user. This field is nullable and defaults to "local".
        email (so.Mapped[str]): The email of the user. This field is nullable.
        cell_phone (so.Mapped[str]): The cell phone number of the user. This field is nullable and indexed.
        full_name (so.Mapped[str]): The full name of the user. This field is not nullable.
        hashed_password (so.Mapped[str]): The hashed password of the user. This field is nullable.
        is_verified (so.Mapped[bool]): A boolean indicating if the user is verified. This field is not nullable and defaults to False.
        is_premium (so.Mapped[bool]): A boolean indicating if the user is a premium user. This field is not nullable and defaults to False.
        is_active (so.Mapped[bool]): A boolean indicating if the user is active. This field defaults to True.
        is_superuser (so.Mapped[bool]): A boolean indicating if the user is a superuser. This field defaults to False.
        phone_verified (so.Mapped[bool]): A boolean indicating if the user's phone number is verified. This field defaults to False.
        __table_args__ (tuple): A tuple containing SQLAlchemy table options.

    Methods
    -------
        as_dict: Returns a dictionary representation of the User object.
    """

    __tablename__ = "users"
    username: so.Mapped[str] = so.mapped_column(nullable=False)
    provider: so.Mapped[str] = so.mapped_column(default="local", nullable=True)
    email: so.Mapped[str] = so.mapped_column(nullable=True)
    cell_phone: so.Mapped[str] = so.mapped_column(nullable=True, index=True)
    full_name: so.Mapped[str] = so.mapped_column(nullable=False)
    hashed_password: so.Mapped[str] = so.mapped_column(nullable=True)
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
        """Returns a dictionary representation of the User object.

        Returns
        -------
            dict: A dictionary where the keys are the column names and the values are the corresponding attribute values.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
