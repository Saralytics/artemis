CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    description VARCHAR(300) NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    currency CHAR(3) NOT NULL,
    country_restrictions TEXT,
    expiry_date TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

drop table if exists users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    country CHAR(2) NOT NULL,
    mobileoperator VARCHAR(200),
    email VARCHAR(200),
    firstname VARCHAR(200),
    lastname VARCHAR(200),
    mobile_country_code VARCHAR(5),
    mobile_number INT,
    registration_date TIMESTAMP NOT NULL,
    device_id VARCHAR(300),
    language CHAR(2),
    plan_id INT NOT NULL REFERENCES plans(id),
    last_login_date TIMESTAMP,
    last_played_date TIMESTAMP,
    created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (email, mobile_number)
);

CREATE TABLE sessions (
    id VARCHAR(15) PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    session_data TEXT,
    start_timestamp TIMESTAMP,
    end_timestamp TIMESTAMP
);

CREATE TABLE direct_billing (
    id SERIAL PRIMARY KEY,
    subscription_id INT NOT NULL,
    user_id INT NOT NULL REFERENCES users(id),
    payment_type_id SMALLINT NOT NULL,
    billing_startdate TIMESTAMP NOT NULL,
    billing_enddate TIMESTAMP,
    plan_id INT NOT NULL REFERENCES plans(id),
    status TEXT NOT NULL CHECK (status in ('success','failure','retry','voided','pending')),
    price_amount_local NUMERIC(10,2),
    price_currency_code CHAR(3),
    created_on TIMESTAMP NOT NULL,
    UNIQUE(subscription_id, user_id, payment_type_id, plan_id, billing_startdate, status)
);

CREATE TABLE labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    join_date TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE TABLE artist (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200),
    label_id INT REFERENCES labels(id),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);


CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    upc TEXT,
    name TEXT,
    artist_id INT REFERENCES artist(id),
    label_id INT REFERENCES labels(id),
    nbr_song SMALLINT,
    release_date TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);


CREATE TABLE user_account_history (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    country CHAR(2) NOT NULL,
    mobileoperator VARCHAR(200),
    email VARCHAR(200),
    firstname VARCHAR(200),
    lastname VARCHAR(200),
    mobile_country_code VARCHAR(5),
    mobile_number INT,
    registration_date TIMESTAMP NOT NULL,
    device_id VARCHAR(300),
    language CHAR(2),
    plan_id INT NOT NULL REFERENCES plans(id),
    last_login_date TIMESTAMP,
    last_played_date TIMESTAMP,
    created_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    isrc VARCHAR(100),
    name TEXT NOT NULL,
    album_id INT REFERENCES albums(id),
    artist_id INT NOT NULL REFERENCES artist(id),
    label_id INT NOT NULL REFERENCES labels(id),
    duration INT,
    file_location TEXT,
    country_restrictions TEXT,
    all_time_plays INT,
    status TEXT NOT NULL CHECK (status in ('active','inactive')),
    release_date TIMESTAMP NOT NULL,
    created_on TIMESTAMP,
    updated_on TIMESTAMP
);


CREATE TABLE usage (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(id),
    action TEXT NOT NULL CHECK (action in ('start', 'pause', 'skip', 'restart', 'complete')),
    songid INT NOT NULL REFERENCES songs(id),
    play_start_timestamp TIMESTAMP,
    play_end_timestamp TIMESTAMP,
    play_seconds INT NOT NULL,
    plan_id INT REFERENCES plans(id),
    usercountry CHAR(2),
    ipcountry CHAR(2),
    operatorcountry CHAR(2),
    is_ondemand BOOLEAN,
    interface TEXT CHECK(interface IN ('ios','android','web')),
    sessionid INT,
    ipaddress VARCHAR,
    rootsongid INT,
    rec_id INT,
    inserted_timestamp TIMESTAMP NOT NULL
);

