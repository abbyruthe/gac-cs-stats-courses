public class Sierpinski {
	
	/**
	 * Draws bunches of triangles within triangles.
	 * <p>
	 * If the level is zero, draws one filled triangle; otherwise, draws three:
	 * one each at the top, bottom right and bottom left of the triangle
	 * <p>
	 * @param x0
	 * @param y0
	 * @param x1
	 * @param y1
	 * @param x2
	 * @param y2
	 * @param level
	 */
	static void sierpinski(double x0, double y0, double x1, double y1, double x2, double y2, int level) {
		if (level == 0) triangle( x0, y0, x1, y1, x2, y2 );
		else { // start recursive else
			double x4 = (x0 +x1)/2;
			double y4 = (y0 +y1)/2;
			double x5 = (x1 +x2)/2;
			double y5 = (y1 +y2)/2;
			double x6 = (x2 +x0)/2;
			double y6 = (y2 +y0)/2;
			sierpinski(x0, y0, x4, y4, x6, y6, level-1); // draws a triangle at the top
			sierpinski(x4, y4, x1, y1, x5, y5, level-1); // draws a triangle at the bottom right
			sierpinski(x6, y6, x5, y5, x2, y2, level-1); // draws a triangle at the bottom left
		} // end recursive else
	}
	
	/**
	 * Draws a filled triangle.
	 * <p>
	 * @param x0
	 * @param y0
	 * @param x1
	 * @param y1
	 * @param x2
	 * @param y2
	 */
	public static void triangle(double x0, double y0, double x1, double y1, double x2, double y2) {
		double[] x = { x0, x1, x2 }; double[] y = { y0, y1, y2 };
		StdDraw.filledPolygon(x, y);
	}
	
	/**
	 * Calls sierpinski method.
	 * <p>
	 * @param args
	 */
	public static void main(String[] args) {
		sierpinski( 0, 0, 1, 0, .5, .866, 5);
	}
}