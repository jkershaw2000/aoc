package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func getInput(fileName string) ([]int, error) {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(data), "\n")
	var nums []int
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		num, err := strconv.Atoi(line)
		if err != nil {
			return nil, err
		}
		nums = append(nums, num)
	}
	return nums, nil
}

func p1(data []int) int {
	var res int
	for ki, i := range data {
		for kj, j := range data {
			if ki != kj && i+j == 2020 {
				res = i * j
				return res
			}
		}
	}
	return res
}

func p2(data []int) int {
	var res int
	for ki, i := range data {
		for kj, j := range data {
			for kx, x := range data {
				if ki != kj && kj != kx && i+j+x == 2020 {
					res = i * j * x
					return res
				}
			}
		}
	}
	return res
}

func main() {
	fileName := "/Users/jack/Documents/Github/aoc-2020/day1/1.in"
	data, err := getInput(fileName)
	if err != nil {
		panic(err)
	}
	fmt.Println(p1(data))
	fmt.Println(p2(data))
}
