-- 16-glam_rock.sql
-- List Glam rock bands by lifespan
SELECT band_name,
IF(split IS NULL, 2020 - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
