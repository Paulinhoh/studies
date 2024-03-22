public class Ordenacao {

    // -------------------------- quick sort -------------------------------
    // cost:
    static void quickSort(int[] arr, int start_pointer, int end_pointer) {

        if (start_pointer < end_pointer) {
            int indexPivot = partition(arr, start_pointer, end_pointer);

            quickSort(arr, start_pointer, indexPivot - 1);
            quickSort(arr, indexPivot + 1, end_pointer);
        }
    }

    static int partition(int[] arr, int start_pointer, int end_pointer) {

        int pivot = arr[end_pointer];
        int i = start_pointer;

        for (int j = start_pointer; j < end_pointer; j++) {
            if (arr[j] <= pivot) {
                int aux = arr[j];
                arr[j] = arr[i];
                arr[i] = aux;
                i++;
            }
        }

        int aux = arr[i];
        arr[i] = arr[end_pointer];
        arr[end_pointer] = aux;

        return i;
    }

    // -------------------------- merge sort -------------------------------
    // cost:
    static void mergeSort(int[] arr, int start_pointer, int end_pointer) {

        if (end_pointer - start_pointer > 1) {
            int mid_pointer = (end_pointer + start_pointer) / 2;

            mergeSort(arr, start_pointer, mid_pointer);
            mergeSort(arr, mid_pointer, end_pointer);
            merge(arr, start_pointer, mid_pointer, end_pointer);
        }
    }

    static void merge(int[] arr, int start_pointer, int mid_pointer, int end_pointer) {
        // int[] left = { arr[start_pointer], arr[mid_pointer] }; // <corrigir>
        int[] left = new int[mid_pointer];
        int[] right = new int[end_pointer - mid_pointer];

        for (int x = 0; x < mid_pointer; x++) {
            left[x] = arr[x];
        }

        for (int x = mid_pointer; x < end_pointer; x++) {
            right[x-mid_pointer] = arr[x];
        }

        int top_left = 0;
        int top_right = 0;

        for (int k = start_pointer; k < end_pointer; k++) {
            if (top_left >= left.length) {
                arr[k] = right[top_right];
                top_right++;
            } else if (top_right >= right.length) {
                arr[k] = left[top_left];
                top_left++;
            } else if (left[top_left] < right[top_right]) {
                arr[k] = left[top_left];
                top_left++;
            } else {
                arr[k] = right[top_right];
                top_right++;
            }
        }
    }

    // -------------------------- insertion sort -------------------------------
    // cost:
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

    // -------------------------- bubble sort -------------------------------
    // cost:
    static void bubbleSort(int[] arr) {

        int size = arr.length;

        for (int j = 0; j < size - 1; j++) {
            for (int i = 0; i < size - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    int aux = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = aux;
                }
            }
        }
    }

    // -------------------------- selection sort -------------------------------
    // cost:
    static void selectionSort(int[] arr) {

        int size = arr.length;

        for (int j = 0; j < size; j++) {
            int indexMin = j;

            for (int i = j; i < size; i++) {
                if (arr[i] < arr[indexMin]) {
                    indexMin = i;
                }
            }

            if (arr[j] > arr[indexMin]) {
                int aux = arr[j];
                arr[j] = arr[indexMin];
                arr[indexMin] = aux;
            }
        }
    }

    // -------------------------- main -----------------------------------------
    public static void main(String[] args) {

        int[] array = { 3, 9, 2, 5, 1, 7 };

        mergeSort(array, 0, array.length - 1);

        System.out.println("\nOrdened array:");

        for (int x : array) {
            System.out.print(x + " ");
        }
    }
}
