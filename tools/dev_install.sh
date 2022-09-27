#!/bin/bash

addons_path=~/.config/blender/3.3/scripts/addons

src_name=dublast
dublf_path=../../DuBLF/dublf/
dupyf_path=../../../Python/DuPYF/dupyf/

src_path=../$src_name/

# convert to absolute paths
src_path=$(cd "$src_path"; pwd)
dublf_path=$(cd "$dublf_path"; pwd)
dupyf_path=$(cd "$dupyf_path"; pwd)

rm -r -f "$addons_path/$src_name"
mkdir "$addons_path/$src_name"

for file in $src_path/*.py; do
    ln -s -t "$addons_path/$src_name" "$file"
    echo "Linked $file"
done

mkdir "$addons_path/$src_name/dublf"

for file in $dublf_path/*.py; do
    ln -s -t "$addons_path/$src_name/dublf" "$file"
    echo "Linked DuBLF file $file"
done

for file in $dupyf_path/*.py; do
    ln -s -t "$addons_path/$src_name/dublf" "$file"
    echo "Linked DuPYF file $file"
done

echo "Done!"
sleep 10