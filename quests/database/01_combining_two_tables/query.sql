SELECT 
    Person.firstName,
    Person.lastName,
    Address.city,
    Address.state

FROM Person 

LEFT JOIN Address -- Left Join keeps original table even if there is no match with address
    ON Address.personId = Person.personId;
