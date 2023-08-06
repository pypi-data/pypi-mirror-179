# PString
_Pretty String for Python_

Use __method chaining__ to add __color, style, and background__ to your strings.

```python
from pstring import PString as ps

# Red color, green background, bold, underline
ps('Hello World').r().bg_g().bold().underline()

# in any order
ps('Hello World').bold().underline().r().bg_g()
```

## Installation

```bash
pip install pstring
```

## Available Styles

![avai_styles](https://user-images.githubusercontent.com/48139961/205517766-1cf55b46-541f-4dbf-9cb4-64a2f8885a4f.png)

