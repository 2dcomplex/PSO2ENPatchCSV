#!/bin/sh
cat PSO2.dict.BASE>/tmp/PSO2.dict
find . -name "*_name.csv" -or -name "ui_charamake_parts.csv" -print0|xargs -0 python3 aspell.py|strings -n 2|sed -e 's/[ \t][ \t]*/\
/g' -e 's/\!//g' -e "s/'//g"|uniq|grep -v -E -f reject*.dict |strings -n 1 >>/tmp/PSO2.dict
cat PSO2.*.dict|strings -n 1 >>/tmp/PSO2.dict
find . -name "*.csv" -not -name "smut_filter.csv" -not -name "*_BACKUP_*.csv" -not -name "*_BASE_*.csv" -not -name "*_REMOTE_*.csv" -print0|xargs -0 python3 aspell.py|strings -n 1|aspell pipe --personal=/tmp/PSO2.dict --encoding utf-8|strings -n 2|fgrep -v -e "*"
#./aspell.sh |tee /tmp/PSO2_aspell.txt|sort|uniq --count|sort -n|2>/tmp/PSO2_aout.txt
