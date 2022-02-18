from common.base import session

# Create the view with the appropriate metrics
query = """
CREATE OR REPLACE VIEW insight_alias AS
SELECT *
FROM campaigns
"""

# Execute and commit
session.execute(query)
session.commit()