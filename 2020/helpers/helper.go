package helpers

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)

func TimeTrack(start time.Time) {
	elapsed := time.Since(start)
	fmt.Printf("in %s.\n", elapsed)
}

func GetInputStringByLine(fileName string) ([]string, error) {
	data, err := ioutil.ReadFile(fileName)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(string(data), "\n")
	var contents []string
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		contents = append(contents, string(line))
	}
	return contents, nil
}

func GetInputIntByLine(fileName string) ([]int, error) {
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

func Find(lst []string, val string) bool {
	for _, str := range lst {
		if str == val {
			return true
		}
	}
	return false
}

func FindInt(lst []int, val int) bool {
	for _, str := range lst {
		if str == val {
			return true
		}
	}
	return false
}

func MinMax(array []int) (int, int) {
	var max int = array[0]
	var min int = array[0]
	for _, value := range array {
		if max < value {
			max = value
		}
		if min > value {
			min = value
		}
	}
	return min, max
}

func Xor(a bool, b bool) bool {
	return (a || b) && !(a && b)
}

func Sum(a []int) int {
	res := 0
	for _, num := range a {
		res = res + num
	}
	return res
}
