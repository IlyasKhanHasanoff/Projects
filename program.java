import java.util.*;
public class program {
	static Scanner input = new Scanner(System.in);
  
    public static void main(String[] args) {
        sum();
    }
    public static double test() {
        System.out.print("Enter wholesale cost $");
        double wholesaleCost = input.nextDouble();
        System.out.print("Enter markup precentage: ");
        double markUp = (input.nextDouble()/100) + 1;
        double result = calculateRetail(wholesaleCost, markUp);
        System.out.println("Retail Cost is $"+result);
        return result;
    }
    public static double calculateRetail(double markUp, double wholesaleCost) {
        double retail = markUp * wholesaleCost;
        return retail;
    }
    public static double[] loop() {
        System.out.print("Enter number of Items: ");
        int num = input.nextInt();
        double[] doubles = new double[num];
        for(int i = 0; i < doubles.length; i++){
            double run = test();
            doubles[i] = run;
        }
        System.out.println(Arrays.toString(doubles));
        System.out.println("Number of Items: "+num);
        return doubles;
    }
    public static double sum(){
        double[] array = loop();
        double add = 0;
        for(int i=0; i < array.length; i++){
            add = add += array[i];
         }
         System.out.println("The Store Will Make $"+ add);
         String title = busName();
         System.out.println("Store Name:"+ title);
         return add;

    }
    public static String busName(){
        System.out.println("Enter Name of Business: ");
        input.nextLine();
        String name = input.nextLine();
        return name;
    }
}
