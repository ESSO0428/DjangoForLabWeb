DROP TABLE IF EXISTS `DegradomeResult`;
CREATE TABLE `DegradomeResult` (
`id` int NOT NULL PRIMARY KEY,
`DataSet` varchar(100) NOT NULL,
`Tissue` varchar(100) NOT NULL,
`Transcript_ID` varchar(100) NOT NULL,
`BLAST_ATH_protein` varchar(100) NOT NULL,
`Category` varchar(100) NOT NULL,
`Cleavage_Position` REAL NOT NULL default 0,
`miRNA_ID` varchar(100) NOT NULL,
`FM_miRNA` REAL NOT NULL default 0,
`5BL_miRNA` REAL NOT NULL default 0,
`5BP_miRNA` REAL NOT NULL default 0,
`5BS_miRNA` REAL NOT NULL default 0,
`FM_target` REAL NOT NULL default 0,
`5BL_target` REAL NOT NULL default 0,
`5BP_target` REAL NOT NULL default 0,
`5BS_target` REAL NOT NULL default 0,
`miRNA_aligned_fragment` varchar(100) NOT NULL,
`alignment` varchar(100) NOT NULL,
`Target_aligned_fragment` varchar(100) NOT NULL,
`Target_Desc` varchar(5000) NOT NULL
) ;
