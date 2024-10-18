package main

import (
	"fmt"
	"sort"
	"strings"
)

type pair struct {
	count     int
	character rune
}

func longestDiverseString(a int, b int, c int) string {
	var happy_string strings.Builder

	counts := []pair{
		{count: a, character: 'a'},
		{count: b, character: 'b'},
		{count: c, character: 'c'},
	}

	for {
		sort.Slice(counts, func(i, j int) bool {
			return counts[i].count > counts[j].count
		})

		added := false

		for i := 0; i < len(counts); i++ {
			n := happy_string.Len()
			if counts[i].count == 0 {
				continue
			}

			if n >= 2 &&
				happy_string.String()[n-1] == byte(counts[i].character) &&
				happy_string.String()[n-2] == byte(counts[i].character) {
				continue
			}

			happy_string.WriteRune(counts[i].character)
			counts[i].count--
			added = true
			break
		}

		if !added {
			break
		}
	}

	return happy_string.String()

	// var letterRunes = []rune("abc")
	// result := a + b + c
	// var happy string
	// happy_rune := make([]rune, result)

	// fmt.Println(happy_rune[0])
	// fmt.Println(happy_rune[2])

	// for i := 0; i < result; i++ {
	// 	if happy_rune[i-1] == happy_rune[i] || happy_rune[i] == happy_rune[i+1] {
	// 		happy_rune[i] = letterRunes[rand.Intn(len(letterRunes))]
	// 	}
	// 	happy += string(letterRunes[rand.Intn(len(letterRunes))])
	// 	n := happy_string.Len()

	// 	happy_rune[i] = letterRunes[rand.Intn(len(letterRunes))]
	// 	happy_string.WriteRune(letterRunes[rand.Intn(len(letterRunes))])

	// 	if n >= 2 &&
	// 		happy_string.String()[n-1] == byte(counts[i].character) &&
	// 		happy_string.String()[n-2] == byte(counts[i].character) {
	// 		continue
	// 	}
	// }
	// return string(happy_rune)
}

func main() {
	fmt.Println(longestDiverseString(1, 1, 7))
}
