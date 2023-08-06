# PyAdvDocx
An open source project inspired from python-docx in which more functionalities are added like advance replace and many more.


[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)  [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![PyPI version](https://img.shields.io/pypi/v/pyadvdocx)](https://pypi.python.org/pypi/pyadvdocx/) 




## Supported OS

[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg) [![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)

## Installing 

```bash 
pip3 install pyadvdocx
```

## Use cases:
```python
from pyadvdocx import text,Document

doc=Document("Example.docx")
text.replace(doc,$name="John Doe")
doc.save("Master work.docx")
```

## License
Project license -  [MIT](./LICENSE)

## Contributing
Anyone is free to contribute and pull request/fork this project.

## Testing:
```bash
cd ./test
pip3 install pyadvdocx
python3 test_text.py
# Look in data dir for *_done.docx files
```