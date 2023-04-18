# OpenAPI-to-Markdown Converter

## Overview 

Convert openapi json doc to clean markdown with some html tables that can be used in supported markdown apps or site publishers like docusaurus.

See an example here: https://lifecyclescience.com/docs/apis/actionhub

## Usage

1. Copy open api doc to `openapi.json`
2. Run this:
```python
import converter
converter.path("<path_starts_with>")
```

Will create `.md` files in the `api` folder with a `<method>_<resource>.md` naming convention.

