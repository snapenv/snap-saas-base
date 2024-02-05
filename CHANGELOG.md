## v0.7.5 (2024-02-05)

### fix

- delete org with member relationship
- delete org with member relationship

### 📝💡 Documentation

- **README.md**: update instructions for commit and version bump using cz_gitmoji

## v0.7.4 (2024-02-01)

### 🐛🚑️ Fixes

- **workspace.py**: convert uuid6.uuid7() to string for id generation in Workspace, WorkspaceMember, WorkspaceKv to avoid type errors ✨ feat(workspace.py): add WorkspaceApiKey and WorkspaceMetric models to support API key management and workspace metrics tracking
- **user.py**: convert uuid6.uuid7() to string to avoid type mismatch issues

### ci

- **deps**: bump actions/checkout from 3 to 4
- **deps**: bump actions/checkout from 3 to 4

### 📝💡 Documentation

- docs updated
- **README.md**: clarify package installation instructions and add new tool installation guides

### 🙈 Ignore

- **,gitignore**: add poetry.lock to .gitignore to prevent version conflicts

## v0.7.3 (2023-09-02)

### ✨ Features

- **model**: change fiel hashed_password to password in model User

## v0.7.2 (2023-09-02)

### ✨ Features

- **models**: add is_premium field to User model

## v0.7.1 (2023-08-31)

### 📝💡 Documentation

- update version

### 🔐🚧📈✏️ 💩👽️🍻💬🥚🌱🚩🥅🩺 Others

- **models**: change User model to allow optional hanshed-password field

## v0.7.0 (2023-08-31)

### ✨ Features

- **schemas**: add User schema

### 📌➕⬇️ ➖⬆️  Dependencies

- upgrade packages
- upgrade Pydantic to version 2 and add some other packages

### 🗃️ Database

- **models**: remove is_premiun field

### 🚨 Linting

- fix lint errors

## v0.6.0 (2023-08-31)

### ✨ Features

- **schemas**: add User schema

### feat

- **uuid7**: change UUID generator from cuid to UUID7

### 📌➕⬇️ ➖⬆️  Dependencies

- upgrade packages
- upgrade Pydantic to version 2 and add some other packages

### 🗃️ Database

- **models**: remove is_premiun field

### 🚨 Linting

- fix lint errors

## v0.5.0 (2023-07-21)

## v0.4.1 (2023-07-15)

### Fix

- correct sqla models

## v0.4.0 (2023-07-15)

## v0.3.0 (2023-07-15)

## v0.2.0 (2023-07-15)

## v0.1.0 (2023-07-08)

### Feat

- add User model
- first commit

### Refactor

- remove server side default from base model
