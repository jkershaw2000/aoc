package main

import (
	"fmt"
	"time"

	"../helpers"
)

func p1(data []int) int {
	defer helpers.TimeTrack(time.Now())
	res := -1
	for i := 25; i < len(data)-25; i++ {
		sums := getAllSums(data[i-25 : i])
		if !helpers.FindInt(sums, data[i]) {
			res = data[i]
			break
		}
	}
	fmt.Printf("Part 1: %d ", res)
	return res
}

func p2Brute(data []int, ans int) {
	defer helpers.TimeTrack(time.Now())
	length := len(data)
	var res int
	for i := 0; i < length; i++ {
		for j := i + 1; j < length; j++ {
			res = helpers.Sum(data[i:j])
			if res == ans {
				min, max := helpers.MinMax(data[i:j])
				fmt.Printf("Part 2: %d ", (min + max))
				return
			} else if res > ans {
				break
			}
		}
	}

}

func getAllSums(lst []int) []int {
	var res []int
	pairs := getPairs(lst)
	for _, pair := range pairs {
		res = append(res, pair[0]+pair[1])
	}
	return removeDuplicates(res)
}

func getPairs(lst []int) [][]int {
	var pairs [][]int
	for i := 0; i < len(lst); i++ {
		for j := i + 1; j < len(lst); j++ {
			pairs = append(pairs, []int{lst[i], lst[j]})
		}
	}
	return pairs
}

func removeDuplicates(lst []int) []int {
	var res []int
	for _, val := range lst {
		if !(helpers.FindInt(res, val)) {
			res = append(res, val)
		}
	}
	return res
}

func p2(data []int, ans int) {
	defer helpers.TimeTrack(time.Now())
	i, j := 0, 1
	sum := data[i] + data[j]
	for sum != ans {
		for sum < ans {
			j++
			sum += data[j]
		}
		for sum > ans {
			sum -= data[i]
			i++
		}
	}
	min, max := helpers.MinMax(data[i:j])
	fmt.Printf("Part 2: %d ", (min + max))
}

func main() {
	fmt.Println("Day 9: ")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day9/9.in"
	data, err := helpers.GetInputIntByLine(fileName)
	if err != nil {
		panic(err)
	}
	part1 := p1(data)
	p2Brute(data, part1)
	p2(data, part1)
}
