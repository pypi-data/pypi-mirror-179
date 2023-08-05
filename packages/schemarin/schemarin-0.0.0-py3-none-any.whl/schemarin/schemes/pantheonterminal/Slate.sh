#!/bin/bash
dconf load /org/pantheon/terminal/settings/ <<COLORS
[/]
name='Slate'
cursor-color='#87d3c4'
foreground='#35b1d2'
background='rgba(34,34,34,.95)'
palette='#222222:#e2a8bf:#81d778:#c4c9c0:#264b49:#a481d3:#15ab9c:#02c5e0:#ffffff:#ffcdd9:#beffa8:#d0ccca:#7ab0d2:#c5a7d9:#8cdfe0:#e0e0e0'
COLORS
