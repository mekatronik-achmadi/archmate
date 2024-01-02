#!/bin/bash

mkdir -p databases/
mkdir -p packages/custom/
cd packages/custom/

repo-add custom.db.tar.gz *.pkg.tar.zst
rm -f *.tar.gz.old

cp -vf custom.db.tar.gz ../../databases/custom.db
#cp -vf custom.files.tar.gz ../../databases/custom.files
rm -f custom.db*
rm -f custom.files*

cd ../../
