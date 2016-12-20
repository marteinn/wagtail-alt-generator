#!/bin/sh

# Bumps the version number to relevant files at the end of any release and hotfix start
#
# Positional arguments:
# $1 The version (including the version prefix)
# $2 The origin remote
# $3 The full branch name (including the release prefix)
# $4 The base from which this release is started
#
# The following variables are available as they are exported by git-flow:
#
# MASTER_BRANCH - The branch defined as Master
# DEVELOP_BRANCH - The branch defined as Develop

VERSION=$1

# Remove v prefix (if present)
VERSION=${VERSION#"v"}

# Generate clean build number
VERSION_BUILD="$(echo $VERSION | tr -d .)"


ROOTDIR=$(git rev-parse --show-toplevel)

# Bump django version
sed -i.bak 's/^__version__.=.*/__version__ = '\'''$VERSION''\''/' $ROOTDIR/wagtailsystemtext/__init__.py
rm wagtailsystemtext/__init__.py.bak

# Bump django build
sed -i.bak 's/^__build__.=.*/__build__ = '$VERSION_BUILD'/' $ROOTDIR/wagtailsystemtext/__init__.py
rm wagtailsystemtext/__init__.py.bak

# Commit changes
git commit -a -m "Version bump $VERSION"

exit 0
