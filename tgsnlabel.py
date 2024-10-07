import os

def print_pdf(file_name):
    # Definiere das Verzeichnis, in dem sich die PDFs befinden
    pdf_directory = '/Users/neumawe1/Desktop'
    
    # Erstelle den vollständigen Pfad zur PDF-Datei
    file_path = os.path.join(pdf_directory, f"{file_name}.pdf")
    
    # Überprüfe, ob die Datei existiert
    if not os.path.isfile(file_path):
        print(f"Die Datei {file_name}.pdf existiert nicht im Verzeichnis {pdf_directory}.")
        return
    
    # Druckbefehl ausführen (dieser Befehl ist für Windows, für andere Betriebssysteme anpassen)
    # os.startfile(file_path, "print")
    os.system(f"lp {file_path}")

if __name__ == "__main__":
    # Eingabe des Dateinamens
    file_name = input("Bitte geben Sie den Namen der PDF-Datei ein (ohne .pdf): ")
    print_pdf(file_name)