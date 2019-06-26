SELECT MAX(Age)
FROM User


SELECT DISTINCT userid
FROM (SELECT userid, COUNT(userid)
	FROM relationship
	WHERE Typ=marriage
	GROUP BY userid
	ORDER BY COUNT(userid) DESC
	LIMIT 1)


SELECT DISTINCT userid
FROM (SELECT userid,COUNT(Einkommen)
	FROM User
	GROUP BY userid
	ORDER BY COUNT(Einkommen) DESC
	LIMIT 1)


SELECT COUNT(userid)
FROM (SELECT dates, COUNT(userid)
	FROM relationship
	WHERE Typ=marriage
	GROUP BY userid
	HAVING COUNT(userid)>2
	ORDER BY COUNT(userid) DESC)


SELECT DISTINCT userid
FROM (SELECT userid,COUNT(userid)
	FROM isfanof 
	GROUP BY userid
	ORDER BY COUNT(userid) DESC
	LIMIT 1)


SELECT DISTINCT userid FROM User
EXCEPT
SELECT userid FROM isfanof NATURAL JOIN relationship
