#!/usr/bin/env python 

import regex

pattern = r'(?:\\cite\{|(?<!^)\G),?\s*([^,}]+)'

with open('main.tex') as f:
    main = f.read()
main_refs = set(regex.findall(pattern, main))

with open('supp.tex') as f:
    supp = f.read()
supp_refs = set(regex.findall(pattern, supp))

supp_refs_not_in_main = supp_refs - main_refs

print(f"The supplemental references not in the main text are {supp_refs_not_in_main}")