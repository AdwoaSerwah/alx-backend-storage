-- 3. Old school band
-- List all bands with Glam rock as their main style, ranked by their longevity (using 'formed' and 'split' for lifespan)

SELECT 
    band_name, 
    IFNULL(
        IF(split IS NOT NULL, (split - formed), (2022 - formed)), 
        0
    ) AS lifespan  -- Calculate lifespan based on 'split' year, or if NULL, use 2022 for current lifespan
FROM 
    metal_bands
WHERE 
    style LIKE '%Glam rock%'  -- Filter for bands where the style contains 'Glam rock'
ORDER BY 
    lifespan DESC;  -- Rank the bands by their lifespan (longest to shortest)
