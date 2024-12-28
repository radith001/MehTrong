import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.scene.text.Font;
import javafx.scene.text.Text;
import javafx.scene.paint.Color;
import javafx.scene.input.KeyEvent;
import java.text.DecimalFormat;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.HashMap;
import java.util.Map;

public class HotelPaymentApp extends Application {
    private TextField namaPetugasField, namaCustomerField, tglCheckinField, lamaSewaField, uangBayarField;
    private ComboBox<String> kodeKamarCombo;
    private Label totalPembayaranLabel, diskonLabel, ppnLabel;
    private TextArea resultArea;

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Aplikasi Pembayaran Hotel");

        // Root Layout
        VBox root = new VBox(20);
        root.setPadding(new Insets(20));

        // Title
        Text title = new Text("Aplikasi Pembayaran Hotel");
        title.setFont(Font.font("Arial", 24));
        title.setFill(Color.DARKBLUE);
        root.getChildren().add(title);

        // Form layout
        GridPane formGrid = new GridPane();
        formGrid.setVgap(10);
        formGrid.setHgap(10);
        formGrid.setPadding(new Insets(10));

        // Nama Petugas
        formGrid.add(new Label("Nama Petugas:"), 0, 0);
        namaPetugasField = new TextField();
        formGrid.add(namaPetugasField, 1, 0);

        // Nama Customer
        formGrid.add(new Label("Nama Customer:"), 0, 1);
        namaCustomerField = new TextField();
        formGrid.add(namaCustomerField, 1, 1);

        // Tanggal Check-in
        formGrid.add(new Label("Tanggal Check-in (dd/MM/yyyy):"), 0, 2);
        tglCheckinField = new TextField();
        formGrid.add(tglCheckinField, 1, 2);

        // Kode Kamar
        formGrid.add(new Label("Kode Kamar:"), 0, 3);
        kodeKamarCombo = new ComboBox<>();
        kodeKamarCombo.getItems().addAll("M - Melati", "S - Sakura", "L - Lily", "A - Anggrek");
        formGrid.add(kodeKamarCombo, 1, 3);

        // Lama Sewa
        formGrid.add(new Label("Lama Sewa (hari):"), 0, 4);
        lamaSewaField = new TextField();
        formGrid.add(lamaSewaField, 1, 4);

        // Uang Bayar
        formGrid.add(new Label("Uang Bayar:"), 0, 5);
        uangBayarField = new TextField();
        formGrid.add(uangBayarField, 1, 5);

        root.getChildren().add(formGrid);

        // Total Pembayaran, Diskon, PPN
        totalPembayaranLabel = new Label("Total Pembayaran: Rp 0");
        diskonLabel = new Label("Diskon: Rp 0");
        ppnLabel = new Label("PPN: Rp 0");

        root.getChildren().addAll(totalPembayaranLabel, diskonLabel, ppnLabel);

        // Buttons
        HBox buttonsBox = new HBox(10);
        buttonsBox.setSpacing(20);
        Button prosesButton = new Button("Proses Pembayaran");
        prosesButton.setOnAction(e -> prosesPembayaran());
        Button clearButton = new Button("Clear");
        clearButton.setOnAction(e -> clearFields());
        buttonsBox.getChildren().addAll(prosesButton, clearButton);

        root.getChildren().add(buttonsBox);

        // Result Area
        resultArea = new TextArea();
        resultArea.setEditable(false);
        resultArea.setPrefHeight(200);
        resultArea.setWrapText(true);
        root.getChildren().add(resultArea);

        // Set Scene
        Scene scene = new Scene(root, 600, 600);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void updateTotalPembayaran() {
        try {
            String kodeKamar = kodeKamarCombo.getValue().split(" ")[0];
            int lamaSewa = Integer.parseInt(lamaSewaField.getText());

            // Harga kamar per malam
            Map<String, Integer> hargaKamar = new HashMap<>();
            hargaKamar.put("M", 650000);
            hargaKamar.put("S", 550000);
            hargaKamar.put("L", 400000);
            hargaKamar.put("A", 350000);

            if (hargaKamar.containsKey(kodeKamar) && lamaSewa > 0) {
                int hargaPerMalam = hargaKamar.get(kodeKamar);
                int jumlahBayar = hargaPerMalam * lamaSewa;

                double diskon = 0;
                if (lamaSewa > 5) {
                    diskon = 0.10;
                } else if (lamaSewa > 3) {
                    diskon = 0.05;
                }

                double totalDiskon = diskon * jumlahBayar;
                double totalBayarSetelahDiskon = jumlahBayar - totalDiskon;
                double ppn = 0.10 * totalBayarSetelahDiskon;
                double totalBayar = totalBayarSetelahDiskon + ppn;

                totalPembayaranLabel.setText("Total Pembayaran: " + formatRupiah(totalBayar));
                diskonLabel.setText("Diskon: " + formatRupiah(totalDiskon) + " (" + (int) (diskon * 100) + "%)");
                ppnLabel.setText("PPN: " + formatRupiah(ppn));
            } else {
                totalPembayaranLabel.setText("Total Pembayaran: Rp 0");
                diskonLabel.setText("");
                ppnLabel.setText("");
            }
        } catch (NumberFormatException e) {
            totalPembayaranLabel.setText("Total Pembayaran: Rp 0");
            diskonLabel.setText("");
            ppnLabel.setText("");
        }
    }

