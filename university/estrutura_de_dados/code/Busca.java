public class Busca {

    // ----------------------- binary search -----------------------------------
    // cost: ln(n)
    // log e base 10 <--> ln e base 2
    static int binarySearch(int[] arr, int key, int start_pointer, int end_pointer) {

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

    // ----------------------- main --------------------------------------------
    public static void main(String[] args) {

        int[] array = { 1, 2, 3, 5, 7, 9 };
        int index = 7;

        int search = binarySearch(array, index, 0, array.length - 1);
        System.out.format("-> %d", search);
    }
}