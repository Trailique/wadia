import java.util.ArrayList;
import java.util.Scanner;

public class Array {
   
    private ArrayList<Integer> al;

    public Array(int capacity) {
        al = new ArrayList<>(capacity);
    }

    //accepts index as an arg and returns the element at that index
    public int get(int index) {
        if(index >=0 && index < al.size()) {
            return al.get(index);
        } else {
            throw new IndexOutOfBoundsException("Index out of Bound");
        }
    }

    //accepts value nd sets the value at that index
    public void set(int index, int value) {
        if(index >= 0 && index < al.size()) {
            al.set(index, value);
        } else {
            throw new IndexOutOfBoundsException("Index out of Bound");
        }
    }

    //returns the last element of the array without removing it
    public int peek() {
        if(!al.isEmpty()) {
            return al.get(al.size() - 1);
        } else {
            throw new IndexOutOfBoundsException("Array is Empty");
        }
    }

    //reurns the size
    public int size() {
        return al.size();
    }

    //checks for empty array 
    public boolean isEmpty() {
        return al.isEmpty();
    }

    //appends the element in the array
    public void append(int value) {
        al.add(value);
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter initial capacity: ");
        int capacity = sc.nextInt();
        Array list = new Array(capacity);

        System.out.println("Enter the elements : ");
        sc.nextLine();
        String[] elements = sc.nextLine().split(" "); //it will read the input containing the space and aplits it into an array of strings

        for (String element : elements) {
            list.append(Integer.parseInt(element));
        } //will covert array of list to int

        System.out.println("Size: " + list.size());
        System.out.println("Last element: " + list.peek());

        System.out.print("Enter index to get value: ");
        int index = sc.nextInt();
        try {
            System.out.println("Element at index " + index + ": " + list.get(index));
        } catch (IndexOutOfBoundsException e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Is array empty? " + list.isEmpty());

        sc.close();
    }

}
