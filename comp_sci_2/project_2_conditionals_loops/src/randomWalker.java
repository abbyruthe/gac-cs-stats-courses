import java.util.Arrays;
import java.util.Random;
public class randomWalker { // start of class

    public static void main(String[] args) { // start of main
    int N = Integer.parseInt(args[0]); // create variable, allocate space and assign value
    int x = 0;
    int y = 0;
    double distance = 0;
    
    for (int j = 0; j < N; j++) { // start for loop
    double direction = Math.random();	
    if (direction >= 0 && direction < 0.25) {// start if
		y++;
	}// end if
	if (direction >= 0.25 && direction < 0.5) {// start if
		x++;
	}// end if
	if (direction >= 0.5 && direction < 0.75) {// start if
		y--;
	}// end if
	else
		x--;
	// writing the coordinates through each iteration
	System.out.println("(" + x + "," + y + ")");;
	
    } // end for loop
    distance = x*x + y*y;
    
    System.out.println(distance);
    } // end of main
} // end of class