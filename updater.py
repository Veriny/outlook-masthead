import csv

f = open("GeneratedCode.txt", "a")

with open ('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        uName = row[0]
        cupp_upload_meta = row[2]
        f.write('<td><a href="http://aragonoutlook.org/author/{}"><img class="aligncenter" src="{}" width="200" height="200" /></a></td>'.format(uName, cupp_upload_meta) + '\n')

f.close()
