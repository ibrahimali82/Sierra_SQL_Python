import psycopg2
import csv
from postgresql_password import postgresql_password

report = 'I:/SQL Queries/Code verification working files/10_3-IllegalAlienSummary.csv'

query = """
SELECT
	v.marc_tag AS "Field",
	v.field_content AS "Value",
	COUNT (v.marc_tag) AS "Count"
FROM
	sierra_view.varfield v
	JOIN sierra_view.record_metadata r ON r.id = v.record_id
		AND r.record_type_code = 'b'
	JOIN sierra_view.bib_record b ON b.record_id = v.record_id
		AND b.bcode3 = '-'
WHERE
	v.marc_tag = '650'
	AND v.field_content SIMILAR TO '%[Ii]llegal alien%'
GROUP BY v.marc_tag, v.field_content
--ORDER BY v.marc_tag ASC;
--ORDER BY v.field_content ASC;
ORDER BY COUNT (v.marc_tag) DESC;
    """

conn = psycopg2.connect(host="sierra-db.library.unt.edu", port="1032", database="iii", user="swolf", password=postgresql_password)

cur = conn.cursor()
cur.execute(query)

report_data = cur.fetchall()

with open(report, 'w', newline='') as csvfile:
    rd = csv.writer(csvfile)
  #  rd.writerow(['Record Number', 'Field Tag', 'MARC Tag', 'Content'])
    for row in report_data:
        rd.writerow(row)

print('csv file generation complete')

