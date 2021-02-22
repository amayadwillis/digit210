# Regex 1 - Movie Data

1. Checked for & < > - replaced `&` with `&amp;`
1. find `^.+` - replace using `<movie>\0</movie>`
1. find `<movie>(.+?)\t` - 25095 results - replace using `\1<title>\2</title>`
1. find `(</title>)(.+?)\t` - 25095 results - replace using `\1<date>\2</date>`
1. find `(</date>)(.+?)\t` - 25095 results - replace using `\1<location>\2</location>`
1. find `(</location>)(.+?)(</movie>)` - 25095 results - replace using `\1<time unit="min">\2</time>\3`
1. -edits-
1. manually added root element
1. find `min</time>` replace with `</time>`