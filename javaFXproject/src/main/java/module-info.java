module com.mycompany.javafxproject {
    requires javafx.controls;
    requires javafx.fxml;

    opens com.mycompany.javafxproject to javafx.fxml;
    exports com.mycompany.javafxproject;
}
