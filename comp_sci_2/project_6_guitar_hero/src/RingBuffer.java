import java.util.Arrays;

public class RingBuffer { // start class
	// instance variables
	public double buffer []; // declaring an array buffer
	public int size;
	public int first;
	public int capacity1;
	
	// constructor
	public RingBuffer(int capacity) { // start constructor
		buffer = new double [capacity]; // creating a buffer object with size capacity
		size = 0; // initializing 
		first = 0;
		capacity1 = capacity; // setting capacity1 equal to the input capacity for the constructor
	} // end constructor
	
	public int size() { // return number of items currently in the buffer
		return size;
	}
	
	public boolean isEmpty() { // is the buffer empty (size = 0)?
		return size == 0;
	}
	
	public boolean isFull() { // is the buffer full (size == capacity1)?
		return size == capacity1;
	}
	
	public void enqueue(double item) { // add item to the end
		if (isFull()) throw new IllegalStateException("Queue is full");
		buffer[(first + size)%capacity1] = item;
		size++; // add one to the size
	}
	
	public double dequeue() { // delete and return item from the front
		size--; // subtract one from the size
		if (first == capacity1-1) {
			first = 0;
			return buffer[capacity1-1]; // returning the last element
		}
		double temp = buffer[first]; // creating a temporary variable that catches the value in the buffer[first]
		first++; // add one to first
		return temp; // return that temporary value
		/* the reason you do this is because after a return statement, you cannot do anything else in a method
		 * so you have the catch that value in a variable and then add one to the first variable and then return that
		 * value last
		 */
	}
	
	public double peek() { // return (but do not delete) item from the front
		if (isEmpty()) throw new IllegalStateException ("Queue is empty");
		return buffer[first];
	}
	
	public static void main(String[] args) { // start main
		// I emptied the main method because I did not think it was necessary. I did conduct proper testing though.
	} // end main
	
} // end class