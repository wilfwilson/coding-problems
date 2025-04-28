SELECT Person.firstName, Person.lastName, address.city, address.state
FROM Person person
LEFT JOIN Address address ON address.personID = person.personID;
