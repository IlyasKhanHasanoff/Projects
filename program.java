import java.util.*;
public class program {
    public static void main(String[] args) {
        sum();
    }

    public static void sum() {
        Scanner input = new Scanner(System.in);
        double[] array = loop(input);
        double add = 0;
        for (int i = 0; i < array.length; i++) {
            add += array[i];
        }
        System.out.println("The Store Will Make $" + add);
        String title = busName(input);
        System.out.println("Store Name: " + title);
        input.close();
    }

    public static void loop(Scanner input) {
        System.out.print("Enter number of Items: ");
        int num = input.nextInt();
        double[] doubles = new double[num];
        for (int i = 0; i < doubles.length; i++) {
            System.out.print("Enter wholesale cost $");
            double wholesaleCost = input.nextDouble();
            System.out.print("Enter markup percentage: ");
            double markUp = (input.nextDouble() / 100) + 1;
            double result = calculateRetail(wholesaleCost, markUp);
            System.out.println("Retail Cost is $" + result);
            doubles[i] = result;
        }
        System.out.println(Arrays.toString(doubles));
        System.out.println("Number of Items: " + num);
    }

    public static double calculateRetail(double wholesaleCost, double markUp) {
        double retail = markUp * wholesaleCost;
        return retail;
    }

    public static String busName(Scanner input) {
        System.out.println("Enter Name of Business: ");
        input.nextLine();
        String name = input.nextLine();
        return name;
    }
}