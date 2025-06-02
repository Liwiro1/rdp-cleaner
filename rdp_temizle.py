import os
import glob
from pathlib import Path

def delete_rdp_files():
    # İndirilenler klasörünün yolunu bul
    downloads_path = Path.home() / "Downloads"
    
    # Alternatif yollar (farklı sistemlerde)
    if not downloads_path.exists():
        downloads_path = Path.home() / "İndirilenler"  # Türkçe Windows
    
    if not downloads_path.exists():
        print("İndirilenler klasörü bulunamadı!")
        return
    
    print(f"İndirilenler klasörü: {downloads_path}")
    
    # .rdp dosyalarını bul
    rdp_pattern = str(downloads_path / "*.rdp")
    rdp_files = glob.glob(rdp_pattern)
    
    if not rdp_files:
        print("Silinecek .rdp dosyası bulunamadı.")
        return
    
    # Bulunan dosyaları listele
    print(f"\nBulunan {len(rdp_files)} .rdp dosyası:")
    for file_path in rdp_files:
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        print(f"  - {file_name} ({file_size} bytes)")
    
    deleted_count = 0
    failed_count = 0
    
    for file_path in rdp_files:
        try:
            os.remove(file_path)
            print(f"✓ Silindi: {os.path.basename(file_path)}")
            deleted_count += 1
        except Exception as e:
            print(f"✗ Silinemedi: {os.path.basename(file_path)} - Hata: {e}")
            failed_count += 1
    
    print(f"\nTamamlandı! {deleted_count} dosya silindi, {failed_count} dosya silinemedi.")

# Güvenli mod - sadece listeleme (silmeden önce test etmek için)
def list_rdp_files_only():
    """Sadece .rdp dosyalarını listeler, silmez"""
    downloads_path = Path.home() / "Downloads"
    
    if not downloads_path.exists():
        downloads_path = Path.home() / "İndirilenler"
    
    if not downloads_path.exists():
        print("İndirilenler klasörü bulunamadı!")
        return
    
    rdp_pattern = str(downloads_path / "*.rdp")
    rdp_files = glob.glob(rdp_pattern)
    
    if not rdp_files:
        print("Hiç .rdp dosyası bulunamadı.")
        return
    
    print(f"Bulunan {len(rdp_files)} .rdp dosyası:")
    for file_path in rdp_files:
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        mod_time = os.path.getmtime(file_path)
        from datetime import datetime
        mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M")
        print(f"  - {file_name} ({file_size} bytes, {mod_date})")

if __name__ == "__main__":
    print("RDP Dosyası Temizleyici")
    print("=" * 30)
    
    # Önce dosyaları listele
    print("1. Dosyalar kontrol ediliyor...")
    list_rdp_files_only()
    
    print("\n" + "=" * 30)
    
    # Sonra silme işlemini başlat
    delete_rdp_files()