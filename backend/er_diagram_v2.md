# ER Diagram

See the ER diagram in: [Database Diagram](https://databasediagram.com/app)

```dbml
Table users {
  user_uuid uuid [primary key]
  id integer [unique]
  email text [unique]
  name varchar
  password text
}

Table user_settings { 
   id integer [primary key]
   user_uuid uuid [unique, foreign key, ref: > users.user_uuid]
   notifications_allowed bool
   user_subscription bool
   night_mode bool
}

Table tag {
  id integer [primary key]
  user_uuid uuid [foreign key, ref: > users.user_uuid]
  name_tag text
}

Table tasks {
  id integer [primary key]
  user_uuid uuid [foreign key, ref: > users.user_uuid]
  name text
  description text
  tag_id integer [foreign key, ref: > tag.id]
  state integer
  priority bool
  start_date timestamp
  end_date timestamp
  created_at timestamp
  modified_at timestamp
}

Table comments {
  id integer [primary key]
  task_id integer [foreign key, ref: > tasks.id]
  user_uuid uuid [foreign key, ref: > users.user_uuid]
  comment text
  created_at timestamp
}

Ref: users.user_uuid < tag.user_uuid // many-to-one

Ref: users.user_uuid < tasks.user_uuid // many-to-one

Ref: tag.id < tasks.tag_id // many-to-one

Ref: tasks.id < comments.task_id // many-to-one

Ref: users.user_uuid < comments.user_uuid // many-to-one

Ref: users.user_uuid - user_settings.user_uuid // one-to-one

Ref: users.user_uuid < comments.user_uuid // many-to-one

Ref: users.user_uuid - user_settings.user_uuid // one-to-one
```