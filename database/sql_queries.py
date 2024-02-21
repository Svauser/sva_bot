CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""
INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""
CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_COUNT_QUERY = """
UPDATE ban SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""
SELECT_BAN_COUNT_QUERY = """
SELECT * FROM BAN_COUNT  WHERE TELEGRAM_ID = ?
"""