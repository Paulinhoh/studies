public class Test {
    static void mergeSort(int[] arr, int end_pointer) {
        if (end_pointer < 2) {
            return;
        }
        int mid = end_pointer / 2;
        int[] l = new int[mid];
        int[] r = new int[end_pointer - mid];

        for (int i = 0; i < mid; i++) {
            l[i] = arr[i];
        }
        for (int i = mid; i < end_pointer; i++) {
            r[i - mid] = arr[i];
        }
        mergeSort(l, mid);
        mergeSort(r, end_pointer - mid);

        merge(arr, l, r, mid, end_pointer - mid);
    }

    static void merge(int[] arr, int[] l, int[] r, int left, int right) {
        int i = 0, j = 0, k = 0;
        while (i < left && j < right) {
            if (l[i] <= r[j]) {
                arr[k++] = l[i++];
            } else {
                arr[k++] = r[j++];
            }
        }
        while (i < left) {
            arr[k++] = l[i++];
        }
        while (j < right) {
            arr[k++] = r[j++];
        }
    }

    static void insertionSort(int[] arr) {
        int size = arr.length;

        for (int i = 1; i < size; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] array = { 3, 9, 2, 5, 1, 7 };

        insertionSort(array);

        System.out.println("\nOrdened array:");

        for (int x : array) {
            System.out.print(x + " ");
        }
    }
}