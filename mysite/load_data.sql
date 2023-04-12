-- SET GLOBAL local_infile=1
LOAD DATA LOCAL INFILE 'KPI_deg_table_combine_mads_and_other_genes.txt'
INTO TABLE DegradomeResult
-- ignore first and second line
LINES TERMINATED BY '\n'
IGNORE 1 LINES
