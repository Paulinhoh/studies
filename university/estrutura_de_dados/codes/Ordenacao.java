public class Ordenacao {
    // -------------------------- counting sort --------------------------------
    // Custo: O(n)
    public static void countSort(int[] arr, int size) {
        int[] output = new int[size + 1];

        int max = arr[0];
        for (int i = 1; i < size; i++) {
            if (arr[i] > max)
                max = arr[i];
        }
        int[] count = new int[max + 1];

        for (int i = 0; i < max; ++i) {
            count[i] = 0;
        }

        for (int i = 0; i < size; i++) {
            count[arr[i]]++;
        }

        for (int i = 1; i <= max; i++) {
            count[i] += count[i - 1];
        }

        for (int i = size - 1; i >= 0; i--) {
            output[count[arr[i]] - 1] = arr[i];
            count[arr[i]]--;
        }

        for (int i = 0; i < size; i++) {
            arr[i] = output[i];
        }
    }

    // -------------------------- quick sort -----------------------------------
    // Custo: O(n*log(n)) --> pivo aleatorio | O(n²) --> pivo ultimo elemento
    public static void quickSort(int[] arr, int start_pointer, int end_pointer) {
        if (start_pointer < end_pointer) {
            int indexPivot = partition(arr, start_pointer, end_pointer);

            quickSort(arr, start_pointer, indexPivot - 1);
            quickSort(arr, indexPivot + 1, end_pointer);
        }
    }

    private static int partition(int[] arr, int start_pointer, int end_pointer) {
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
    // Custo: O(n*log(n))
    public static void mergeSort(int[] arr, int end_pointer) {
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

    private static void merge(int[] arr, int[] l, int[] r, int left, int right) {
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

    // -------------------------- insertion sort -------------------------------
    // Custo: O(n²)
    public static void insertionSort(int[] arr) {
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
    // Custo: O(n²)
    public static void bubbleSort(int[] arr) {
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
    // Custo: O(n²)
    public static void selectionSort(int[] arr) {
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
}
