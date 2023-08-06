#!/bin/sh
# -----------------------------------------------------------------------------
# Global constants
#
ME=$(readlink -f $0)
ME_DIR=$(dirname "$ME")
ME_DIR=${ME_DIR%%/}

ASSETS_ARCHIVE=$ME_DIR/late-command-assets.tgz

if [ -n "$TEST_PREFIX" ]; then
    # For local tests before packaging to ISO
    PREFIX="$TEST_PREFIX"
    alias in-target='echo "in-target:"'
else
    PREFIX=""
fi

echo "[late-command] run $ME, PREFIX=$PREFIX"

# -----------------------------------------------------------------------------
# Parse command line and write log
#

mkdir -p $PREFIX/target/var/log
echo "installed: $(date --utc +%Y-%m-%dT%H:%M:%SZ)" > $PREFIX/target/var/log/debseed-context

while true; do
    [ $# -eq 0 ] && break
    key="$1"
    shift
    
    [ $# -eq 0 ] && break
    value="$1"
    shift

    if [ "$key" = "--ssh_public_key" ]; then
        ssh_public_key="$value"
    elif [ "$key" = "--srv_group" ]; then
        srv_group="$value"
    fi

    echo "${key#--}: $value" >> $PREFIX/target/var/log/debseed-context
done


# -----------------------------------------------------------------------------
# Deployments
#
if [ -f "$ASSETS_ARCHIVE" ]; then
    echo "[late-command] extract $ASSETS_ARCHIVE"
    tar -C "$PREFIX/" -xzvf "$ASSETS_ARCHIVE"
fi


username=$(debconf-get passwd/username)

if [ -n "$username" ]; then
    echo "[late-command] deploy profile for user $username"
    mkdir -p $PREFIX/target/home/$username
    cp -a $PREFIX/target/etc/skel/. $PREFIX/target/home/$username/.

    if [ -n "$ssh_public_key" ]; then
        echo "[late-command] deploy authorized ssh key for user $username"
        mkdir -p $PREFIX/target/home/$username/.ssh
        echo "$ssh_public_key" > $PREFIX/target/home/$username/.ssh/authorized_keys
    fi

    in-target chown -R $username:$username /home/$username
fi

if [ -d "$PREFIX/target/etc/sudoers.d" ]; then
    echo "[late-command] fix /etc/sudoers.d permissions"
    in-target find /etc/sudoers.d -type f -exec chmod 440 -- {} +
fi

if [ "$(ls -A $PREFIX/target/usr/local/share/ca-certificates)" ]; then
    echo "[late-command] run update-ca-certificates"
    in-target update-ca-certificates
fi

if [ -f "$PREFIX/target/etc/vim" ] && [ -e "$PREFIX/target/usr/bin/vim.basic" ]; then
    echo "[late-command] run update-alternatives for vim"
    in-target update-alternatives --set editor /usr/bin/vim.basic
fi


if [ -f "$PREFIX/target/usr/etc/npmrc" ]; then
    # /usr/etc/npmrc is used by yarn and npm (modern versions)
    # /etc/npmrc is used by ancient versions of npm (e.g. 7.5.2 included with Debian Bullseye)
    echo "[late-command] make link to /usr/etc/npmrc"
    mkdir -p $PREFIX/target/etc/
    in-target ln -s /usr/etc/npmrc /etc/npmrc   
fi

if [ -n "$srv_group" ]; then
    echo "[late-command] deploy /srv permissions and acls"
    in-target chgrp -R "$srv_group" /srv # set group for existing files and folder under /srv
    in-target chmod g=rwx,g+s /srv # set group write permission, and the setgid bit so that files and folder under /srv will be created with the same group as /srv
    in-target setfacl -R -m g::rwx /srv    # set the group ACLs recursively for existing files and folders
    in-target setfacl -R -d -m g::rwx /srv # set the default group ACLs recursively

    # NOTE: chmod must be done once more after reboot (see `late-command-assets/target/etc/systemd/system/debseed-firstboot.service`),
    # because Debian Installer seems to erase this before reboot
fi

if [ -f "$PREFIX/target/etc/systemd/system/debseed-firstboot.service" ]; then
    echo "[late-command] enable debseed-firstboot service"
    in-target systemctl enable debseed-firstboot
fi

#TODO/ROADMAP: simulate run-parts (not available in Debian Installer)
#echo "[late-command] run parts"
#run-parts -v $ME_DIR/late-command.d 

echo "[late-command] done"
