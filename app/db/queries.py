INSERT_USER = """
INSERT INTO users (name, email, pass_hash)
VALUES (%s, %s, %s) 
RETURNING *;
"""
