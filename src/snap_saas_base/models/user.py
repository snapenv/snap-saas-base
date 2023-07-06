import sqlalchemy as sa
import sqlalchemy.orm as so

from snap_saas_base.models.base_model_postgres import AbstractModel

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class User(AbstractModel):
    # Users Table
    __tablename__ = "users"
    # __mapper_args__ = {"eager_defaults": True}
    username: so.Mapped[str] = so.mapped_column(nullable=False)
    provider: so.Mapped[str] = so.mapped_column(default="local", nullable=True)
    email: so.Mapped[str] = so.mapped_column(nullable=True)
    cell_phone: so.Mapped[str] = so.mapped_column(nullable=True, index=True)
    full_name: so.Mapped[str] = so.mapped_column(nullable=False)
    password: so.Mapped[str] = so.mapped_column(nullable=True)
    is_verified: so.Mapped[bool] = so.mapped_column(
        nullable=False, default=False, server_default=sa.text("false")
    )
    is_premium: so.Mapped[bool] = so.mapped_column(
        nullable=False, default=False, server_default=sa.text("false")
    )
    is_superuser: so.Mapped[bool] = so.mapped_column(default=False, server_default=sa.text("false"))
    phone_verified: so.Mapped[bool] = so.mapped_column(
        default=False, server_default=sa.text("false")
    )

    __table_args__ = (sa.UniqueConstraint("username", "provider"),)

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
