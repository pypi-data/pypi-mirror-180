#!/bin/bash
# ================================================================================
# replace these values with the values you need for your build
# ================================================================================
org="utah"
app="arches"
packager="George Tsiones"
version="1.0"
release="00001"
summary="Python Flask Based CMS"
license="GPL"
url="https://utahproject.org" 		# URL is optional and can be commented out 
group="system"
#
#  
description="
--------------------------------------------------------------------------------
Arches is a self contained deployable CMS 
which has 2 implemented backing stores.
--------------------------------------------------------------------------------
"
# ================================================================================



# assign a variable with a temp description file name.
temp_description_file=$(mktemp)

# write description data to temp file. Will get imported by the rpmspec
echo "$description" > $temp_description_file

if [[ "$url" == "" ]]; then
	url="--"
fi

# The command below runs rpmbuild and passes your values into the build
rpmbuild \
	--define "_org $org " \
	--define "_app $app " \
	--define "_packager $packager " \
	--define "_version $version" \
	--define "_release $release" \
	--define "_summary $summary" \
	--define "_description_file $temp_description_file" \
	--define "_license $license" \
	--define "_url $url" \
	--define "_group $group" \
	--build-in-place \
	--target x86_64 \
	-bb server_config/centos8/$app-rpm2.spec

# remove the temp description file
rm -f $temp_description_file
