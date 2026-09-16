# Q2 - SQL and Databases

## Overview

This section contains SQL queries for the Rfam database questions in the
Data Engineer assignment.

The queries were tested against the public Rfam MySQL database.

## Database Connection

```text
Host: mysql-rfam-public.ebi.ac.uk
Port: 4497
Database: Rfam
User: rfamro
```

No password is required for the public read-only Rfam database.

## Tables Used

- `taxonomy`
- `rfamseq`
- `family`
- `full_region`

### Table Relationships

```text
taxonomy.ncbi_id -> rfamseq.ncbi_id

family.rfam_acc -> full_region.rfam_acc

full_region.rfamseq_acc -> rfamseq.rfamseq_acc
```

---

## Q2.1 - Acacia Plants

### Requirement

Find how many types of Acacia plants can be found in the taxonomy table.

### Approach

The query counts taxonomy entries whose species name starts with `Acacia`.

### Query

```sql
SELECT COUNT(*) AS acacia_count
FROM taxonomy
WHERE species LIKE 'Acacia%';
```

### Result

```text
326
```

This represents 326 entries in the `taxonomy` table whose `species` value
starts with `Acacia`.

---

## Q2.2 - Longest Wheat DNA Sequence

### Requirement

Find the type of wheat with the longest DNA sequence.

### Approach

The `taxonomy` and `rfamseq` tables are joined using `ncbi_id`.

The taxonomy table contains several records related to wheat. For this query,
the wheat plant records are identified using the `Triticum` genus.

Only DNA sequence types are considered:

- `DNA`
- `genomic DNA`

The maximum sequence length is then calculated for each wheat type.

### Query

```sql
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
```

### Result

```text
Triticum durum (durum wheat) | 836514780
```

The longest DNA sequence found for the matching wheat records is
`836,514,780` bases.

---

## Q2.3 / Q2.4 - Paginated Family Results

### Requirement

Return the 9th page of Rfam families where the longest DNA sequence is
greater than 1,000,000.

The results must:

- Include only families whose longest DNA sequence is greater than 1,000,000.
- Be sorted by DNA sequence length in descending order.
- Return the family accession ID.
- Return the family name.
- Return the maximum sequence length.
- Return page 9.
- Return 15 results per page.

### Approach

The three relevant tables are joined through `full_region`:

```text
family
   |
   | rfam_acc
   v
full_region
   |
   | rfamseq_acc
   v
rfamseq
```

For each family, `MAX(r.length)` is used to find its longest associated DNA
sequence.

`HAVING` is used because the filtering condition is applied to the aggregated
maximum sequence length.

### Pagination

For page 9 with 15 results per page:

```text
OFFSET = (page - 1) * results_per_page
       = (9 - 1) * 15
       = 120
```

Therefore:

```sql
LIMIT 15 OFFSET 120
```

### Query

```sql
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
```

The secondary sort by `f.rfam_acc ASC` provides deterministic ordering when
multiple families have the same maximum sequence length.

### Result

```text
RF01219  | snoR100       | 836514780
RF01220  | snoR104       | 836514780
RF01224  | snoR80        | 836514780
RF01227  | snoR83        | 836514780
RF01284  | snoR8a        | 836514780
RF01286  | snoR26        | 836514780
RF01292  | snoR2         | 836514780
RF01300  | snoU49        | 836514780
RF01847  | Plant_U3      | 836514780
RF01848  | ACEA_U3       | 836514780
RF01856  | Protozoa_SRP  | 836514780
RF01911  | MIR2118       | 836514780
RF03160  | twister-P1    | 836514780
RF03209  | MIR9657       | 836514780
RF03674  | MIR5387       | 836514780
```

> Note: Queries involving aggregation across the public Rfam tables can take
> several minutes to execute.

---

## Files

```text
q2/
├── queries.sql
└── README.md
```

`queries.sql` contains the SQL queries used to answer all questions in this
section.
