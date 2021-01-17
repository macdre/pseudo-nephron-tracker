INSERT INTO enrolled_patients
(
	user_id,
	enrolled_date
)
VALUES
('5ea3772a1cc1ac0c1463d467', '2020-06-01')
ON CONFLICT ON CONSTRAINT enrolled_patients_pkey
DO NOTHING;