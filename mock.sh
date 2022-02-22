#!/bin/bash

git clone https://github.com/walkccc/LeetCode.git
cd LeetCode
git clone -b mkdocs --single-branch https://github.com/walkccc/LeetCode.git mkdocs
git clone -b scripts --single-branch https://github.com/walkccc/LeetCode.git scripts

python3 scripts/main.py --mock

cp README.md mkdocs/docs/preface.md
cp STYLEGUIDE.md mkdocs/docs/styleguide.md

cd mkdocs
mkdocs serve
