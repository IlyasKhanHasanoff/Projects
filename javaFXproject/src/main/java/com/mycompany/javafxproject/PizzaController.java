package com.mycompany.javafxproject;
import javafx.application.Platform;
import javafx.fxml.FXML;
import javafx.scene.control.*;

public class PizzaController {

    @FXML
    private RadioButton rbHawaiian;
    @FXML
    private RadioButton rbBrooklyn;
    @FXML
    private RadioButton rbAustralian;
    @FXML
    private ToggleGroup tgType;
    @FXML
    private Label lblQuantity;
    @FXML
    private TextField tfQuantity;
    @FXML
    private Label lblSize;
    @FXML
    private ChoiceBox<String> cbSize;
    @FXML
    private TextArea taSummary;
    @FXML
    private TextField tfUsername; // Added TextField for username
    @FXML
    private TextField tfAge; // Added TextField for age

    // Define pizza prices
    private static final double SMALL_HAWAIIAN_PRICE = 12.99;
    private static final double MEDIUM_HAWAIIAN_PRICE = 15.99;
    private static final double LARGE_HAWAIIAN_PRICE = 18.99;
    private static final double SMALL_BROOKLYN_PRICE = 11.99;
    private static final double MEDIUM_BROOKLYN_PRICE = 14.99;
    private static final double LARGE_BROOKLYN_PRICE = 17.99;
    private static final double SMALL_AUSTRALIAN_PRICE = 10.99;
    private static final double MEDIUM_AUSTRALIAN_PRICE = 13.99;
    private static final double LARGE_AUSTRALIAN_PRICE = 16.99;

    @FXML
    private void initialize() {
        // Initialize the pizza size options in the ChoiceBox
        cbSize.getItems().addAll("Small", "Medium", "Large");
        cbSize.setValue("Small"); // Set the default size
    }

    @FXML
    private void handleOrderButtonAction() {
        String pizzaType = getSelectedPizzaType();
        int quantity = Integer.parseInt(tfQuantity.getText());
        String size = cbSize.getValue();
        String username = tfUsername.getText(); // Get the username input
        String age = tfAge.getText(); // Get the age input

        double price;
        String pizzaName = "";
        switch (pizzaType) {
            case "Hawaiian":
                pizzaName = "Hawaiian";
                price = getPizzaPrice(pizzaName, size);
                break;
            case "Brooklyn":
                pizzaName = "Brooklyn";
                price = getPizzaPrice(pizzaName, size);
                break;
            case "Australian":
                pizzaName = "Australian";
                price = getPizzaPrice(pizzaName, size);
                break;
            default:
                pizzaName = "Unknown";
                price = 0.0;
        }

        double totalCost = price * quantity;

        // Construct the order summary
        String orderSummary = "Username: " + username + "\n" // Add username
                + "Age: " + age + "\n" // Add age
                + "Pizza Type: " + pizzaName + "\n"
                + "Size: " + size + "\n"
                + "Quantity: " + quantity + "\n"
                + "Price: $" + String.format("%.2f", price) + "\n"
                + "Total Cost: $" + String.format("%.2f", totalCost) + "\n";

        // Append the order summary to the existing text in taSummary using Platform.runLater
        Platform.runLater(() -> taSummary.appendText(orderSummary));
    }

    @FXML
    private void handleResetButtonAction() {
        // Handle the reset button click event
        tfQuantity.clear();
        tfUsername.clear();
        tfAge.clear();
        taSummary.clear();
    }

    private String getSelectedPizzaType() {
        if (rbHawaiian.isSelected()) {
            return "Hawaiian";
        } else if (rbBrooklyn.isSelected()) {
            return "Brooklyn";
        } else if (rbAustralian.isSelected()) {
            return "Australian";
        } else {
            return "Unknown";
        }
    }

    private double getPizzaPrice(String pizzaType, String size) {
        double price;
        switch (size) {
            case "Small":
                price = (pizzaType.equals("Hawaiian")) ? SMALL_HAWAIIAN_PRICE
                        : (pizzaType.equals("Brooklyn")) ? SMALL_BROOKLYN_PRICE
                        : (pizzaType.equals("Australian")) ? SMALL_AUSTRALIAN_PRICE : 0.0;
                break;
            case "Medium":
                price = (pizzaType.equals("Hawaiian")) ? MEDIUM_HAWAIIAN_PRICE
                        : (pizzaType.equals("Brooklyn")) ? MEDIUM_BROOKLYN_PRICE
                        : (pizzaType.equals("Australian")) ? MEDIUM_AUSTRALIAN_PRICE : 0.0;
                break;
            case "Large":
                price = (pizzaType.equals("Hawaiian")) ? LARGE_HAWAIIAN_PRICE
                        : (pizzaType.equals("Brooklyn")) ? LARGE_BROOKLYN_PRICE
                        : (pizzaType.equals("Australian")) ? LARGE_AUSTRALIAN_PRICE : 0.0;
                break;
            default:
                price = 0.0;
        }

        return price;
    }
}
