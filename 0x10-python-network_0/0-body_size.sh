#!/usr/bin/env bash
URL="$1"
curl -sI $URL | grep -i Content-length
