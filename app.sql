drop table if exists fatalities;
create table fatalities (
	id serial,
	patient_name text,
	date_of_event date,
	age integer,
	citizenship text,
	event_location text,
	event_location_district text,
	event_location_region text,
	date_of_death date
	gender text
	type_of_injury text
);

insert into fatalities (patient_name, date_of_event, age, citizenship, event_location, event_location_district, event_location_region, date_of_death, gender, type_of_injury) 
values
	('Abd a-Rahman Suleiman Muhammad Abu Daghash', '2023-09-24', '32', 'Palestinian','Nur Shams R.C.', 'Tulkarm','West Bank', '2023-09-24','male','gunfire'),
	('Usayed Farhan Muhammad Ali Abu Ali', '2023-09-24', '21', 'Palestinian','Nur Shams R.C.', 'Tulkarm', 'West Bank', '2023-09-24','male','gunfire'),
	('Abdallah Imad Saed Abu Hassan', '2023-09-22', '16', 'Palestinian', 'Kfar Dan', 'Jenin', 'West Bank', '2023-09-22','male','gunfire'),
	('Durgham Muhammad Yihya al-Akhras', '2023-09-20', '19', 'Palestinian', 'Aqbat Jaber R.C.', 'Jericho', 'West Bank', '2023-09-20','male','gunfire'),
	('Rafaat Omar Ahmad Khamaisah', '2023-09-19', '15', 'Palestinian', 'Jenin R.C.', 'Jenin', 'West Bank', '2032-09-19','male','gunfire'),
	('Ata Yaseer Ata Musa', '2023-09-19', '29', 'Palestinian', 'Jenin R.C.', 'Jenin', 'West Bank', '2023-09-20','male','gunfire'),
	('Yusef Salem Yusef Radwan', '2023-09-19', '24', 'Palestinian', 'Gaza City', 'Gaza', 'Gaza Strip', '2023-09-19','male','gunfire'),
	('Mahmoud Khaled Sud Ararawi', '2023-09-19', '25', 'Palestinian', 'Jenin R.C.', 'Jenin', 'West Bank', '2023-09-19','male','gunfire'),
	('Mahmoud Ali Nafea a-Sadi', '2023-09-19', '23', 'Palestinian', 'Jenin R.C.', 'Jenin', 'West Bank', '2023-09-19','male','gunfire'),
	('Milad Munzer Waji a-Rai', '2023-09-09', '15', 'Palestinian', 'al-Arrub R.C.', 'Hebron', 'West Bank', '2023-09-09','male','gunfire')
	;