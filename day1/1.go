package main

import (
	"fmt"
	"time"

	"../helpers"
)

func p1(data []int) {
	defer helpers.TimeTrack(time.Now())
	var res int
	for ki, i := range data {
		for kj, j := range data {
			if ki != kj && i+j == 2020 {
				res = i * j
			}
		}
	}
	fmt.Printf("Part 1: %d ", res)
}

func p2(data []int) {
	defer helpers.TimeTrack(time.Now())
	var res int
	for ki, i := range data {
		for kj, j := range data {
			for kx, x := range data {
				if ki != kj && kj != kx && i+j+x == 2020 {
					res = i * j * x
				}
			}
		}
	}
	fmt.Printf("Part 2: %d ", res)
}

func main() {
	fmt.Println("Day 1: Report Repair")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day1/1.in"
	data, err := helpers.GetInputIntByLine(fileName)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
