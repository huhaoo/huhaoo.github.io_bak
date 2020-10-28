if [ -f index.md ]
then
	rm index.md
fi
touch index.md

find md_pub/ -name "[!.]*" | while read i
do
	if [ -f $i ]
	then
		echo>>index.md "[$i]($i)"
		echo>>index.md ""
	fi
done
find files/ -name "[!.]*" | while read i
do

	if [ -f $i ]
	then
		echo>>index.md "[$i]($i)"
		echo>>index.md ""
	fi

done
