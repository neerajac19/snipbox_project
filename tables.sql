-- User table (Django default model, included here for reference)
CREATE TABLE auth_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password VARCHAR(128),
    last_login DATETIME NULL,
    is_superuser BOOLEAN NOT NULL,
    username VARCHAR(150) UNIQUE NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL
);

-- Tag table
CREATE TABLE snipboxapp_tag (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) UNIQUE NOT NULL
);

-- Snipbox table
CREATE TABLE snipboxapp_snipbox (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    note TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user (id)
);

-- Many-to-Many relationship between Snipbox and Tag
CREATE TABLE snipboxapp_snipbox_tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    snipbox_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (snipbox_id) REFERENCES snipboxapp_snipbox (id),
    FOREIGN KEY (tag_id) REFERENCES snipboxapp_tag (id),
    UNIQUE (snipbox_id, tag_id)
);
