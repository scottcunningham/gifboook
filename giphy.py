#!/usr/bin/env python

import giphypop
import random


def search(term):
    g = giphypop.Giphy()
    results = [x for x in g.search(term)]
    if len(results) == 0:
        return ':(('
    else:
        return random.choice(results[:5]).media_url
