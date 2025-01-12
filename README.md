# Task management

## To-do

- [x] add proof of concept endpoints
- [ ] add authentication
  - [x] signup
    - [x] store user
    - [x] store password with bcrypt
      - [x] create salt per user
    - [x] verify email by ott
    - [x] jwt access token for accessing routes
  - [x] login
    - [x] MVP
    - [x] generate jwt access token and send back
  - [ ] protect all routes except the signup/login with Bearer token
- [ ] add input validation
- [ ] task CRUD endpoints
- [ ] implement role based access control (normal & readonly users)
  - [ ] per task configurable

## data model

user:

| id  | name | email | pass_hash | salt                                      | is_verified | permissions | created_at |
| --- | ---- | ----- | --------- | ----------------------------------------- | ----------- | ----------- | ---------- |
|     |      |       |           | (should be stored elsewhere in real apps) |             |             |            |

task:

| id  | title | description | status | priority | asignee | created_at |
| --- | ----- | ----------- | ------ | -------- | ------- | ---------- |

token:

| id  | owner_id               | value | expires_at |
| --- | ---------------------- | ----- | ---------- |
|     | user owning auth token |       | timestamp  |
