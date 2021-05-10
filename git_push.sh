#!/bin/bash
message=${1:-'Edited files'}    

git add .
git commit -m "$message"
git push
