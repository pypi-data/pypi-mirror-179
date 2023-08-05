#!/usr/bin/env make -j2

# TBlock default Makefile
# Run 'make help' to show help message

# Define variables
PYTHON ?= /usr/bin/env python3
ROOT ?= /
DESTDIR ?= $(ROOT)/usr

all: build build-files

.PHONY: all clean build-wheel build-sdist build-pypi test test-pytest test-bandit test-flake8 install install-openrc uninstall uninstall-openrc install-config uninstall-config

# ----- CLEAN -----

clean:
	rm -rf build dist README.txt ./docs/man/*.1.gz ./docs/man/*.5.gz *.1 *.5 *.egg-info tblock/__pycache__ tblock/*/__pycache__ test/__pycache__ test/fake_root *.bin

# ----- BUILD -----

build:
	$(PYTHON) -m build --wheel --no-isolation

build-pypi:
	$(PYTHON) -m build

build-files: docs/man/tblock.1.gz docs/man/tblockc.1.gz docs/man/tblockd.1.gz

docs/man/tblock.1.gz:
	gzip -k9 ./docs/man/tblock.1

docs/man/tblockc.1.gz:
	gzip -k9 ./docs/man/tblockc.1

docs/man/tblockd.1.gz:
	gzip -k9 ./docs/man/tblockd.1

# ----- TEST -----

test:
	$(PYTHON) -V
	+make test-unittest test-bandit test-codestyle

test-unittest:
	/bin/sh test/server.sh --restart
	$(PYTHON) -m unittest -v
	/bin/sh test/server.sh --stop

test-bandit:
	$(PYTHON) -m bandit -r tblock -c .bandit.yml

test-codestyle:
	$(PYTHON) -m pycodestyle tblock test

# ----- INSTALL -----

install: all install-files install-service-systemd install-python-module
install-openrc: all install-files install-service-openrc install-python-module
install-runit: all install-files install-service-runit install-python-module

install-files: build-files
	install -Dm644 ./docs/man/tblock.1.gz $(DESTDIR)/share/man/man1/tblock.1.gz
	install -Dm644 ./docs/man/tblockc.1.gz $(DESTDIR)/share/man/man1/tblockc.1.gz
	install -Dm644 ./docs/man/tblockd.1.gz $(DESTDIR)/share/man/man1/tblockd.1.gz
	install -Dm644 LICENSE $(DESTDIR)/share/licenses/tblock/LICENSE.txt

install-service-systemd:
	install -Dm644 assets/services/systemd/tblockd.service $(DESTDIR)/lib/systemd/system/tblockd.service

install-service-openrc:
	install -Dm755 assets/services/openrc/tblockd.initd $(ROOT)/etc/init.d/tblockd

install-service-runit:
	install -Dm755 assets/services/runit/tblockd.run $(ROOT)/etc/runit/sv/tblockd/run

install-python-module: 
	$(PYTHON) -m installer --destdir="$(ROOT)" dist/*.whl

install-config:
	install -Dm644 assets/config/tblock.conf $(ROOT)/etc/tblock.conf

# ----- UNINSTALL -----
uninstall: uninstall-python-module uninstall-files uninstall-service-systemd
uninstall-openrc: uninstall-python-module uninstall-files uninstall-service-openrc
uninstall-runit: uninstall-python-module uninstall-files uninstall-service-runit

uninstall-python-module:
	rm -f $(DESTDIR)/bin/tblock
	rm -f $(DESTDIR)/bin/tblockc
	rm -f $(DESTDIR)/bin/tblockd
	rm -rf $(DESTDIR)/lib/python3.*/site-packages/tblock
	rm -rf $(DESTDIR)/lib/python3.*/site-packages/tblock-*.dist-info
	rm -rf $(DESTDIR)/lib/python3.*/site-packages/tblock-*.egg-info

uninstall-files:
	rm -f $(DESTDIR)/share/man/man1/tblock.1.gz
	rm -f $(DESTDIR)/share/man/man1/tblockc.1.gz
	rm -f $(DESTDIR)/share/man/man1/tblockd.1.gz
	rm -f $(DESTDIR)/share/man/man5/tblock.conf.5.gz
	rm -f $(DESTDIR)/share/licenses/tblock/LICENSE.txt

uninstall-service-systemd:
	rm -f $(DESTDIR)/lib/systemd/system/tblockd.service

uninstall-service-openrc:
	rm -f $(ROOT)/etc/init.d/tblockd

uninstall-service-runit:
	rm -f $(ROOT)/etc/runit/sv/tblockd/run

uninstall-config:
	rm -f $(ROOT)/etc/tblock.conf
