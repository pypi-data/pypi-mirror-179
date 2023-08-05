#!/bin/bash
dconf load /org/pantheon/terminal/settings/ <<COLORS
[/]
name='Builtin Pastel Dark'
cursor-color='#ffa560'
foreground='#bbbbbb'
background='rgba(0,0,0,.95)'
palette='#4f4f4f:#ff6c60:#a8ff60:#ffffb6:#96cbfe:#ff73fd:#c6c5fe:#eeeeee:#7c7c7c:#ffb6b0:#ceffac:#ffffcc:#b5dcff:#ff9cfe:#dfdffe:#ffffff'
COLORS
