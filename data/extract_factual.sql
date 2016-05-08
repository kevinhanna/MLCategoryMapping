SELECT
  JSON_EXTRACT(raw_data, "$.tax_ids") AS vtax,
  eid,
  ag.account_group_id,
  JSON_EXTRACT(raw_data, "$.website") AS website,
  JSON_EXTRACT(raw_data, "$.company_name") AS company_name
FROM [datastore.VAccountGroupModel] AS ag
JOIN [datastore.LIS] AS lis ON lis.accountGroupId=ag.account_group_id
WHERE lis.src = 11480 //Factual
AND lis.gl=2
AND JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["active'
LIMIT 1000