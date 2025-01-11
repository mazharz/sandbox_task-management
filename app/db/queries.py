"""database queries"""

INSERT_USER = """
INSERT INTO users (name, email, pass_hash, salt)
VALUES ('%s', '%s', '%s', '%s') 
RETURNING *;
"""

FIND_USER = """
SELECT * FROM users WHERE email = '%s';
"""
