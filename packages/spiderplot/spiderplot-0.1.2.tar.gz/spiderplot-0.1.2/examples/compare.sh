#!/usr/bin/env bash
OUTDIR="./cmp/"
mkdir -p "$OUTDIR"
for subdir in out*; do
    _suffix=${subdir%%+(/)}
    for f in ${subdir}/*/*.png; do
        _basename=${f##*/}
        _basename=${_basename%%.*}
        cp -f "$f" "$OUTDIR/$_basename-$_suffix.png"
    done
done
