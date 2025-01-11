# Task management

## To-do

- [x] add proof of concept endpoints
- [ ] add authentication
  - [ ] signup
    - [x] store user
    - [x] store password with bcrypt
      - [x] create salt per user
    - [ ] generate ott
    - [ ] verify by ott
    - [ ] return generated jwt access token for accessing routes
  - [ ] add input validation
  - [ ] login
    - [x] MVP
    - [ ] generate jwt access token and send back
  - [ ] protect all routes except the signup/login with Bearer token
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

| id  | owner_id               | token |
| --- | ---------------------- | ----- |
|     | user owning auth token |       |
