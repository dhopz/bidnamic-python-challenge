from ..common.base import session

# Create the view with the appropriate metrics
query = """
CREATE OR REPLACE VIEW as insight_structure_value AS
SELECT DISTINCT structure_value, 
    search_term,
    SUM(cost) AS total_cost, 
    SUM(conversion_value) AS total_conversion_value,
    (SUM(conversion_value)/SUM(cost))::numeric(10,2) AS roas
FROM campaigns
INNER JOIN search_terms_all ON campaigns.campaign_id = search_terms_all.campaign_id
WHERE conversion_value > 1
GROUP BY structure_value,search_term
ORDER BY total_cost DESC
LIMIT 10;
"""

# Execute and commit
session.execute(query)
session.commit()