-- Keep a log of any SQL queries you execute as you solve the mystery.

-- I want to analtyze crime_scene_reports
SELECT description FROM crime_scene_reports
WHERE
year ='2021' AND
month ='7' AND
day = '28' AND
street = 'Humphrey Street';

-- Informations of transcript :
-- 1) Thef at 10:15 am.
--2) Place Humphrey Street bakery
--IDEA is to use the information of transcript.

SELECT activity , license_plate , id FROM bakery_security_logs
WHERE
year ='2021' AND
month ='7' AND
day = '28' AND
hour = '10' AND
minute = '15';

-- I want to have id of suspects and so persons that enter and exit from bakery near 10:15 am
SELECT * FROM bakery_security_logs
WHERE
year ='2021' AND
month ='7' AND
day = '28';

-- id suspects :
-- 1) 260 exit 10:16 am
-- 2) 261 exit 10:18 am SUSPECT less the 60 second call licence 94KL13X
-- 3) 262 exit at 10:18 am
-- 4) 263 exit at 10:19 am
--5) 264 10:20
-- 6) 265 10:21
-- 7) 266 10:23
-- 8) 267 10:23



--I can analyze the call of this persons
SELECT * FROM phone_calls
WHERE
caller = "(367) 555-5533" ;

-- helper phone should be (375) 555-8161

-- Call durations :
-- 1) 260: 67
-- 2) 261: 38 SUSPECT (during fly you cannot use phone,and after stolen something yoiu have to go fast) || Interwiever said less then a minutes of call. NO
--IMPORTANT caller (031) 555-6622 and receiver (910) 555-3251
--3) 262 : 404
-- 4) 263: 560


-- I want to see wich of these people where interwie, because if one of them is thief, he has to go fast at airport
SELECT * FROM interviews
WHERE
interviews.year ='2021' AND
interviews.month ='7' AND
interviews.day = '28';
-- Thief speaks less the a minute at phone (261 done it) and he will take the first fly the next days out from city. 261 OK
-- Thief witdraw any money from atm beafor the intewiever id 162 arrived in bakery. 261 OK 20 punds withdraw
-- After exit 10 minutes from go away with car from parking
-- First fly the next days


SELECT * FROM atm_transactions
WHERE id = '267';
-- I checked and ther's a transaction in these day from 261 ,262 ,263,264,265,266,267

SELECT * FROM flights
--JOIN airports ON airports.id = flights.origin_airport_id
JOIN airports ON airports.id = flights.destination_airport_id
JOIN passengers ON passengers.flight_id = flights.id
WHERE
year ='2021' AND
month ='7' AND
day = '29' AND
hour = '8';
-- He escaped at New York

-- I'm tryng to add people tab at the previous ones
SELECT * FROM flights
--JOIN airports ON airports.id = flights.origin_airport_id
JOIN airports ON airports.id = flights.destination_airport_id
JOIN passengers ON passengers.flight_id = flights.id
WHERE
year ='2021' AND
month ='7' AND
day = '29' AND
hour = '8';


--IMPORTANT caller (031) 555-6622 and receiver (910) 555-3251
SELECT * FROM people
WHERE
phone_number = "(375) 555-8161";
--license_plate = "94KL13X";



--NOT Because she is not in aircraft
-- thief: Carina passport 9628244268 AND license_plate Q12B3Z3
-- helper : Jacqueline
--Thei are not Carol was not on flight
----Beverly no beacause she license-plate NULL
--Alexander passport NUll
--Britnay passport NULL
-- John passport 8174538026 license 4468KVT No on fly
-- Patricia passport 5806941094 license R0590D5 NO on fly
-- .......... i hve to try using licence, because maybe id of phone is not coincident
-- licence found  94KL13X SUSPECT -- > suspect Bruce phone (367) 555-5533 passaport 5773159633 is on fly, helper phone number Robin

-- Second suspicius
--(669) 555-6918
--(971) 555-6468 helper


-- hold ideas NOT Working
--SELECT people.name FROM people
--JOIN phone_calls ON people.id = phone_calls.id
--WHERE
--phone_calls.id = '260';












































-- I want to understand that
SELECT name , transcript FROM interviews
JOIN bakery_security_logs ON interviews.id = bakery_security_logs.id
WHERE
bakery_security_logs.year ='2021' AND
bakery_security_logs.month ='7' AND
bakery_security_logs.day = '28' AND
bakery_security_logs.hour = '10' AND
bakery_security_logs.minute = '15';
