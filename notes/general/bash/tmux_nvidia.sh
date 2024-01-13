#!/bin/bash

tmux_path=$(command -v tmux)
if [ -z "$tmux_path" ];then echo "tmux not found";exit;fi

smi_path=$(command -v nvidia-smi)
if [ -z "$smi_path" ];then echo "nvidia-smi not found";exit;fi

htop_path=$(command -v htop)
if [ -z "$htop_path" ];then echo "htop not found";exit;fi

#adb kill-server
#sudo adb start-server

session="process"
tmux new -d -s $session
tmux split-window -v -t $session

tmux send-keys -t $session:0.0 'htop -t' C-m
tmux send-keys -t $session:0.1 'watch -n1 nvidia-smi' C-m

tmux attach -t $session
