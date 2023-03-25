curl https://www.boursorama.com/cours/1rPRI/ > html.txt

grep -A 30 'class="stb0" cx="25" cy="25" rx="25" ry="25"/><path class="stb1"' html.txt > result.txt
grep -A 1 'PERNOD RICARD' result.txt > line.txt
value=$(grep -oP '(?<=<span class="c-instrument c-instrument--last" data-ist-last>)[0-9.]+(?=</span>)' line.txt)
echo "$(date -u +'%H:%M' -d '+1 hour') $value" >> value.txt
