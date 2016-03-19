tesseract screenshot.png out
grep -e '^[0-9]' -e '^[A-Z]' out.txt | sed -s 's/[ ]//g' | cut -c 1-5 | sed '/[^[:alnum:]]/d' | sed '/[[:lower:]]/d' | grep -e '[0-9]$' -e '[A-Z]$' > tmp.txt
