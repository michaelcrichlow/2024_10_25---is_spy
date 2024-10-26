package test

import "core:fmt"
import "core:math"
print :: fmt.println

main :: proc() {

	print(is_spy(1124))

	// OUTPUT:
	// true
}

is_spy :: proc(n: int) -> bool {
	test_val := n
	rem: int
	local_array: [dynamic]int
	defer delete(local_array)

	for test_val != 0 {
		test_val, rem = math.divmod(test_val, 10)
		append(&local_array, rem)
	}

	return sum_iterable(local_array[:]) == product(local_array[:])
}
