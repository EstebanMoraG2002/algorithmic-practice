-- 0180 Consecutive Numbers

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        LEAD(num, 1) OVER (ORDER BY id) AS next_num_1,
        LEAD(num, 2) OVER (ORDER BY id) AS next_num_2
    FROM Logs
) AS t
WHERE num = next_num_1
  AND num = next_num_2;
