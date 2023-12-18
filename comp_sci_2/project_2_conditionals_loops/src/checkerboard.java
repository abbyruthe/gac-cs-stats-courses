public class checkerboard {

	public static void main(String[] args) {
		int n = Integer.parseInt(args[0]);
		for (int i = 1; i <= n; i++) { // start big for loop
			for (int j = 1; j <= n; j++) { // start little loop
				if (i % 2 == 0)
					System.out.print(" *");
				else
					System.out.print("* ");
			} // end little loop
			System.out.println("");
		} // end big for loop
	}
}