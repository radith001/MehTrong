import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

public class HelloJavaFX extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Membuat tombol
        Button btn = new Button();
        btn.setText("Say 'Hello World'");

        // Menambahkan aksi pada tombol
        btn.setOnAction(event -> System.out.println("Hello, World!"));

        // Mengatur layout
        StackPane root = new StackPane();
        root.getChildren().add(btn);

        // Membuat scene
        Scene scene = new Scene(root, 300, 250);

        // Mengatur stage
        primaryStage.setTitle("Hello JavaFX!");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);  // Memanggil metode launch() dari Application
    }
}
