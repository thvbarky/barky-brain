#!/bin/bash
cd ~/Documents/GitHub/barky-brain
DATE=$(date +%Y-%m-%d)
if git status --porcelain | grep -q "veille\|briefs\|synthese"; then
  git add 16-veille/ 08-ads/briefs/
  git commit -m "veille + briefs: $DATE"
  git push origin main
fi
