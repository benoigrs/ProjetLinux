#daily resume
cut -d ' ' -f 2 value.txt > values.txt

values=$(tail -n 100 values.txt)

mean=$(echo "$values" | awk '{ sum += $1 } END { print sum / NR }')
variance=$(echo "$values" | awk '{ sum += ($1 - mean)^2 } END { print sum / NR }' mean="$mean")

first=$(echo "$values" | head -n 1)
last=$(echo "$values" | tail -n 1)
return=$(echo "scale=2; (($last-$first)/$first)*100" | bc)

echo "Mean: $mean" > daily.txt
echo "Variance: $variance" >> daily.txt
echo "Return: $return%" >> daily.txt
