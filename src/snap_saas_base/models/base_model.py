from datetime import datetime

import sqlalchemy as sa
import sqlalchemy.orm as so
import uuid6

db_naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# https://blog.miguelgrinberg.com/post/what-s-new-in-sqlalchemy-2-0


class AbstractModel(so.DeclarativeBase):
    """Abstract base class for SQLAlchemy models. This class provides common
    attributes and methods for all models.

    Attributes
    ----------
    __abstract__ : bool
        SQLAlchemy attribute to indicate that this is an abstract base class.
    metadata : sa.MetaData
        SQLAlchemy MetaData instance with a naming convention.
    id : so.Mapped[str]
        Unique identifier for each instance, non-nullable and auto-generated.
    created_at : so.Mapped[datetime]
        Timestamp of when the instance was created, non-nullable and auto-generated.
    updated_at : so.Mapped[datetime]
        Timestamp of when the instance was last updated, non-nullable and auto-updated.

    Note:
        The `id` attribute uses the `cuid.cuid` function to generate a unique identifier.
        The `created_at` and `updated_at` attributes use the `datetime.utcnow` function to generate timestamps.
        The `updated_at` attribute is also updated every time the instance is updated.
    """

    __abstract__ = True
    metadata: sa.MetaData = sa.MetaData(naming_convention=db_naming_convention)  # type: ignore

    id: so.Mapped[str] = so.mapped_column(nullable=False, default=uuid6.uuid7, primary_key=True)
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        default=datetime.utcnow,
        # server_default=func.now(),
    )
    updated_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime(timezone=False),
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        # server_default=func.now(),
        # server_onupdate=func.now(),
    )
