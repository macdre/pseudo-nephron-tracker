CREATE TABLE patient_vital_history
(
	user_id TEXT,
	entry_date DATE,
	systolic_pressure INTEGER,
	diastolic_pressure INTEGER,
	weight_in_kg REAL,	
	initial_drain INTEGER,
	total_uf INTEGER,
	average_dwell TEXT,
	added_lost_dwell_type TEXT,
	added_lost_dwell_value TEXT,
	drain_color TEXT,
	drain_clarity TEXT,
	fibrin_present TEXT,
	exit_color TEXT,
	exit_sensitivity TEXT,
	exit_condition TEXT,
	bowel_obs TEXT,
	treatment_problems TEXT,
	comments TEXT,
	PRIMARY KEY (user_id, entry_date)
);