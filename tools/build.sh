#!/bin/bash

src_name=dublast

src_path=../$src_name/

# convert to absolute paths
duik_path=$(cd "$src_path"; pwd)

rm -r -f $src_name
mkdir $src_name

for file in $src_path/*.py; do
    cp -t $src_name "$file"
    echo "Deployed $file"
done

zip -r -m $src_name.zip $src_name

# build doc
cd ../src-docs
mkdocs build

echo "Done!"