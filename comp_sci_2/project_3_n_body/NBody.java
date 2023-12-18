import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;


public class NBody { // begin class

	/**
	 * @param args
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args) throws FileNotFoundException { // begin main
		
		double G = 6.67 * Math.pow(10, -11);
		double big_t = Double.parseDouble(args[0]); // how long it goes
		double delta_t = Double.parseDouble(args[1]); // how many steps it goes

		String resourceFolder = "resources/";
		String fileName = resourceFolder + args[2];
		FileInputStream fileInputStream = new FileInputStream(fileName);
		System.setIn(fileInputStream);

		// Use StdIn to read from the file.
		int numBodies = StdIn.readInt();
		double universeRadius = StdIn.readDouble();

		// Print out the values read in (remove all this from your final version)
		StdOut.println("big_t          = " + big_t);
		StdOut.println("delta_t        = " + delta_t);
		StdOut.println("numBodies      = " + numBodies);
		StdOut.println("universeRadius = " + universeRadius);
		
		// declare an  array for initial x-position
				double [] x_position = new double[numBodies];
		// declare an array for initial y-position
				double [] y_position = new double[numBodies];
		// declare an array for initial x-velocity
				double [] x_velocity = new double[numBodies];
		// declare an array for initial y-velocity
				double [] y_velocity = new double[numBodies];
		// declare an array for mass of planet
				double [] mass = new double[numBodies];
		// declare an array for pictures 
				String [] gif = new String[numBodies];
		
				
				// so we know array index at zero is one, array index at one is sun, ...
				// what goes in the parentheses for initializing the array is the size you want to make it
		// then  I need to read the data in by going through a loop numBodies times
		for (int i = 0; i < numBodies; i++) { // start of for
			// put initial x-position in  body array
			double x_pos_value = StdIn.readDouble();
			x_position[i] = x_pos_value;
			
			// put initial y-position in body array
			double y_pos_value = StdIn.readDouble();
			y_position[i] = y_pos_value;
			
			// put x-velocity in body array
			double x_vel_value = StdIn.readDouble();
			x_velocity[i] = x_vel_value;
			
			// put y-velocity in body array
			double y_vel_value = StdIn.readDouble();
			y_velocity[i] = y_vel_value;
			
			// put mass in body array
			double mass_value = StdIn.readDouble();
			mass[i] = mass_value;
			
			// put pic in body  array
			String picture = StdIn.readString();
			gif[i] = picture;
			
			
		} // end of for
		
		// putting up background picture
		// need to set the scale for the universe
		StdDraw.setXscale(-universeRadius, universeRadius); // it is negative because it is a radius
		StdDraw.setYscale(-universeRadius, universeRadius);
		StdDraw.enableDoubleBuffering();
		
		// put a picture in, background picture
		StdDraw.picture(0, 0, "resources/starfield.jpg"); // because it is in the resources folder
		
		//PAIRWISE FORCE SECTION
		
		// now start calculating deltax and deltay
		// deltax and deltay are the difference between x position and y position between each planet
		
		
		// THIS IS ONE ITERATION
		// has to go on bigT iterations
		
		// double [] force = new double[numBodies];
		double [] force_y = new double[numBodies];
		double [] force_x = new double[numBodies];
		
		double time_step = 0;
		
		while(time_step <= big_t) { // begin while
		// pairwise loop
		for (int i = 0; i < numBodies; i++) { // start for 1
			force_x[i]= 0;
			force_y[i] = 0;
			// force_y[i] = 0;
			for (int j = 0; j < numBodies; j++) { // start for 2
				if (i != j) { // start if
					double delta_x_value = x_position[j] - x_position[i];
					
					// calc delta_y
					double delta_y_value = y_position[j] - y_position[i];
					
					// calc r
					double r_value = Math.sqrt(Math.pow(delta_x_value, 2) + Math.pow(delta_y_value, 2));
					
					// calc Force
					double force_value = (G * mass[i] * mass[j]) / Math.pow(r_value, 2);
					
					// calc F_y; store then in single array
					double force_y_value = force_value * (delta_y_value / r_value);
					force_y[i] += force_y_value;
					
					// calc F_x; store them in single array
					double force_x_value = force_value * (delta_x_value / r_value);
					force_x[i] += force_x_value;
					
				} // end if
			} // end for 2
		} // end for 1
		
		// for each body,  calculate the acceleration and net force
		// from acceleration, you can calculate velocity
		// from velocity, you can calculate its new position
		
		// force for each of the bodies
		// this loop is a force calculator
		
		
		for (int i = 0; i < numBodies; i++) { // start for 2
			// single body operation
			// calc acceleration x for each of the bodies given force x
			
			double acc_x_value = force_x[i] / mass[i];
			
			// calc acceleration y for each of the bodies given force y
			
			double acc_y_value = force_y[i] / mass[i];

			// calc new velocity v_x
			double x_velo_value =  delta_t * acc_x_value;
			x_velocity[i] += x_velo_value;
			
			// calc new velocity v_y
			double y_velo_value =  delta_t * acc_y_value;
			y_velocity[i] += y_velo_value;
			
			// calc new position x for each of the bodies, update x_position[i]
			double pos_x_value = x_velocity[i] * delta_t;
			x_position[i] += pos_x_value;
			
			// calc new position y for each of the bodies, update y_position[i]
			double pos_y_value = y_velocity[i] * delta_t;
			y_position[i] += pos_y_value;
			
		} // end for 2
	
		
		// we have now new position X and Y for each of the bodies
		// now I can draw the picture
		// redraw the background picture again
		
		StdDraw.clear();
		StdDraw.picture(0, 0, "resources/starfield.jpg"); // because it is in the resources folder
		
		// for each of the bodies given position x and position y, I redraw it
		for(int i = 0; i < numBodies; i++) { // start for 3
			// for each of the bodies, given x_position[i] and y_position[i], draw that body
			// stdDraw(position x, position y, what the picture is)
			StdDraw.picture(x_position[i], y_position[i], "resources/" + gif[i]);
			StdDraw.show(); // show that picture for 30 seconds
		 } // end for 3
		StdDraw.pause(30);
		
		time_step += delta_t;
		
		} // end big while
		
		
		
		// print out the final state of the universe meaning:
		// print out the final position "x", position "y", vel "x", vel "y", mass, picture

		// printing out final state of 
		
		for(int i = 0; i < numBodies; i++) { // start 4th for loop
			System.out.println(x_position[i]);
			System.out.println(y_position[i]);
			System.out.println(x_velocity[i]);
			System.out.println(y_velocity[i]);
			System.out.println(mass[i]);
			System.out.println(gif[i]);
		} // end 4th for loop
		
		
		
		
		
		
	} // end main 
} // end class
