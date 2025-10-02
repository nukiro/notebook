#!/usr/bin/env bash
set -euo pipefail

# Ensure 'make' is installed
if ! command -v make >/dev/null 2>&1; then
  echo "Error: 'make' not found in '$folder'." >&2
  exit 127
fi

# Check that the directory param is passed
if [[ $# -lt 1 ]]; then
    echo "Error: a directory is required." >&2
    exit 1
fi

FOLDER="$1"; shift || true

# Check that the folder exists and is a directory
if [[ ! -d "$FOLDER" ]]; then
  echo "Error: '$FOLDER' is not a directory or doesn't exist." >&2
  exit 2
fi

# Verify a makefile exists in the folder
if [[ ! -f "$FOLDER/makefile" ]]; then
  echo "Error: no makefile found in '$FOLDER'." >&2
  exit 2
fi

cd -- "$FOLDER"

# --- option parse ---
while (($#)); do
  case "$1" in
    -s|--source)    make s; exit 0 ;;
    -h|--header)    make h; exit 0 ;;
    -o|--object)    make o; exit 0 ;;
    -c|--clean)     make clean; exit 0 ;;
    *)              echo "Error: Unknown option: $1" >&2; exit 2 ;;
  esac
  shift || true
done

make

