from datetime import datetime

def calculate_days_from_birth(birth_date_str):
    # Mengubah string tanggal lahir menjadi objek datetime
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    
    # Mendapatkan tanggal hari ini
    today = datetime.today()
    
    # Menghitung selisih hari antara hari ini dan tanggal lahir
    delta = today - birth_date
    
    return delta.days

if __name__ == "__main__":
    birth_date_str = input("Masukkan tanggal lahir Anda (format YYYY-MM-DD): ")
    days = calculate_days_from_birth(birth_date_str)
    print(f"Jumlah hari dari tanggal lahir Anda hingga hari ini adalah: {days} hari")