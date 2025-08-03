import base64

def image_to_base64(image_path, output_file="base64.txt"):
    """
    Converts an image to its Base64 encoding and saves it to a file.

    Args:
        image_path (str): The path to the input image file.
        output_file (str): The path to the output text file where the Base64 string will be saved.
    """
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        with open(output_file, "w") as text_file:
            text_file.write(encoded_string)
        print(f"Image '{image_path}' successfully converted to Base64 and saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        image_to_base64(image_path)
    else:
        print("Usage: python script.py <image_path>")