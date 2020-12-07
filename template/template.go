package main

import (
	"fmt"
	"time"

	"../helpers"
)

func p1(data []string) {
	defer helpers.TimeTrack(time.Now())
	res := 0
	fmt.Printf("Part 2: %d ", res)
}

func p2(data []string) {
	defer helpers.TimeTrack(time.Now())
	res := 0
	fmt.Printf("Part 2: %d ", res)
}

func main() {
	fmt.Println("Day N: ")
	fileName := "/Users/jack/Documents/Github/aoc-2020/dayN/N.in"
	data, err := helpers.GetInputStringByLine(fileName)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
