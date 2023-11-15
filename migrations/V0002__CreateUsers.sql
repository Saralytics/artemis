create table users (
  id serial primary key not null,
  country char(2) not null,
  mobileoperator varchar(200),
  mobile_number integer,
  mobile_country_code varchar(5),
  email varchar(200),
  firstname varchar(200),
  lastname varchar(200),
  registraion_date timestamp,
  device_id varchar(300),
  status_code smallint not null CHECK (status_code IN (0, 1, 2)),
  language char(2),
  plan_id integer not null,
  created_at timestamp default current_timestamp,
  updated_at timestamp  default current_timestamp
);