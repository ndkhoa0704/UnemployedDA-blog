#!/bin/bash
set -o allexport && source ~/.env && set +o allexport


date +%d-%m-%y/%H:%M:%S
cd $REPO_PATH

echo "$REPO_PATH"

if ! git pull | grep -q 'Already up to date.'
then
    docker exec unemployedda-blog-server /bin/sh -c "alembic upgrade head"
    docker restart unemployedda-blog-server
fi