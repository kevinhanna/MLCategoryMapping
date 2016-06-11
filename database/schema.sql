CREATE TABLE listing_history (
	account_group_id VARCHAR(11) NOT NULL, 
	listing_id VARCHAR(36) NOT NULL, 
	epoch_date DATETIME NOT NULL, 
	string_date DATE NOT NULL, 
	source_id INTEGER NOT NULL, 
	match_details_company INTEGER NOT NULL, 
	match_details_address INTEGER NOT NULL, 
	match_details_city INTEGER NOT NULL, 
	match_details_state INTEGER NOT NULL, 
	match_details_zip INTEGER NOT NULL, 
	match_details_phone INTEGER NOT NULL, 
	match_details_website INTEGER NOT NULL, 
	ag_company VARCHAR(512) NOT NULL, 
	ag_address VARCHAR(512) NOT NULL, 
	ag_city VARCHAR(200) NOT NULL, 
	ag_state VARCHAR(30) NOT NULL, 
	ag_zip VARCHAR(100) NOT NULL, 
	ag_country VARCHAR(2) NOT NULL, 
	ag_phone VARCHAR(13) NOT NULL, 
	ag_website VARCHAR(512) NOT NULL, 
	lis_name VARCHAR(512) NOT NULL, 
	lis_address VARCHAR(512) NOT NULL, 
	lis_city VARCHAR(200) NOT NULL, 
	lis_state VARCHAR(30) NOT NULL, 
	lis_zip VARCHAR(100) NOT NULL, 
	lis_country VARCHAR(64) NOT NULL, 
	lis_website VARCHAR(2000) NOT NULL, 
	lis_phone VARCHAR(185) NOT NULL, 
	lis_url VARCHAR(255) NOT NULL, 
	match_quality VARCHAR(1) NOT NULL, 
	match_score INTEGER, 
	good_listing INTEGER NOT NULL,
	listing_history_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

CREATE TABLE listing_training (
	listing_training_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	address VARCHAR(512) NOT NULL,
	tokens_pickle BLOB,
	country VARCHAR(2)
);

	