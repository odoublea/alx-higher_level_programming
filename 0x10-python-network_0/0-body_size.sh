#!/usr/bin/bash
URL="$1"
curl -sI $URL | grep -i Content-length
