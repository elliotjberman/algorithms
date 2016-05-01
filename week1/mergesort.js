function mergesort(array){
	if (array.length > 1){

		var middle = Math.floor(array.length/2);
		var firstHalf = array.slice(0, middle);
		var lastHalf = array.slice(middle, array.length);

		mergesort(firstHalf);
		mergesort(lastHalf);

		var i = 0;
		var j = 0;
		var k = 0;

		while (i < firstHalf.length && j < lastHalf.length) {
			if (firstHalf[i] < lastHalf[j]) {
				array[k] = firstHalf[i];
				i++;
			}
			else {
				array[k] = lastHalf[j];
				j++;
			}
			k++;
		}

		while (i < firstHalf.length) {
			array[k] = firstHalf[i];
			i++;
			k++;
		}

		while (j < lastHalf.length) {
			array[k] = lastHalf[j];
			j++;
			k++;
		}

	}

	return array

}

var stanfordArray = [5, 4, 1, 8, 7, 2, 6, 3];
console.log(mergesort(stanfordArray));
