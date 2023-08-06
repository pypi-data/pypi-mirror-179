# ~/.bashrc: executed by bash(1) for non-login shells.

# Set the prompt (red)
PS1='${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Colorize ls
export LS_OPTIONS='--color=auto'
eval "`dircolors`"
alias ls='ls $LS_OPTIONS'

# Some more ls aliases
alias ll='ls $LS_OPTIONS -l'
alias ll='ls $LS_OPTIONS -A'
alias l='ls $LS_OPTIONS -lA'
