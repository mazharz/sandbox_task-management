# Task management

## To-do

- [x] add proof of concept endpoints
- [ ] add authentication
  - [ ] signup
  - [ ] store password with bcrypt
  - [ ] login
  - [ ] generate jwt token for accessing routes
  - [ ] protect all routes but the signup/login with Bearer token
- [ ] implement role based access control (normal & readonly users)
  - [ ] per task configurable
- [ ] task CRUD endpoints

## data model

user:

| id  | username | name | email | pass_hash | role | created_at |
| --- | -------- | ---- | ----- | --------- | ---- | ---------- |

task:

| id  | title | description | status | priority | asignee | created_at |
| --- | ----- | ----------- | ------ | -------- | ------- | ---------- |

token:

| id  | owner_id               | token |
| --- | ---------------------- | ----- |
|     | user owning auth token |       |
