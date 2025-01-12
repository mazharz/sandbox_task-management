"""database queries"""

INSERT_USER = """
INSERT INTO users (name, email, pass_hash, salt)
VALUES ('%s', '%s', '%s', '%s') 
RETURNING *;
"""

FIND_USER = """
SELECT * FROM users
WHERE email = '%s';
"""

INSERT_VERIFICATION_TOKEN = """
INSERT INTO tokens (owner_id, value, expires_at)
VALUES ('%s', '%s', '%s');
"""

FIND_VERIFICATION_TOKEN = """
SELECT * FROM tokens
INNER JOIN users
    ON users.id = tokens.owner_id
WHERE
    users.email = '%s'
    AND
    expires_at > (now() at time zone 'utc');
"""

VERIFY_USER = """
UPDATE users
SET is_verified = true
WHERE id = '%s';
"""
