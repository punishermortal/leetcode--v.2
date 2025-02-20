func search(array []byte, n, k int) ([]byte, int) {
	if n == 0 {
		return array, k - 1
	}
	letters := []byte("abc")
    for _, letter := range letters {
		if len(array) > 0 && array[len(array)-1] == letter {
			continue
		}
		new_array := make([]byte, len(array))
		copy(new_array, array)
		new_array = append(new_array, letter)
		found, new_k := search(new_array, n-1, k)
		k = new_k
		if k == 0 {
			return found, new_k
		}
	}
	return []byte{}, k
}
func byte_to_string(arr []byte) string {
    // this convers byte arr to string ... is there better option ?? pls let me know I'm just learning go
	new_string := make([]string, len(arr))
	for _, v := range arr {
		new_string = append(new_string, string(v))

	}
	return strings.Join(new_string, "")
}
func getHappyString(n int, k int) string {
	result, _ := search([]byte{}, n, k)

	return byte_to_string(result)
}