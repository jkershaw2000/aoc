package main

import (
	"fmt"
	"sort"
	"strconv"
	"time"

	"../helpers"
)

func p1(data []string) []int {
	defer helpers.TimeTrack(time.Now())
	res := make([]int, 1)
	decoding := map[rune]string{'F': "0", 'B': "1", 'L': "0", 'R': "1"}
	for _, barcode := range data {
		row, col := barcode[:7], barcode[7:]
		rowBin, colBin := "", ""
		for _, letter := range row {
			rowBin = rowBin + decoding[letter]
		}
		for _, letter := range col {
			colBin = colBin + decoding[letter]
		}
		rowNum, _ := strconv.ParseInt(rowBin, 2, 64)
		colNum, _ := strconv.ParseInt(colBin, 2, 64)
		res = append(res, (int(rowNum)*8)+int(colNum))
	}
	_, max := helpers.MinMax(res)
	fmt.Printf("Part 1: %d ", max)
	return res
}

func p2(data []string, ids []int) {
	defer helpers.TimeTrack(time.Now())
	var res int
	sort.Ints(ids)
	for i := 0; i < len(ids); i++ {
		if ids[i+1]-ids[i] == 2 {
			res = ids[i] + 1
			break
		}
	}
	fmt.Printf("Part 2: %d ", res)
}

func main() {
	fmt.Println("Day 5: Binary Boarding")
	fileName := "/Users/jack/Documents/Github/aoc-2020/day5/5.in"
	data, err := helpers.GetInputStringByLine(fileName)
	if err != nil {
		panic(err)
	}
	res := p1(data)
	p2(data, res)
}
