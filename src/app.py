# Bloque de código para descargar y extraer los datos sobre las noticias falsas, desde la API de Kaggle
# Este bloque puede ser llamado desde el main.py o desde el notebook de Jupyter
import requests
import zipfile
import pandas as pd
import io
import os

# URL del archivo zip en Kaggle
zip_url = "https://www.kaggle.com/api/v1/datasets/download/clmentbisaillon/fake-and-real-news-dataset"

# Función para descargar el archivo zip y extraer los archivos CSV
# de la carpeta de salida especificada
def download_extract_zip_to_csv(output_dir="../data"):
    try:
        print(f"Downloading zip file from: {zip_url}...")
        response = requests.get(zip_url, stream=True)
        response.raise_for_status()

        zip_filename = "downloaded_data.zip"
        with open(zip_filename, 'wb') as zip_file:
            for chunk in response.iter_content(chunk_size=8192):
                zip_file.write(chunk)
        print(f"Zip file downloaded successfully to: {zip_filename}")

        print(f"Extracting CSV files...")
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            extracted_files = zip_ref.namelist()
            csv_files_extracted = False

            os.makedirs(output_dir, exist_ok=True)

            for file in extracted_files:
                if file.endswith(".csv"):
                    print(f"Found CSV file: {file}")
                    with zip_ref.open(file) as csv_file_in_zip:
                        csv_content = io.TextIOWrapper(csv_file_in_zip, encoding='utf-8')
                        df = pd.read_csv(csv_content)
                        output_path = os.path.join(output_dir, file)
                        df.to_csv(output_path, index=False, encoding='utf-8')
                        print(f"CSV file saved to: {output_path}")
                        csv_files_extracted = True

            if not csv_files_extracted:
                print("No .csv files found within the zip archive.")
                return False

        os.remove(zip_filename)
        print(f"Deleted the downloaded zip file: {zip_filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Download error: {e}")
        return False
    except zipfile.BadZipFile as e:
        print(f"Error with the zip file: {e}")
        return False
    except pd.errors.EmptyDataError:
        print("One or more of the extracted CSV files are empty.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    


if __name__ == "__main__":
    download_successful = download_extract_zip_to_csv(output_dir="data")

    if download_successful:
        print("Successfully downloaded and extracted the CSV files.")
    else:
        print("There was an issue during the download or extraction process.")