---

name: "Bug Report"
about: "There is a bug in the software!"
title: "A clear and short title"
ref: "main"
labels:
- "Kind: Bug"
- "Status: Stale"
- "Priority: High"

---

### Before opening:
<!--
Before opening, please ensure that this issue is not duplicated.
Also, please remember that the more information you provide about the bug, the
faster we will be able to work on a fix.
-->

- [ ] This issue is not duplicated
- [ ] I am running [the latest stable version of TBlock](https://codeberg.org/tblock/tblock/releases/latest)

### Bug description
<!--
Please write a clear and concise description
-->

### Steps to reproduce

- This issue is repoducible: `yes/no`
<!-- 
If it is reproducible, enter the steps to reproduce it below
-->

1. Do something
2. Do something else
3. See error


### Error code

- This issue results in TBlock to crash: `yes/no`
<!-- 
If so, please enter the output of your terminal emulator below
-->

```

```

### Possible solutions or causes
<!--
If you are a developer, you can write your ideas about what causes this bug or how to fix it in this section. Otherwise, leave it blank or delete it.
-->


### System information
<!--
This section is not mandatory, but they can be really helpful in some cases.
If, however, you don't wish to disclose such information, you are free to delete this section.
-->

I am running TBlock on:
- [ ] GNU/Linux, Linux: `distribution`, `init` <!-- If you don't know which init system you use, it is probably "systemd" -->
- [ ] macOS: `version`
- [ ] Microsoft Windows: `version`
- [ ] *BSD
- [ ] Android: `version`, using Termux: `version`
- [ ] Other: `name`, `version`

I installed TBlock on my machine with:
- [ ] My distribution's official package repository
- [ ] AUR/Chaotic-AUR
- [ ] Fedora COPR
- [ ] Ubuntu PPA
- [ ] Debian package
- [ ] Homebrew
- [ ] Scoop
- [ ] Windows EXE installer
- [ ] Python pip
- [ ] Manually (with `make`) from the latest tag
- [ ] Manually (with `make`) from the main branch


The output of `tblock -Lk` is the following:

```

```

The output of `tblock -s` is the following:

```

```

### Logs
<!-- 
If you want, you can attach TBlock's log file for more information.
This is not required, but it can be useful for some bugs. Feel free to delete this section if you don't want to provide your log file.

Under UNIX-like systems, you can find the log file under:
-> /var/log/tblock.log

Under Android with Termux, you can find the log file under:
-> /data/data/com.termux/files/usr/var/log/tblock.log

Under Windows, you can find the log file under:
-> %ALLUSERSPROFILE%\TBlock\tblock.log
-->
