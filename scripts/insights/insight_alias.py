from ..common.base import session

# Create the view with the appropriate metrics
query = """
CREATE OR REPLACE VIEW insight_alias AS
SELECT DISTINCT alias, 
    search_term,
    SUM(cost) AS total_cost, 
    SUM(conversion_value) AS total_conversion_value,
    (SUM(conversion_value)/SUM(cost))::numeric(10,2) AS roas
FROM adgroups
INNER JOIN search_terms_all ON adgroups.ad_group_id = search_terms_all.ad_group_id
WHERE conversion_value > 1
GROUP BY alias,search_term
ORDER BY total_cost DESC
LIMIT 10;
"""

# Execute and commit
session.execute(query)
session.commit()