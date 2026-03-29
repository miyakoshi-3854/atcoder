#!/bin/bash

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
RESET='\033[0m'

contest=""
if [ -f ./contest ]; then
  contest=$(cat ./contest)
fi

if [ -z "$contest" ]; then
  echo -ne "${BLUE}📝 Contest? ${RESET}"
  read contest
  echo "$contest" > ./contest
fi

echo -ne "${BLUE}📝 Problem? ${RESET}"
read problem

dir="_result/${contest}/${problem}"

mkdir -p "$dir"

dest="$dir/main.py"
if [ -f "$dest" ]; then
  n=2
  while [ -f "$dir/main_${n}.py" ]; do
    n=$((n + 1))
  done
  echo -e "${YELLOW}⚠️  Already exists: ${dir}/main.py → Saving as main_${n}.py${RESET}"
  dest="$dir/main_${n}.py"
fi

echo -e "${BLUE}📁 Saving to ${dest}${RESET}"
cp main.py "$dest"

echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
git add "$dest"
git commit -m "${contest} ${problem} (${dest##*/})"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"

echo -e "${GREEN}🔄 Resetting main.py & test.py from template${RESET}"
cp _template/main.py ./main.py
cp _template/test.py ./test.py

echo ""
echo -e "${GREEN}✅ Done: ${contest}/${problem}/${dest##*/}${RESET}"
