import re
import sys
from urllib.parse import quote

if __name__ == "__main__":

    if len(sys.argv)!=2:
        exit(0)

    text = open(sys.argv[1],encoding="utf-8").read()

    parts = text.split("$$")

    for i, part in enumerate(parts):
        if i & 1:
            parts[i] = f'![math](https://www.zhihu.com/equation?tex={quote(part.strip())})'

    text_out = "\n\n".join(parts)

    lines = text_out.split('\n')
    for lid, line in enumerate(lines):
        parts = re.split(r"\$(.*?)\$", line)
        for i, part in enumerate(parts):
            if i & 1:
                parts[i] = f'![math](https://www.zhihu.com/equation?tex={quote(part.strip())})'
        lines[lid] = ' '.join(parts)
    text_out = "\n".join(lines)

    with open(sys.argv[1], "w", encoding='utf-8') as f:
        f.write(text_out)
