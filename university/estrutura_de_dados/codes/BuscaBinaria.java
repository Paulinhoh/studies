// Custo: ln(n)
public class BuscaBinaria {
    public static int binarySearch(int[] arr, int key, int start_pointer, int end_pointer) {

        while (start_pointer <= end_pointer) {
            int mid_pointer = (start_pointer + end_pointer) / 2;

            if (key < arr[mid_pointer]) {
                return binarySearch(arr, key, start_pointer, mid_pointer - 1);
            } else if (key > arr[mid_pointer]) {
                return binarySearch(arr, key, mid_pointer + 1, end_pointer);
            } else {
                return mid_pointer;
            }
        }
        return -1;
    }
}