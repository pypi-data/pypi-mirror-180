# HashToDocx
Write File Information to docx(for Forensic)

# Install
```sh
$ pip install HashToDocx 
```

# Usage
## 1. Basic Usage Example
```python
from HashToDocx import HashToDocx

docx = HashToDocx()
docx.scanDir('sample') # input target Directories
docx.save('123.docx') # save to docx
```

## 2. Recursive Directory Usage Example
```python
from HashToDocx import HashToDocx

docx = HashToDocx()
docx.scanDir(
    dir     = 'sample',   # input target Directories
    option  = 'recursive' 
) 

docx.save('123.docx') # # save to docx
```

## 3. set Range parsing field
You can filter only the fields you want by adjusting the list variable.
```python
from HashToDocx import HashToDocx

# Field
Field = ['filename', 'size', 'md5', 'sha1', 'sha256', 'ctime', 'mtime', 'atime']

docx = HashToDocx(Field)
docx.scanDir('sample') # input target Directories
docx.save('123.docx') # # save to docx
```
