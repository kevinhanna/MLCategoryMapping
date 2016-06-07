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
AND (JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["health'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["homeservices'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["hotelstravel'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["massmedia'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["nightlife'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["pets'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["professional'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["publicservicesgovt'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["realestate'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["religiousorgs'
  OR JSON_EXTRACT(raw_data, "$.tax_ids") CONTAINS '["restaurants'
  )

LIMIT 15000