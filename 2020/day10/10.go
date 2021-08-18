package main

import (
	"fmt"
	"sort"
	"time"

	"../helpers"
)

func p1(data []int) {
	defer helpers.TimeTrack(time.Now())
	var oneJolt int = 0
	var threeJolt int = 1
	var currentJoltage int = 0
	for _, adapter := range data {
		diff := adapter - currentJoltage
		if diff == 1 {
			oneJolt++
			currentJoltage++
		} else {
			threeJolt++
			currentJoltage += 3
		}
	}
	fmt.Printf("Part 1: %d ", oneJolt*threeJolt)
}

func p2(data []int) {
	defer helpers.TimeTrack(time.Now())

}

func main() {
	fmt.Println("Day 10: Adapter Array")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day10/10.in"
	data, err := helpers.GetInputIntByLine(fileName)
	sort.Ints(data)
	if err != nil {
		panic(err)
	}
	p1(data)
	p2(data)
}
