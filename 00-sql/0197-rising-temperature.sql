-- 0197 Rising Temperature

SELECT w1.id AS Id
FROM Weather AS w1
JOIN Weather AS w2
    ON w1.recordDate = w2.recordDate + INTERVAL '1 day'
WHERE w1.temperature > w2.temperature;
