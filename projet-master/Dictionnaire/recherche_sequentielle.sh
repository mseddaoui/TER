#!/bin/bash

function current_datetime {
python - <<END
import time
print (time.time())
END
}

# Call it
tdebut=$(current_datetime)
echo le temp debut: $tdebut
grep -E "^u" dictionnaire.txt | wc -l

# Call it and capture the output

trecherche=$(current_datetime)
#echo apres la recherche le temps est: $trecherche 
echo le temps consacré à la recherche est 
echo "$trecherche $tdebut  " | awk '{print $1 - $2}'

