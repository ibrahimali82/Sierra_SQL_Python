import psycopg2
import csv
from postgresql_password import postgresql_password

report = 'I:/SQL Queries/Code verification working files/9_2-BadSubjectSource.csv'

query = """
SELECT
	r.record_type_code || r.record_num || 'a' AS "Record Number",
	s.marc_ind2 AS "Indicator 2",
	s.content AS "$2 Content"
FROM
	sierra_view.subfield s
	JOIN sierra_view.record_metadata r ON r.id = s.record_id
		AND r.record_type_code = 'b'
WHERE
	s.field_type_code = 'd'
	AND s.tag = '2'
	AND (s.content NOT IN ('aat','fast','gmgpc','gsafd','gtmm','gttg','homoit','lcgft','lctgm','liv','local','migfg','mim','nasat','olacvggt','rbbin','rbgenr','rbpap','rbpri','rbprov','rbpub','rbtyp','waww (2004/05, 2006/07 only)')
	OR (s.marc_ind2 != '7'
	AND s.content IN ('aat','fast','gmgpc','gsafd','gtmm','gttg','homoit','lcgft','lctgm','liv','local','migfg','mim','nasat','olacvggt','rbbin','rbgenr','rbpap','rbpri','rbprov','rbpub','rbtyp')))
ORDER BY r.record_num ASC;
    """

conn = psycopg2.connect(host="sierra-db.library.unt.edu", port="1032", database="iii", user="swolf", password=postgresql_password)

cur = conn.cursor()
cur.execute(query)

report_data = cur.fetchall()

with open(report, 'w', newline='') as csvfile:
    rd = csv.writer(csvfile)
  #  rd.writerow(['Rec#', 'Ind2', '$2Content'])
    for row in report_data:
        rd.writerow(row)

print('csv file generation complete')

