
# PyPageSummarizer
A Python library to summarize the main content of a webpage using Google T5 AI model.
## Features
- Extract the main content from a webpage.
- Summarize the main content extracted from a webpage.


## Libraries Used

 - [Requests](https://pypi.org/project/requests/)
 - [Trafilatura](https://pypi.org/project/trafilatura/)
 - [Transformers](https://pypi.org/project/transformers/)
 - [PyTorch](https://pypi.org/project/torch/)


## Use Prerelease Version

Download main.py from this repository and install the following Python libraries.

```bash
  pip install requests
  pip install trafilatura
  pip install transformers
  pip install torch
```
And run it.

    
## Functions
1.Extract the main content from a webpage.
```bash
maincontent(url)
```
URL - String.
\
\
2.Summarize the main content extracted from a webpage.
```bash
summarize(url,maxlength,minlength)
```
url - String.\
maxlength - Integer.\
minlength - Integer.
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@sorawithwetubon](https://github.com/sorawithwetubon)

