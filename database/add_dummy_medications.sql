INSERT INTO patient_medications
(
	user_id,
	medication_name,
	medication_dose
)
VALUES
('5ea3772a1cc1ac0c1463d467', 'Yellows', '10mg twice daily'),
('5ea3772a1cc1ac0c1463d467', 'Oranges', '200mg once daily'),
('5ea3772a1cc1ac0c1463d467', 'Purples', 'idk'),
('5ea3772a1cc1ac0c1463d467', 'Blues', 'all of them')
ON CONFLICT ON CONSTRAINT patient_medications_pkey
DO NOTHING;