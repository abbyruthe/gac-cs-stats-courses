import java.io.FileInputStream;
import java.util.Arrays;
public class EditDistance {
	


	
	public static void main(String[] args) { // start of main
		
		try { // start try

	        System.setIn(new FileInputStream("resources/" + args[0]));

	    } // end try
	    catch (Exception e) { // start catch

	        System.err.printf("Exception caught: %s\n", e.toString());

	        System.exit(0);

	    } // end catch


	    String x = StdIn.readLine();

	    String y = StdIn.readLine();



	    printEditDistance(x, y);
	    
	   
	    // String x = randomDNAString(12);

	    // String y = randomDNAString(12);

	    // System.out.println(x);
	    // System.out.println(y);
	    
	    System.out.println(editDistance(x,y));
	    
	    
	    System.out.println(recursiveEditDistance(x, y));
	    
	    timeRecursiveEditDistance(x,y);
	    
	    timeEditDistance(x,y);
	    
	    System.out.println(randomDNAString(5));
	    
	    
	    
	} // end of main
	
	
	
	private static int recursiveEditDistance(String x, String y) { // start recursion method
		
		return recursiveEditDistance2(x,y, 0, 0);
		
		
	} // end recursion method
	
	private static int recursiveEditDistance2(String x, String y, int i, int j) { // start recursion method
		
		if (i == x.length()) {
			return (y.length()-j) *2;
		}
		else if (j == y.length()) {
			return (x.length()-i) *2;
		}
		else {
			int option1 = recursiveEditDistance2(x,y,i+1,j)+2;
			int option2 = recursiveEditDistance2(x,y,i,j+1)+2;
			int option3 = recursiveEditDistance2(x,y,i+1,j+1);
			if(x.charAt(i) != y.charAt(j)) option3 += 1;
			return Math.min(option1, Math.min(option2, option3));
		}
		
	} // end recursion method
	
	/**

	 * @param x a non-null String

	 * @param y a non-null String

	 * @return the the edit distance between x and y

	 * 

	 * This procedure should use dynamic programming to compute the edit distance

	 */

	private static int editDistance(String x, String y) { // start editDistance
		int[][] table = makeTable(x,y);
		return table[0][0];
	} // end editDistance

	public static int[][] makeTable(String x, String y){
		int[][] opt = new int[x.length() + 1][y.length() + 1];
		for (int i = x.length(); i >= 0; i--) { // start i for 
			for (int j = y.length(); j >= 0; j--) { // start j for
				
				// base cases
				if (i == x.length()) { // start base case if 
					opt[i][j] = (y.length()-j)*2;
				} // end base case if
				
				else if (j == y.length()) { // start base else if 
					opt[i][j] = (x.length()-i)*2;
				} // end base case else if
				
				
				else { // begin else
					// has to be a mismatch and both cannot be gaps
					int option1 = opt[i+1][j+1];
					int option2 = opt[i+1][j] + 2;
					int option3 = opt[i][j+1] + 2;
					if (x.charAt(i) != y.charAt(j)) {
						option1 += 1;
					}
					opt[i][j] = Math.min(option1, Math.min(option2, option3));
				} // end big else
			} // end j for
		} // end i for
		return opt;
	}

	/**

	 * @param x a non-null String

	 * @param y a non-null String

	 * 

	 * This procedure should use dynamic programming to compute the edit distance

	 * and print it and an optimal alignment in the vertical format shown in the

	 * project assignment.

	 * NOTE: There may be multiple optimal alignments.

	 *       This procedure needs to print one optimal alignment.

	 */

	private static void printEditDistance(String x, String y) { // start printEditDistance
		int[][] table = makeTable(x,y);
		int i = 0;
		int j = 0;
		while(true){
			if(i == x.length() && j == y.length()) break;
			else if (i == x.length()) System.out.println("- " + y.charAt(j) + " 2");
			else if (j == y.length()) System.out.println(x.charAt(j) + " -" + " 2");
			else if (table[i][j] == table[i][j+1] + 2) { 
				System.out.println(x.charAt(j) + " -" + " 2");
				j++;
				}
			else if (table[i][j] == table[i+1][j] + 2) {
				System.out.println("- " + y.charAt(j) + " 2");
				i++;
				}
			else {
				if(x.charAt(i) == y.charAt(j)) System.out.println(x.charAt(i) + " " + y.charAt(j) + " " + 0);
				else System.out.println(x.charAt(i) + " " + y.charAt(j) + " " + 1);
				i++;
				j++;
			}
		}
	} // end printEditDistance

	  

	/**

	 * @param x a non-null String

	 * @param y a non-null String

	 * 

	 * Prints out the edit distance between x and y and the time taken to compute it

	 * using the recursive version recursiveEditDistance

	 */

	public static void timeRecursiveEditDistance(String x, String y) { // start timeRecursiveEditDistance
		Stopwatch watch = new Stopwatch();
		System.out.println(recursiveEditDistance(x,y));
		double timeSpent = watch.elapsedTime();
		System.out.println(timeSpent);
	} // end timeRecursiveEditDistance

	/**

	 * @param x a non-null String

	 * @param y a non-null String

	 * 

	 * Prints out the edit distance between x and y and the time taken to compute it

	 * using the dynamic programming version editDistance

	 */

	public static void timeEditDistance(String x, String y) { // start timeEditDistance
		Stopwatch watch1 = new Stopwatch();
		System.out.println(editDistance(x,y));
		double timeSpent1 = watch1.elapsedTime();
		System.out.println(timeSpent1);
	} // end timeEditDistance

	/**

	 * @param dnaLength a non-negative int

	 * @return a random String of length dnaLength comprised of the four chars A, T, G, and C

	 */

	
	public static String randomDNAString(int dnaLength) { // start randomDNAString
		String str1 = "";
		for (int i = 0; i < dnaLength; i++) { // start for
			double value = Math.random();
			if (value < 0.25) str1 += "A";
			else if (value < 0.5) str1 += "T";
			else if (value < 0.75) str1 += "G";
			else str1 += "C";
		} // end for
		
		return str1;
	} // end randomDNAString
	
	
} // end class

