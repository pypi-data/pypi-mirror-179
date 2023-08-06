# Battleship 🛥️

Simple Battleship game in Python.

This is a simple naive implementation with dynamic grid support.

## Challenge

Create an application to allow a single human player to play a one-sided game of Battleships against ships placed by the computer.

The program should create a 10x10 grid, and place a number of ships on the grid at random with the following sizes:

* 1x Battleship (5 squares)
* 2x Destroyers (4 squares)

The player enters coordinates of the form “A5”, where "A" is the column and "5" is the row, to specify a square to target. Shots result in hits, misses or sinks. The game ends when all ships are sunk.

## Run

```bash
pip3 install battleship
python3 -m battleship
```

## Build Automation

[![Build Status](https://github.com/joamag/battleship/workflows/Main%20Workflow/badge.svg)](https://github.com/joamag/battleship/actions)
