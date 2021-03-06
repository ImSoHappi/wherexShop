CREATE TABLE IF NOT EXISTS company (
  id SERIAL PRIMARY KEY,
  NAME VARCHAR(100) NOT NULL,
  STATE CHAR DEFAULT '1'
);

CREATE TABLE IF NOT EXISTS person (
  ID SERIAL PRIMARY KEY,
  NAME VARCHAR(100) NOT NULL,
  STATE CHAR DEFAULT '1',
  COMPANY_ID INT REFERENCES company(id) NOT NULL
);

CREATE TABLE IF NOT EXISTS car (
  id SERIAL PRIMARY KEY,
  TYPE INT NOT NULL,
  DESCRIPTION VARCHAR(150),
  PERSON_ID INT REFERENCES person(id)
);
 
INSERT INTO company(name, state)
VALUES('Starken', DEFAULT), ('Chilexpress', DEFAULT), ('MercadoEnvios', '0');

INSERT INTO person(company_id, name, state)
VALUES(1, 'Pedro', '0'), (1, 'Juan', DEFAULT), 
		  (2, 'Marcos', DEFAULT), (2, 'Francisca', DEFAULT), 
		  (3, 'Tomas', '0'), (3, 'Alejandro', DEFAULT);

insert into car(TYPE, DESCRIPTION, PERSON_ID)
VALUES
(1, 'Furgon nuevo', 1),
(1, 'Camioneta usada', 1), 
(2, 'Sin comentarios', 3), 
(3, 'automovil', NULL)
;

/* REQUERIMIENTO 1 */
SELECT person.id, person.name, person.state, person.company_id, car.id AS car_id, car.type AS car_type  
FROM person INNER JOIN car ON (person.id = car.person_id)
WHERE car.type = '1'
;

/* REQUERIMIENTO 2 */
SELECT company.name AS company_name, person.name AS person_name, car.description AS car_description, car.type AS car_type 
FROM company
	FULL OUTER JOIN person ON (company.id = person.company_id)
  FULL OUTER JOIN car ON (person.id = car.person_id)
;
	
/* REQUERIMIENTO 3 */
SELECT person.id, person.name, person.state, company.id AS company_id
FROM person INNER JOIN company ON (company.id = person.company_id)
WHERE person.state = '1' AND company.id = 3
;

/* REQUERIMIENTO 4 */
SELECT person.id, person.name, person.state
FROM person
;

/* REQUERIMIENTO 5 */
SELECT company.id AS company_id, person.id AS person_id, person.name AS person_name, person.state as person_state, car.id AS car_id 
FROM company
	FULL OUTER JOIN person ON (company.id = person.company_id)
  LEFT OUTER JOIN car ON (person.id = car.person_id)
ORDER BY company.id, person.name
;

/* REQUERIMIENTO 6 */
SELECT company.name AS company_name, person.name as person_name, car.description AS car_description 
FROM company
	FULL OUTER JOIN person ON (company.id = person.company_id)
  FULL OUTER JOIN car ON (person.id = car.person_id)
;