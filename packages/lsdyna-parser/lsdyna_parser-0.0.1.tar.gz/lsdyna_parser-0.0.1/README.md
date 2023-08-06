The following code will return a dictionary containing all entities of the Ls-Dyna model. An entity consits of the Keyword and the corresponding cards as a list of parameter lines.
```python
from lsdyna_parser import parse_lsdyna_deck
parsed_dyna = parse_lsdyna_deck(path='example_lsdyna_deck.k')
```
The parser can be used as a starting point for model analysis and CAE process automation.