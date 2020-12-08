package main

import (
	"fmt"
	"time"

	"../helpers"
)

func p1(data []string) {
	defer helpers.TimeTrack(time.Now())
	res, pos := 0, 0
	for _, line := range data {
		if line[pos] == '#' {
			res++
		}
		pos = (pos + 3) % len(line)
	}
	fmt.Printf("Part 1: %d ", res)
}

func p2(data []string) {
	defer helpers.TimeTrack(time.Now())
	res := 1
	slopes := [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	for _, slope := range slopes {
		posX, posY := 0, 0
		temp := 0
		for posY < len(data) {
			if data[posY][posX] == '#' {
				temp++
			}
			posY = posY + slope[1]
			posX = (posX + slope[0]) % len(data[0])
		}
		res = res * temp
	}
	fmt.Printf("Part 2: %d ", res)
}

func main() {
	fmt.Println("Day 3: Toboggan Trajectory")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day3/3.in"
	data, err := helpers.GetInputStringByLine(fileName)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
