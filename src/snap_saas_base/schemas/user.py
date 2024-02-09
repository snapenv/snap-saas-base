"""User schema."""

from datetime import datetime

# from operator import le
from pydantic import BaseModel, ConfigDict, EmailStr, Field


# Schemas
class UserBaseSchema(BaseModel):
    username: str = Field(
        ...,
        title="User Login",
        description="Username used in login.",
        examples=["user@domain.com"],
    )
    provider: str = Field(
        ...,
        title="Auth provider",
        description="Authentication provider used in the registration of this user.",
        examples=["Auth0"],
    )
    email: EmailStr = Field(
        ...,
        title="Email",
        description="User email. Must be not used by another existent user.",
        examples=["user@domain.com"],
    )
    cell_phone: str = Field(
        ...,
        title="Mobile Number",
        description="Mobile phone number in full international format.",
        examples=["+5527999884321"],
    )
    full_name: str = Field(
        ...,
        title="Name",
        description="User full name.",
        examples=["John Doe"],
    )
    avatar: str | None = Field(
        ...,
        title="Avatar",
        description="User avatar picture URL.",
        examples=["John Doe"],
    )
    is_verified: bool = Field(
        False,
        title="Verified",
        description="User email verified.",
        examples=[False],
    )
    is_premium: bool = Field(
        False,
        title="Premium",
        description="User is premium.",
        examples=[False],
    )
    is_active: bool = Field(
        True,
        title="Active",
        description="User active.",
        examples=[True],
    )
    is_superuser: bool = Field(
        False,
        title="Superuser",
        description="User is super admin.",
        examples=[False],
    )

    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        # allow_population_by_alias=True,
    )


class UserInDBBaseSchema(UserBaseSchema):
    id: str = Field(
        ...,
        title="ID",
        description="Unique ID.",
        examples=["ckasokq6g0000yvxuigfa2agy"],
    )
    password: str | None = Field(
        ...,
        title="Password",
        description="User password.",
        examples=["$2b$12$7ytDry1IsxATsnVwZgLeQOTAkQIPlxCfuNXPM67HQaYSGApzsYXdi"],
    )
    created_at: datetime | None = Field(
        ...,
        title="Create At",
        description="Timestamp when this record was created.",
        examples=["2021-03-02T13:28:54.589000"],
    )
    updated_at: datetime | None = Field(
        ...,
        title="Updated At",
        description="Timestamp when this record was last updated.",
        examples=["2022-08-02T09:48:54.000000"],
    )


# Properties to receive on item creation
class UserCreateSchema(UserBaseSchema):
    password: str | None = Field(
        None,
        title="Password",
        description="Initial plain password.",
        examples=["clic9r1n9000gzqk480ghulbd"],
    )


# Properties to receive on item update
class UserUpdateSchema(UserBaseSchema):
    pass


USER_EXAMPLES_PAYLOAD = {
    "UserDefault": {
        "summary": "User create example",
        "description": "Example for user creation",
        "value": {
            "username": "johndoe",
            "full_name": "John Doe",
            "provider": "local",
            "email": "john.doe@domain.com",
            "cell_phone": "55279998812345",
            "avatar": "",
            "is_verified": True,
            "is_premium": False,
            "is_active": True,
            "is_superuser": False,
            "password": "SomeGoodPassword",
        },
    },
}
