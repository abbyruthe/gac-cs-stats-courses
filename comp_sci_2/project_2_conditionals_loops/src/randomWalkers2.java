import java.util.Arrays;
import java.util.Random;

public class randomWalkers2 { // start of class

	public static void main(String[] args) { // start of main
		int N = Integer.parseInt(args[0]); // create variable, allocate space and assign value
		int T = Integer.parseInt(args[1]);
		int x = 0;
		int y = 0;
		double total = 0;
		double msd = 0;
		double average_squared_distance = 0;

		for (int i = 0; i < T; i++) { // start for loop 2
			x = 0;
			y = 0;

			for (int j = 0; j < N; j++) { // start for loop
				double direction = Math.random();
				if (direction >= 0 && direction < 0.25) {// start if
					y++;
				} // end if
				if (direction >= 0.25 && direction < 0.5) {// start if
					x++;
				} // end if
				if (direction >= 0.5 && direction < 0.75) {// start if
					y--;
				} // end if
				else
					x--;
				// writing the coordinates through each iteration

			} // end j for loop
			msd = Math.pow(x, 2) + Math.pow(y, 2);
			System.out.println(msd);
			total += msd;

		} // end for loop 2
		average_squared_distance = total / T;
		System.out.println("average squared distance = " + average_squared_distance);

	} // end of main
} // end of class