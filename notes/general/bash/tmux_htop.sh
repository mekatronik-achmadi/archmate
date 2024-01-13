#!/bin/bash

################# check binary #################
tmux_path=$(command -v tmux)
if [ -z "$tmux_path" ];then echo "tmux not found";exit;fi

htop_path=$(command -v htop)
if [ -z "$htop_path" ];then echo "htop not found";exit;fi

ifconfig_path=$(command -v ifconfig)
if [ -z "$ifconfig_path" ];then echo "ifconfig not found";exit;fi

df_path=$(command -v df)
if [ -z "$ifconfig_path" ];then echo "df not found";exit;fi

################# start and check session #################
session="htop_info"
tmux has-session -t $session 2>/dev/null

if [ $? != 0 ]; then
	tmux new -d -s $session

################# split window into 2 panes #################
	tmux split-window -h -t $session

################# start programs in each pane #################
	tmux send-keys -t $session:0.0 'htop -t' C-m
	tmux send-keys -t $session:0.1 'ifconfig;df -h' C-m

################# actual tmux running #################
	tmux attach -t $session
fi

