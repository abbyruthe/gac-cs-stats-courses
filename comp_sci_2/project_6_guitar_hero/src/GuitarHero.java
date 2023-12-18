public class GuitarHero {
	
	public static void main(String[] args) {
		
		String keyboard = "q2we4r5ty7u8i9op-[=zxdcfvgbnjmk,.;/' ";
		// creating an array of keyboard called keyboard_array
		GuitarString[] keyboard_array = new GuitarString[keyboard.length()];
		
		// calculate the values for all of the characters in the keyboard and put them in the keyboard_array
		for (int i = 0; i < keyboard.length(); i++) {
			keyboard_array[i] = new GuitarString (440 * Math.pow(1.05956,(i - 24)));
		}
		
		// an infinite loop
        while (true) { 

            // check if the user has typed a key; if so, process it   
            if (StdDraw.hasNextKeyTyped()) {
                char key = StdDraw.nextKeyTyped();
                	if (keyboard.indexOf(key) == -1) continue;
                		keyboard_array[keyboard.indexOf(key)].pluck(); 
            }
            
            // compute the superposition of samples
            double sample = 0;
            for(int i = 0; i < keyboard.length(); i++) {
            	sample += keyboard_array[i].sample();
            }

            // play the sample on standard audio
            StdAudio.play(sample);

            // advance the simulation of each guitar string by one step 
            for (int i = 0; i < keyboard.length(); i++) {
            	keyboard_array[i].tic();
            }
        }
     }
	
	
}