    private String formatRupiah(double amount) {
        DecimalFormat formatter = new DecimalFormat("###,###,###");
        return "Rp " + formatter.format(amount).replace(",", ".");
    }

    private void prosesPembayaran() {
        try {
            String namaPetugas = namaPetugasField.getText();
            String namaCustomer = namaCustomerField.getText();
            String tglCheckin = tglCheckinField.getText();
            String kodeKamar = kodeKamarCombo.getValue().split(" ")[0];
            int lamaSewa = Integer.parseInt(lamaSewaField.getText());
            int uangBayar = Integer.parseInt(uangBayarField.getText());

            if (namaPetugas.isEmpty() || namaCustomer.isEmpty() || !validateDate(tglCheckin) || lamaSewa <= 0 || uangBayar <= 0) {
                showAlert("Error", "Masukkan semua data dengan benar!", Alert.AlertType.ERROR);
                return;
            }

            Map<String, Integer> hargaKamar = new HashMap<>();
            hargaKamar.put("M", 650000);
            hargaKamar.put("S", 550000);
            hargaKamar.put("L", 400000);
            hargaKamar.put("A", 350000);

            Map<String, String> namaKamar = new HashMap<>();
            namaKamar.put("M", "Melati");
            namaKamar.put("S", "Sakura");
            namaKamar.put("L", "Lily");
            namaKamar.put("A", "Anggrek");

            if (!hargaKamar.containsKey(kodeKamar)) {
                showAlert("Error", "Kode kamar tidak valid!", Alert.AlertType.ERROR);
                return;
            }

            int hargaPerMalam = hargaKamar.get(kodeKamar);
            String namaKamarPesan = namaKamar.get(kodeKamar);
            int jumlahBayar = hargaPerMalam * lamaSewa;

            double diskon = 0;
            if (lamaSewa > 5) {
                diskon = 0.10;
            } else if (lamaSewa > 3) {
                diskon = 0.05;
            }

            double totalDiskon = diskon * jumlahBayar;
            double totalBayarSetelahDiskon = jumlahBayar - totalDiskon;
            double ppn = 0.10 * totalBayarSetelahDiskon;
            double totalBayar = totalBayarSetelahDiskon + ppn;
            double uangKembali = uangBayar - totalBayar;

            String bukti = String.format(
                    "Bukti Pemesanan Kamar\nHotel SEJUK ASRI\n" +
                            "=====================\n" +
                            "Nama Petugas: %s\n" +
                            "Nama Customer: %s\n" +
                            "Tanggal Check-in: %s\n" +
                            "Nama Kamar Yang dipesan: %s\n" +
                            "Harga sewa per malam: %s\n" +
                            "Lama sewa: %d hari\n" +
                            "Diskon: %s (%d%%)\n" +
                            "PPN: %s\n" +
                            "Jumlah Bayar: %s\n" +
                            "Total Bayar: %s\n" +
                            "Uang Bayar: %s\n" +
                            "Uang Kembali: %s\n",
                    namaPetugas, namaCustomer, tglCheckin, namaKamarPesan,
                    formatRupiah(hargaPerMalam), lamaSewa, formatRupiah(totalDiskon),
                    (int) (diskon * 100), formatRupiah(ppn), formatRupiah(jumlahBayar),
                    formatRupiah(totalBayar), formatRupiah(uangBayar), formatRupiah(uangKembali)
            );

            resultArea.setText(bukti);
        } catch (NumberFormatException e) {
            showAlert("Error", "Masukkan semua data dengan benar!", Alert.AlertType.ERROR);
        }
    }

    private boolean validateDate(String dateText) {
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            LocalDate.parse(dateText, formatter);
            return true;
        } catch (DateTimeParseException e) {
            return false;
        }
    }

    private void clearFields() {
        namaPetugasField.clear();
        namaCustomerField.clear();
        tglCheckinField.clear();
        lamaSewaField.clear();
        uangBayarField.clear();
        kodeKamarCombo.getSelectionModel().clearSelection();
        totalPembayaranLabel.setText("Total Pembayaran: Rp 0");
        diskonLabel.setText("Diskon: Rp 0");
        ppnLabel.setText("PPN: Rp 0");
        resultArea.clear();
    }

    private void showAlert(String title, String message, Alert.AlertType type) {
        Alert alert = new Alert(type);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
