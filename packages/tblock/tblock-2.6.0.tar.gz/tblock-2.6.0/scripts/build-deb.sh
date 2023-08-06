#!/bin/bash


CURRENT_DIR=$(pwd)
PKGVERSION=$(git describe --tags `git rev-list --tags --max-count=1`)
if [[ "$1" == "" ]]; then
	PKGREV="1"
else
	PKGREV="$1"
fi

__get_src__()
{
	wget https://codeberg.org/tblock/tblock/archive/$PKGVERSION.tar.gz -O "$CURRENT_DIR/../$PKGVERSION.tar.gz"
	cp "$CURRENT_DIR/debian/changelog" "$CURRENT_DIR/../changelog.bak"
	cp "$CURRENT_DIR/debian/control" "$CURRENT_DIR/../control.bak"
	cp "$CURRENT_DIR/debian/rules" "$CURRENT_DIR/../rules.bak"
}

__restore__()
{
	cp "$CURRENT_DIR/../changelog.bak" "$CURRENT_DIR/debian/changelog"
	cp "$CURRENT_DIR/../control.bak" "$CURRENT_DIR/debian/control"
	cp "$CURRENT_DIR/../rules.bak" "$CURRENT_DIR/debian/rules"
}

__clean_build_dir__()
{
	rm -rf $CURRENT_DIR/debian/tblock*
}

__build_ubuntu__()
{
	VERSION=$1
	CODE_NAME=$2
	FULL_VERSION="$PKGVERSION""$VERSION"
	cp "$CURRENT_DIR/../$PKGVERSION.tar.gz" "$CURRENT_DIR/../tblock_$FULL_VERSION.orig.tar.gz"
	sed -i "s/stable/$CODE_NAME/" debian/changelog
	sed -i "s/$PKGVERSION-$PKGREV/$FULL_VERSION/g" debian/changelog
	debuild -S -d
	__restore__
}

__build_ubuntu_all__()
{
	__build_ubuntu__ "~ubuntu18.04.$PKGREV" "bionic"
	__build_ubuntu__ "~ubuntu20.04.$PKGREV" "focal"
	__build_ubuntu__ "~ubuntu22.04.$PKGREV" "jammy"
	__build_ubuntu__ "~ubuntu22.10.$PKGREV" "kinetic"
}

__upload_ubuntu__()
{
	dput tblock "$CURRENT_DIR/*.change"
}

__build_debian__()
{
	INIT=$1
	if [[ "$1" == "systemd" ]]; then
		PACKAGE_NAME="tblock"
	else
		PACKAGE_NAME="tblock-$INIT"
	fi
	cp "$CURRENT_DIR/../$PKGVERSION.tar.gz" "$CURRENT_DIR/../$PACKAGE_NAME""_$PKGVERSION.orig.tar.gz"
	sed -i "s/tblock/$PACKAGE_NAME/g" debian/changelog
	sed -i "s/tblock/$PACKAGE_NAME/g" debian/control
	sed -i "s/tblock/$PACKAGE_NAME/" debian/rules
	sed -i "s/install-service-systemd/install-service-$INIT/" debian/rules
	debuild -d
	__clean_build_dir__
	__restore__
}

__build_debian_all__()
{
	__build_debian__ "systemd"
	__build_debian__ "openrc"
	__build_debian__ "runit"
}

__restore__
__clean_build_dir__
__get_src__
__build_ubuntu_all__
__build_debian_all__
__clean_build_dir__
__restore__

