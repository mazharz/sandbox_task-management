drop table if exists tasks;
drop table if exists tokens;
drop table if exists users;

create table tasks (name varchar(255));

create table users (
  id serial primary key,
  name varchar(100) not null,
  email varchar(200) not null unique,
  pass_hash varchar(100) not null,
  salt varchar(100) not null,
  is_verified boolean not null default false,
  permissions varchar(2) not null default 'rw', -- also r for readonly
  created_at timestamp not null default CURRENT_TIMESTAMP
);

create table tokens (
  id serial primary key,
  owner_id int references users (id),
  value varchar(50) not null,
  expires_at timestamp with time zone not null
);
