-- 2. Best band ever!
-- Rank country origins of bands by the number of (non-unique) fans

SELECT 
    origin, 
    SUM(fans) AS nb_fans  -- Sum the number of fans for each origin
FROM 
    metal_bands
GROUP BY 
    origin  -- Group by country origin
ORDER BY 
    nb_fans DESC;  -- Order by the total number of fans in descending order
