Table users {
  user_uuid uuid [primary key]
  id integer [unique]
  email text [unique]
  name varchar
  password text
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
  state bool
  created_at timestamp
  modified_at timestamp
}

Ref: users.user_uuid < tag.user_uuid // many-to-one

Ref: users.user_uuid < tasks.user_uuid // many-to-one

Ref: tag.id < tasks.tag_id // many-to-one