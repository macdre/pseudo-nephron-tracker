CREATE TABLE patient_vital_history
(
	user_id TEXT,
	entry_date DATE,
	systolic_pressure INTEGER,
	diastolic_pressure INTEGER,
	weight_in_kg REAL,	
	PRIMARY KEY (user_id, entry_date)
);