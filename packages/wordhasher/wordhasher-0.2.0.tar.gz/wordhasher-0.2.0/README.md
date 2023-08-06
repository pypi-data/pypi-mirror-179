# WordHasher
Hashes are cool. But gosh they are ugly to read...

Let's convert them to verb-noun-adjective form to be more human friendly!

We are going to use [WordNet](https://wordnet.princeton.edu/) to get some words and [hashlib](https://docs.python.org/3/library/hashlib.html) to get some hashes.

# Example
``` python
>>> from wordhasher import WordHasher
>>> wh = WordHasher()
>>> print(wh)
WordHasher:
     nouns: 9698
adjectives: 3644
     verbs: 2872
>>> wh.from_str('This is a test.') 
catnap-abatic-upshot
>>> wh.from_str(__file__)
syphon-abashed-decidua
>>> wh.sample()
keep-vain-smugness-247
>>> wh.sample(mode="an")
inviting-patrial
>>> wh.sample(mode="anN")
unsaved-asshole-908
```

## Credits
> Princeton University "About WordNet." WordNet. Princeton University. 2010. 
