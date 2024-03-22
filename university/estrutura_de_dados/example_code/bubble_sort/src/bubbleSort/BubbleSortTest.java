package bubbleSort;

public class BubbleSortTest {

	public static void main(String args[])
	{
		
		int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
		
		int n = arr.length;
				
		BubbleSort.bubbleSort(arr, n);
		
		System.out.println("Sorted array: ");
		
		BubbleSort.printArray(arr, n);
	}
	
}
