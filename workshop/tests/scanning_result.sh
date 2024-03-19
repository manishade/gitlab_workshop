#!/bin/bash

if jq -e '( ([.vulnerabilities[] | select(.severity | contains("Critical"))] | length) > 1 )' ./gl-container-scanning-report.json; then
    echo "Too many vulnerabilities found in image. Please correct it. Refer to the slides/readme.md for the correct image";
    exit 1;
fi