#!/usr/bin/env sh

# perl -ne "print $_\n"
cat | perl -ne "if(/db_column=/){s/(.*?)(db_column=)('.*?')(.*?)\)(.*?)\$//;print \$1.\$2.\$3.\$4.\", verbose_name=\$3\)\$5\\n\"}else{print}"

