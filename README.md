# Task management

## To-do

- [x] add proof of concept endpoints
- [ ] add authentication
  - [ ] signup
    - [x] store user
    - [ ] store password with bcrypt
      - [ ] create salt per user
    - [ ] generate ott
    - [ ] verify by ott
    - [ ] return generated jwt token for accessing routes
  - [ ] add input validation
  - [ ] login
  - [ ] protect all routes except the signup/login with Bearer token
- [ ] task CRUD endpoints
- [ ] implement role based access control (normal & readonly users)
  - [ ] per task configurable

## data model

user:

| id  | name | email | pass_hash | is_verified | permissions | created_at |
| --- | ---- | ----- | --------- | ----------- | ----------- | ---------- |

task:

| id  | title | description | status | priority | asignee | created_at |
| --- | ----- | ----------- | ------ | -------- | ------- | ---------- |

token:

| id  | owner_id               | token |
| --- | ---------------------- | ----- |
|     | user owning auth token |       |
