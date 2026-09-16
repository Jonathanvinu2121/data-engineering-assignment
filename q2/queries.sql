-- Q2.1
-- Count taxonomy entries whose species name starts with Acacia.

SELECT COUNT(*) AS acacia_count
FROM taxonomy
WHERE species LIKE 'Acacia%';


-- Q2.2
-- Find the wheat type with the longest DNA sequence.

SELECT
    t.species,
    MAX(r.length) AS longest_sequence
FROM taxonomy t
JOIN rfamseq r
    ON t.ncbi_id = r.ncbi_id
WHERE t.species LIKE 'Triticum%'
  AND r.mol_type IN ('DNA', 'genomic DNA')
GROUP BY t.ncbi_id, t.species
ORDER BY longest_sequence DESC
LIMIT 1;


-- Q2.3
-- Return page 9 with 15 families per page.
-- Only families whose longest DNA sequence is greater than 1,000,000.

SELECT
    f.rfam_acc AS family_accession,
    f.rfam_id AS family_name,
    MAX(r.length) AS max_sequence_length
FROM family f
JOIN full_region fr
    ON f.rfam_acc = fr.rfam_acc
JOIN rfamseq r
    ON fr.rfamseq_acc = r.rfamseq_acc
WHERE r.mol_type IN ('DNA', 'genomic DNA')
GROUP BY f.rfam_acc, f.rfam_id
HAVING MAX(r.length) > 1000000
ORDER BY max_sequence_length DESC, f.rfam_acc ASC
LIMIT 15 OFFSET 120;

