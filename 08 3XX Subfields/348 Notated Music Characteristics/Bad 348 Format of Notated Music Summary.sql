--
-- Bad 348 Format of Notated Music Summary
--
--
-- Bad 348 $2 Source Code Summary
--
SELECT
	s.content AS "Content",
	COUNT (s.content) AS "Count"
FROM
	sierra_view.record_metadata r
	JOIN sierra_view.subfield s ON s.record_id = r.id
		AND s.marc_tag = '348'
		AND s.tag = '2'
WHERE
	r.record_type_code = 'b'
	AND s.content NOT IN (
		'rda',
		'rdafnm')
GROUP BY s.content
UNION
--
-- Bad 348 $a Format of Notated Music Summary
--
SELECT
	s.content AS "Content",
	COUNT (s.content) AS "Count"
FROM
	sierra_view.record_metadata r
	JOIN sierra_view.subfield s ON s.record_id = r.id
		AND s.marc_tag = '348'
		AND s.tag = 'a'
WHERE
	r.record_type_code = 'b'
	AND s.content NOT IN (
		'choir book',
		'chorus score',
		'condensed score',
		'part',
		'piano conductor part',
		'piano score',
		'score',
		'study score',
		'table book',
		'violin conductor part',
		'vocal score')
GROUP BY s.content
UNION
--
-- Bad 348 $b Format of Notated Music Code Summary
--
SELECT
	s.content AS "Content",
	COUNT (s.content) AS "Count"
FROM
	sierra_view.record_metadata r
	JOIN sierra_view.subfield s ON s.record_id = r.id
		AND s.marc_tag = '348'
		AND s.tag = 'b'
WHERE
	r.record_type_code = 'b'
--	AND s.content NOT IN ('')
GROUP BY s.content;