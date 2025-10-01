#!/usr/bin/env bash
set -euo pipefail

# Ensure 'make' is installed
if ! command -v make >/dev/null 2>&1; then
  echo "Error: 'make' not found in '$folder'." >&2
  exit 127
fi

# Check that the directory param is passed
if [[ $# -ne 1 ]]; then
    echo "Error: a directory is required." >&2
    exit 1
fi

folder=$1

# Check that the folder exists and is a directory
if [[ ! -d "$folder" ]]; then
  echo "Error: '$folder' is not a directory or doesn't exist." >&2
  exit 2
fi

# Verify a makefile exists in the folder
if [[ ! -f "$folder/makefile" ]]; then
  echo "Error: no makefile found in '$folder'." >&2
  exit 2
fi


cd -- "$folder"
make
