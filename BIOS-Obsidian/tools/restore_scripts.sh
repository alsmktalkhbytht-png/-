#!/usr/bin/env bash
# Restore every BIOS generator/helper into a new working folder (e.g. a new session's scratchpad)
# and rewrite the old scratchpad path inside them.
#   bash BIOS-Obsidian/tools/restore_scripts.sh <new-folder>
# Then a new handout script starts with:
#   import sys; sys.path.insert(0, "<new-folder>/imm456")
#   from ci import *      # C R SEC H2 L N FLOW T F FF SIDE B Q TF TR IM P INSHORT TERMS balance save HEM
set -euo pipefail
NEW="${1:?usage: restore_scripts.sh <new-folder>}"
HERE="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$NEW"
cp -r "$HERE/scripts/." "$NEW/"
# any earlier session scratchpad path (it changes every session) -> the new folder
grep -rlE "/tmp/claude-0/[^\"' ]+/scratchpad" "$NEW" | while read -r f; do sed -i -E "s#/tmp/claude-0/[^\"' ]+/scratchpad#$NEW#g" "$f"; done
echo "restored into $NEW"
