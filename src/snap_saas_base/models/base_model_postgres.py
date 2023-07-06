from datetime import datetime

import cuid
import sqlalchemy as sa
import sqlalchemy.orm as so

db_naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_N_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_N_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# https://blog.miguelgrinberg.com/post/what-s-new-in-sqlalchemy-2-0


# class AbstractModel(Base):
class AbstractModel(so.DeclarativeBase):
    """Base Models.

    Args:
        Base (_type_): Inherits Base from SQLAlchemy and specifies columns for inheritance.
    """

    __abstract__ = True
    # metadata: sa.MetaData = sa.MetaData(naming_convention=db_naming_convention)
    metadata: sa.MetaData = sa.MetaData(naming_convention=db_naming_convention)  # type: ignore

    id: so.Mapped[str] = so.mapped_column(nullable=False, default=cuid.cuid, primary_key=True)
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
