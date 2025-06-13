import pytesseract

from PIL import Image


def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    extracted_text = extract_text_from_image("receipt.png")
    print("Extracted Text:\n")
    print(extracted_text)
