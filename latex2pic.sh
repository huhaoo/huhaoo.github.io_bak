if [ -d "md_pub" ]
then
	rm -r md_pub
fi

cp md md_pub -r

find md_pub -name "*.md" | while read i
do
	python3 latex2pic.py $i
	echo "$i done."
done
