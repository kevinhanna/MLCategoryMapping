LOAD DATA LOCAL INFILE '/Users/kevinhanna/Downloads/ListingHistory-20160527_listing_history_FULL.csv' INTO TABLE listing_history FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

#ALTER TABLE `listing_history` ADD `listing_history_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE listing_history ADD training_tokens VARCHAR(255);

#CREATE INDEX ag_index ON listing_history (account_group_id);
#CREATE INDEX source_index ON listing_history (source_id);
#CREATE INDEX date_index ON listing_history (epoch_date);
#CREATE INDEX ag_source_date_index ON listing_history (account_group_id, source_id, epoch_date);