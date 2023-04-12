#!/usr/bin env sh
hour=240
DB="django"
SourceFile="ctable.sql"

mysql() {
  mycli -h mysql --local-infile=1 -u root -p hsieH708! "$@"
  # mycli -u root -p hsieH708! "$@"
  # mysql -h mysql -u root "$@"
  # mysql -h 127.0.0.1 -u root "$@"
  # python manage.py dbshell --no-local=False
  # python manage.py dbshell
}

mysql <<EOF
# create database $DB; 
EOF

# generate table
mysql $DB < $SourceFile

# insert data
mysql $DB < load_data.sql

