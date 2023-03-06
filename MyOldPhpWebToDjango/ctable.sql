DROP TABLE IF EXISTS `app2_degradomeresult`;
CREATE TABLE `app2_degradomeresult` (
`id` int NOT NULL PRIMARY KEY,
`DataSet` varchar(100) NOT NULL,
`Tissue` varchar(100) NOT NULL,
`Transcript_ID` varchar(100) NOT NULL,
`BLAST_ATH_protein` varchar(100) NOT NULL,
`Category` varchar(100) NOT NULL,
`Cleavage_Position` float NOT NULL default '0',
`miRNA_ID` varchar(100) NOT NULL,
`FM_miRNA` float NOT NULL default '0',
`x5BL_miRNA` float NOT NULL default '0',
`x5BP_miRNA` float NOT NULL default '0',
`x5BS_miRNA` float NOT NULL default '0',
`FM_target` float NOT NULL default '0',
`x5BL_target` float NOT NULL default '0',
`x5BP_target` float NOT NULL default '0',
`x5BS_target` float NOT NULL default '0',
`miRNA_aligned_fragment` varchar(100) NOT NULL,
`alignment` varchar(100) NOT NULL,
`Target_aligned_fragment` varchar(100) NOT NULL,
`Target_Desc` varchar(5000) NOT NULL
) ;
