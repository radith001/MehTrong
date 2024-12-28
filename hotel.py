import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class HotelSejukAsri:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel METRO ASRI - Transaksi Pembayaran")

        # Set the dimensions of the window
        window_width = 650
        window_height = 750

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position for centering the window
        position_x = int(screen_width / 2 - window_width / 2)
        position_y = int(screen_height / 2 - window_height / 2)

        # Set the geometry of the window
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.root.configure(bg='#87CEEB')  # Light blue background color

        self.create_widgets()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # Bind close event

    def create_widgets(self):
        # Main frame on top of the background
        self.main_frame = tk.Frame(self.root, bg='#8250D2', padx=10, pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Input Nama Petugas
        tk.Label(self.main_frame, text="Nama Petugas:", bg='#87CEEB', font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.nama_petugas = tk.Entry(self.main_frame, font=('Arial', 12))
        self.nama_petugas.grid(row=0, column=1, padx=10, pady=5)
        self.nama_petugas.bind('<Return>', self.focus_next_widget)

        # Input Nama Customer
        tk.Label(self.main_frame, text="Nama Customer:", bg='#87CEEB', font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.nama_customer = tk.Entry(self.main_frame, font=('Arial', 12))
        self.nama_customer.grid(row=1, column=1, padx=10, pady=5)
        self.nama_customer.bind('<Return>', self.focus_next_widget)

        # Input Tanggal Check-in
        tk.Label(self.main_frame, text="Tanggal Check-in (dd/mm/yyyy):", bg='#87CEEB', font=('Arial', 12)).grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.tgl_checkin = tk.Entry(self.main_frame, font=('Arial', 12))
        self.tgl_checkin.grid(row=2, column=1, padx=10, pady=5)
        self.tgl_checkin.bind('<Return>', self.focus_next_widget)

        # Input Kode Kamar
        tk.Label(self.main_frame, text="Kode Kamar:", bg='#87CEEB', font=('Arial', 12)).grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.kode_kamar = ttk.Combobox(self.main_frame, values=["M - Melati", "S - Sakura", "L - Lily", "A - Anggrek"], font=('Arial', 12))
        self.kode_kamar.grid(row=3, column=1, padx=10, pady=5)
        self.kode_kamar.current(0)
        self.kode_kamar.bind('<<ComboboxSelected>>', self.update_total_pembayaran)
        self.kode_kamar.bind('<Return>', self.focus_next_widget)

        # Input Lama Sewa
        tk.Label(self.main_frame, text="Lama Sewa (hari):", bg='#87CEEB', font=('Arial', 12)).grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.lama_sewa = tk.Entry(self.main_frame, font=('Arial', 12))
        self.lama_sewa.grid(row=4, column=1, padx=10, pady=5)
        self.lama_sewa.bind('<KeyRelease>', self.update_total_pembayaran)
        self.lama_sewa.bind('<Return>', self.focus_next_widget)

        # Label untuk menampilkan total pembayaran
        self.total_pembayaran_label = tk.Label(self.main_frame, text="Total Pembayaran: Rp 0", bg='#87CEEB', font=('Arial', 12))
        self.total_pembayaran_label.grid(row=5, column=0, columnspan=2, pady=10)

        # Label untuk menampilkan diskon
        self.diskon_label = tk.Label(self.main_frame, text="", bg='#87CEEB', font=('Arial', 12))
        self.diskon_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Label untuk menampilkan PPN
        self.ppn_label = tk.Label(self.main_frame, text="", bg='#87CEEB', font=('Arial', 12))
        self.ppn_label.grid(row=7, column=0, columnspan=2, pady=5)

        # Input Uang Bayar
        tk.Label(self.main_frame, text="Uang Bayar:", bg='#87CEEB', font=('Arial', 12)).grid(row=8, column=0, sticky=tk.W, padx=10, pady=5)
        self.uang_bayar = tk.Entry(self.main_frame, font=('Arial', 12))
        self.uang_bayar.grid(row=8, column=1, padx=10, pady=5)
        self.uang_bayar.bind('<Return>', self.focus_next_widget)

        # Tombol untuk Proses Pembayaran
        self.proses_button = tk.Button(self.main_frame, text="Proses Pembayaran", command=self.proses_pembayaran, font=('Arial', 12), bg='#4CAF50', fg='white', relief=tk.RAISED)
        self.proses_button.grid(row=9, column=0, columnspan=2, pady=10)
        self.proses_button.bind("<Enter>", self.on_enter_button)
        self.proses_button.bind("<Leave>", self.on_leave_button)

        # Tombol untuk Clear
        self.clear_button = tk.Button(self.main_frame, text="Clear", command=self.clear_fields, font=('Arial', 12), bg='#f44336', fg='white', relief=tk.RAISED)
        self.clear_button.grid(row=10, column=0, columnspan=2, pady=10)
        self.clear_button.bind("<Enter>", self.on_enter_clear_button)
        self.clear_button.bind("<Leave>", self.on_leave_clear_button)

        # Area untuk menampilkan hasil
        self.result_area = tk.Text(self.main_frame, height=15, width=60, font=('Arial', 12), bg='#ffffff', wrap=tk.WORD)
        self.result_area.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
        self.result_area.config(state='disabled')

    def on_enter_button(self, event):
        event.widget.config(bg='#45a049', relief=tk.SUNKEN)

    def on_leave_button(self, event):
        event.widget.config(bg='#4CAF50', relief=tk.RAISED)

    def on_enter_clear_button(self, event):
        event.widget.config(bg='#e53935', relief=tk.SUNKEN)

    def on_leave_clear_button(self, event):
        event.widget.config(bg='#f44336', relief=tk.RAISED)

    def focus_next_widget(self, event):
        current_widget = event.widget
        widget_list = [
            self.nama_petugas,
            self.nama_customer,
            self.tgl_checkin,
            self.kode_kamar,
            self.lama_sewa,
            self.uang_bayar
        ]
        try:
            current_index = widget_list.index(current_widget)
            next_widget = widget_list[current_index + 1]
            next_widget.focus()
        except IndexError:
            pass
        return 'break'

    def format_rupiah(self, amount):
        return f"Rp {amount:,.0f}".replace(',', '.')

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def update_total_pembayaran(self, event=None):
        try:
            kode_kamar = self.kode_kamar.get().split(" ")[0]
            lama_sewa = int(self.lama_sewa.get())

            harga_kamar = {
                'M': 650000,
                'S': 550000,
                'L': 400000,
                'A': 350000
            }

            if kode_kamar in harga_kamar and lama_sewa > 0:
                harga_per_malam = harga_kamar[kode_kamar]
                jumlah_bayar = harga_per_malam * lama_sewa

                if lama_sewa > 5:
                    diskon = 0.10
                elif lama_sewa > 3:
                    diskon = 0.05
                else:
                    diskon = 0

                total_diskon = diskon * jumlah_bayar
                total_bayar_setelah_diskon = jumlah_bayar - total_diskon
                ppn = 0.10 * total_bayar_setelah_diskon
                total_bayar = total_bayar_setelah_diskon + ppn

                self.total_pembayaran_label.config(text=f"Total Pembayaran: {self.format_rupiah(total_bayar)}")
                self.diskon_label.config(text=f"Diskon: {self.format_rupiah(total_diskon)} ({int(diskon * 100)}%)")
                self.ppn_label.config(text=f"PPN: {self.format_rupiah(ppn)}")
            else:
                self.total_pembayaran_label.config(text="Total Pembayaran: Rp 0")
                self.diskon_label.config(text="")
                self.ppn_label.config(text="")
        except ValueError:
            self.total_pembayaran_label.config(text="Total Pembayaran: Rp 0")
            self.diskon_label.config(text="")
            self.ppn_label.config(text="")

    def proses_pembayaran(self):
        try:
            nama_petugas = self.nama_petugas.get()
            nama_customer = self.nama_customer.get()
            tgl_checkin = self.tgl_checkin.get()
            kode_kamar = self.kode_kamar.get().split(" ")[0]
            lama_sewa = int(self.lama_sewa.get())
            uang_bayar = int(self.uang_bayar.get())

            if not nama_petugas or not nama_customer or not self.validate_date(tgl_checkin) or lama_sewa <= 0 or uang_bayar <= 0:
                messagebox.showerror("Error", "Masukkan semua data dengan benar!")
                return

            harga_kamar = {
                'M': 650000,
                'S': 550000,
                'L': 400000,
                'A': 350000
            }

            nama_kamar = {
                'M': "Melati",
                'S': "Sakura",
                'L': "Lily",
                'A': "Anggrek"
            }

            if kode_kamar not in harga_kamar:
                messagebox.showerror("Error", "Kode kamar tidak valid!")
                return

            harga_per_malam = harga_kamar[kode_kamar]
            nama_kamar_pesan = nama_kamar[kode_kamar]
            jumlah_bayar = harga_per_malam * lama_sewa

            if lama_sewa > 5:
                diskon = 0.10
            elif lama_sewa > 3:
                diskon = 0.05
            else:
                diskon = 0

            total_diskon = diskon * jumlah_bayar
            total_bayar_setelah_diskon = jumlah_bayar - total_diskon
            ppn = 0.10 * total_bayar_setelah_diskon
            total_bayar = total_bayar_setelah_diskon + ppn
            uang_kembali = uang_bayar - total_bayar

            # Tampilkan Bukti Pemesanan
            bukti = (
                f"Bukti Pemesanan Kamar\nHotel SEJUK ASRI\n"
                f"=================\n"
                f"Nama Petugas: {nama_petugas}\n"
                f"Nama Customer: {nama_customer}\n"
                f"Tanggal Check-in: {tgl_checkin}\n"
                f"Nama Kamar Yang dipesan: {nama_kamar_pesan}\n"
                f"Harga sewa per malam: {self.format_rupiah(harga_per_malam)}\n"
                f"Lama sewa: {lama_sewa} hari\n"
                f"Diskon: {self.format_rupiah(total_diskon)} ({int(diskon * 100)}%)\n"
                f"PPN: {self.format_rupiah(ppn)}\n"
                f"Jumlah Bayar: {self.format_rupiah(jumlah_bayar)}\n"
                f"Total Bayar: {self.format_rupiah(total_bayar)}\n"
                f"Uang Bayar: {self.format_rupiah(uang_bayar)}\n"
                f"Uang Kembali: {self.format_rupiah(uang_kembali)}\n"
            )
            self.result_area.config(state='normal')
            self.result_area.delete('1.0', tk.END)
            self.result_area.insert(tk.END, bukti)
            self.result_area.config(state='disabled')
        except ValueError:
            messagebox.showerror("Error", "Masukkan semua data dengan benar!")

    def clear_fields(self):
        self.nama_petugas.delete(0, tk.END)
        self.nama_customer.delete(0, tk.END)
        self.tgl_checkin.delete(0, tk.END)
        self.kode_kamar.current(0)
        self.lama_sewa.delete(0, tk.END)
        self.uang_bayar.delete(0, tk.END)
        self.total_pembayaran_label.config(text="Total Pembayaran: Rp 0")
        self.diskon_label.config(text="")
        self.ppn_label.config(text="")
        self.result_area.config(state='normal')
        self.result_area.delete('1.0', tk.END)
        self.result_area.config(state='disabled')

    def on_closing(self):
        if messagebox.askokcancel("Keluar", "Apakah Anda ingin keluar dari aplikasi?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelSejukAsri(root)
    root.mainloop()