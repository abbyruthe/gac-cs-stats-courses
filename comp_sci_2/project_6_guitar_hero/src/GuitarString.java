import java.util.Arrays;

public class GuitarString { // start main
	// instance variables
	int n;
	public RingBuffer b; // declaring an object that is type RingBuffer so it has all the methods that a RingBuffer
	// object would have to be used later
	int tic1;
	
	
	
	// constructor 1
	// create a guitar string of the given frequency, using a sampling rate of 44,100
	public GuitarString(double frequency) { // start constructor 1
		n = (int)Math.ceil(44100 / frequency); // used Math.ceil to round the value of n up to the nearest integer
		// then a cast the value of n as an int using (int)
		b = new RingBuffer(n); // creating b
		for (int i = 0; i < b.capacity1; i++) {
			b.enqueue(0); // filling the RingBuffer object b array with all zeros initially
		}
		tic1 = 0; // initializing the tic11 object utilized later
	} // end constructor 1
	
	// constructor 2
	// create a guitar string whose size and initial values are given by the array
	public GuitarString(double[] init) { // start constructor
		b = new RingBuffer(init.length); // creating the RingBuffer object b with the size of b being the size of the
		// parameter given
		b.buffer = init; // initializes RingBuffer object buffer (the array itself) with all the values in the init array
		tic1 = 0; // again, initializing the tic1 object
		} // end constructor 2
	
	// having two different constructors is an example of overloading with different type of input values
	
	
	
	// various methods
	// replaces the N items in the ring buffer with N random value between -0.5 and +0.5
	public void pluck() { 
		for (int i = 0; i < b.size; i++) { // start for
			double value = Math.random();
			value = value-0.5;
			b.dequeue(); // take out the original value in buffer[i]
			b.enqueue(value); // replace with a random double between -0.5 and 0.5 
		} // end for
	}
	
	// advance the simulation one time step
	public void tic() {
		double delete = b.dequeue(); // removes the first value of the buffer array
		double var3 = (b.peek() + delete)/2 * 0.994; // value found on the cs website for the energy decay factor
		b.enqueue(var3); // add var3 to the first of the buffer array
		tic1++; // everytime we go through this method, we add 1 to the variable "tic" for a later method
	}
	
	public double sample() { // return (but do not delete) item from the front
		if (b.isEmpty()) throw new IllegalStateException ("Buffer is empty");
		return b.peek();
	}
	
	// return the number of times that the tic method was run
	public int time() {
		return tic1; 
	}
	
	public static void main(String[] args) { // start main
		// empty, but did adequate testing
	} // end main
	
	
} // end main