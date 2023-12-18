public class RGBtoCMYK { // start class

    public static void main(String[] args) { // start main
    double red = Integer.parseInt(args[0]);
    double green = Integer.parseInt(args[1]);
    double blue = Integer.parseInt(args[2]);
    double white = 0;
    double cyan = 0;
    double magenta = 0;
    double yellow = 0;
    double black = 0;
    
    white = Math.max(Math.max(red/255, green/255), blue/255); 
    if (white == 0) { // start if
    	cyan = 0;
    	magenta = 0;
    	yellow = 0;
    	black = 1;
    } // end if
    else { // start else
    	cyan = (white -(red/255.0))/white;
    	magenta = (white-(green/255.0))/white;
    	yellow = (white-(blue/255.0))/white;
    	black = 1.0 - white;
    } // end else
    System.out.println("cyan = " + cyan);
    System.out.println("magenta = " + magenta);
    System.out.println("yellow = " + yellow);
    System.out.println("black = " + black);
    
    } // end main
} // end class
