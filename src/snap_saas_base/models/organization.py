import sqlalchemy as sa
import sqlalchemy.orm as so


from snap_saas_base.models.base_model_postgres import AbstractModel

# https://github.com/sqlalchemy/sqlalchemy/discussions/6165


class Organization(AbstractModel):
    __tablename__ = "organizations"

    name: so.Mapped[str] = so.mapped_column(nullable=False)
    slug: so.Mapped[str] = so.mapped_column(nullable=False, unique=True)
    bucket: so.Mapped[str] = so.mapped_column(nullable=False)
    created_by: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id", ondelete="RESTRICT"), nullable=False
    )
    revoke_link: so.Mapped[bool] = so.mapped_column(default=False, server_default=sa.text("false"))
    org_member: so.WriteOnlyMapped["OrgMember"] = so.relationship(
        back_populates="org", cascade="all, delete-orphan"
    )
    # org_workspaces: so.WriteOnlyMapped["Workspace"] = so.relationship(back_populates="org", cascade="all, delete-orphan")

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class OrgMember(AbstractModel):
    __tablename__ = "organizations_members"

    org_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False
    )
    member_id: so.Mapped[str] = so.mapped_column(
        sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role: so.Mapped[str] = so.mapped_column(nullable=False)
    # member: so.Mapped["User"] = so.relationship(back_populates="org_member")
    org: so.Mapped["Organization"] = so.relationship(back_populates="org_member")

    __table_args__ = (
        sa.Index("ix_organizations_members_org_id_member_id_role", "org_id", "member_id", "role"),
    )

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
