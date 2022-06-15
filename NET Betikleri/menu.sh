#!/usr/bin/bash

choise=$(whiptail --menu "" --notags --title "Net Komutları" 10 40 3 "1" "sh ver" "2" "sh users" 3>&2 2>&1 1>&3)

case $choise in
    "1") result=$(python show_ver.py);;
    "2") pass
esac

whiptail --msgbox --scrolltext "$result" 50 70
