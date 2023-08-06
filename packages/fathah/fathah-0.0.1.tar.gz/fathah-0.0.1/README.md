## fathah
Lightweight NLP preprocessing package for Arabic language

### Installation
```sh
pip install fathah
```

### Usage
```python
from fathah import TextClean

text = "اَلسّلاَمُ عَلَيْكُمْ  وَرَحْمَةُ الله وَبَرَكَاتُهُ"
cleaner = TextClean(text)
cleaner.remove_diacritics()

# Outputs: السلام عليكم ورحمة الله وبركاته
```


*This package is under development. Contributions are highly welcome*

[Github](https://github.com/fathah) | [IG](https://instagram.com/fatha_cr)