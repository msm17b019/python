# JSON Methods in Python (`json` Module)

Python’s built-in `json` module allows easy parsing and generation of JSON data, which is commonly used for APIs, config files, and logs.

---

## Import JSON Module
```python
import json
```

# JSON Methods Summary

| Function            | Purpose                             | Input           | Output         |
|---------------------|-------------------------------------|------------------|------------------|
| `json.load(f)`      | Read JSON from file                 | File object      | Python object    |
| `json.loads(s)`     | Read JSON from string               | String           | Python object    |
| `json.dump(obj, f)` | Write Python object to JSON file    | Python object    | File output      |
| `json.dumps(obj)`   | Convert Python object to JSON string| Python object    | JSON string      |

