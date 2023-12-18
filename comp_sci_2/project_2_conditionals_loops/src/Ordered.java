public class Ordered {

    public static void main(String[] args) {
    int var1 = Integer.parseInt(args[0]); // create variable, allocate space and assign value
    int var2 = Integer.parseInt(args[1]); // creating the variable, allocate space, assign in 1 step
    int var3 = Integer.parseInt(args[2]);
    // (var1 < var2 < var3)||(var1>var2>var3)
    System.out.println(var1<var2 && var2<var3 || var1>var2 && var2>var3);
    }
}