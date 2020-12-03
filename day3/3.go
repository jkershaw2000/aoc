package main

import (
	"fmt"
	"time"

	"../helpers"
)

func createSlopes() [][]int {
	// Is there a better way to do this?
	// Seems extremly long winded. Potentialy use a struct.
	slopes := make([][]int, 5)
	for i := range slopes {
		slopes[i] = make([]int, 2)
	}
	slopes[0][0] = 1
	slopes[0][1] = 1
	slopes[1][0] = 3
	slopes[1][1] = 1
	slopes[2][0] = 5
	slopes[2][1] = 1
	slopes[3][0] = 7
	slopes[3][1] = 1
	slopes[4][0] = 1
	slopes[4][1] = 2
	return slopes
}

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
	slopes := createSlopes()
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
