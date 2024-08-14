#!/bin/bash
set -o allexport && source ~/.env && set +o allexport

date +%d-%m-%y/%H:%M:%S
cd $REPO_PATH
echo "$REPO_PATH"

if ! git pull | grep -q 'Already up to date.'
then
    docker compose down
    docker rmi unemployedda-blog
    docker compose up -d
fi